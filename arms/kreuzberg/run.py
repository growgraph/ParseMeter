"""Kreuzberg 4.10 (Rust core, MIT): ``extract_file_sync`` with markdown output, defaults otherwise.

Variant ``default``: no layout model, OCR fallback left at its default (Tesseract, only
when a page has no text layer); result cache off so timings are real.
"""

import os
from pathlib import Path

from kreuzberg import ConcurrencyConfig, ExtractionConfig, extract_file_sync

PACKAGES = ["kreuzberg"]
EXTRA = {"license": "MIT"}
THREADS = int(os.environ.get("OMP_NUM_THREADS", os.cpu_count() or 4))


def make(variant: str):
    if variant != "default":
        raise ValueError(f"unknown variant {variant!r}")
    config = ExtractionConfig(
        output_format="markdown",
        use_cache=False,
        concurrency=ConcurrencyConfig(max_threads=THREADS),
    )

    def convert(pdf: Path, assets: Path) -> str:
        return extract_file_sync(pdf, config=config).content

    return convert
