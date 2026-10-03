"""Download a stratified slice of olmOCR-Bench (ODC-BY) at a pinned revision.

Writes ``../data/olmocr/bench_data/{<cat>.jsonl, pdfs/<cat>/*.pdf}`` in the layout
``olmocr.bench.benchmark`` expects, keeping only the tests of the sampled PDFs.
"""

import json
import random
import shutil
from pathlib import Path

from huggingface_hub import hf_hub_download

from study.paths import DATA

REPO = "allenai/olmOCR-bench"
REVISION = "54a96a6fb6a2bd3b297e59869491db4d3625b711"
CATEGORIES = ["arxiv_math", "headers_footers", "multi_column", "table_tests", "long_tiny_text", "old_scans_math"]
PER_CATEGORY = 25
SEED = 20261001


def _get(path: str) -> Path:
    return Path(hf_hub_download(REPO, path, repo_type="dataset", revision=REVISION))


def main() -> None:
    root = DATA / "olmocr" / "bench_data"
    root.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    manifest: dict[str, list[str]] = {}
    for cat in CATEGORIES:
        rows = [json.loads(line) for line in _get(f"bench_data/{cat}.jsonl").read_text().splitlines() if line.strip()]
        rows = [r for r in rows if r.get("checked") != "rejected"]
        pdfs = sorted({r["pdf"] for r in rows})
        chosen = sorted(rng.sample(pdfs, min(PER_CATEGORY, len(pdfs))))
        manifest[cat] = chosen
        keep = set(chosen)
        with open(root / f"{cat}.jsonl", "w") as fh:
            for r in rows:
                if r["pdf"] in keep:
                    fh.write(json.dumps(r) + "\n")
        for pdf in chosen:
            dst = root / "pdfs" / pdf
            if not dst.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(_get(f"bench_data/pdfs/{pdf}"), dst)
        print(cat, len(chosen), "pdfs", sum(1 for r in rows if r["pdf"] in keep), "tests")
    (DATA / "olmocr" / "manifest.json").write_text(
        json.dumps({"repo": REPO, "revision": REVISION, "seed": SEED, "license": "ODC-BY-1.0", "pdfs": manifest}, indent=2)
    )


if __name__ == "__main__":
    main()
