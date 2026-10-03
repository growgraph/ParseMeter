"""Score arms: our probes over whole-document markdown, plus the olmOCR-Bench slice.

    PYTHONPATH=. uv run python -m study.score [arm ...] [--set docs|olmocr|all]

Writes ``out/scores/<arm>.jsonl`` (one row per test). A document without output (error,
budget) or whose output holds no text (only image placeholders, or nothing) fails all of its
probes, and the row says why; otherwise every ``absent`` probe would pass on an empty file.
"""

import argparse
import json
import re
from pathlib import Path

from olmocr.bench.tests import BaselineTest, load_tests

from study.paths import DATA, OUT, PROBES
from study.probes import load_probes, run_test

OLMOCR = DATA / "olmocr" / "bench_data"


def arms() -> list[str]:
    return sorted(p.name for p in OUT.iterdir() if (p / "env.json").exists())


def _status(arm: str) -> dict[str, str]:
    st: dict[str, str] = {}
    log = OUT / arm / "timing.jsonl"
    if log.exists():
        for line in log.read_text().splitlines():
            r = json.loads(line)
            st[r["id"]] = r["status"]
    return st


def _md(path: Path) -> str | None:
    return path.read_text(errors="replace") if path.exists() else None


def has_text(md: str) -> bool:
    """Whether markdown carries any text once image placeholders and comments are removed."""
    return re.search(r"\w", re.sub(r"<!--.*?-->|!\[[^\]]*\]\([^)]*\)|<img[^>]*>", "", md, flags=re.S)) is not None


def score_docs(arm: str, docs: list[str] | None = None) -> list[dict]:
    st = _status(arm)
    rows = []
    for f in sorted(PROBES.glob("*.jsonl")):
        doc = f.stem
        if docs and doc not in docs:
            continue
        md = _md(OUT / arm / "docs" / f"{doc}.md")
        for row, test in load_probes(f):
            if md is None:
                ok, msg = False, f"no output ({st.get(doc, 'not run')})"
            elif not has_text(md):
                ok, msg = False, "output holds no text"
            else:
                ok, msg = run_test(test, md)
            rows.append({"arm": arm, "set": "docs", "doc": doc, "id": row["id"], "category": row["category"], "type": row["type"], "passed": ok, "msg": msg})
    return rows


def score_olmocr(arm: str) -> list[dict]:
    st = _status(arm)
    rows = []
    seen_pdfs: set[str] = set()
    for f in sorted(OLMOCR.glob("*.jsonl")):
        cat = f.stem
        tests = load_tests(str(f))
        pdfs = sorted({t.pdf for t in tests})
        for pdf in pdfs:
            if pdf not in seen_pdfs and not any(t.type == "baseline" for t in tests if t.pdf == pdf):
                tests.append(BaselineTest(id=f"{pdf}_baseline", pdf=pdf, page=1, type="baseline"))
            seen_pdfs.add(pdf)
        for t in tests:
            doc = t.pdf.removesuffix(".pdf")
            md = _md(OUT / arm / "olmocr" / f"{doc}.md")
            ok, msg = (False, f"no output ({st.get(doc, 'not run')})") if md is None else run_test(t, md)
            rows.append({"arm": arm, "set": "olmocr", "doc": doc, "id": t.id, "category": "baseline" if t.type == "baseline" else cat, "type": t.type, "passed": ok, "msg": msg})
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("arms", nargs="*")
    ap.add_argument("--set", default="all", choices=["docs", "olmocr", "all"])
    ap.add_argument("--doc", action="append")
    args = ap.parse_args()
    (OUT / "scores").mkdir(exist_ok=True)
    for arm in args.arms or arms():
        rows = []
        if args.set in ("docs", "all"):
            rows += score_docs(arm, args.doc)
        if args.set in ("olmocr", "all"):
            rows += score_olmocr(arm)
        suffix = "" if args.set == "all" and not args.doc else f".{args.set}" + (".partial" if args.doc else "")
        with open(OUT / "scores" / f"{arm}{suffix}.jsonl", "w") as fh:
            for r in rows:
                fh.write(json.dumps(r) + "\n")
        n = len(rows)
        print(f"{arm}: {sum(r['passed'] for r in rows)}/{n} passed")


if __name__ == "__main__":
    main()
