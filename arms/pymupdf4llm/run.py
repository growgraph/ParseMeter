"""PyMuPDF4LLM ``to_markdown`` with its defaults (header/footer handling as shipped).

Variants:
  default  legacy heuristic path (``pymupdf_rag``), layout engine switched off
  layout   PyMuPDF-Layout GNN path (ONNX), the default when ``pymupdf-layout`` is installed
"""

from pathlib import Path

import pymupdf4llm

PACKAGES = ["pymupdf4llm", "pymupdf", "pymupdf-layout", "onnxruntime"]
EXTRA = {"license": "AGPL-3.0 or Artifex commercial (pymupdf, pymupdf4llm, pymupdf-layout)"}


def make(variant: str):
    if variant not in ("default", "layout"):
        raise ValueError(f"unknown variant {variant!r}")
    pymupdf4llm.use_layout(variant == "layout")

    def convert(pdf: Path, assets: Path) -> str:
        return pymupdf4llm.to_markdown(str(pdf))

    return convert
