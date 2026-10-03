"""Compare arms on the documents a given set of arms has converted (coverage-matched).

    PYTHONPATH=. uv run python -m study.subset --covered-by mineru-standard,paddle-vl,docling-granite

Every arm is scored on the same documents: those with output from all ``--covered-by`` arms.
Arms lacking output for any of those documents are left out of the table.
"""

import argparse

import pandas as pd

from study.aggregate import OLMOCR_CATS, by_regime, load_scores
from study.probes import CATEGORIES


def _covered(s: pd.DataFrame) -> pd.Series:
    return ~s.msg.astype(str).str.startswith("no output")


def table(s: pd.DataFrame, cats: list[str], total: str, skip: tuple[str, ...] = ()) -> pd.DataFrame:
    t = s.pivot_table(index="arm", columns="category", values="passed", aggfunc="mean")
    cols = [c for c in cats if c in t.columns]
    t[total] = t[[c for c in cols if c not in skip]].mean(axis=1)
    extra = ["figure_text"] if "figure_text" in t.columns else []
    return t[[total, *cols, *extra]].sort_values(total, ascending=False)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--covered-by", required=True, help="comma-separated arm names")
    args = ap.parse_args()
    ref = args.covered_by.split(",")
    s = load_scores()
    s = s.assign(covered=_covered(s))
    by_doc = s.groupby(["arm", "set", "doc"]).covered.all()
    keys = set.intersection(*(set(by_doc[arm][by_doc[arm]].index) for arm in ref))
    full = [a for a in s.arm.unique() if all(by_doc.get((a, *k), False) for k in keys)]
    sub = s[s.arm.isin(full) & s.set.str.cat(s.doc, sep="|").isin({f"{k[0]}|{k[1]}" for k in keys})]
    docs, olm = sub[sub.set == "docs"], sub[sub.set == "olmocr"]
    print(f"documents: {sorted(d for st, d in keys if st == 'docs')}; olmOCR pages: {sum(st == 'olmocr' for st, _ in keys)}")
    print(f"arms with full coverage: {len(full)}; dropped: {sorted(set(s.arm.unique()) - set(full))}\n")
    if not docs.empty:
        print("## our probes\n\n" + table(docs, CATEGORIES, "macro").round(3).to_markdown() + "\n")
        print("tests per category: " + ", ".join(f"{k} {v}" for k, v in docs[docs.arm == ref[0]].category.value_counts().items()) + "\n")
    if not olm.empty:
        print("## olmOCR slice\n\n" + table(olm, OLMOCR_CATS, "overall", skip=("baseline",)).round(3).to_markdown() + "\n")
    print("## by regime (share of tests passed)\n\n" + by_regime(sub).round(3).to_markdown() + "\n")
    print("pages per regime: " + ", ".join(f"{k} {v}" for k, v in sub[sub.arm == ref[0]].drop_duplicates("doc").regime.value_counts().items()))


if __name__ == "__main__":
    main()
