"""A0: poppler pdftotext, reading order (no -layout) — the floor."""

import subprocess
from pathlib import Path

PACKAGES: list[str] = []
EXTRA = {"poppler": subprocess.run(["pdftotext", "-v"], capture_output=True, text=True).stderr.splitlines()[0]}


def make(variant: str):
    def convert(pdf: Path, assets: Path) -> str:
        return subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"], capture_output=True, text=True, check=True).stdout

    return convert
