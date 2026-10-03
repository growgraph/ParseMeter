# PDF converter landscape (as of 2026-10)

Scope: document-to-markdown converters relevant to feeding a knowledge-graph extractor —
pipelines we run locally on CPU, self-hostable VLMs we can only cite (GPU), and hosted APIs.
Every version, licence and number below was read from a primary source (repository, PyPI,
Hugging Face model card or API, paper, or the benchmark's own leaderboard) on 2026-10-02;
source IDs in brackets resolve in [Sources](#sources). "unverified" means no primary source
was found; nothing is estimated. Published benchmark numbers are reproduced as published,
with who ran them and in which configuration — they are not re-measured here. Vendor-run
numbers (a tool's authors scoring their own tool) are marked as such.

## Table 1 — Tools

Kind: **P** = pipeline/library (layout + OCR + table models, text layer where available),
**V** = end-to-end or two-stage VLM, **A** = hosted API only. "CPU-feasible" records what the
source documents (a CPU path, an ONNX/llama.cpp backend, or a CPU device option), not speed.
Size is the parameter count from the model card or the Hugging Face safetensors total.

### Pipelines and libraries we run locally

| Tool | Kind | Version (date) | Code licence | Weights licence | Self-host / server | CPU-feasible | Size | Sources |
|---|---|---|---|---|---|---|---|---|
| Docling (standard PDF pipeline) | P | docling 2.132.0 (2026-10-01); docling-serve 1.36.0 (2026-10-01) | MIT | layout `docling-layout-heron` / `docling-layout-egret-large`: Apache-2.0; `docling-models` (TableFormer): tagged CDLA-Permissive-2.0 + Apache-2.0 | yes; docling-serve REST, MCP server | yes (default `pip install` is CPU torch) | layout 31–43 M (egret-large / heron) | [S27][S28][S11] |
| Docling VLM pipeline: granite-docling-258M | V (in P) | model 2025-09-17; `granite-docling-2stage-258m` 2026-03-11 | MIT (Docling) | Apache-2.0 | yes (transformers, vLLM, MLX, Ollama specs) | yes (CPU in `supported_devices`) | 258 M | [S28][S29] |
| Docling VLM pipeline: GLM-OCR | V (in P) | `GLMOCR_*` specs on docling main (2026-10) | MIT (Docling) | MIT (GLM-OCR); its own SDK adds PP-DocLayoutV3 (Apache-2.0) | yes | transformers on CPU possible; no CPU figure published | 0.9 B (card) / 1.33 B safetensors | [S28][S31] |
| Docling VLM pipeline: LightOnOCR-2-1B | V (in P) | `LIGHTONOCR_*` specs on docling main | MIT (Docling) | Apache-2.0 | yes | card example selects `cpu` when no GPU; no CPU figure published | 1.0 B | [S28][S32] |
| MinerU 4.x | P (+V) | mineru 4.0.10 (2026-09-29) | MinerU Open Source License (Apache-2.0 + additional terms, see Licence notes) | MinerU2.5-2509-1.2B: tagged AGPL-3.0; MinerU2.5-Pro-2604 / -2605-1.2B: Apache-2.0 | yes; `mineru server`, V1 API, router, Gradio | yes: `basic` tier ONNX CPU; `standard`/`advanced` ONNX + llama.cpp "CPU works, Vulkan recommended" | VLM 1.2 B | [S18][S19][S20][S21] |
| MinerU2.5 / MinerU2.5-Pro (VLM) | V | 2509 (2025-09-17); Pro-2604 (2026-04-02); Pro-2605 (2026-05-20) | (MinerU) | see row above | yes (vLLM, LMDeploy, llama.cpp) | via MinerU llama.cpp backend | 1.2 B | [S20][S21][S22] |
| Marker 2 | P (+V) | marker-pdf 2.0.0 (2026-07-20) | Apache-2.0 (was GPL-3.0 through 1.10.2) | Surya weights: modified AI Pubs OpenRAIL-M, US$5 M revenue/funding cap + non-compete clause | yes; FastAPI `marker_server` (no `--use_llm` over API) | yes: `fast` is the CPU default, VLM via llama.cpp; `--disable_ocr` is pure CPU | Surya OCR 2: 650 M; fast-mode layout "20M" rf-detr | [S10][S11][S12][S13] |
| Surya OCR 2 | V | surya-ocr 0.22.1 (2026-07-20); model `surya-ocr-2` 2026-05-14 | Apache-2.0 from 0.20.0 (2026-05-27); GPL-3.0 before | modified OpenRAIL-M, US$5 M cap + non-compete | yes (vLLM or llama.cpp server) | yes (llama.cpp; Apple Silicon figure published, no x86 figure) | 650 M (0.69 B safetensors) | [S12][S14][S15] |
| PaddleOCR PP-StructureV3 | P | paddleocr 3.7.0 (2026-06-11) | Apache-2.0 | Apache-2.0 | yes (PaddleX serving) | yes (CPU paddle wheel) | multi-model set | [S23][S57] |
| PaddleOCR-VL 1.0 / 1.5 / 1.6 | V (2-stage: PP-DocLayout + 0.9B VLM) | 1.0 2025-10-16; 1.5 2026-01-28; 1.6 2026-05-27 | Apache-2.0 | Apache-2.0 | yes (vLLM, SGLang, llama.cpp) | VLM via official GGUF (1.5 llama.cpp support 2026-03-06; 1.6-GGUF 2026-05-29) | 0.9 B (0.96 B safetensors) | [S24][S25][S26] |
| PyMuPDF4LLM (+ pymupdf-layout) | P | 1.28.2 (2026-08-06) | AGPL-3.0 or Artifex commercial | pymupdf-layout model: same dual licence | library only | yes ("CPU-only. No GPU required", pymupdf-layout summary) | — | [S34] |
| Kreuzberg / Xberg | P | kreuzberg 4.10.4 (2026-09-21, 4.x LTS); renamed **Xberg**, xberg 1.3.2 (2026-10-02, first release 1.0.1 on 2026-07-28) | MIT | uses PP-DocLayout-V3, RT-DETR, TATR, SLANet (per README); per-model licences unverified | yes; REST (`xberg serve`), MCP | yes ("CPU by default, no GPU required") | — | [S35] |
| Unstructured (open source) | P | unstructured 0.27.10 (2026-09-27) | Apache-2.0 | YOLOX layout Apache-2.0, Table Transformer MIT (local install metadata) | library; hosted platform separate | yes | — | [S36][S57] |
| GROBID | P (scholarly TEI) | 0.9.1 (2026-08-04) | Apache-2.0 | Apache-2.0 (local note) | yes; REST service, docker | yes | — | [S37][S57] |
| pdftotext (poppler) | P (text layer only) | poppler 26.09.0 (tarball on poppler.freedesktop.org; latest git tag listed via API 26.08.0, 2026-08-02) | GPL (poppler README: "licensed under the GPL, not the LGPL") | — | CLI | yes | — | [S38] |

### Self-hostable VLMs (cited only; GPU in all published configurations)

| Tool | Kind | Version (date) | Code licence | Weights licence | Self-host / server | CPU-feasible | Size | Sources |
|---|---|---|---|---|---|---|---|---|
| olmOCR 2 (Ai2) | V | toolkit olmocr 0.4.27 (2026-03-12); model olmOCR-2-7B-1025(-FP8), v0.4.0 2025-10-21 | Apache-2.0 | Apache-2.0 (fine-tune of Qwen2.5-VL-7B-Instruct) | yes (vLLM, docker) | no ("requires a GPU", README) | 7 B (8.29 B safetensors) | [S1][S39] |
| Chandra OCR 2 (Datalab) | V | chandra-ocr 0.2.0 (2026-03-18); model 2026-03-16 | Apache-2.0 | modified OpenRAIL-M, **US$2 M** revenue/funding cap + non-compete | yes (vLLM, HF) | unverified | 5.3 B | [S16][S17] |
| Chandra OCR 1 (0.1.x) | V | 2025-10-21 | Apache-2.0 | modified OpenRAIL-M | yes | unverified | 9 B (8.77 B) | [S1][S16] |
| dots.ocr / dots.mocr (rednote) | V | dots.ocr 2025-07-30; dots.mocr 2026-03-19 (listed as "dots.ocr 1.5" in Datalab tables) | MIT (repo) | MIT | yes (vLLM) | unverified | 3.0 B | [S40] |
| DeepSeek-OCR / DeepSeek-OCR-2 | V | 2025-10-17 / 2026-01-27 | MIT / Apache-2.0 | MIT / Apache-2.0 | yes (vLLM, HF) | unverified | 3 B MoE (~570 M active per jina-ocr-v1 card) | [S41][S48] |
| Nanonets-OCR2-3B | V | 2025-10-13 | — | **not stated on card**; base model Qwen2.5-VL-3B-Instruct is under the Qwen Research licence | yes (HF, vLLM) | unverified | 3.75 B | [S42] |
| MonkeyOCR (pro-1.2B / pro-3B) | V | pro models 2025-07-09 (cards updated 2026) | Apache-2.0 | **academic research and non-commercial evaluation only** | yes | unverified | 1.2 B / 3 B | [S43] |
| Qwen3-VL-8B (general VLM as OCR) | V | 2025-10-11 | Apache-2.0 | Apache-2.0 | yes | unverified | 8.77 B | [S45] |
| GLM-OCR (Zhipu / zai-org) | V (2-stage with PP-DocLayoutV3) | model 2026-01-30; SDK glmocr 0.1.5 (2026-04-08) | Apache-2.0 (SDK repo) | MIT | yes (vLLM, SGLang, Ollama, MLX) | unverified | 0.9 B | [S31] |
| LightOnOCR-1B-1025 / LightOnOCR-2-1B | V | 2025-10-20 / 2026-01-16 | — | Apache-2.0 | yes (vLLM, transformers ≥5) | see Docling row | 1.16 B / 1.0 B | [S32][S33] |
| Infinity-Parser-7B / Infinity-Parser2 (Pro, Flash) | V | 7B 2025-10-17; Parser2 2026-05-11 | — | Apache-2.0 | yes (vLLM) | unverified | 7 B / Pro 35.1 B / Flash 2.2 B | [S44] |
| HunyuanOCR (Tencent) | V | 2025-11-18 (1.5 referenced in third-party tables) | — | Tencent Hunyuan Community licence — **excludes EU, UK, South Korea** | yes | unverified | 1.1 B | [S46] |
| Falcon-OCR (TII) | V | 2026-02-22 | — | Apache-2.0 | yes (vLLM) | unverified | 270 M (+30 M layout) | [S47] |
| jina-ocr-v1 (Jina) | V | 2026-09-01 | — | **CC-BY-NC-4.0** | yes; also hosted (r.jina.ai) | unverified | 3 B MoE, ~570 M active | [S48] |
| Qianfan-OCR (Baidu) | V | 2026-03-18 | — | Apache-2.0 | yes | unverified | 4 B | [S49] |
| TeleOCR / OvisOCR2 / Unlimited-OCR | V | 2026-08-14 / 2026-07-13 / 2026-06-19 | — | Apache-2.0 / Apache-2.0 / MIT | yes | unverified | 1.4 B / 0.85 B / 3.3 B | [S50] |

### Hosted APIs (cited only)

| Tool | Kind | Version (date) | Code licence | Weights licence | Self-host / server | CPU-feasible | Size | Sources |
|---|---|---|---|---|---|---|---|---|
| Mistral OCR | A | docs list OCR 4.1 (`mistral-ocr-4-1`) as current, OCR 3 (25.12) active, OCR 4.0 retired 2026-09-30; 4.1 release date not stated | — | closed | no | n/a | — | [S51] |
| Azure Document Intelligence (Layout) | A (+ containers) | REST 2024-11-30 v4.0 GA; Layout container April 2025; no newer GA in the 2026 what's-new | — | closed | Layout/Read containers exist | n/a | — | [S52] |
| Google Document AI Layout Parser / Gemini | A | GA `pretrained-layout-parser-v1.0-2024-06-03`; preview v1.5 (Gemini 2.5, 2025-08-25), v1.6 (Gemini 3.0, 2025-12-01 / 2026-01-13), v3.1-lite (2026-08-11) | — | closed | no | n/a | — | [S53] |
| AWS Textract | A | no public model versioning; developer-guide history last entry 2022 | — | closed | no | n/a | — | [S54] |
| LlamaParse (LlamaIndex) | A | tiers "Cost Effective", "Agentic", "Agentic Plus" (ParseBench); client llama-cloud-services 0.6.94 (2026-02-13, MIT) | client MIT | closed | no | n/a | — | [S55][S56] |
| Reducto | A | "Reducto", "Reducto (Agentic)", "Reducto (r-1)" (ParseBench rows); no version page found | — | closed | no | n/a | — | [S55] |
| Datalab hosted API | A | modes Fast / Balanced / Accurate (ParseBench); runs Chandra variants (Surya card) | — | closed | on-prem licence offered | n/a | — | [S10][S15][S55] |
| Unstructured hosted platform | A | client unstructured-client 0.46.2 (2026-08-24, MIT) | client MIT | closed | no | n/a | — | [S56] |
| OpenAI GPT models as OCR | A | GPT-4o (olmOCR-Bench, OmniDocBench), GPT-5.2 2025-12-11 (OmniDocBench) | — | closed | no | n/a | — | [S3][S7] |

### Feature claims (sourced only)

Only claims stated by the tool's own source are listed; absence means "not stated", not "absent".

| Tool | Tables | Equations (LaTeX) | Headers/footers | Cross-page tables | Figures |
|---|---|---|---|---|---|
| Docling | table structure (README) | formulas (README) | — | — | image classification; chart understanding (README) |
| MinerU2.5-Pro | +5.54 TEDS over MinerU2.5 on OmniDocBench (card) | CDM 97.29 on dense formulas (card) | — | card: "under integration" | image and chart parsing (card) |
| Marker 2 | text-layer reconstruction, VLM fallback; `--use_llm` "merge tables across pages" | VLM OCR of equations and inline math (balanced; fast with `--ocr_inline_math`) | — | only with `--use_llm` | images extracted; with `--use_llm` + `--disable_image_extraction` replaced by description |
| PaddleOCR-VL-1.5/1.6 | yes | yes | — | "automatic cross-page table merging and cross-page paragraph heading recognition" (1.5 card) | charts, seals |
| olmOCR 2 | HTML tables | yes | "Automatically removes headers and footers" (README) | — | — |
| LightOnOCR-2 | yes | yes | **keeps** headers/footers by design (RLVR rewards their presence) | — | bbox variants localise images |
| Chandra 2 | HTML/markdown/JSON | yes | — | — | "Extracts images and diagrams, with captions and structured data" |
| dots.mocr | yes | yes | its olmOCR-Bench run deletes page-header/footer cells | — | "Parse Anything" (report title) |
| Unstructured | element types incl. Header/Footer | — | element-typed | — | — |

## Table 2 — olmOCR-Bench published numbers

**Benchmark version.** olmOCR-Bench has no version number. Data: HF dataset `allenai/olmOCR-bench`,
1,403 single-page PDFs, 7,010 unit tests in 7 categories plus one "baseline" test per PDF
(≈8,400 tests in total, as Marker and Surya count them). Last data change 2025-08-01; 2026
commits touch only README and `eval.yaml` [S3]. The PaddleOCR-VL report cites 1,402 PDFs [S24].
**Overall** is the unweighted mean of the 8 category pass rates including Headers & Footers and
Base (checked: olmOCR v0.4.0 and Marker 2 rows reproduce their published overall). Tables in
markdown cannot pass rowspan/colspan tests (HTML needed); math must render in KaTeX with `$`,
`$$`, `\(` or `\[` delimiters [S2].

Columns: ArXiv = arxiv_math, OSM = old_scans_math, Tab = table_tests, OS = old_scans,
H&F = headers_footers, MC = multi_column, LTT = long_tiny_text, Base = baseline. "—" = not published.

### 2a. All 8 categories (official definition)

| Tool (config) | ArXiv | OSM | Tab | OS | H&F | MC | LTT | Base | Overall | Who ran / source |
|---|---|---|---|---|---|---|---|---|---|---|
| Infinity-Parser2-Pro (35 B) | — | — | — | — | — | — | — | — | 87.6 | authors; per-category only as image [S44][S4] |
| Datalab hosted API | 90.4 | 90.2 | 90.7 | 54.6 | 91.6 | 83.7 | 92.3 | 99.9 | 86.7 ± 0.8 | Datalab (vendor) [S16] |
| Chandra 2 (5.3 B, vLLM) | 86.9 | 89.1 | 92.1 | 51.1 | 91.4 | 82.1 | 93.7 | 99.9 | 85.8 ± 0.8 | Datalab (vendor) [S16] |
| dots.mocr (= "dots.ocr 1.5") | 85.9 | 85.5 | 90.7 | 48.2 | 94.0 | 85.3 | 81.6 | 99.7 | 83.9 ± 0.9 | authors; header/footer cells deleted from output [S40] |
| jina-ocr-v1 | — | — | — | — | — | — | — | — | 83.4 | authors [S48] |
| Surya OCR 2 (0.65 B, `default` preset) | 88.3 | 81.4 | 86.6 | 41.8 | 92.5 | 82.4 | 93.7 | 99.7 | 83.3 | Datalab (vendor), "adjustments … for our output HTML format" [S15] |
| Chandra OCR 0.1.0 (9 B) | 82.2 | 80.3 | 88.0 | 50.4 | 90.8 | 81.2 | 92.3 | 99.9 | 83.1 ± 0.9 | authors (marked * by Ai2) [S1] |
| Infinity-Parser 7B | 84.4 | 83.8 | 85.0 | 47.9 | 88.7 | 84.2 | 86.4 | 99.8 | 82.5 | authors (*) [S1] |
| olmOCR v0.4.0 (olmOCR-2-7B-1025-FP8) | 83.0 | 82.3 | 84.9 | 47.7 | 96.1 | 83.7 | 81.9 | 99.7 | 82.4 ± 1.1 | Ai2 (vendor) [S1][S2] |
| Falcon-OCR | — | — | — | — | — | — | — | — | 80.3 | HF leaderboard entry citing the card; the card now shows a 7-category table (2b) [S4][S47] |
| PaddleOCR-VL (1.0, 0.9 B) | 85.7 | 71.0 | 84.1 | 37.8 | 97.0 | 79.9 | 85.7 | 98.5 | 80.0 ± 1.0 | authors, report Table 4 [S24] |
| Qianfan-OCR (4 B) | — | — | — | — | — | — | — | — | 79.8 | authors [S49] |
| dots.ocr (3 B) | 82.1 | 64.2 | 88.3 | 40.9 | 94.1 | 82.4 | 81.2 | 99.5 | 79.1 ± 1.0 | authors [S24][S40] |
| olmOCR v0.3.0 | 78.6 | 79.9 | 72.9 | 43.9 | 95.1 | 77.3 | 81.2 | 98.9 | 78.5 ± 1.1 | Ai2 [S2] |
| PaddleOCR-VL-1.5 | — | — | — | — | — | — | — | — | 78.5 | Infinity-Parser2 card (runner not stated) [S44] |
| MinerU2.5 | 81.1 | 74.0 | 85.1 | 33.8 | 96.3 | 65.5 | 89.8 | 94.4 | 77.5 ± 1.0 | PaddleOCR-VL team [S24] |
| Marker v1.10.0 | 83.8 | 69.7 | 74.8 | 32.3 | 86.6 | 79.4 | 85.7 | 99.6 | 76.5 ± 1.0 | Datalab (vendor) [S16] |
| Gemini Flash 3.5 (API) | — | — | — | — | — | — | — | — | 76.4 (digital-only 79.1) | Datalab [S10] |
| DeepSeek-OCR-2 | — | — | — | — | — | — | — | — | 76.3 | unverified: HF leaderboard cites a tweet; also in Infinity-Parser2 card [S4][S44] |
| Marker 1.10.1 (`force_ocr=True`, `use_llm=False`) | 83.8 | 66.8 | 72.9 | 33.5 | 86.6 | 80.0 | 85.7 | 99.3 | 76.1 ± 1.1 | Ai2 in-house [S1][S6] |
| Marker 2.0.0 `balanced` (GPU, B200) | 83.9 | 63.8 | 73.4 | 43.2 | 95.9 | 76.6 | 71.3 | 99.7 | 76.0 (digital-only 83.5) | Datalab (vendor) [S10] |
| DeepSeek-OCR | 77.2 | 73.6 | 80.2 | 33.3 | 96.1 | 66.4 | 79.4 | 99.8 | 75.7 ± 1.0 | Ai2 [S1] (Datalab run: 75.4 [S16]) |
| MinerU 2.5.4 (VLM backend, MinerU2.5-2509-1.2B) | 76.6 | 54.6 | 84.9 | 33.7 | 96.6 | 78.2 | 83.5 | 93.7 | 75.2 ± 1.1 | authors (*) [S1] |
| GLM-OCR | — | — | — | — | — | — | — | — | 75.2 | HF leaderboard ("GLM-OCR API evaluation"); no per-category source [S4] |
| MinerU `pipeline` backend (GPU, `-b pipeline -m auto`) | — | — | — | — | — | — | — | — | 72.7 (digital-only 83.3) | Datalab, MinerU version not stated [S10][S11] |
| Mistral OCR API (2025 model) | 77.2 | 67.5 | 60.6 | 29.3 | 93.6 | 71.3 | 77.1 | 99.4 | 72.0 ± 1.1 | Ai2 [S1] |
| Marker 1.8.2 | 76.0 | 57.9 | 57.6 | 27.8 | 84.9 | 72.9 | 84.6 | 99.1 | 70.1 ± 1.1 | attributed to olmOCR-Bench in [S24] |
| GPT-4o (anchored) | 53.5 | 74.5 | 70.0 | 40.7 | 93.8 | 69.3 | 60.6 | 96.8 | 69.9 ± 1.1 | Ai2 [S3] |
| Nanonets-OCR2-3B | 75.4 | 46.1 | 86.8 | 40.9 | 32.1 | 81.9 | 93.0 | 99.6 | 69.5 ± 1.1 | Ai2 [S1] |
| Marker 2.0.0 `fast` (GPU) | 23.4 | 59.8 | 69.0 | 43.2 | 93.2 | 76.0 | 68.3 | 99.9 | 66.6 (digital-only 71.6) | Datalab (vendor) [S10] |
| Qwen3-VL-8B | 70.2 | 75.1 | 45.6 | 37.5 | 89.1 | 62.1 | 43.0 | 94.3 | 64.6 ± 1.1 | Datalab [S16] |
| Gemini Flash 2 (anchored) | 54.5 | 56.1 | 72.1 | 34.2 | 64.7 | 61.5 | 71.5 | 95.6 | 63.8 ± 1.2 | Ai2 [S3] |
| MinerU v1.3.10 (pipeline) | 75.4 | 47.4 | 60.9 | 17.3 | 96.6 | 59.0 | 39.1 | 96.6 | 61.5 ± 1.1 | Ai2 [S3] |
| Marker v1.6.2 | 24.3 | 22.1 | 69.8 | 24.3 | 87.1 | 71.0 | 76.9 | 99.5 | 59.4 ± 1.1 | Ai2 [S3] |
| Docling default pipeline (GPU, `PdfPipelineOptions()` defaults) | — | — | — | — | — | — | — | — | 50.3 (digital-only 64.0) | Datalab, Docling version not stated [S10][S11] |
| GOT-OCR | 52.7 | 52.0 | 0.2 | 22.1 | 93.6 | 42.0 | 29.9 | 94.0 | 48.3 ± 1.1 | Ai2 [S3] |
| Marker 2.0.0 `fast --disable_ocr` (CPU) | 0.0 | 0.0 | 46.1 | 14.3 | 92.8 | 67.0 | 43.2 | 85.9 | 43.6 (digital-only 55.8) | Datalab (vendor) [S10] |
| liteparse (CPU) / no OCR | — | — | — | — | — | — | — | — | 22.4 / 20.4 | Datalab [S10] |

"Digital-only" (Datalab) = mean of the 6 non-scanned categories (excludes OS and OSM) [S11].
Datalab's Marker harness applies an output normalisation (`postprocess.py`: `<sub>/<sup>` →
Unicode, strip markdown escapes, drop image alt-text) worth "~+0.3" on balanced; `--raw` disables it [S11].

### 2b. Headers & Footers excluded (7-category mean)

Two sources report olmOCR-Bench without H&F, arguing it rewards omitting visible text. These
overall values are **not comparable** with 2a.

LightOnOCR paper, Table 1 (arXiv 2601.14251v2, 2026-06-30); baselines "taken from the
corresponding published works", DeepSeek-OCR and Mistral OCR 3 run by LightOn [S33]:

| Tool | ArXiv | OSM | Tab | OS | MC | LTT | Base | Overall (7) |
|---|---|---|---|---|---|---|---|---|
| LightOnOCR-2-1B | 89.6 | 85.6 | 89.0 | 42.2 | 84.8 | 91.4 | 99.6 | 83.2 ± 0.9 |
| dots.ocr-1.5 | 85.9 | 85.5 | 90.7 | 48.2 | 85.3 | 81.6 | 99.7 | 82.4 ± 0.9 |
| Chandra-9B | 82.2 | 80.3 | 88.0 | 50.4 | 81.2 | 92.3 | 99.9 | 81.7 ± 0.9 |
| olmOCR-2-8B | 82.9 | 82.1 | 84.3 | 48.3 | 84.3 | 81.4 | 99.7 | 80.4 ± 1.1 |
| Mistral OCR 3 API (LightOn run) | 85.6 | 69.7 | 85.5 | 43.5 | 81.2 | 88.5 | 99.7 | 79.1 ± 1.0 |
| PaddleOCR-VL | 85.7 | 71.0 | 84.1 | 37.8 | 79.9 | 85.7 | 98.5 | 77.5 ± 1.0 |
| LightOnOCR-1B-1025 | 81.4 | 71.6 | 76.4 | 35.2 | 80.0 | 88.7 | 99.5 | 76.1 ± 1.1 |
| MonkeyOCR-pro-3B | 83.8 | 68.8 | 74.7 | 36.1 | 76.6 | 80.1 | 95.3 | 73.6 ± 1.0 |
| DeepSeek-OCR (LightOn run) | 77.5 | 74.5 | 77.3 | 33.1 | 67.3 | 83.0 | 99.3 | 73.1 ± 1.0 |
| MinerU2.5 | 76.6 | 54.6 | 84.9 | 33.7 | 78.2 | 81.2 | 83.5 | 70.4 ± 1.0 |

LightOnOCR-2-1B scores 19.74 on H&F under the original definition (paper Table 5). The MinerU2.5
row's LTT/Base (81.2 / 83.5) do not match the authors' 83.5 / 93.7 in 2a; it looks like a
transcription shift in the paper.

Falcon-OCR card (runner of the third-party rows not stated) [S47]:

| Tool | ArXiv | OSM | Tab | OS | MC | LTT | Base | Average (7) |
|---|---|---|---|---|---|---|---|---|
| dots-mocr | 85.9 | 82.3 | 91.4 | 48.5 | 86.5 | 93.9 | 99.7 | 84.0 |
| chandra-ocr-2 | 86.5 | 83.4 | 90.2 | 49.0 | 83.9 | 93.4 | 99.9 | 83.8 |
| Falcon OCR 1.5 (e2e) | 83.6 | 83.6 | 88.9 | 41.8 | 85.1 | 94.1 | 99.9 | 82.4 |
| mineru2.5-pro | 87.1 | 83.4 | 86.0 | 36.1 | 84.4 | 93.7 | 99.5 | 81.5 |
| ovis-ocr-2 | 89.3 | 80.3 | 87.5 | 33.1 | 87.4 | 92.8 | 98.0 | 81.2 |
| Falcon OCR 1.5 (pipeline) | 80.0 | 75.5 | 88.6 | 42.2 | 85.4 | 93.0 | 99.8 | 80.6 |
| paddleocr-vl-1.6 | 87.8 | 68.8 | 81.3 | 39.0 | 84.1 | 91.6 | 98.4 | 78.7 |
| unlimited-ocr | 86.1 | 72.3 | 83.7 | 30.6 | 85.8 | 91.2 | 99.5 | 78.5 |
| hunyuan-ocr-1.5 | 86.9 | 75.1 | 78.7 | 35.2 | 80.6 | 89.6 | 99.8 | 78.0 |
| glm-ocr | 80.3 | 66.8 | 74.8 | 41.6 | 78.6 | 91.4 | 98.9 | 76.1 |
| deepseek-ocr-2 | 78.8 | 65.7 | 75.8 | 31.2 | 82.2 | 81.7 | 97.4 | 73.3 |

HF community leaderboard for the dataset (all entries `verified: false`, i.e. self-reported or
transcribed) [S4]: Infinity-Parser2-Pro 87.6, chandra-ocr-2 85.8, dots.mocr 83.9, jina-ocr-v1 83.4,
surya-ocr-2 83.3, LightOnOCR-2-1B 83.2 (7-category, see 2b), chandra 83.1, Infinity-Parser-7B 82.5,
Falcon-OCR 80.3, Qianfan-OCR 79.8, dots.ocr 79.1, DeepSeek-OCR-2 76.3, LightOnOCR-1B-1025 76.1,
DeepSeek-OCR 75.7, MinerU2.5 75.2, GLM-OCR 75.2. The Surya card notes the LightOnOCR entry
"uses a different benchmark methodology" [S15]; the leaderboard mixes 7- and 8-category means.

## Table 3 — OmniDocBench published numbers

**Versions.** v1.0 (Dec 2024; EN/ZH-split, edit-distance overall) → v1.5 (2025-09-25: +374 pages,
newspaper/note images at 200 DPI, hybrid text/formula matching, Overall =
((1 − TextEdit)·100 + TableTEDS + FormulaCDM) / 3) → v1.6 (2026-04-10: +296 harder pages,
Multi-Granularity Adaptive Matching, CDM reimplemented in Python; 1,651 pages total) → v1.7
(2026-04-30: Qianfan-OCR added, skills-based evaluation). The main-branch leaderboard caption
still reads "v1.6_full" (last README update 2026-09-11). OmniDocBench is maintained by
OpenDataLab, which also develops MinerU [S7].

Text and reading order are edit distances (lower is better); formula CDM and table TEDS higher is better.

### 3a. v1.6 (main-branch README, 2026-09-11) [S7]

| Tool | Type | Size | Overall | Text edit | Formula CDM | Table TEDS | Table TEDS-S | Read-order edit |
|---|---|---|---|---|---|---|---|---|
| TeleOCR | VLM | 1.2 B | 96.91 | 0.0267 | 96.59 | 96.82 | 98.18 | 0.1184 |
| OvisOCR2 | VLM | 0.8 B | 96.47 | 0.0265 | 97.49 | 94.58 | 96.98 | 0.1120 |
| PaddleOCR-VL-1.6 | VLM | 0.9 B | 96.34 | 0.0326 | 97.53 | 94.76 | 97.10 | 0.1278 |
| MinerU2.5-Pro (Pro-2605-1.2B) | VLM | 1.2 B | 95.75 | 0.036 | 97.45 | 93.42 | 95.92 | 0.120 |
| GLM-OCR | VLM | 0.9 B | 95.22 | 0.044 | 97.18 | 92.83 | 95.39 | 0.133 |
| PaddleOCR-VL-1.5 | VLM | 0.9 B | 94.93 | 0.038 | 96.89 | 91.67 | 94.37 | 0.130 |
| PaddleOCR-VL | VLM | 0.9 B | 94.18 | 0.040 | 95.91 | 90.65 | 93.74 | 0.135 |
| Unlimited-OCR | VLM | 3 B | 94.00 | 0.0394 | 95.72 | 90.21 | 93.36 | 0.1281 |
| Qianfan-OCR | VLM | 4 B | 93.90 | 0.04 | 95.08 | 90.53 | 93.31 | 0.13 |
| MinerU-2.5 | VLM | 1.2 B | 93.04 | 0.045 | 95.77 | 87.88 | 91.47 | 0.130 |
| Gemini 3 Pro | general VLM | — | 92.91 | 0.064 | 95.99 | 89.15 | 92.96 | 0.165 |
| Gemini 3 Flash | general VLM | — | 92.62 | 0.066 | 95.16 | 89.29 | 93.51 | 0.172 |
| dots.ocr | VLM | 3 B | 90.77 | 0.048 | 89.95 | 87.18 | 90.58 | 0.138 |
| DeepSeek-OCR 2 | VLM | 3 B | 90.25 | 0.050 | 91.84 | 83.89 | 87.75 | 0.144 |
| HunyuanOCR | VLM | 1 B | 89.95 | 0.088 | 87.68 | 91.01 | 93.23 | 0.171 |
| Qwen3-VL-235B | general VLM | 235 B | 89.78 | 0.063 | 92.55 | 83.07 | 86.75 | 0.166 |
| MonkeyOCR-pro-3B | VLM | 3 B | 88.57 | 0.074 | 88.74 | 84.35 | 88.62 | 0.189 |
| GPT-5.2 (2025-12-11) | general VLM | — | 86.59 | 0.114 | 88.21 | 82.95 | 87.93 | 0.193 |
| MinerU-Pipeline (MinerU 3.4.0) | pipeline | — | 86.47 | 0.055 | 83.07 | 81.88 | 88.68 | 0.153 |
| olmOCR (sglang; model version not stated) | VLM | 7 B | 85.74 | 0.139 | 88.10 | 83.00 | 87.17 | 0.216 |
| Mistral OCR (listed as version 2503) | API | — | 85.66 | 0.097 | 89.91 | 76.78 | 80.93 | 0.171 |
| Nanonets-OCR-s | VLM | 3 B | 83.61 | 0.108 | 81.46 | 80.18 | 84.51 | 0.213 |
| Marker (1.8.2) | pipeline | — | 78.44 | 0.157 | 85.24 | 65.77 | 73.24 | 0.243 |

Not on the v1.6 board: Docling, PP-StructureV3, granite-docling, Unstructured, PyMuPDF4LLM,
Chandra, LightOnOCR, olmOCR 2. jina-ocr-v1 reports 91.14 on v1.6 [S48]; Infinity-Parser2-Pro
93.95 [S44] (both self-reported).

### 3b. v1.5 (branch `v1_5`) [S8]

| Tool | Type | Size | Overall | Text edit | Formula CDM | Table TEDS | Table TEDS-S | Read-order edit |
|---|---|---|---|---|---|---|---|---|
| PaddleOCR-VL-1.5 | VLM | 0.9 B | 94.50 | 0.035 | 94.21 | 92.76 | 95.79 | 0.042 |
| GLM-OCR | VLM | 0.9 B | 94.35 | 0.045 | 93.65 | 93.89 | 96.50 | 0.047 |
| PaddleOCR-VL | VLM | 0.9 B | 92.86 | 0.035 | 91.22 | 90.89 | 94.76 | 0.043 |
| MinerU2.5 | VLM | 1.2 B | 90.93 | 0.045 | 88.86 | 88.44 | 92.42 | 0.044 |
| HunyuanOCR | VLM | 1 B | 90.57 | 0.085 | 86.01 | 94.19 | 95.96 | 0.082 |
| Gemini-3 Pro | general VLM | — | 90.17 | 0.062 | 88.79 | 87.83 | 93.32 | 0.074 |
| DeepSeek-OCR-2 | VLM | 3 B | 89.17 | 0.049 | 86.85 | 85.60 | 90.06 | 0.060 |
| MonkeyOCR-pro-3B | VLM | 3 B | 88.85 | 0.075 | 87.25 | 86.78 | 90.63 | 0.128 |
| dots.ocr | VLM | 3 B | 88.41 | 0.048 | 83.22 | 86.78 | 90.62 | 0.053 |
| DeepSeek-OCR | VLM | 3 B | 87.01 | 0.073 | 83.37 | 84.97 | 88.80 | 0.086 |
| PP-StructureV3 | pipeline | — | 86.73 | 0.073 | 85.79 | 81.68 | 89.48 | 0.073 |
| GPT5.2 | general VLM | — | 85.75 | 0.124 | 86.93 | 82.76 | 88.25 | 0.106 |
| Nanonets-OCR-s | VLM | 3 B | 85.59 | 0.093 | 85.90 | 80.14 | 85.57 | 0.108 |
| olmOCR | VLM | 7 B | 81.79 | 0.096 | 86.04 | 68.92 | 74.77 | 0.121 |
| Mathpix | API | — | 80.11 | 0.168 | 84.75 | 72.43 | 79.25 | 0.165 |
| Mistral OCR | API | — | 78.83 | 0.164 | 82.84 | 70.03 | 78.04 | 0.144 |
| MinerU2-pipeline | pipeline | — | 75.51 | 0.209 | 76.55 | 70.90 | 79.11 | 0.225 |
| GPT-4o | general VLM | — | 75.02 | 0.217 | 79.70 | 67.07 | 76.09 | 0.148 |
| Marker-1.8.2 | pipeline | — | 71.30 | 0.206 | 76.66 | 57.88 | 71.17 | 0.250 |

### 3c. v1.0 (branch `v1_0`, English columns only) — the only Docling/Unstructured entries [S9]

| Tool (version) | Overall edit ↓ | Text edit ↓ | Formula edit ↓ | Formula CDM | Table TEDS | Table edit ↓ | Read-order edit ↓ |
|---|---|---|---|---|---|---|---|
| PP-StructureV3 | 0.145 | 0.058 | 0.295 | 81.8 | 77.2 | 0.159 | 0.069 |
| MinerU-pipeline-2.1.1 | 0.162 | 0.072 | 0.313 | 79.2 | 77.4 | 0.166 | 0.097 |
| Marker-1.7.1 | 0.296 | 0.085 | 0.374 | 79.0 | 67.6 | 0.609 | 0.116 |
| SmolDocling-256M (transformers) | 0.493 | 0.262 | 0.753 | 32.1 | 44.9 | 0.729 | 0.227 |
| Unstructured-0.17.2 | 0.586 | 0.198 | 0.999 | — | 0 | 1 | 0.145 |
| Docling-2.14.0 | 0.589 | 0.416 | 0.999 | — | 61.3 | 0.627 | 0.313 |

Docling 2.14.0 predates formula enrichment defaults and current layout models; this row is a
historical reference, not a calibration target.

### Self-reported OmniDocBench figures that differ from the official board

| Tool | Card claims | Official board | Sources |
|---|---|---|---|
| GLM-OCR | 94.62 (v1.5) | 94.35 (v1.5) | [S31][S8] |
| MinerU2.5-Pro | 95.69 (v1.6) | 95.75 (v1.6) | [S21][S7] |
| MinerU2.5 | 92.98 (v1.6, in Pro card) | 93.04 (v1.6) | [S21][S7] |
| PaddleOCR-VL-1.6 | 96.33 (v1.6) | 96.34 (v1.6) | [S26][S7] |
| Qianfan-OCR | 93.12 (v1.5) | 93.90 (v1.6) | [S49][S7] |

### Other benchmarks (cited for context only)

**ParseBench** (LlamaIndex, arXiv 2604.08538; ~2,078 pages of insurance/finance/government
documents; dimensions Tables, Charts, Content Faithfulness, Semantic Formatting, Visual
Grounding; `leaderboard.csv` updated 2026-09-29). Vendor-authored: its sponsor's product leads.
Charts and visual grounding score near zero for tools that emit markdown without chart data or
boxes, so overall values mix capability coverage with quality [S55].

| Provider (ParseBench label) | Overall | Tables | Charts | Content faith. | Sem. format. | Visual ground. |
|---|---|---|---|---|---|---|
| LlamaParse Agentic | 87.01 | 88.88 | 88.68 | 91.78 | 81.44 | 84.25 |
| Infinity-Parser2-Pro | 74.28 | 86.4 | 61.3 | 89.7 | 59.1 | 74.9 |
| Reducto (Agentic) | 72.97 | 80.42 | 73.4 | 86.37 | 57.6 | 67.07 |
| MinerU2.5-Pro-2605-1.2B | 72.78 | 77.59 | 61.64 | 87.88 | 57.49 | 79.30 |
| Chandra-ocr-2 | 70.1 | 89.2 | 65.1 | 83.7 | 61.4 | 51.2 |
| Datalab Accurate | 69.95 | 90.29 | 62.40 | 83.87 | 40.79 | 72.38 |
| Mistral OCR 4 (Annotation) | 68.23 | 73.94 | 40.11 | 89.55 | 66.37 | 71.17 |
| PaddleOCR-VL-1.6 | 67.43 | 67.77 | 54.24 | 82.71 | 54.64 | 77.8 |
| Surya OCR 2 | 64.83 | 82.68 | 21.95 | 86.57 | 61.36 | 71.59 |
| Azure Document Intelligence (Layout) | 59.64 | 86.00 | 1.56 | 84.93 | 51.93 | 73.78 |
| PyMuPDF4LLM | 53.49 | 72.00 | 2.19 | 79.34 | 52.04 | 61.89 |
| Docling-models | 50.65 | 66.41 | 52.76 | 66.93 | 1.03 | 66.11 |
| Google Cloud Document AI | 50.39 | 55.10 | 1.44 | 83.65 | 50.51 | 61.26 |
| LightOnOCR-2-1B | 48 | 75.5 | 13.5 | 87.8 | 63.2 | 0 |
| AWS Textract | 47.88 | 84.58 | 5.97 | 74.76 | 3.71 | 70.36 |
| GLM-OCR | 29.6 | 66.1 | 1.7 | 78 | 2.3 | 0 |

**Docling technical report** (arXiv 2501.17887v1, 2025-01-27): CPU conversion time per page on
an 8-vCPU AMD EPYC 7R13 VM, 8 threads, OCR + table structure on — Docling 2.5.2 3.1 s, MinerU
0.9.3 3.3 s, Unstructured 0.16.5 4.2 s, Marker 0.3.10 > 16 s; on an L4 GPU MinerU 0.21 s,
Docling 0.49 s, Marker 0.86 s [S30]. All four tools have changed major versions since.

**granite-docling-258M card** (docling-eval; vs SmolDocling-256M-preview): full-page OCR edit
distance 0.45 (0.48), F1 0.84 (0.80); equation F1 0.968 (0.947); FinTabNet 150 dpi TEDS
structure 0.97 (0.82), with content 0.96 (0.76); layout mAP 0.27 (0.23) [S29].

**Published throughput** (GPU unless stated): Surya OCR 2 5.35 pages/s on one RTX 5090 (vLLM,
concurrency 128) and 0.108 pages/s on Apple Silicon (llama.cpp Metal, `--parallel 8`) [S15];
Chandra 2 1.44 pages/s on one H100 (vLLM, 96 sequences) [S16]; Marker 2 on one B200:
balanced 2.9, fast 7.4, fast-no-OCR (CPU-bound) 23.7 pages/s; MinerU pipeline 0.54; Docling 2.1
[S10]; LightOnOCR-2 5.71, olmOCR-2 FP8 3.28, DeepSeek-OCR 2.36, PaddleOCR-VL 2.14, Chandra 1.70,
dots.ocr 0.88 pages/s on one H100 [S33]. No x86 CPU throughput is published for any VLM in Table 1.

Not collected: READoc, CC-OCR (not found cited by the 2026 sources above as a primary comparison).

## Calibration targets

For comparing our CPU harness's per-category olmOCR-Bench-style scores with published ones.
Common caveats for every row: olmOCR-Bench is single-page PDFs scored by unit tests; Overall
includes Base and H&F; published runs are on GPU (vLLM) unless stated, while our VLM arms run
llama.cpp GGUF on CPU (quantisation and sampler may differ); and a tool's own run often applies
output normalisation (Marker `postprocess.py`, dots.mocr header/footer deletion, Surya HTML
adjustments).

### Marker

| Config (version, hardware) | ArXiv | OSM | Tab | OS | H&F | MC | LTT | Base | Overall | Who ran |
|---|---|---|---|---|---|---|---|---|---|---|
| 2.0.0 `balanced` — Surya VLM layout + full-page OCR on bad pages, inline math OCR; GPU B200 (vLLM); no LLM | 83.9 | 63.8 | 73.4 | 43.2 | 95.9 | 76.6 | 71.3 | 99.7 | 76.0 | Datalab [S10] |
| 2.0.0 `fast` — rf-detr layout + pdftext, VLM for equations and garbled blocks; GPU | 23.4 | 59.8 | 69.0 | 43.2 | 93.2 | 76.0 | 68.3 | 99.9 | 66.6 | Datalab [S10] |
| 2.0.0 `fast --disable_ocr` — no VLM; **CPU** | 0.0 | 0.0 | 46.1 | 14.3 | 92.8 | 67.0 | 43.2 | 85.9 | 43.6 | Datalab [S10] |
| 1.10.1 — `force_ocr=True`, `use_llm=False` (olmOCR runner) | 83.8 | 66.8 | 72.9 | 33.5 | 86.6 | 80.0 | 85.7 | 99.3 | 76.1 | Ai2 [S1][S6] |
| v1.10.0 — config not stated | 83.8 | 69.7 | 74.8 | 32.3 | 86.6 | 79.4 | 85.7 | 99.6 | 76.5 | Datalab [S16] |

Mapping: our `marker nocr` ↔ `fast --disable_ocr` (both CPU, same mode — the closest match in
this document); our `fast` and `balanced` ↔ the GPU rows, differing only in VLM serving (our
llama.cpp CPU vs vLLM). No published number uses `--use_llm`; the harness has an `accurate`
(balanced + LLM) recipe but no reported score [S11].

### MinerU

| Config (version, hardware) | ArXiv | OSM | Tab | OS | H&F | MC | LTT | Base | Overall | Who ran |
|---|---|---|---|---|---|---|---|---|---|---|
| MinerU 2.5.4, VLM backend (MinerU2.5-2509-1.2B) | 76.6 | 54.6 | 84.9 | 33.7 | 96.6 | 78.2 | 83.5 | 93.7 | 75.2 | MinerU authors [S1] |
| MinerU2.5 (VLM; version not stated) | 81.1 | 74.0 | 85.1 | 33.8 | 96.3 | 65.5 | 89.8 | 94.4 | 77.5 | PaddleOCR-VL team [S24] |
| MinerU2.5-Pro (7 categories, H&F excluded) | 87.1 | 83.4 | 86.0 | 36.1 | — | 84.4 | 93.7 | 99.5 | 81.5 (7-cat) | Falcon-OCR card [S47] |
| `pipeline` backend, `-m auto`, GPU (version not stated, ~2026-07) | — | — | — | — | — | — | — | — | 72.7 (digital-only 83.3) | Datalab [S10][S11] |
| v1.3.10 pipeline | 75.4 | 47.4 | 60.9 | 17.3 | 96.6 | 59.0 | 39.1 | 96.6 | 61.5 | Ai2 [S3] |

Mapping: our `mineru basic` (ONNX pipeline, MinerU 4.0.10) has no published per-category
analogue; the nearest is the Datalab `pipeline` overall (72.7, GPU, 3.x/4.x version unstated) and
the old v1.3.10 row. Our `mineru standard` (pipeline + MinerU2.5-Pro VLM for tables, formulas,
figures) sits between the pipeline and the full-page VLM rows; no published hybrid number.

### Docling

| Config (version, hardware) | Per-category | Overall | Who ran |
|---|---|---|---|
| Default `PdfPipelineOptions()` ("text layer for born-digital, OCR for image regions"), GPU, version not stated (~2026-07) | not published | 50.3 (digital-only 64.0) | Datalab [S10][S11] |
| Ai2 maintains `run_docling.py` (`docling <pdf>`, optional `--pipeline vlm --vlm-model smoldocling`) | not published | not published | [S6] |

No first-party olmOCR-Bench number from the Docling project was found. Model-level numbers for
the models Docling's VLM pipeline can call (not Docling-wrapped runs): GLM-OCR 75.2 overall
(HF leaderboard, no per-category) and 7-category per-category in 2b (Falcon card); LightOnOCR-2-1B
7-category per-category in 2b plus H&F 19.74.

### PaddleOCR-VL

| Config (version) | ArXiv | OSM | Tab | OS | H&F | MC | LTT | Base | Overall | Who ran |
|---|---|---|---|---|---|---|---|---|---|---|
| PaddleOCR-VL 1.0 (layout model + 0.9 B VLM), GPU | 85.7 | 71.0 | 84.1 | 37.8 | 97.0 | 79.9 | 85.7 | 98.5 | 80.0 | authors [S24] |
| PaddleOCR-VL-1.5 | — | — | — | — | — | — | — | — | 78.5 | Infinity-Parser2 card [S44] |
| PaddleOCR-VL-1.6 (H&F excluded) | 87.8 | 68.8 | 81.3 | 39.0 | — | 84.1 | 91.6 | 98.4 | 78.7 (7-cat) | Falcon-OCR card [S47] |

PP-StructureV3: no published olmOCR-Bench number found (Ai2 ships `run_paddlepaddle.py`
with `PP-OCRv5_server_det`, orientation/unwarping off, GPU, but reports no score [S6]).
OmniDocBench v1.5: 86.73 overall [S8]. Our `paddle vl` arm runs PaddleOCR-VL-1.6 GGUF via
llama.cpp; the 1.6 row above is the only published per-category reference and omits H&F.

### granite-docling-258M

No published olmOCR-Bench or OmniDocBench (v1.5/v1.6) score was found. Available references:
the card's docling-eval metrics (above) and SmolDocling-256M on OmniDocBench v1.0 (English
overall edit 0.493). A 2026 OCR-error paper reports Granite-Docling "performs poorly" on
degraded historical scans without an olmOCR-Bench figure (arXiv 2604.06160).

## Licence notes

- **Datalab (Marker, Surya, Chandra).** Code: Apache-2.0 since Surya 0.20.0 (2026-05-27) and
  Marker 2.0.0 (2026-07-20); GPL-3.0-or-later up to Surya 0.17.1 and Marker 1.10.2 [S13][S14].
  Weights: modified AI Pubs OpenRAIL-M. Surya `MODEL_LICENSE` forbids use "for any
  purpose" by an entity with more than US$5,000,000 gross revenue in the prior year or more than
  US$5,000,000 total equity/debt funding (personal and research use excepted), and by any entity
  that "provides … any product or service that competes with any product or service offered by"
  Datalab [S12] (the Marker README states the same US$5 M terms). Chandra 2's licence has the same structure with a **US$2,000,000** threshold [S16].
  Marker 2's CPU `--disable_ocr` path still loads Datalab's small layout model; its weights
  licence was not separately verified. An older `surya_layout` HF repo is tagged CC-BY-NC-SA-4.0 (2024).
- **MinerU.** Licence changed four times in 2026, starting from AGPL-3.0: Apache-2.0 (2026-03-20) → AGPL-3.0
  (2026-03-28) → Apache-2.0 (2026-04-14) → "MinerU Open Source License" (2026-04-17) [S19].
  Current text: Apache-2.0 plus (1) a separate commercial licence is required once the user and
  affiliates exceed 100 million MAU or US$20 million monthly revenue; (2) online services built on
  MinerU must state that MinerU is used; (3) automatic termination if either is breached [S19].
  Weights: MinerU2.5-2509-1.2B is tagged AGPL-3.0 on HF; MinerU2.5-Pro (2604, 2605) Apache-2.0 [S20][S21].
- **PyMuPDF, PyMuPDF4LLM, pymupdf-layout:** AGPL-3.0 or Artifex commercial [S34].
- **Poppler (pdftotext):** GPL ("programs which call Poppler must be licensed under the GPL as well") [S38].
- **MonkeyOCR weights:** "academic research and non-commercial evaluation only"; commercial use
  needs a written licence [S43].
- **jina-ocr-v1:** CC-BY-NC-4.0 [S48].
- **HunyuanOCR:** Tencent Hunyuan Community licence "does not apply in the European Union, United
  Kingdom and South Korea"; use or output outside the Territory is unlicensed; >100 M MAU needs
  a separate grant [S46].
- **Nanonets-OCR2-3B:** no licence on the model card; its base, Qwen2.5-VL-3B-Instruct, carries the
  Qwen Research licence [S42].
- **GLM-OCR:** weights MIT, but the document pipeline adds PP-DocLayoutV3 (Apache-2.0) [S31].
- **Benchmarks:** olmOCR-Bench data ODC-BY-1.0 (AI2 responsible-use guidelines) [S3]; ParseBench
  code and dataset Apache-2.0 [S55]; OmniDocBench repo Apache-2.0, HF dataset card has no licence field [S7].

## Gaps (unverified)

- No olmOCR-Bench score from the Docling project, IBM (granite-docling), PaddlePaddle
  (PP-StructureV3), Unstructured, PyMuPDF4LLM, Kreuzberg/Xberg, GROBID or pdftotext.
- Docling (50.3) and MinerU pipeline (72.7) olmOCR-Bench numbers come from a competitor
  (Datalab) without tool versions or per-category scores.
- DeepSeek-OCR-2 76.3 has no primary source (a tweet and a third-party card).
- Per-category olmOCR-Bench for PaddleOCR-VL-1.5, GLM-OCR (8-category), jina-ocr-v1,
  Qianfan-OCR and Infinity-Parser2 exists only as images or not at all.
- Mistral OCR 4.1 release date; Reducto, Textract and Datalab API model versions.
- CPU throughput for any VLM on x86 (only Apple Silicon/Metal for Surya OCR 2).
- Licence of Marker 2's rf-detr layout weights and of Kreuzberg/Xberg's bundled layout/table models.

## Sources

All accessed 2026-10-02.

- [S1] allenai/olmocr README (news, benchmark table): https://github.com/allenai/olmocr ; releases via GitHub API (v0.4.27, 2026-03-12)
- [S2] olmOCR-Bench README: https://github.com/allenai/olmocr/tree/main/olmocr/bench
- [S3] olmOCR-bench dataset card and commit history: https://huggingface.co/datasets/allenai/olmOCR-bench
- [S4] olmOCR-bench HF community leaderboard: https://huggingface.co/api/datasets/allenai/olmOCR-bench/leaderboard (shown on the dataset page)
- [S5] olmOCR 2: Unit Test Rewards for Document OCR, arXiv 2510.19817: https://arxiv.org/abs/2510.19817 ; olmOCR, arXiv 2502.18443: https://arxiv.org/abs/2502.18443
- [S6] olmOCR-Bench runners (`run_marker.py`, `run_docling.py`, `run_mineru.py`, `run_paddlepaddle.py`, `run_paddlevl.py`): https://github.com/allenai/olmocr/tree/main/olmocr/bench/runners
- [S7] OmniDocBench README (main; updates, v1.6 leaderboard, model versions): https://github.com/opendatalab/OmniDocBench ; paper arXiv 2412.07626
- [S8] OmniDocBench v1.5 leaderboard: https://github.com/opendatalab/OmniDocBench/tree/v1_5
- [S9] OmniDocBench v1.0 leaderboard: https://github.com/opendatalab/OmniDocBench/tree/v1_0
- [S10] Marker README (Performance, Benchmarks, modes, licence): https://github.com/datalab-to/marker
- [S11] Marker benchmark harness and competitor runners: https://github.com/datalab-to/marker/tree/master/benchmarks
- [S12] Surya MODEL_LICENSE: https://github.com/datalab-to/surya/blob/master/MODEL_LICENSE ; Marker MODEL_LICENSE: https://github.com/datalab-to/marker/blob/master/MODEL_LICENSE
- [S13] marker-pdf on PyPI (1.10.2 GPL-3.0-or-later; 2.0.0 Apache-2.0): https://pypi.org/project/marker-pdf/ ; LICENSE commit "Release prep … Apache 2.0" (2026-07-17)
- [S14] surya-ocr on PyPI (0.17.1 GPL; 0.20.0+ Apache-2.0): https://pypi.org/project/surya-ocr/
- [S15] Surya OCR 2 model card: https://huggingface.co/datalab-to/surya-ocr-2
- [S16] Chandra OCR 2 model card and LICENSE: https://huggingface.co/datalab-to/chandra-ocr-2 ; Chandra 1: https://huggingface.co/datalab-to/chandra
- [S17] Chandra repository: https://github.com/datalab-to/chandra
- [S18] MinerU README (4.0 tiers, engines): https://github.com/opendatalab/MinerU ; PyPI https://pypi.org/project/mineru/
- [S19] MinerU LICENSE.md and its commit history: https://github.com/opendatalab/MinerU/blob/master/LICENSE.md
- [S20] MinerU2.5-2509-1.2B card: https://huggingface.co/opendatalab/MinerU2.5-2509-1.2B
- [S21] MinerU2.5-Pro cards: https://huggingface.co/opendatalab/MinerU2.5-Pro-2604-1.2B , https://huggingface.co/opendatalab/MinerU2.5-Pro-2605-1.2B
- [S22] MinerU2.5 report arXiv 2509.22186; MinerU2.5-Pro report arXiv 2604.04771
- [S23] PaddleOCR repository and PyPI (3.7.0): https://github.com/PaddlePaddle/PaddleOCR
- [S24] PaddleOCR-VL report, arXiv 2510.14528 (Table 4): https://arxiv.org/abs/2510.14528 ; card https://huggingface.co/PaddlePaddle/PaddleOCR-VL
- [S25] PaddleOCR-VL-1.5 card: https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5
- [S26] PaddleOCR-VL-1.6 card and GGUF: https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6 , https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6-GGUF
- [S27] Docling README, PyPI, docling-serve releases: https://github.com/docling-project/docling , https://github.com/docling-project/docling-serve ; layout models https://huggingface.co/docling-project/docling-layout-heron , https://huggingface.co/docling-project/docling-layout-egret-large , https://huggingface.co/docling-project/docling-models
- [S28] Docling VLM model specs: https://github.com/docling-project/docling/blob/main/docling/datamodel/vlm_model_specs.py
- [S29] granite-docling-258M card: https://huggingface.co/ibm-granite/granite-docling-258M ; 2-stage: https://huggingface.co/docling-project/granite-docling-2stage-258m
- [S30] Docling technical report, arXiv 2501.17887v1: https://arxiv.org/abs/2501.17887
- [S31] GLM-OCR card: https://huggingface.co/zai-org/GLM-OCR ; SDK https://github.com/zai-org/GLM-OCR ; report arXiv 2603.10910
- [S32] LightOnOCR-2-1B card: https://huggingface.co/lightonai/LightOnOCR-2-1B ; LightOnOCR-1B-1025: https://huggingface.co/lightonai/LightOnOCR-1B-1025
- [S33] LightOnOCR paper, arXiv 2601.14251v2 (2026-06-30): https://arxiv.org/html/2601.14251v2
- [S34] pymupdf4llm and pymupdf-layout on PyPI: https://pypi.org/project/pymupdf4llm/ , https://pypi.org/project/pymupdf-layout/
- [S35] kreuzberg on PyPI: https://pypi.org/project/kreuzberg/ ; Xberg README and releases: https://github.com/xberg-io/xberg ; https://pypi.org/project/xberg/
- [S36] Unstructured: https://github.com/Unstructured-IO/unstructured ; https://pypi.org/project/unstructured/
- [S37] GROBID: https://github.com/kermitt2/grobid (release 0.9.1)
- [S38] Poppler: https://poppler.freedesktop.org/ ; README https://gitlab.freedesktop.org/poppler/poppler
- [S39] olmOCR-2-7B-1025 card: https://huggingface.co/allenai/olmOCR-2-7B-1025
- [S40] dots.ocr card https://huggingface.co/rednote-hilab/dots.ocr ; dots.mocr card https://huggingface.co/rednote-hilab/dots.mocr ; reports arXiv 2512.02498, 2603.13032
- [S41] DeepSeek-OCR https://huggingface.co/deepseek-ai/DeepSeek-OCR ; DeepSeek-OCR-2 https://huggingface.co/deepseek-ai/DeepSeek-OCR-2
- [S42] Nanonets-OCR2-3B card https://huggingface.co/nanonets/Nanonets-OCR2-3B ; Qwen2.5-VL-3B-Instruct (licence `qwen-research`) https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct
- [S43] MonkeyOCR README, "License and Commercial Use": https://github.com/Yuliang-Liu/MonkeyOCR
- [S44] Infinity-Parser-7B https://huggingface.co/infly/Infinity-Parser-7B ; Infinity-Parser2-Pro https://huggingface.co/infly/Infinity-Parser2-Pro ; report arXiv 2506.03197
- [S45] Qwen3-VL-8B-Instruct: https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct
- [S46] HunyuanOCR card and LICENSE: https://huggingface.co/tencent/HunyuanOCR
- [S47] Falcon-OCR card: https://huggingface.co/tiiuae/Falcon-OCR
- [S48] jina-ocr-v1 card: https://huggingface.co/jinaai/jina-ocr-v1
- [S49] Qianfan-OCR card: https://huggingface.co/baidu/Qianfan-OCR
- [S50] https://huggingface.co/StarDoc-AI/TeleOCR , https://huggingface.co/ATH-MaaS/OvisOCR2 , https://huggingface.co/baidu/Unlimited-OCR
- [S51] Mistral models overview: https://docs.mistral.ai/getting-started/models/models_overview/
- [S52] Azure Document Intelligence, What's new (updated 2026-07-10): https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/whats-new
- [S53] Google Document AI Layout Parser: https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk
- [S54] Amazon Textract document history: https://docs.aws.amazon.com/textract/latest/dg/document-history.html
- [S55] ParseBench README and leaderboard.csv: https://github.com/run-llama/ParseBench ; paper arXiv 2604.08538
- [S56] llama-cloud-services and unstructured-client on PyPI: https://pypi.org/project/llama-cloud-services/ , https://pypi.org/project/unstructured-client/
- [S57] Local arm notes (installed versions, package licence metadata): [arms/](arms/)
