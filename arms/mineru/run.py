"""MinerU 4.x, local parse (no doclib server, no remote service).

Variants (MinerU tiers):
  basic     ONNX small-model pipeline (layout + OCR + formula + table models)
  standard  hybrid: MinerU2.5-Pro 1.2B VLM via the bundled llama.cpp engine (CPU)

Markdown is ``ParseResult.save()``'s ``markdown.md``; its image files are copied to ``assets``.
"""

import os
import shutil
import tempfile
from pathlib import Path

THREADS = int(os.environ.get("OMP_NUM_THREADS", os.cpu_count() or 4))
os.environ.setdefault("MINERU_INTRA_OP_NUM_THREADS", str(THREADS))
os.environ.setdefault("MINERU_MODEL_SOURCE", "huggingface")
os.environ.setdefault("MINERU_MODEL_SMALL_BACKEND", "onnx")
os.environ.setdefault("MINERU_MODEL_VLM_ENGINE", "llama-cpp")

import mineru_llama_cpp  # noqa: E402
from mineru.parser import MinerUParser  # noqa: E402
from mineru.parser.api_server import _preload_server_models  # noqa: E402
from mineru.parser.writer import FileBasedDataWriter  # noqa: E402

# The bundled llama.cpp engine ships a Vulkan backend and defaults to n_gpu_layers=99, so on a
# machine with an integrated GPU the VLM silently runs there. The benchmark is CPU only.
_engine_init = mineru_llama_cpp.Engine.__init__


def _cpu_engine_init(self, *args, **kwargs):
    kwargs["n_gpu_layers"] = 0
    _engine_init(self, *args, **kwargs)


mineru_llama_cpp.Engine.__init__ = _cpu_engine_init

PACKAGES = ["mineru", "docvortex", "mineru-llama-cpp", "mineru-vl-utils", "onnxruntime"]
EXTRA = {
    "license": "MinerU Open Source License (Apache-2.0 based, with additional conditions)",
    "vlm_model": "MinerU2.5-Pro-2605-1.2B (GGUF, llama.cpp engine, n_gpu_layers=0) — standard tier only",
    "small_backend": "onnx",
}


def make(variant: str):
    if variant not in ("basic", "standard"):
        raise ValueError(f"unknown variant {variant!r}")
    parser = MinerUParser(tier=variant, parse_mode="auto", image_analysis=True)
    # The parse server's own warm-up: VLM predictor (standard) + hybrid small models + table/OCR atoms.
    _preload_server_models(variant, vlm_config=parser.vlm_config)

    def convert(pdf: Path, assets: Path) -> str:
        res = parser.parse(pdf, page_range="")
        with tempfile.TemporaryDirectory() as tmp:
            res.save(FileBasedDataWriter(tmp))
            md = (Path(tmp) / "markdown.md").read_text(encoding="utf-8")
            for f in Path(tmp).rglob("*"):
                if f.is_file() and f.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
                    dest = assets / f.relative_to(tmp)
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(f, dest)
        return md

    return convert
