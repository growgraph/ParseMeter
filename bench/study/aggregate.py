"""Tables from ``out/scores/*.jsonl`` + timing logs -> ``out/summary/*.csv`` and a markdown digest.

    PYTHONPATH=. uv run python -m study.aggregate
"""

import json
from functools import cache

import pandas as pd
import yaml

from study import completeness
from study.paths import OUT, SOURCES
from study.probes import CATEGORIES


def _groups() -> dict[str, list[str]]:
    """Document ids per ``group`` in sources.yaml (papers, reports, scanned)."""
    out: dict[str, list[str]] = {}
    for d in yaml.safe_load(SOURCES.read_text())["documents"]:
        out.setdefault(d["group"], []).append(d["id"])
    return out


GROUPS = _groups()
OLMOCR_CATS = ["arxiv_math", "headers_footers", "long_tiny_text", "multi_column", "old_scans_math", "table_tests", "baseline"]


REGIMES = ["digital", "scan_ocr", "scan"]


def load_scores() -> pd.DataFrame:
    """All score rows, with each document's regime (``study.regime``) from ``out/doclist.json``."""
    frames = [pd.read_json(f, lines=True) for f in sorted((OUT / "scores").glob("*.jsonl")) if "." not in f.stem]
    if not frames:
        return pd.DataFrame()
    s = pd.concat(frames, ignore_index=True)
    regime = {d["id"]: d.get("regime", "digital") for d in json.loads((OUT / "doclist.json").read_text())}
    return s.assign(regime=s.doc.map(regime))


def by_regime(s: pd.DataFrame) -> pd.DataFrame:
    """arm x regime: share of tests passed (test-weighted, baseline tests excluded)."""
    t = s[s.category != "baseline"].pivot_table(index="arm", columns="regime", values="passed", aggfunc="mean")
    return t[[r for r in REGIMES if r in t.columns]].sort_values(t.columns[0], ascending=False)


def by_kind(s: pd.DataFrame) -> pd.DataFrame:
    """arm x {digital, scanned}: like ``by_regime`` with the two scan regimes pooled."""
    k = s[s.category != "baseline"].assign(kind=lambda d: d.regime.where(d.regime == "digital", "scanned"))
    t = k.pivot_table(index="arm", columns="kind", values="passed", aggfunc="mean")
    return t[[c for c in ("digital", "scanned") if c in t.columns]].sort_values(t.columns[0], ascending=False)


def load_timing() -> pd.DataFrame:
    rows = []
    for arm_dir in sorted(OUT.iterdir()):
        log = arm_dir / "timing.jsonl"
        if not log.exists():
            continue
        seen = {}
        for line in log.read_text().splitlines():
            r = json.loads(line)
            seen[r["id"]] = r  # last attempt wins
        for r in seen.values():
            rows.append({"arm": arm_dir.name, **r})
    return pd.DataFrame(rows)


@cache
def _ref(doc_id: str, path: str):
    return completeness.reference(doc_id, path)


def completeness_table(arms: list[str]) -> pd.DataFrame:
    rows = []
    for d in completeness.docs():
        ref = _ref(d["id"], d["path"])
        for arm in arms:
            md = OUT / arm / "docs" / f"{d['id']}.md"
            if md.exists():
                rows.append({"arm": arm, "doc": d["id"], **completeness.score(ref, completeness.words(md.read_text(errors="replace")))})
    return pd.DataFrame(rows)


def probe_table(docs: pd.DataFrame) -> pd.DataFrame:
    """arm x category share passed, plus the macro mean over categories (figure_text kept apart)."""
    t = docs.pivot_table(index="arm", columns="category", values="passed", aggfunc="mean")
    cats = [c for c in CATEGORIES if c in t.columns]
    t["macro"] = t[cats].mean(axis=1)
    return t[["macro", *cats] + (["figure_text"] if "figure_text" in t.columns else [])].sort_values("macro", ascending=False)


def olmocr_table(olm: pd.DataFrame) -> pd.DataFrame:
    """arm x olmOCR category share passed, plus the mean of the non-baseline categories."""
    t = olm.pivot_table(index="arm", columns="category", values="passed", aggfunc="mean")
    cats = [c for c in OLMOCR_CATS if c in t.columns]
    t["overall"] = t[[c for c in cats if c != "baseline"]].mean(axis=1)
    return t[["overall", *cats]].sort_values("overall", ascending=False)


def core_scores(s: pd.DataFrame) -> pd.DataFrame:
    """Rows on core documents, for the arms that converted every core document (like-for-like)."""
    core = {d["id"] for d in json.loads((OUT / "doclist.json").read_text()) if d.get("core")}
    c = s[s.doc.isin(core)]
    missing = c[c.msg.astype(str).str.startswith("no output")].arm.unique()
    return c[~c.arm.isin(missing)]


def main() -> None:
    summ = OUT / "summary"
    summ.mkdir(exist_ok=True)
    s = load_scores()
    docs = s[s.set == "docs"]
    olm = s[s.set == "olmocr"]

    # our probes: arm x category, separately for each corpus group and overall (macro over categories)
    tables = {}
    for gname, gdocs in {"all": None, **GROUPS}.items():
        tables[f"probes_{gname}"] = probe_table(docs if gdocs is None else docs[docs.doc.isin(gdocs)])
    counts = docs.groupby(["arm", "category"]).size().unstack(fill_value=0)
    tables["probe_counts"] = counts

    # olmOCR-Bench slice: per category mean and the mean of categories
    if not olm.empty:
        tables["olmocr"] = olmocr_table(olm)
        tables["olmocr_by_regime"] = by_regime(olm)
    if docs.regime.nunique() > 1:
        tables["probes_by_regime"] = by_regime(docs)

    # core subset: every arm with full core coverage, on the same documents
    c = core_scores(s)
    if not c.empty:
        cd, co = c[c.set == "docs"], c[c.set == "olmocr"]
        tables["core_probes"] = probe_table(cd)
        for gname, gdocs in GROUPS.items():
            if cd.doc.isin(gdocs).any():
                tables[f"core_probes_{gname}"] = probe_table(cd[cd.doc.isin(gdocs)])
        tables["core_olmocr"] = olmocr_table(co)
        tables["core_by_regime"] = by_regime(c)
        tables["core_by_kind"] = by_kind(c)

    # born-digital documents (the 10-Ks included), arms that converted every one of them
    dd = docs[docs.regime == "digital"]
    gaps = dd[dd.msg.astype(str).str.startswith("no output")].arm.unique()
    if not dd.empty:
        tables["digital_probes"] = probe_table(dd[~dd.arm.isin(gaps)])

    # cost
    tm = load_timing()
    if not tm.empty:
        ok = tm[tm.status == "ok"].copy()
        ok["s_per_page"] = ok.seconds / ok.pages
        cost = ok.groupby(["arm", "set"]).agg(pages=("pages", "sum"), seconds=("seconds", "sum"), median_s_per_page=("s_per_page", "median"), max_rss_mb=("max_rss_mb", "max")).reset_index()
        cost["s_per_page"] = cost.seconds / cost.pages
        status = tm.groupby(["arm", "set", "status"]).size().unstack(fill_value=0).reset_index()
        tables["cost"] = cost.merge(status, on=["arm", "set"], how="left").set_index(["arm", "set"])

    arms = sorted(docs.arm.unique())
    comp = completeness_table(arms)
    if not comp.empty:
        tables["completeness_by_doc"] = comp.set_index(["arm", "doc"])
        tables["completeness"] = comp.groupby("arm")[["recall", "precision", "f1"]].mean().sort_values("f1", ascending=False)

    with open(summ / "digest.md", "w") as fh:
        for name, t in tables.items():
            t.to_csv(summ / f"{name}.csv")
            fh.write(f"## {name}\n\n{t.round(3).to_markdown()}\n\n")
    print((summ / "digest.md").read_text())


if __name__ == "__main__":
    main()
