# mineru arm

- Version: mineru 4.0.10 (docvortex 0.5.8, mineru-llama-cpp 0.1.2, mineru-vl-utils 2.0.5, onnxruntime 1.30.0), Python 3.12.
- Install: `uv sync` (dep `mineru==4.0.10`; the base package already carries ONNX + the llama.cpp engine — `[torch]` / `[full]` extras are for PyTorch / vLLM-LMDeploy GPU backends and are not needed on CPU).
- API: `mineru.parser.MinerUParser(tier=…, parse_mode="auto").parse(pdf)` → `ParseResult.save()`; the arm returns its `markdown.md` and moves the image files into `assets/`. No doclib (document-library server, SQLite, telemetry) and no `--remote` service is involved. Models are warmed in `make` via the API server's own preload (`mineru.parser.api_server._preload_server_models`).
- Env set by `run.py`: `MINERU_MODEL_SOURCE=huggingface`, `MINERU_MODEL_SMALL_BACKEND=onnx`, `MINERU_MODEL_VLM_ENGINE=llama-cpp`, `MINERU_INTRA_OP_NUM_THREADS=$OMP_NUM_THREADS` (MinerU's ONNX default is 4 threads).
- Models (`~/.mineru/models/`): `MinerU-4_models_onnx` 819 MB (PP-DocLayoutV2 layout, PP-OCRv6 det/rec, PP-FormulaNet, table models); `MinerU2.5-Pro-2605-1.2B-GGUF` 1.2 GB (standard tier only).
- License: MinerU Open Source License (Apache-2.0 based, with additional conditions) for code; model weights published by OpenDataLab under the same family of terms (check the HF model cards before redistribution).
- Server mode: `mineru-kit api-server` (self-hosted v1 REST API), `mineru-kit vlm-server` (OpenAI-compatible VLM), `mineru server start` (doclib).
- Variants:
  - `basic` (effort `medium`): ONNX small-model pipeline; text from the PDF text layer, OCR only where needed.
  - `standard` (effort `high`): same pipeline + MinerU2.5-Pro 1.2B VLM through the bundled llama.cpp engine on CPU (auto-selected on CPU). In txt mode the VLM re-extracts the non-text layout blocks (tables, formulas, figures…); body text still comes from the text layer. The full-page two-step VLM is the `advanced` tier (not built here).
- CPU caveat: none — both tiers run on CPU. VLM predictor load is ~51 s (setup, not per document). The bundled llama.cpp engine keeps its own default thread count (`n_threads=-1`, physical cores).
- Smoke (natcomm-2020, 7 pages, machine shared with another arm): basic 44.2 s (6.3 s/page, 3.4 GB RSS, setup 6.8 s); standard 48.9 s (7.0 s/page, 3.7 GB RSS, setup 53 s). A cold first run without preload took 76 s.
- Output notes: title `#`, section heads `##` (Results, Discussion, Methods, References…); inline math as LaTeX (`$\mathsf{…}$` even for chemical formulas like CaTiO3), affiliations/footnotes wrapped in `<small><span class="docvortex-page-footnote" …>` HTML, superscripts as `<sup>`, drop cap split (`P <sup>erovskites</sup>`), figures split into many `![](images/page_N_chart_M.jpg)` crops with panel letters as separate lines; running header `ARTICLE` + DOI kept at the top only. basic and standard produced byte-identical markdown on this paper (no tables/display equations).
