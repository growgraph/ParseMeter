# unstructured arm

- Version: unstructured 0.27.10, unstructured-inference 1.6.13, unstructured.pytesseract 0.3.15, onnxruntime 1.30.0, torch 2.14.1 (CPU use), Python 3.12.
- Install: `uv sync` (dep `unstructured[pdf]==0.27.10`); needs system `tesseract` (5.5 here) and poppler (`pdftoppm`).
- Models (`~/.cache/huggingface/hub`): `unstructuredio/yolo_x_layout` 207 MB (YOLOX layout, ONNX), `microsoft/table-transformer-structure-recognition` 111 MB (torch). Both loaded in `make` (the table model is otherwise loaded lazily on the first table).
- License: Apache-2.0 (unstructured, unstructured-inference, YOLOX layout weights); Table Transformer weights MIT; Tesseract Apache-2.0.
- Server mode: the separate `unstructured-api` docker image (`downloads.unstructured.io/unstructured-io/unstructured-api`), not used here.
- Variant `hires`: `partition_pdf(filename, strategy="hi_res", infer_table_structure=True)`; elements → markdown in `run.py`: Title `#`, ListItem `- `, Table `metadata.text_as_html`, Image `<!-- image -->`, FigureCaption text, Formula `$$…$$`, rest as paragraphs; only element types unstructured itself labels Header/Footer/PageNumber (and PageBreak) are dropped. Scarf analytics disabled (`SCARF_NO_ANALYTICS`, `DO_NOT_TRACK`).
- CPU: all CPU; `OMP_THREAD_LIMIT` set for tesseract. Slowest of the CPU arms.
- Smoke (natcomm-2020, 7 pages): 124.4 s cold run (17.8 s/page, incl. lazy table-model load) and 216.2 s warm run (30.9 s/page) while the marker `balanced` llama-server smoke ran concurrently — expect ~15–20 s/page on an idle machine; 2.1 GB RSS.
- Output notes: Title elements are frequent false positives/negatives — the paper title is NarrativeText, `# ARTICLE` (running head) is a Title, section heads (Results, Methods…) are `#`; stray single-glyph elements at the top of the document (`;`, `,`, `0`…`9` from embedded font/badge artwork); running footers (`NATURE COMMUNICATIONS | …`) and page numbers survive because they were classified as text, not Footer/PageNumber; figure-internal text OCR'd as many short paragraphs interleaved with 32 `<!-- image -->` markers; no tables detected in this paper; hyphenated line breaks kept (`perfor- mance`).
