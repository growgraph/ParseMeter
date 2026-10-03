"""PaddleOCR 3.x on CPU (paddlepaddle CPU wheel, oneDNN).

Variants:
  structurev3  PP-StructureV3 pipeline (layout + OCR + tables + formulas); pages joined with
               ``concatenate_markdown_pages`` (paragraph-continuation aware)
  vl           PaddleOCR-VL 1.6 (PP-DocLayoutV3 + 0.9B VLM). The VLM runs in llama.cpp
               ``llama-server`` (official PaddlePaddle/PaddleOCR-VL-1.6-GGUF, CPU build vendored
               under ``bin/``) via ``vl_rec_backend="llama-cpp-server"``; the server is started
               in ``make`` and stopped at exit
  vl-native    same pipeline with the default native Paddle VLM backend on CPU (~14 min/page here)

VL pages are joined with ``restructure_pages(merge_tables=True, relevel_titles=True,
concatenate_pages=True)``. All pipelines rasterise pages and recognise text from pixels (no
text layer). Markdown image files are written under ``assets`` at the referenced paths.
"""

import atexit
import os
import signal
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

os.environ.setdefault("PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK", "True")
os.environ.setdefault("PADDLE_PDX_MODEL_SOURCE", "huggingface")
THREADS = int(os.environ.get("OMP_NUM_THREADS", os.cpu_count() or 4))
HERE = Path(__file__).resolve().parent
LLAMA = HERE / "bin" / "llama-b11324" / "llama-server"
GGUF_REPO = "PaddlePaddle/PaddleOCR-VL-1.6-GGUF"
SLOTS = 4
# llama.cpp decode collapses when its threads exceed the free physical cores (spin barriers):
# measured 12 threads 0.4 tok/s vs 4 threads 14 tok/s on this 6-core/12-thread CPU under load.
LLAMA_THREADS = int(os.environ.get("ARM_LLAMA_THREADS", max(1, (os.cpu_count() or 2) // 2)))

from paddleocr import PaddleOCRVL, PPStructureV3  # noqa: E402
from paddlex.inference import load_pipeline_config  # noqa: E402

PACKAGES = ["paddleocr", "paddlex", "paddlepaddle", "openai"]
EXTRA = {
    "device": "cpu",
    "cpu_threads": THREADS,
    "vl_model": "PaddleOCR-VL-1.6 (0.9B) + PP-DocLayoutV3; vl: GGUF via llama.cpp b11324 CPU build",
    "llama_threads": LLAMA_THREADS,
    "license": "Apache-2.0 (code and model weights)",
}


def _save_images(md: dict, assets: Path) -> None:
    for rel, img in (md.get("markdown_images") or {}).items():
        dest = assets / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        img.save(dest)


def _start_llama_server() -> str:
    from huggingface_hub import hf_hub_download

    model = hf_hub_download(GGUF_REPO, "PaddleOCR-VL-1.6-GGUF.gguf")
    mmproj = hf_hub_download(GGUF_REPO, "PaddleOCR-VL-1.6-GGUF-mmproj.gguf")
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    log = open(HERE / "llama-server.log", "ab")
    proc = subprocess.Popen(
        [str(LLAMA), "-m", model, "--mmproj", mmproj, "--host", "127.0.0.1", "--port", str(port),
         "--temp", "0", "--threads", str(LLAMA_THREADS), "--parallel", str(SLOTS), "--ctx-size", str(8192 * SLOTS)],
        stdout=log, stderr=subprocess.STDOUT,
    )

    def stop() -> None:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=20)
            except subprocess.TimeoutExpired:
                proc.kill()

    atexit.register(stop)
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))  # run atexit cleanup on kill
    deadline = time.time() + 600
    while time.time() < deadline:
        if proc.poll() is not None:
            raise RuntimeError("llama-server exited during start-up; see arms/paddle/llama-server.log")
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=2) as r:
                if r.status == 200:
                    return f"http://127.0.0.1:{port}/v1"
        except OSError:
            pass
        time.sleep(1)
    raise RuntimeError("llama-server did not become healthy within 600 s")


def _vl_config() -> dict:
    # The OpenAI client default (600 s) is shorter than a long block generation on CPU.
    cfg = dict(load_pipeline_config("PaddleOCR-VL-1.6"))
    vl = cfg["SubModules"]["VLRecognition"]
    genai = dict(vl.get("genai_config") or {})
    genai["client_kwargs"] = {**(genai.get("client_kwargs") or {}), "timeout": 3600}
    vl["genai_config"] = genai
    return cfg


def make(variant: str):
    common = {"device": "cpu", "cpu_threads": THREADS, "enable_mkldnn": True}
    if variant == "structurev3":
        # As in the PaddleOCR quick-start for documents: no page orientation / unwarping (UVDoc)
        # pre-pass, which warps born-digital pages.
        pipe = PPStructureV3(use_doc_orientation_classify=False, use_doc_unwarping=False, **common)

        def convert(pdf: Path, assets: Path) -> str:
            pages = [res.markdown for res in pipe.predict(str(pdf))]
            for md in pages:
                _save_images(md, assets)
            return pipe.concatenate_markdown_pages(pages)["markdown_texts"]

        return convert

    if variant == "vl":
        url = _start_llama_server()
        pipe = PaddleOCRVL(
            pipeline_version="v1.6",
            vl_rec_backend="llama-cpp-server",
            vl_rec_server_url=url,
            vl_rec_max_concurrency=SLOTS,
            paddlex_config=_vl_config(),
            **common,
        )
    elif variant == "vl-native":
        pipe = PaddleOCRVL(pipeline_version="v1.6", **common)
    else:
        raise ValueError(f"unknown variant {variant!r}")

    def convert(pdf: Path, assets: Path) -> str:
        pages = list(pipe.predict(str(pdf)))
        doc = pipe.restructure_pages(pages, merge_tables=True, relevel_titles=True, concatenate_pages=True)
        md = doc[0].markdown
        _save_images(md, assets)
        return md["markdown_texts"]

    return convert
