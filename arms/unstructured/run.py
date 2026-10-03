"""Unstructured ``partition_pdf(strategy="hi_res", infer_table_structure=True)`` rendered to markdown.

Elements -> markdown (fixed, no tuning): Title ``#``; ListItem ``- ``; Table via
``metadata.text_as_html``; Image ``<!-- image -->``; FigureCaption as text; Formula
``$$…$$``; everything else as a paragraph. Only the element types unstructured itself
labels as page furniture — Header, Footer, PageNumber — are dropped (plus PageBreak markers).
"""

import os
from pathlib import Path

os.environ.setdefault("SCARF_NO_ANALYTICS", "true")
os.environ.setdefault("DO_NOT_TRACK", "true")
THREADS = int(os.environ.get("OMP_NUM_THREADS", os.cpu_count() or 4))
os.environ.setdefault("OMP_THREAD_LIMIT", str(THREADS))  # tesseract

from unstructured.partition.pdf import partition_pdf  # noqa: E402
from unstructured_inference.models import tables  # noqa: E402
from unstructured_inference.models.base import DEFAULT_MODEL, get_model  # noqa: E402

PACKAGES = ["unstructured", "unstructured-inference", "unstructured.pytesseract", "onnxruntime", "pdfminer.six"]
EXTRA = {
    "layout_model": f"unstructured-inference default ({DEFAULT_MODEL}, ONNX)",
    "ocr": "system tesseract",
    "table_model": "microsoft/table-transformer-structure-recognition (torch)",
    "license": "Apache-2.0 (unstructured, unstructured-inference, YOLOX layout weights); table-transformer weights MIT",
}
DROP = {"Header", "Footer", "PageNumber", "PageBreak"}


def to_markdown(elements) -> str:
    out = []
    for el in elements:
        cat = el.category
        text = (el.text or "").strip()
        if cat in DROP:
            continue
        if cat == "Title":
            out.append(f"# {text}" if text else "")
        elif cat == "ListItem":
            out.append(f"- {text}")
        elif cat == "Table":
            out.append(getattr(el.metadata, "text_as_html", None) or text)
        elif cat == "Image":
            out.append("<!-- image -->")
        elif cat == "Formula":
            out.append(f"$${text}$$" if text else "")
        else:
            out.append(text)
    return "\n\n".join(x for x in out if x) + "\n"


def make(variant: str):
    if variant != "hires":
        raise ValueError(f"unknown variant {variant!r}")
    get_model()  # download + load the default layout model once
    tables.load_agent()  # table-transformer, otherwise loaded lazily on the first table

    def convert(pdf: Path, assets: Path) -> str:
        elements = partition_pdf(filename=str(pdf), strategy="hi_res", infer_table_structure=True)
        return to_markdown(elements)

    return convert
