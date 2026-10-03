"""Marker 2.x (marker-pdf), CPU. Heavy models run in surya's local servers:
rf-detr fast layout + DistilBert ocr-error (persistent batch servers) and the surya-ocr-2
VLM in a llama.cpp ``llama-server`` (CPU build vendored under ``bin/``).

Variants:
  fast      ``mode=fast``: rf-detr layout, pdftext text layer, VLM only for equations,
            garbled blocks and table fallback (marker's CPU default)
  nocr      ``mode=fast`` + ``disable_ocr``: pure text layer, no VLM calls
  balanced  ``mode=balanced``: VLM layout + full-page OCR where text quality is poor
            (marker's GPU default), here through llama.cpp on CPU

Servers this process spawns are stopped at exit, so every run starts cold and nothing
lingers between arms.
"""

import atexit
import json
import os
import signal
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
THREADS = int(os.environ.get("OMP_NUM_THREADS", os.cpu_count() or 4))
LLAMA = HERE / "bin" / "llama-b11324" / "llama-server"
os.environ.setdefault("TORCH_DEVICE", "cpu")
os.environ.setdefault("SURYA_INFERENCE_BACKEND", "llamacpp")
os.environ.setdefault("LLAMA_CPP_BINARY", str(LLAMA))
os.environ.setdefault("LLAMA_CPP_NGL", "0")
# llama.cpp decode collapses when its threads exceed the free physical cores (spin barriers),
# so the VLM server gets one thread per physical core; ARM_LLAMA_THREADS overrides.
LLAMA_THREADS = int(os.environ.get("ARM_LLAMA_THREADS", max(1, (os.cpu_count() or 2) // 2)))
os.environ.setdefault("LLAMA_CPP_EXTRA_ARGS", f"--threads {LLAMA_THREADS}")
os.environ.setdefault("FAST_LAYOUT_NUM_THREADS", str(THREADS))
# CPU llama.cpp: fewer KV slots than the GPU-sized default of 8, and a request timeout long
# enough for a full-page OCR generation on CPU (default 600 s times out under load).
os.environ.setdefault("SURYA_INFERENCE_PARALLEL", "4")
os.environ.setdefault("SURYA_INFERENCE_TIMEOUT_SECONDS", "3600")

from marker.config.parser import ConfigParser  # noqa: E402
from marker.converters.pdf import PdfConverter  # noqa: E402
from marker.models import create_model_dict  # noqa: E402
from marker.output import text_from_rendered  # noqa: E402

PACKAGES = ["marker-pdf", "surya-ocr", "pdftext", "torch"]
EXTRA = {
    "llama_cpp": "b11324 ubuntu-x64 CPU build (llama-server)",
    "llama_threads": LLAMA_THREADS,
    "vlm_model": "datalab-to/surya-ocr-2-gguf (surya-2.gguf + mmproj)",
    "layout_model": "datalab-to/surya_layout2 (rf-detr, fast mode)",
    "license": "code Apache-2.0; weights modified AI Pubs Open Rail-M (free for research, personal use, "
    "and orgs under $5M funding/revenue; commercial licence otherwise)",
}
VARIANTS = {
    "fast": {"mode": "fast"},
    "nocr": {"mode": "fast", "disable_ocr": True},
    "balanced": {"mode": "balanced"},
}
SENTINELS = Path.home() / ".cache" / "datalab" / "surya"


def _sentinels() -> dict[str, dict]:
    out = {}
    for p in SENTINELS.glob("*_server.json"):
        try:
            out[p.name] = json.loads(p.read_text())
        except (OSError, ValueError):
            pass
    return out


def _stop_new_servers(before: dict[str, dict]) -> None:
    for name, info in _sentinels().items():
        if name in before and before[name].get("pid") == info.get("pid"):
            continue
        pid = info.get("pid")
        if pid:
            try:
                os.kill(int(pid), signal.SIGTERM)
            except (ProcessLookupError, PermissionError):
                pass
        (SENTINELS / name).unlink(missing_ok=True)


def make(variant: str):
    if variant not in VARIANTS:
        raise ValueError(f"unknown variant {variant!r}")
    before = _sentinels()
    atexit.register(_stop_new_servers, before)
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))  # run atexit cleanup on kill
    cfg = ConfigParser({"output_format": "markdown", **VARIANTS[variant]})
    models = create_model_dict(inference_backend="llamacpp")
    # Spawn the servers now so their start-up is setup time, not first-document time.
    models["fast_layout_model"]._client._client._ensure_started()
    models["ocr_error_model"]._client._client._ensure_started()
    if variant != "nocr":
        models["inference_manager"].start()
    converter = PdfConverter(
        config=cfg.generate_config_dict(),
        artifact_dict=models,
        processor_list=cfg.get_processors(),
        renderer=cfg.get_renderer(),
        llm_service=cfg.get_llm_service(),
    )

    def convert(pdf: Path, assets: Path) -> str:
        text, _, images = text_from_rendered(converter(str(pdf)))
        if images:
            assets.mkdir(parents=True, exist_ok=True)
            for name, img in images.items():
                img.save(assets / name)
        return text

    return convert
