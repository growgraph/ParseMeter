# docling arm

- Version: docling 2.132.0, docling-core 2.99.0, docling-parse 7.22.1, docling-ibm-models 4.0.3, transformers 5.18.0, torch 2.14.1 (CPU), Python 3.12.
- Install: `uv sync`. Models download from Hugging Face on first use.
- Output: `DocumentConverter.convert(pdf).document.export_to_markdown()`; no images written.
- Models: heron layout (`docling-project/docling-layout-heron`, 164 MB, Apache-2.0), TableFormer (`docling-project/docling-models`, 342 MB, CDLA-Permissive-2.0), RapidOCR PP-OCRv6 (62 MB, chosen by the `auto` OCR engine on this machine), CodeFormulaV2 (CDLA-Permissive-2.0, `formula` and `tuned` only), egret-large layout (Apache-2.0, `tuned` only).
- License: code MIT (docling, docling-core, docling-parse).
- Server mode: `docling-serve` (separate package).
- Threads: `num_threads` from `OMP_NUM_THREADS` (12 in `run_queue.sh`) for every variant, including `default`, which reads the same variable.
- Variants. `default` is `DocumentConverter()` untouched: docling-parse backend, heron layout, OCR on bitmap regions, TableFormer accurate with cell matching. The ladder changes one setting at a time from it:

  | Variant | Change from `default` |
  |---|---|
  | `noocr` | `do_ocr=False` |
  | `fast` | `do_ocr=False`, TableFormer `mode=fast` |
  | `layoutonly` | `do_ocr=False`, `do_table_structure=False` (tables come out as layout text) |
  | `native` | `NativePdfPipeline`: text cells in parser order, no layout, table or OCR model |
  | `fullocr` | OCR `mode=full_page` (ignores the text layer) |
  | `formula` | `do_formula_enrichment=True` (equations to LaTeX) |
  | `lean` | `fast` + `do_formula_enrichment=True` |
  | `textlayer` | pypdfium2 backend, `do_ocr=False`, `force_backend_text=True` |
  | `tuned` | egret-large layout, formula enrichment, picture classification and images, heading hierarchy |
  | `granite`, `glmocr`, `lightonocr` | `VlmPipeline` with granite-docling-258M, GLM-OCR 0.9B, LightOnOCR-2-1B (transformers, CPU) |
