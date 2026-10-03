# marker arm

- Version: marker-pdf 2.0.0, surya-ocr 0.22.1, pdftext 0.7.1, torch 2.14.1 (CPU), Python 3.12. llama.cpp `llama-server` b11324 (ubuntu-x64 CPU build) vendored at `bin/llama-b11324/` (44 MB).
- Install: `uv sync` (dep `marker-pdf==2.0.0`), then the llama.cpp CPU binary:
  `cd arms/marker/bin && curl -sL https://github.com/ggml-org/llama.cpp/releases/download/b11324/llama-b11324-bin-ubuntu-x64.tar.gz | tar xz`.
  marker 2 needs `llama-server` on CPU (or Docker+NVIDIA vLLM on GPU) for its surya VLM.
- Architecture: every model runs in a local surya server — rf-detr fast layout and DistilBert ocr-error (persistent python batch servers, `keep_alive`) and the surya-ocr-2 VLM in `llama-server`. `run.py` spawns them in `make` (setup time, not first-document time) and stops the ones it spawned at exit (also on SIGTERM); server logs/sentinels live in `~/.cache/datalab/surya/`.
- Models: `datalab-to/surya-ocr-2-gguf` 1.4 GB (surya-2.gguf + mmproj), `datalab-to/surya_layout2` 136 MB (rf-detr layout + order head), `~/.cache/datalab/models/ocr_error_detection` 262 MB.
- License: code Apache-2.0 (marker-pdf 2.0.0 and surya-ocr 0.22.1 wheels); weights under a modified AI Pubs Open Rail-M (free for research, personal use and organisations under $5M funding/revenue; commercial licence otherwise).
- Server mode: `marker_server --port 8001` (FastAPI, "small-scale use").
- Env set by `run.py`: `TORCH_DEVICE=cpu`, `SURYA_INFERENCE_BACKEND=llamacpp`, `LLAMA_CPP_BINARY=bin/…/llama-server`, `LLAMA_CPP_NGL=0`, `LLAMA_CPP_EXTRA_ARGS=--threads <physical cores, 6 here; ARM_LLAMA_THREADS overrides>`, `FAST_LAYOUT_NUM_THREADS=12`, `SURYA_INFERENCE_PARALLEL=4` (default 8 KV slots), `SURYA_INFERENCE_TIMEOUT_SECONDS=3600` (default 600).
- Variants (`ConfigParser({"output_format": "markdown", …})` → `PdfConverter` → `text_from_rendered`; images saved to `assets/`):
  - `fast` — `mode=fast` (marker's CPU default): rf-detr layout, pdftext text layer, VLM only for equations, garbled/empty blocks and low-score tables.
  - `nocr` — `mode=fast` + `disable_ocr=True`: pure text layer, no VLM calls (llama-server not started).
  - `balanced` — `mode=balanced` (marker's GPU default): VLM layout + full-page OCR for pages with flagged blocks, via llama.cpp on CPU.
- Smoke (natcomm-2020, 7 pages, machine shared with other arms):
  - `nocr`: 5.9 s (0.84 s/page), 1.1 GB RSS (servers' RSS not included).
  - `fast`: 16.1 s (2.3 s/page), 2.0 GB RSS; setup 96 s on first run (downloads + server spawn).
  - `balanced`: 1585 s (226 s/page), 1.2 GB driver RSS + llama-server; setup 30 s. Works on CPU but is impractical on this 6-core/12-thread laptop CPU under load: llama-server decoded ~0.2 tok/s per slot (prompt ~7 tok/s) while another arm ran. A first attempt with the defaults (8 slots, 600 s request timeout) hit `Inference error: Request timed out`, hence the 4-slot / 3600 s settings. That smoke ran llama-server with 12 threads; `llama-bench` on this CPU under the same background load gives 0.4 tok/s decode at 12 threads vs 2.2 at 6 and 14 at 4 (spin-barrier oversubscription), so `run.py` now defaults llama-server to one thread per physical core — re-measure balanced in the queue run.
- Output notes (fast and nocr look the same on this paper; balanced differs only in heading levels — `## ARTICLE`, `###`/`####` section heads, run-in paragraph heads promoted to `####`): `# ARTICLE` running head promoted to H1, title `#`, DOI line as `#`, section heads `####`; author names carry ORCID links split mid-word (`Zho[u](orcid) [1](orcid)`); `<span id="page-N-M"></span>` anchors before blocks; affiliations as `<sup>` footnotes; figures as `![](_page_N_Figure_M.jpeg)` with captions as paragraphs; running footers removed; no display equations in this paper.
