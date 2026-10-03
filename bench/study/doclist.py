"""Write ``out/doclist.json``: our documents (sources.yaml) plus the olmOCR-Bench slice."""

import json

import pypdfium2
import yaml

from study.paths import DATA, OUT, ROOT, SOURCES
from study.regime import classify


CORE_EXCLUDE = {"apple-10k-2025", "sfix-10k-2026"}  # 190 pages of filings: fast arms only
CORE_OLMOCR_PER_CATEGORY = 10


def build() -> list[dict]:
    rows = []
    for d in yaml.safe_load(SOURCES.read_text())["documents"]:
        rows.append({"set": "docs", "id": d["id"], "path": d["path"], "pages": d["pages"], "core": d["id"] not in CORE_EXCLUDE, "regime": classify(ROOT / d["path"])})
    manifest = json.loads((DATA / "olmocr" / "manifest.json").read_text())
    for pdfs in manifest["pdfs"].values():
        for i, rel in enumerate(pdfs):
            path = DATA / "olmocr" / "bench_data" / "pdfs" / rel
            rows.append(
                {
                    "set": "olmocr",
                    "id": rel.removesuffix(".pdf"),
                    "path": str(path.relative_to(ROOT)),
                    "pages": len(pypdfium2.PdfDocument(path)),
                    "core": i < CORE_OLMOCR_PER_CATEGORY,
                    "regime": classify(path),
                }
            )
    return rows


def main() -> None:
    OUT.mkdir(exist_ok=True)
    rows = build()
    (OUT / "doclist.json").write_text(json.dumps(rows, indent=1))
    print(len(rows), "documents,", sum(r["pages"] for r in rows), "pages")
    for reg in ("digital", "scan_ocr", "scan"):
        sel = [r for r in rows if r["regime"] == reg]
        print(f"  {reg}: {len(sel)} documents, {sum(r['pages'] for r in sel)} pages")


if __name__ == "__main__":
    main()
