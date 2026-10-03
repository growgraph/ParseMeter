# pymupdf4llm arm

- Versions: pymupdf4llm 1.28.2, pymupdf 1.28.2, pymupdf-layout 1.28.2 (Python 3.12).
- Install: `uv sync` (deps `pymupdf4llm==1.28.2`, `pymupdf-layout==1.28.2`).
- Models: none downloaded; the layout GNN (ONNX) ships inside the `pymupdf-layout` wheel (`pymupdf/layout/` is 51 MB).
- License: code and bundled layout model are dual AGPL-3.0 / Artifex commercial.
- Server mode: none (library only).
- Variants:
  - `default` — `use_layout(False)`: legacy heuristic `pymupdf_rag` path. Note: installing `pymupdf-layout` makes layout the package default, so this variant switches it off explicitly.
  - `layout` — PyMuPDF-Layout path (`to_markdown` defaults: `header=True`, `footer=True`, i.e. page furniture kept; `use_ocr=True` OCRs picture regions/pages with Tesseract when it decides to).
- CPU: pure CPU; layout path calls system Tesseract (5.5) for OCR.
- Smoke (natcomm-2020, 7 pages, machine shared with another arm): default 4.94 s (0.71 s/page, 194 MB RSS); layout 6.28 s (0.90 s/page, 387 MB RSS).
- Output notes: `default` drops the article title, emits hard line wraps and keeps running headers/footers. `layout` recovers the title (`# <mark>…</mark>`), section heads `###`, joins paragraphs, keeps running headers/footers and page numbers, and emits figure-internal text between `<!-- Start of picture text -->` … `<!-- End of picture text -->` (OCR'd axis labels); no images written.
