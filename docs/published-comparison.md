# Our numbers next to published ones

Generated table: `out/summary/published_vs_ours.csv` (`PYTHONPATH=. uv run python -m study.published`).
Published rows and source ids are from [landscape.md](landscape.md).

Our olmOCR-Bench numbers come from a slice of the benchmark: 25 PDFs per category for the arms
that ran on everything, and the first 10 PDFs per category for the arms that ran on the core set
only (MinerU `standard`, PaddleOCR-VL; Marker `fast` on some categories). Each score is the
share of the category's tests passed. The interval is a bootstrap 95% interval over PDFs
(2,000 resamples, fixed seed). "Digital-only" is the mean of the six categories without the two
old-scan ones; Datalab reports it for runs without per-category numbers. Published runs are on
GPU (vLLM) unless stated; ours are CPU, with VLMs as llama.cpp GGUF builds.

## olmOCR-Bench: does the harness reproduce published scores?

| Our arm | Published run (source) | Category | Ours [95% CI] | PDFs | Published |
|---|---|---|---|---|---|
| Marker `nocr` | Marker 2.0.0 `fast --disable_ocr`, CPU (Datalab) | digital-only | 55.0 [50.4, 59.9] | 25 | 55.8 |
| | | table_tests | 44.8 [31.1, 59.0] | 25 | 46.1 |
| | | headers_footers | 94.6 [88.5, 100] | 25 | 92.8 |
| | | multi_column | 67.0 [53.8, 78.7] | 25 | 67.0 |
| | | long_tiny_text | 40.3 [21.7, 59.9] | 25 | 43.2 |
| Docling `default` | Docling default `PdfPipelineOptions()`, GPU (Datalab) | digital-only | 62.7 [57.8, 67.7] | 25 | 64.0 |
| MinerU `basic` (4.0.10) | MinerU `pipeline -m auto`, GPU (Datalab) | digital-only | 83.0 [79.3, 86.3] | 25 | 83.3 |
| Marker `fast` | Marker 2.0.0 `fast`, GPU (Datalab) | digital-only | 68.8 [62.8, 74.9] | 10 | 71.6 |
| | | arxiv_math | 15.2 [8.2, 23.3] | 25 | 23.4 |
| | | old_scans_math | 77.3 [64.2, 87.8] | 10 | 59.8 |
| PaddleOCR-VL 1.6 | PaddleOCR-VL 1.0, GPU (authors) | digital-only | 84.8 [78.0, 91.0] | 10 | 88.5 |
| | PaddleOCR-VL 1.6, H&F not reported (Falcon-OCR card) | arxiv_math | 75.5 [52.7, 93.2] | 10 | 87.8 |
| | | table_tests | 81.4 [57.4, 100] | 10 | 81.3 |
| | | long_tiny_text | 85.5 [80.5, 94.9] | 10 | 91.6 |
| MinerU `standard` (pipeline + MinerU2.5-Pro on tables, formulas, figures) | MinerU 2.5.4 full-page VLM (authors) | digital-only | 79.7 [73.3, 85.8] | 10 | 85.6 |
| | | table_tests | 62.8 [40.0, 86.2] | 10 | 84.9 |
| | MinerU2.5-Pro full-page VLM (Falcon-OCR card) | multi_column | 65.0 [46.2, 82.6] | 10 | 84.4 |

**Where the numbers agree.**
- *Matches within a point:* the three CPU or pipeline runs with a direct published match — Marker `nocr` on every category, Docling defaults and MinerU `basic` on the digital-only mean.
- *Inside our intervals:* Marker `fast` and PaddleOCR-VL, which run a VLM on llama.cpp on CPU here instead of vLLM on GPU.
- *What this rules out:* the runner, the normalisation and the slice do not bias the scores, and a GGUF build on CPU loses little against the published GPU runs.

**Where they differ.**
- **MinerU `standard` is not the full-page VLM that MinerU publishes.** It runs the layout pipeline and sends only tables, formulas and figures to the VLM. That is why it scores below the full-page MinerU2.5 rows on tables (63 vs 85) and on multi-column pages (65 vs 84), and why it is much faster. The intervals are wide (10 PDFs).
- **Marker `fast` scores above Datalab's run on old scans with math (77 vs 60) and below it on arXiv math (15 vs 23).** In `fast` mode the VLM handles only equations and garbled blocks, so the result depends on which blocks get flagged. The VLM serving also differs: llama.cpp here, vLLM there.
- **PaddleOCR-VL-1.6 is 6–12 points below the Falcon-OCR card on arXiv math and long tiny text**, and inside the interval on everything else. The card does not state its runner.

## OmniDocBench: does the ranking agree?

OmniDocBench is not run here (its data licence is non-commercial). Its ordering of the same tools is:
- **v1.6:** PaddleOCR-VL 1.6 96.3, MinerU2.5-Pro 95.8, the MinerU pipeline 86.5, Marker 1.8.2 78.4.
- **v1.0:** PP-StructureV3, then the MinerU pipeline, then Marker. Docling 2.14 and Unstructured are last, both with table TEDS of 61 or below.

Our core ranking agrees on:
- *Top pair:* MinerU with its VLM and PaddleOCR-VL-1.6 (0.82 and 0.78 on our probes).
- *Middle:* the MinerU pipeline (0.71).
- *Bottom of the layout-model tools:* Docling with defaults and Unstructured (0.61 and 0.55).

It disagrees on:
- **The order of the top two.** On our probes MinerU `standard` leads, because they weight page stitching and footnotes, and PaddleOCR-VL's default configuration drops footnotes. On the olmOCR slice PaddleOCR-VL leads (0.80 vs 0.76), as on OmniDocBench.
- **PP-StructureV3.** It is below the MinerU pipeline on our probes (0.65 vs 0.71) and on the olmOCR slice (0.68 vs 0.75), while OmniDocBench v1.0 ranks it first. It also drops footnotes by default (0.36 on footnote probes).

## CPU speed

The Docling technical report times three tools on an 8-vCPU AMD EPYC with OCR and tables on: Docling 2.5.2 at 3.1 s/page, MinerU 0.9.3 at 3.3, Unstructured 0.16.5 at 4.2, and Marker 0.3.10 above 16. Ours, on a 6-core/12-thread laptop CPU with newer versions:

| Tool | Configuration | s/page, our born-digital documents | s/page, all core pages |
|---|---|---|---|
| Docling | defaults | 4.2 | 4.8 |
| MinerU | `basic` | 2.5 | 4.6 |
| Unstructured | `hires` | 4.2 | 4.2 |
| Marker | `fast` (VLM via llama.cpp) | 11 | 38 |

The tools sit in the same order and within a factor of about 1.5 of the published times. Marker 2's `fast` mode calls a VLM that the 0.3 series did not have.

## What published numbers cannot check

No public benchmark scores the following, and our probes exist for them:
- **page stitching**: a sentence joined across a page break with no furniture in between;
- **footnotes** kept in the text and placed correctly;
- **heading levels** in markdown;
- **configuration sensitivity**: published runs are one configuration per tool, usually its defaults.

The Docling finding has no published counterpart: OCR off and the fast table model give the
same score as the defaults on born-digital documents at 3–4× less time, and the formula model
adds equations (0.76 → 0.84) at a cost that grows with the number of equations.
