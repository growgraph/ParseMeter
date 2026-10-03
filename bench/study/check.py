"""Probe review: run one document's probes against every arm that has output, print a grid.

    PYTHONPATH=. uv run python -m study.check <doc> [--fails]

A test failing on every arm is suspect (typo, or a string the PDF does not contain);
read it against the page before trusting it.
"""

import argparse

from study.paths import OUT, PROBES
from study.probes import load_probes, run_test


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("doc")
    ap.add_argument("--fails", action="store_true", help="only tests failing on every arm")
    args = ap.parse_args()
    arms = sorted(p.name for p in OUT.iterdir() if (p / "docs" / f"{args.doc}.md").exists())
    mds = {a: (OUT / a / "docs" / f"{args.doc}.md").read_text(errors="replace") for a in arms}
    print("arms:", " ".join(f"[{i}]{a}" for i, a in enumerate(arms)))
    for row, test in load_probes(PROBES / f"{args.doc}.jsonl"):
        res = [run_test(test, mds[a]) for a in arms]
        marks = "".join("." if ok else "X" for ok, _ in res)
        if args.fails and any(ok for ok, _ in res):
            continue
        label = row.get("text") or row.get("before") or row.get("caption") or row.get("pattern") or row.get("cell") or row.get("math")
        print(f"{marks}  {row['id']} {row['category']:<13} {row['type']:<13} {str(label)[:70]}")
        if args.fails:
            print("      ", res[0][1][:150])


if __name__ == "__main__":
    main()
