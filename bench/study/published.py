"""Our olmOCR-Bench slice scores next to published ones for the same tools.

    PYTHONPATH=. uv run python -m study.published

Published rows are copied from ``docs/landscape.md`` (source ids there). Writes
``out/summary/published_vs_ours.csv``: per arm and olmOCR category, our share passed (mean over
tests), the number of PDFs it rests on, a bootstrap 95% interval over PDFs, and the published
value; plus the "digital-only" mean (the six categories without the two old-scan ones) that
Datalab reports for runs without per-category numbers.
"""

import numpy as np
import pandas as pd

from study.aggregate import load_scores
from study.paths import OUT

CATS = ["arxiv_math", "old_scans_math", "table_tests", "old_scans", "headers_footers", "multi_column",
        "long_tiny_text", "baseline"]
DIGITAL = ["arxiv_math", "table_tests", "headers_footers", "multi_column", "long_tiny_text", "baseline"]
SLICE = [c for c in CATS if c != "old_scans"]  # categories our slice samples

# (our arm, published config, source, per-category values in CATS order or None, digital-only or None)
PUBLISHED = [
    ("docling-default", "Docling default PdfPipelineOptions(), GPU", "Datalab [S10]", None, 64.0),
    ("mineru-basic", "MinerU pipeline -m auto, GPU", "Datalab [S10]", None, 83.3),
    ("mineru-basic", "MinerU v1.3.10 pipeline", "Ai2 [S3]", [75.4, 47.4, 60.9, 17.3, 96.6, 59.0, 39.1, 96.6], None),
    ("mineru-standard", "MinerU 2.5.4 VLM (MinerU2.5-2509-1.2B)", "MinerU authors [S1]",
     [76.6, 54.6, 84.9, 33.7, 96.6, 78.2, 83.5, 93.7], None),
    ("mineru-standard", "MinerU2.5-Pro (H&F not reported)", "Falcon-OCR card [S47]",
     [87.1, 83.4, 86.0, 36.1, None, 84.4, 93.7, 99.5], None),
    ("marker-fast", "Marker 2.0.0 fast, GPU", "Datalab [S10]", [23.4, 59.8, 69.0, 43.2, 93.2, 76.0, 68.3, 99.9], 71.6),
    ("marker-nocr", "Marker 2.0.0 fast --disable_ocr, CPU", "Datalab [S10]",
     [0.0, 0.0, 46.1, 14.3, 92.8, 67.0, 43.2, 85.9], 55.8),
    ("paddle-vl", "PaddleOCR-VL 1.0, GPU", "PaddleOCR-VL authors [S24]",
     [85.7, 71.0, 84.1, 37.8, 97.0, 79.9, 85.7, 98.5], None),
    ("paddle-vl", "PaddleOCR-VL 1.6 (H&F not reported)", "Falcon-OCR card [S47]",
     [87.8, 68.8, 81.3, 39.0, None, 84.1, 91.6, 98.4], None),
]
REPS, SEED = 2000, 20261003


def _ours(olm: pd.DataFrame, arm: str, rng: np.random.Generator) -> dict[str, tuple[float, int, float, float]]:
    """category -> (share passed, PDFs, 2.5%, 97.5%) over the PDFs the arm converted (core-only arms:
    10 per category); the interval resamples PDFs within each category."""
    a = olm[(olm.arm == arm) & ~olm.msg.astype(str).str.startswith("no output")]
    out, draws = {}, {}
    for cat in SLICE:
        c = a[a.category == cat]
        if c.empty:
            continue
        per_pdf = c.groupby("doc").passed.agg(["sum", "count"])
        n = len(per_pdf)
        idx = rng.integers(0, n, size=(REPS, n))
        boot = per_pdf["sum"].to_numpy()[idx].sum(1) / per_pdf["count"].to_numpy()[idx].sum(1)
        draws[cat] = boot
        out[cat] = (c.passed.mean(), n, *np.percentile(boot, [2.5, 97.5]))
    if all(c in draws for c in DIGITAL):
        boot = np.mean([draws[c] for c in DIGITAL], axis=0)
        out["digital_only"] = (np.mean([out[c][0] for c in DIGITAL]), min(out[c][1] for c in DIGITAL),
                               *np.percentile(boot, [2.5, 97.5]))
    return out


def table() -> pd.DataFrame:
    s = load_scores()
    olm = s[s.set == "olmocr"]
    rng = np.random.default_rng(SEED)
    ours = {arm: _ours(olm, arm, rng) for arm in dict.fromkeys(p[0] for p in PUBLISHED)}
    rows = []
    for arm, config, source, cats, digital in PUBLISHED:
        pub = dict(zip(CATS, cats)) if cats else {}
        if digital is None and cats and all(pub.get(c) is not None for c in DIGITAL):
            digital = round(float(np.mean([pub[c] for c in DIGITAL])), 1)
        pub["digital_only"] = digital
        for cat in [*SLICE, "digital_only"]:
            if pub.get(cat) is None or cat not in ours[arm]:
                continue
            v, n, lo, hi = ours[arm][cat]
            rows.append({"arm": arm, "published_config": config, "source": source, "category": cat,
                         "ours": round(100 * v, 1), "ours_lo": round(100 * lo, 1), "ours_hi": round(100 * hi, 1),
                         "pdfs": n, "published": pub[cat], "diff": round(100 * v - pub[cat], 1),
                         "within_ci": 100 * lo <= pub[cat] <= 100 * hi})
    return pd.DataFrame(rows)


def main() -> None:
    t = table()
    dest = OUT / "summary" / "published_vs_ours.csv"
    t.to_csv(dest, index=False)
    pd.set_option("display.width", 220)
    print(t.to_string(index=False))
    print("->", dest)


if __name__ == "__main__":
    main()
