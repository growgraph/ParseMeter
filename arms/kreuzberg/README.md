# kreuzberg arm

- Version: kreuzberg 4.10.4 (4.10.x LTS line; Rust core in the wheel), Python 3.12.
- Install: `uv sync` (dep `kreuzberg==4.10.4`).
- Models: none for this variant (no layout model, no OCR triggered on born-digital PDFs); nothing under `~/.cache`.
- License: MIT (code). No weights used.
- Server mode: the standalone `kreuzberg` CLI binary (`kreuzberg serve`, REST/MCP) is a separate download from the GitHub releases page (kreuzberg-dev/kreuzberg-lts); the PyPI wheel's `kreuzberg` entry point only prints that hint.
- Variant `default`: `extract_file_sync(pdf, ExtractionConfig(output_format="markdown", use_cache=False, concurrency=ConcurrencyConfig(max_threads=12)))`. The result cache is off so repeat runs are timed honestly. Optional layout detection (`LayoutDetectionConfig`) and OCR backends are not enabled.
- CPU: pure CPU, single document is effectively single-threaded and very fast.
- Smoke (natcomm-2020, 7 pages): 0.43 s (0.06 s/page), 84 MB RSS.
- Output notes: text-layer extraction with font-size heading heuristics — many false headings (`## 0.5`, `### c`, body lines promoted to `###` in two-column pages); title split across a paragraph and an `#` heading merged with the author line; figure axis text inline; running headers/footers kept; no image placeholders; equations as plain text.
