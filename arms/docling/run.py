"""Docling 2.132, markdown via ``export_to_markdown()``.

Variants. ``default`` is ``DocumentConverter()`` with every option at its default:
docling-parse backend, heron layout model, OCR (auto engine, RapidOCR here) on bitmap regions,
TableFormer accurate with cell matching. The ladder below changes one thing at a time from it:

  noocr       default, OCR off
  fast        noocr + TableFormer fast
  layoutonly  noocr + no table-structure model (tables come out as layout text)
  native      model-free ``NativePdfPipeline``: text cells in parser order, no layout model
  fullocr     default, OCR on the full page (ignores any text layer)
  formula     default + formula enrichment (CodeFormulaV2 -> LaTeX)
  lean        fast + formula enrichment: born-digital input, equations decoded
  textlayer   pypdfium2 backend, OCR off, text from the PDF text layer (``force_backend_text``)
  tuned       egret_large layout model, formula enrichment, picture classification and
              images, heading hierarchy
  granite     VLM pipeline, granite-docling-258M (transformers, CPU)
  glmocr      VLM pipeline, GLM-OCR 0.9B
  lightonocr  VLM pipeline, LightOnOCR-2-1B
"""

import os
from pathlib import Path

from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.datamodel import vlm_model_specs
from docling.datamodel.accelerator_options import AcceleratorOptions
from docling.datamodel.base_models import InputFormat
from docling.datamodel.layout_model_specs import DOCLING_LAYOUT_EGRET_LARGE
from docling.datamodel.pipeline_options import (
    HeadingHierarchyOptions,
    LayoutOptions,
    NativePdfPipelineOptions,
    OcrAutoOptions,
    OcrMode,
    PdfPipelineOptions,
    TableFormerMode,
    TableStructureOptions,
    ThreadedPdfPipelineOptions,
    VlmPipelineOptions,
)
from docling.document_converter import DocumentConverter, NativePdfFormatOption, PdfFormatOption
from docling.pipeline.vlm_pipeline import VlmPipeline

PACKAGES = ["docling", "docling-core", "docling-parse", "docling-ibm-models", "transformers", "torch"]
THREADS = int(os.environ.get("OMP_NUM_THREADS", os.cpu_count() or 4))
VLM = {
    "granite": vlm_model_specs.GRANITEDOCLING_TRANSFORMERS,
    "glmocr": vlm_model_specs.GLMOCR_TRANSFORMERS,
    "lightonocr": vlm_model_specs.LIGHTONOCR_TRANSFORMERS,
}
# One-setting departures from the standard pipeline's defaults.
LADDER = {
    "noocr": dict(do_ocr=False),
    "fast": dict(do_ocr=False, table_structure_options=TableStructureOptions(mode=TableFormerMode.FAST)),
    "layoutonly": dict(do_ocr=False, do_table_structure=False),
    "fullocr": dict(ocr_options=OcrAutoOptions(mode=OcrMode.FULL_PAGE)),
    "formula": dict(do_formula_enrichment=True),
    "lean": dict(do_ocr=False, table_structure_options=TableStructureOptions(mode=TableFormerMode.FAST),
                 do_formula_enrichment=True),
}


def make(variant: str):
    accel = AcceleratorOptions(num_threads=THREADS, device="cpu")
    if variant == "default":
        conv = DocumentConverter()
    else:
        if variant in LADDER:
            opts = ThreadedPdfPipelineOptions(accelerator_options=accel, **LADDER[variant])
            fmt = PdfFormatOption(pipeline_options=opts)
        elif variant == "native":
            fmt = NativePdfFormatOption(pipeline_options=NativePdfPipelineOptions(accelerator_options=accel))
        elif variant == "textlayer":
            opts = PdfPipelineOptions(accelerator_options=accel, do_ocr=False, force_backend_text=True)
            fmt = PdfFormatOption(pipeline_options=opts, backend=PyPdfiumDocumentBackend)
        elif variant == "tuned":
            opts = PdfPipelineOptions(
                accelerator_options=accel,
                layout_options=LayoutOptions(model_spec=DOCLING_LAYOUT_EGRET_LARGE),
                do_formula_enrichment=True,
                do_picture_classification=True,
                generate_picture_images=True,
                heading_hierarchy_options=HeadingHierarchyOptions(enabled=True),
            )
            fmt = PdfFormatOption(pipeline_options=opts)
        elif variant in VLM:
            opts = VlmPipelineOptions(accelerator_options=accel, vlm_options=VLM[variant])
            fmt = PdfFormatOption(pipeline_cls=VlmPipeline, pipeline_options=opts)
        else:
            raise ValueError(f"unknown variant {variant!r}")
        conv = DocumentConverter(format_options={InputFormat.PDF: fmt})
    conv.initialize_pipeline(InputFormat.PDF)

    def convert(pdf: Path, assets: Path) -> str:
        return conv.convert(pdf).document.export_to_markdown()

    return convert
