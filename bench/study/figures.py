"""Trade-off figures: quality against time per page, per metric, on the like-for-like core set.

    PYTHONPATH=. uv run python -m study.aggregate && PYTHONPATH=. uv run python -m study.figures

Reads ``out/summary/core_*.csv`` and the arms' ``timing.jsonl``; writes SVG + PNG to
``figures/``. Time is wall seconds per page on one machine, over the pages a panel scores
(all core pages, or only the born-digital / scanned / olmOCR ones), so on fixed hardware it is
also the compute-cost axis.
"""

import json
from collections.abc import Callable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap, ListedColormap  # noqa: E402
from matplotlib.patches import Patch, Rectangle  # noqa: E402
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator, PercentFormatter  # noqa: E402

from study.paths import OUT, ROOT  # noqa: E402

FIG = ROOT / "figures"

INK = "#293241"
MUTED = "#6B7280"
GRID = "#E5E7EB"
GREY = "#C9CED6"
ACCENT = "#E67E22"
BLUE = "#224777"
SEQ = LinearSegmentedColormap.from_list("parsemeter", ["#F4F6FA", "#9DB3D6", BLUE])
FOOTER = "ParseMeter · github.com/growgraph/ParseMeter · one laptop CPU, 12 threads · 2026-10"

LABEL = {
    "pdftotext": "pdftotext",
    "docling-default": "Docling (defaults)",
    "docling-textlayer": "Docling (text layer, no OCR)",
    "docling-noocr": "Docling (no OCR)",
    "docling-fast": "Docling (no OCR, fast tables)",
    "docling-layoutonly": "Docling (no OCR, no table model)",
    "docling-native": "Docling (native, no models)",
    "docling-fullocr": "Docling (full-page OCR)",
    "docling-formula": "Docling (+ formula model)",
    "docling-lean": "Docling (lean)",
    "docling-tuned": "Docling (tuned)",
    "mineru-basic": "MinerU (basic)",
    "mineru-standard": "MinerU (standard, +VLM)",
    "marker-nocr": "Marker (no OCR)",
    "marker-fast": "Marker (fast)",
    "paddle-vl": "PaddleOCR-VL 1.6",
    "paddle-structurev3": "PP-StructureV3",
    "pymupdf4llm-default": "PyMuPDF4LLM (default)",
    "pymupdf4llm-layout": "PyMuPDF4LLM (layout)",
    "kreuzberg-default": "Kreuzberg (default)",
    "unstructured-hires": "Unstructured (hi_res)",
}
DESCRIBE = {"docling-lean": "lean: no OCR, fast tables, + formula"}  # longer names where space allows
# how the arm reads a page; colour-blind-safe Okabe-Ito colours
KIND = {
    "pdftotext": "text layer only", "pymupdf4llm-default": "text layer only",
    "kreuzberg-default": "text layer only", "marker-nocr": "text layer only",
    "docling-default": "layout models", "docling-textlayer": "layout models",
    "docling-noocr": "layout models", "docling-fast": "layout models", "docling-layoutonly": "layout models",
    "docling-fullocr": "layout models", "docling-native": "text layer only",
    "docling-formula": "layout models + VLM on parts", "docling-lean": "layout models + VLM on parts",
    "pymupdf4llm-layout": "layout models", "mineru-basic": "layout models",
    "unstructured-hires": "layout models", "paddle-structurev3": "layout models",
    "docling-tuned": "layout models + VLM on parts", "marker-fast": "layout models + VLM on parts",
    "mineru-standard": "layout models + VLM on parts",
    "paddle-vl": "full-page VLM",
}
COLOUR = {
    "text layer only": "#8C8C8C",
    "layout models": "#0072B2",
    "layout models + VLM on parts": "#E69F00",
    "full-page VLM": "#CC79A7",
}
# Docling configurations labelled in the overviews only when on the frontier (all of them: fig_docling)
DOCLING_LADDER = {"docling-noocr", "docling-fast", "docling-layoutonly", "docling-native", "docling-fullocr",
                  "docling-formula", "docling-lean"}
METRICS = [  # (panel title, source table, column)
    ("Page stitching", "core_probes", "stitching"),
    ("Tables", "core_probes", "tables"),
    ("Equations (display)", "core_probes", "math"),
    ("Sub/superscripts", "core_probes", "inline"),
    ("Footnotes", "core_probes", "footnotes"),
    ("Headers/footers removed", "core_probes", "furniture"),
    ("Headings", "core_probes", "headings"),
    ("Scans without text layer", "core_by_regime", "scan"),
]
HEAT_GROUPS = [  # (group, [(column title, table, column)])
    ("Structure", [("Page\nstitching", "core_probes", "stitching"), ("Footnotes", "core_probes", "footnotes"),
                   ("Headers/footers\nremoved", "core_probes", "furniture"), ("Headings", "core_probes", "headings")]),
    ("Content", [("Tables", "core_probes", "tables"), ("Equations", "core_probes", "math"),
                 ("Sub/super-\nscripts", "core_probes", "inline")]),
    ("Scans", [("Hidden OCR\nlayer", "core_by_regime", "scan_ocr"), ("No text\nlayer", "core_by_regime", "scan")]),
    ("Public", [("olmOCR-Bench\nslice", "core_olmocr", "overall")]),
]


def _style() -> None:
    plt.rcParams.update({
        "font.family": "sans-serif", "font.sans-serif": ["Inter", "DejaVu Sans"], "font.size": 10,
        "text.color": INK, "axes.labelcolor": INK, "axes.edgecolor": MUTED, "axes.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "axes.grid.axis": "y", "grid.color": GRID, "grid.linewidth": 0.8,
        "xtick.color": MUTED, "ytick.color": MUTED, "xtick.labelcolor": INK, "ytick.labelcolor": INK,
        "axes.titlesize": 11, "axes.titleweight": "semibold", "axes.titlelocation": "left", "axes.titlepad": 8,
        "legend.frameon": False, "savefig.dpi": 200, "svg.fonttype": "none",
    })


def _docs() -> dict[str, dict]:
    return {d["id"]: d for d in json.loads((OUT / "doclist.json").read_text())}


def seconds_per_page(where: Callable[[dict], bool] = lambda d: True) -> pd.Series:
    """Wall seconds per page over the core pages (our documents + olmOCR) matching ``where``."""
    docs = _docs()
    out = {}
    for arm in LABEL:
        log = OUT / arm / "timing.jsonl"
        if not log.exists():
            continue
        last = {}
        for line in log.read_text().splitlines():
            r = json.loads(line)
            last[r["id"]] = r
        ok = [r for i, r in last.items() if i in docs and docs[i].get("core") and where(docs[i]) and r["status"] == "ok"]
        if ok:
            out[arm] = sum(r["seconds"] for r in ok) / sum(r["pages"] for r in ok)
    return pd.Series(out)


def frontier(x: pd.Series, y: pd.Series) -> list[str]:
    """Arms not beaten on both axes: nothing faster scores as well or better."""
    best, keep = -1.0, []
    for arm in x.sort_values().index:
        if y[arm] > best:
            keep.append(arm)
            best = y[arm]
    return keep


def _fmt_s(v: float, _=None) -> str:
    return f"{v * 1000:.0f} ms" if v < 0.1 else f"{v:g} s" if v < 60 else f"{v / 60:g} min"


XMIN, XMAX = 0.006, 150


def _axes(ax, xlabel: bool = True, percent: bool = True) -> None:
    ax.set_xscale("log")
    ax.set_xlim(XMIN, XMAX)
    ax.xaxis.set_major_locator(FixedLocator([0.01, 0.1, 1, 10, 60]))
    ax.xaxis.set_major_formatter(FuncFormatter(_fmt_s))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.set_ylim(0, 1.02)
    ax.yaxis.set_major_locator(FixedLocator([0, 0.2, 0.4, 0.6, 0.8, 1.0]))
    if percent:
        ax.yaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    if xlabel:
        ax.set_xlabel("CPU time per page (log scale)")


def _panel(ax, x: pd.Series, y: pd.Series, title: str, label: str = "all", fontsize: float = 8,
           extra: tuple[str, ...] = (), names: dict[str, str] = LABEL) -> list[str]:
    """Scatter + frontier. Labelled and coloured: every main arm ("all"), or the frontier, Docling
    with defaults and ``extra`` ("frontier"); the rest are grey context."""
    arms = [a for a in y.index if a in x.index and a in LABEL]
    x, y = x[arms].clip(lower=XMIN * 1.4), y[arms]
    f = frontier(x, y)
    main = [a for a in arms if a not in DOCLING_LADDER or a in f]
    shown = {"all": main, "frontier": [*f, "docling-default", *extra], "none": []}[label]
    shown = [a for a in dict.fromkeys(shown) if a in arms]
    coloured = set(shown) | set(f)
    xs, ys = [*x[f], XMAX], [*y[f], y[f[-1]]]
    ax.fill_between(xs, ys, 0, step="post", color=INK, alpha=0.04, lw=0, zorder=0)
    ax.step(xs, ys, where="post", color=INK, lw=1.4, zorder=1)
    for a in arms:
        if a in coloured:
            ax.scatter(x[a], y[a], s=70 if a in f else 48, color=COLOUR[KIND[a]],
                       edgecolor=INK if a in f else "white", lw=1.0, zorder=3)
        else:
            ax.scatter(x[a], y[a], s=22, color=GREY, zorder=2)
    _axes(ax, xlabel=False)
    if title:
        ax.set_title(title)
    _labels(ax, [(x[a], y[a], a) for a in shown], fontsize, names=names, obstacles=[(x[a], y[a]) for a in arms])
    return f


def _labels(ax, pts: list[tuple[float, float, str]], fontsize: float, names: dict[str, str] = LABEL,
            obstacles: list[tuple[float, float]] = ()) -> None:
    """Label each point near itself: the first slot, right then left, stepping up/down, that clears
    other labels and every plotted point."""
    from matplotlib.text import Text
    from matplotlib.transforms import Bbox

    fig = ax.figure
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    dots = [ax.transData.transform((ox, oy)) for ox, oy in [*obstacles, *((x, y) for x, y, _ in pts)]]
    placed = [Bbox.from_extents(dx - 5, dy - 5, dx + 5, dy + 5) for dx, dy in dots]
    steps = [0] + [d * k for k in range(1, 10) for d in (1, -1)]
    frame = ax.get_window_extent()
    for x, y, a in sorted(pts, key=lambda p: -p[1]):
        ann = ax.annotate(names[a], (x, y), xytext=(7, 0), textcoords="offset points", va="center", fontsize=fontsize,
                          fontweight="semibold" if a in ("docling-default", "docling-lean") else "normal", zorder=4,
                          color=INK, bbox={"boxstyle": "square,pad=0.1", "fc": "white", "ec": "none", "alpha": 0.85},
                          arrowprops={"arrowstyle": "-", "color": "#9CA3AF", "lw": 0.5, "shrinkA": 0, "shrinkB": 3})
        best = None
        for dy in steps:
            for side, ha in ((8, "left"), (-8, "right")):
                ann.set_ha(ha)
                ann.xyann = (side, dy * fontsize * 0.8)
                ann.update_positions(renderer)
                box = Text.get_window_extent(ann, renderer).padded(2)
                hits = sum(box.overlaps(b) for b in placed)
                if box.x0 < frame.x0 or box.x1 > frame.x1 or box.y0 < frame.y0 or box.y1 > frame.y1:
                    hits += 100
                if best is None or hits < best[0]:
                    best = (hits, ha, ann.xyann, box)
                if hits == 0:
                    break
            if best[0] == 0:
                break
        _, ha, xy, box = best
        ann.set_ha(ha)
        ann.xyann = xy
        placed.append(box)


def _arrow(ax, x: pd.Series, y: pd.Series, a: str, b: str, text: str = "", fontsize: float = 9) -> None:
    """A highlighted move from arm ``a`` to arm ``b`` (same tool, different settings)."""
    if a not in x.index or b not in x.index or a not in y.index or b not in y.index:
        return
    ax.annotate("", xy=(x[b], y[b]), xytext=(x[a], y[a]), zorder=5,
                arrowprops={"arrowstyle": "-|>", "color": ACCENT, "lw": 1.8, "shrinkA": 7, "shrinkB": 7,
                            "connectionstyle": "arc3,rad=0.35"})
    if text:
        ax.annotate(text, ((x[a] * x[b]) ** 0.5, min(y[a], y[b])), xytext=(0, -14), textcoords="offset points",
                    ha="center", va="top", fontsize=fontsize, color=ACCENT, fontweight="semibold", zorder=5)


def _legend(fig, frontier: bool = True, y: float = 0.035, ncol: int = 6, fontsize: float = 8.5) -> None:
    handles = [plt.Line2D([], [], marker="o", ls="", color=c, label=k) for k, c in COLOUR.items()]
    if frontier:
        handles.append(plt.Line2D([], [], color=INK, lw=1.4, label="Pareto frontier (outlined: nothing faster scores higher)"))
        handles.append(Patch(color=INK, alpha=0.08, label="dominated"))
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, y), ncol=ncol, fontsize=fontsize,
               handletextpad=0.4, columnspacing=1.4)


def _footer(fig, y: float = 0.005) -> None:
    fig.text(0.995, y, FOOTER, ha="right", va="bottom", fontsize=7, color=MUTED)


def _save(fig, name: str, tight: bool = True, dpi: int | None = None) -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    for ext in ("svg", "png"):
        fig.savefig(FIG / f"{name}.{ext}", bbox_inches="tight" if tight else None, pad_inches=0.15,
                    **({"dpi": dpi} if dpi else {}))
    plt.close(fig)


def _pages_per_hour_axis(ax) -> None:
    sec = ax.secondary_xaxis("top", functions=(lambda s: 3600 / np.maximum(s, 1e-9), lambda p: 3600 / np.maximum(p, 1e-9)))
    sec.set_xlabel("pages per hour", fontsize=8, color=MUTED)
    sec.xaxis.set_major_locator(FixedLocator([60, 360, 3600, 36000, 360000]))
    sec.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))
    sec.tick_params(labelsize=7.5, colors=MUTED)


def fig_overall(t: pd.Series, tables: dict[str, pd.DataFrame]) -> None:
    fig, ax = plt.subplots(figsize=(10, 6.6))
    _panel(ax, t, tables["core_probes"]["macro"], "", fontsize=9)
    ax.set_xlabel("CPU time per page (log scale) — on fixed hardware, also the compute cost")
    ax.set_ylabel("probes passed (10 core documents, mean over categories)")
    _pages_per_hour_axis(ax)
    fig.suptitle("Quality against time: the frontier runs from text extraction to a VLM", x=0.06, ha="left",
                 fontsize=13, fontweight="semibold", y=1.0)
    _legend(fig, y=0.03, ncol=3)
    _footer(fig)
    fig.subplots_adjust(bottom=0.2)
    _save(fig, "frontier_overall")


def fig_regimes(tk: dict[str, pd.Series], tables: dict[str, pd.DataFrame]) -> None:
    fig, axes = plt.subplots(1, 4, figsize=(20, 5.8), sharey=True)
    for ax, (title, y, x) in zip(axes, [
        ("olmOCR-Bench slice (60 pages)", tables["core_olmocr"]["overall"], tk["olmocr"]),
        ("Born-digital pages", tables["core_by_regime"]["digital"], tk["digital"]),
        ("Scans with a hidden OCR layer", tables["core_by_regime"]["scan_ocr"], tk["scan_ocr"]),
        ("Scans without a text layer", tables["core_by_regime"]["scan"], tk["scan"]),
    ]):
        _panel(ax, x, y, title, label="frontier", extra=("docling-fast", "docling-lean") if "Born" in title else ())
        ax.set_xlabel("CPU time per page on these pages")
    _arrow(axes[1], tk["digital"].clip(lower=XMIN * 1.4), tables["core_by_regime"]["digital"], "docling-default", "docling-fast")
    axes[0].set_ylabel("tests passed")
    fig.suptitle("The frontier moves with the kind of document (frontier arms and Docling with defaults labelled)",
                 x=0.06, ha="left", fontsize=13, fontweight="semibold")
    _legend(fig, y=0.0)
    _footer(fig, y=-0.04)
    fig.subplots_adjust(bottom=0.2, wspace=0.08)
    _save(fig, "frontier_regimes")


def fig_metrics(t: pd.Series, tables: dict[str, pd.DataFrame]) -> None:
    fig, axes = plt.subplots(2, 4, figsize=(20, 10.4), sharex=True, sharey=True)
    for ax, (title, tab, col) in zip(axes.flat, METRICS):
        _panel(ax, t, tables[tab][col], title, label="frontier", fontsize=7.5)
    for ax in axes[1]:
        ax.set_xlabel("CPU time per page")
    for ax in axes[:, 0]:
        ax.set_ylabel("probes passed")
    fig.suptitle("Each metric has its own frontier (frontier arms and Docling with defaults labelled)",
                 x=0.06, ha="left", fontsize=13, fontweight="semibold")
    _legend(fig, y=0.0)
    _footer(fig, y=-0.025)
    fig.subplots_adjust(bottom=0.1, hspace=0.25, wspace=0.08)
    _save(fig, "frontier_by_metric")


def _sp(s: float) -> str:
    return "<0.1" if s < 0.1 else f"{s:.1f}" if s < 10 else f"{s:.0f}"


def _heat(ax, m: pd.DataFrame, groups: list[tuple[str, int]] | None = None, fontsize: float = 8.5) -> None:
    """Single-hue heatmap; the best cell of each column outlined."""
    ax.imshow(m.values, cmap=SEQ, vmin=0, vmax=1, aspect="auto")
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    best = m.max()
    for i in range(len(m)):
        for j, c in enumerate(m.columns):
            v = m.iloc[i, j]
            if pd.isna(v):
                continue
            ax.text(j, i, f"{v * 100:.0f}", ha="center", va="center", fontsize=fontsize,
                    color="white" if v > 0.62 else INK)
            if v >= best[c] - 1e-9:
                ax.add_patch(Rectangle((j - 0.47, i - 0.45), 0.94, 0.9, fill=False, ec=ACCENT, lw=2, zorder=3))
    ax.set_xticks(range(len(m.columns)), m.columns, fontsize=8.5)
    ax.xaxis.tick_top()
    ax.tick_params(length=0)
    if groups:
        start = 0
        for name, n in groups:
            if start:
                ax.axvline(start - 0.5, color="white", lw=5)
            ax.text(start + (n - 1) / 2, -1.55, name.upper(), ha="center", va="bottom", fontsize=8, color=MUTED,
                    fontweight="semibold", transform=ax.transData)
            start += n


def fig_heatmap(tables: dict[str, pd.DataFrame], t: pd.Series) -> None:
    cols = [c for _, cs in HEAT_GROUPS for c in cs]
    arms = [a for a in tables["core_probes"].index if a in LABEL]
    m = pd.DataFrame({title: tables[tab][col].reindex(arms) for title, tab, col in cols})
    m = m.loc[tables["core_probes"]["macro"].reindex(arms).sort_values(ascending=False).index]
    fig, ax = plt.subplots(figsize=(12.5, 0.42 * len(m) + 1.6))
    _heat(ax, m, [(g, len(cs)) for g, cs in HEAT_GROUPS])
    ax.set_yticks(range(len(m)), [f"{LABEL[a]}   {_sp(t.get(a, float('nan')))} s/page" for a in m.index], fontsize=9)
    fig.suptitle("No free lunch: the best arm (outlined) changes with the metric",
                 x=0.02, ha="left", fontsize=13, fontweight="semibold", y=1.0)
    fig.text(0.02, 0.965, "% of probes passed on the core set; rows by mean over categories", fontsize=9, color=MUTED)
    _footer(fig, y=0.0)
    fig.subplots_adjust(top=0.87, bottom=0.03)
    _save(fig, "metric_heatmap")


# Structure each converter's native output keeps apart from body text, coded from
# docs/representation.md (evidence there, from the installed
# source). 2 = by default as run, 1 = only with a non-default option / only in the native JSON /
# partial, 0 = not available, None = unverified.
ASPECTS = [
    "Headers/footers\nseparated", "Footnotes\ntyped", "Footnote linked\nto marker/float",
    "Table cells\nwith spans", "Cross-page\ntable merge", "Figure element\n+ linked caption",
    "Equations\nas LaTeX", "Heading\nlevels", "Explicit\nreading order", "Page + bbox\nper element",
]
REPRESENTATION = {
    "Docling (defaults)":  [2, 2, 1, 2, 0, 2, 1, 1, 1, 2],
    "MinerU":              [2, 2, 1, 2, 2, 2, 2, 2, 2, 2],
    "Marker (fast)":       [2, 2, 1, 1, 1, 2, 2, 2, 1, 2],
    "PP-StructureV3":      [2, 1, 0, 2, 0, 1, 2, 2, 2, 2],
    "PaddleOCR-VL 1.6":    [2, 1, 0, 2, 2, 1, 2, 2, 2, 1],
    "PyMuPDF4LLM (layout)":[1, 2, 0, 1, 0, 1, 0, 2, 2, 2],
    "Kreuzberg":           [1, 1, 0, 1, None, 0, None, 1, 1, 1],
    "Unstructured":        [2, 0, 0, 2, 0, 1, 0, 0, 1, 2],
    "GROBID":              [1, 2, 1, 1, 0, 2, 0, 1, 1, 1],
    "pdftotext":           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
}


def fig_representation() -> None:
    rows = list(REPRESENTATION)
    m = np.array([[np.nan if v is None else v for v in REPRESENTATION[r]] for r in rows], dtype=float)
    cmap = ListedColormap(["#F4F6FA", "#9DB3D6", BLUE])
    cmap.set_bad("#FFFFFF")
    fig, ax = plt.subplots(figsize=(13, 0.5 * len(rows) + 2.4))
    ax.imshow(np.ma.masked_invalid(m), cmap=cmap, vmin=0, vmax=2, aspect="auto")
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    mark = {0: "–", 1: "opt", 2: "yes"}
    for i in range(len(rows)):
        for j in range(len(ASPECTS)):
            v = m[i, j]
            ax.text(j, i, "?" if np.isnan(v) else mark[int(v)], ha="center", va="center", fontsize=8.5,
                    color="white" if v == 2 else INK)
    ax.set_xticks(range(len(ASPECTS)), ASPECTS, fontsize=8.5)
    ax.xaxis.tick_top()
    ax.set_yticks(range(len(rows)), rows, fontsize=9.5)
    ax.set_xticks(np.arange(-0.5, len(ASPECTS)), minor=True)
    ax.set_yticks(np.arange(-0.5, len(rows)), minor=True)
    ax.grid(which="minor", color="white", lw=2)
    ax.tick_params(which="both", length=0)
    fig.suptitle("What the native output keeps apart from body text", x=0.02, ha="left", fontsize=13,
                 fontweight="semibold", y=1.0)
    fig.text(0.02, 0.955, "yes = by default as run · opt = needs a non-default option, only in the native JSON, "
             "or partial · – = not available · ? = unverified", fontsize=9, color=MUTED)
    _footer(fig, y=0.0)
    fig.subplots_adjust(top=0.78)
    _save(fig, "representation")


TOOLS = {  # tool -> its measured configurations, cheapest first
    "Docling": ["docling-native", "docling-layoutonly", "docling-fast", "docling-noocr", "docling-textlayer",
                "docling-default", "docling-fullocr", "docling-lean", "docling-formula", "docling-tuned"],
    "MinerU": ["mineru-basic", "mineru-standard"],
    "Marker": ["marker-nocr", "marker-fast"],
    "PaddleOCR": ["paddle-structurev3", "paddle-vl"],
    "PyMuPDF4LLM": ["pymupdf4llm-default", "pymupdf4llm-layout"],
}


def fig_settings(t: pd.Series, tables: dict[str, pd.DataFrame]) -> None:
    """Same tool, different settings: the spread between a tool's configurations."""
    panels = [
        ("Our probes (core, mean over categories)", tables["core_probes"]["macro"]),
        ("olmOCR-Bench slice", tables["core_olmocr"]["overall"]),
        ("Scans without a text layer", tables["core_by_regime"]["scan"]),
    ]
    fig, axes = plt.subplots(1, len(panels), figsize=(17, 6.4), sharey=True)
    tools = list(TOOLS)
    for ax, (title, y) in zip(axes, panels):
        for i, tool in enumerate(tools):
            arms = [a for a in TOOLS[tool] if a in y.index]
            if not arms:
                continue
            vals = y[arms]
            ax.plot([vals.min(), vals.max()], [i, i], color="#D7DCE3", lw=6, solid_capstyle="round", zorder=1)
            named = arms if len(arms) <= 3 else list({vals.idxmin(), vals.idxmax(), "docling-default"})
            for a in arms:
                ax.scatter(y[a], i, s=70, color=COLOUR[KIND[a]], edgecolor="white", lw=1, zorder=3)
                if a not in named:
                    continue
                cfg = LABEL[a].split("(", 1)[1].rstrip(")") if "(" in LABEL[a] else LABEL[a]
                up = sorted(named, key=lambda n: y[n]).index(a) % 2 == 0
                ax.annotate(f"{cfg}\n{_sp(t.get(a, float('nan')))} s/page", (y[a], i), xytext=(0, 9 if up else -9),
                            textcoords="offset points", ha="center", va="bottom" if up else "top", fontsize=7.5)
        ax.set_xlim(-0.1, 1.04)
        ax.set_ylim(-0.7, len(tools) - 0.3)
        ax.set_title(title)
        ax.grid(axis="x")
        ax.grid(axis="y", visible=False)
        ax.xaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
        ax.set_xlabel("passed")
    axes[0].set_yticks(range(len(tools)), tools, fontsize=10)
    axes[0].tick_params(axis="y", length=0)
    axes[0].invert_yaxis()
    fig.suptitle("Same tool, different settings: configuration moves quality as much as the choice of tool",
                 x=0.06, ha="left", fontsize=13, fontweight="semibold")
    _legend(fig, frontier=False, y=0.0)
    _footer(fig, y=-0.03)
    fig.subplots_adjust(bottom=0.15, wspace=0.05)
    _save(fig, "settings_spread")


DOCLING_GROUPS = [
    ("Overall", [("All probes", "core_probes", "macro"), ("olmOCR\nslice", "core_olmocr", "overall")]),
    ("By document", [("Born-\ndigital", "core_by_regime", "digital"), ("Scan, hidden\nOCR layer", "core_by_regime", "scan_ocr"),
                     ("Scan, no\ntext layer", "core_by_regime", "scan")]),
    ("By element", [("Tables", "core_probes", "tables"), ("Page\nstitching", "core_probes", "stitching"),
                    ("Equations", "core_probes", "math"), ("Headings", "core_probes", "headings")]),
]


def fig_docling(t: pd.Series, tables: dict[str, pd.DataFrame]) -> None:
    """Every Docling configuration: mean probe score against time (numbered), and per metric."""
    macro = tables["core_probes"]["macro"]
    docling = sorted((a for a in TOOLS["Docling"] if a in t.index and a in macro.index), key=lambda a: t[a])
    num = {a: i + 1 for i, a in enumerate(docling)}
    fig, (ax, hm) = plt.subplots(1, 2, figsize=(19, 7), gridspec_kw={"width_ratios": [1, 1.3]})

    arms = [a for a in macro.index if a in t.index and a in LABEL]
    x, y = t[arms].clip(lower=XMIN * 1.4), macro[arms]
    f = frontier(x, y)
    xs, ys = [*x[f], XMAX], [*y[f], y[f[-1]]]
    ax.fill_between(xs, ys, 0, step="post", color=INK, alpha=0.04, lw=0, zorder=0)
    ax.step(xs, ys, where="post", color=INK, lw=1.4, zorder=1)
    others = [a for a in arms if a not in docling]
    ax.scatter(x[others], y[others], s=22, color=GREY, zorder=2)
    for a in docling:
        ax.scatter(x[a], y[a], s=210, color=COLOUR[KIND[a]], edgecolor=INK if a in f else "white", lw=1, zorder=3)
        ax.annotate(str(num[a]), (x[a], y[a]), ha="center", va="center", fontsize=8, color="white",
                    fontweight="bold", zorder=4)
    _axes(ax)
    ax.set_ylabel("probes passed (core, mean over categories)")
    ax.set_title("Quality against time (grey: the other tools)")

    cols = [c for _, cs in DOCLING_GROUPS for c in cs]
    m = pd.DataFrame({title: tables[tab][col].reindex(docling) for title, tab, col in cols})
    _heat(hm, m, [(g, len(cs)) for g, cs in DOCLING_GROUPS])
    names = {a: DESCRIBE.get(a, LABEL[a].split("(", 1)[1].rstrip(")")) for a in docling}
    hm.set_yticks(range(len(m)), [f"{num[a]}  {names[a]}   {_sp(t[a])} s/page" for a in m.index], fontsize=9.5)
    for k, a in enumerate(m.index):
        if a in ("docling-default", "docling-lean"):
            hm.get_yticklabels()[k].set_fontweight("bold")
    fig.suptitle("Docling, one tool: what each setting costs and buys", x=0.02, ha="left", fontsize=13,
                 fontweight="semibold", y=1.02)
    fig.text(0.02, 0.975, "Rows cheapest first; % passed; best configuration per column outlined", fontsize=9, color=MUTED)
    _legend(fig, y=0.0)
    _footer(fig, y=-0.035)
    fig.subplots_adjust(bottom=0.14, top=0.8, wspace=0.55)
    _save(fig, "docling_settings")


def fig_hero(tk: dict[str, pd.Series], tables: dict[str, pd.DataFrame]) -> None:
    """One image for a social feed (1200 x 1500 px): born-digital vs scanned, the Docling settings move."""
    fig, axes = plt.subplots(2, 1, figsize=(8, 10), sharex=True)
    panels = [("Born-digital PDFs", tables["core_by_kind"]["digital"], tk["digital"], ("docling-fast", "docling-lean")),
              ("Scanned PDFs", tables["core_by_kind"]["scanned"], tk["scanned"], ("paddle-vl", "marker-fast"))]
    names = {**LABEL, "docling-default": "Docling, default settings", "docling-fast": "Docling, OCR off + fast tables",
             "docling-lean": "Docling, + formula model"}
    for ax, (title, y, x, extra) in zip(axes, panels):
        _panel(ax, x, y, title, label="frontier", fontsize=9.5, extra=extra, names=names)
        ax.title.set_fontsize(13)
        ax.set_ylabel("tests passed", fontsize=10.5)
    _arrow(axes[0], tk["digital"].clip(lower=XMIN * 1.4), tables["core_by_kind"]["digital"], "docling-default", "docling-fast")
    axes[1].set_xlabel("CPU time per page (log scale)", fontsize=10.5)
    fig.text(0.04, 0.975, "No single best PDF converter", fontsize=19, fontweight="bold", va="top")
    fig.text(0.04, 0.938, "It depends on the PDF, and on the settings. 21 configurations of 8 self-hostable tools,\n"
             "hand-written tests on 10 open documents + 60 olmOCR-Bench pages", fontsize=10.5, color=MUTED, va="top")
    _legend(fig, y=0.035, ncol=3, fontsize=8.5)
    _footer(fig, y=0.012)
    fig.subplots_adjust(top=0.86, bottom=0.14, hspace=0.22, left=0.11, right=0.97)
    _save(fig, "hero", tight=False, dpi=150)


def main() -> None:
    _style()
    names = ["core_probes", "core_olmocr", "core_by_regime", "core_by_kind"]
    tables = {n: pd.read_csv(OUT / "summary" / f"{n}.csv", index_col=0) for n in names}
    t = seconds_per_page()
    tk = {
        "olmocr": seconds_per_page(lambda d: d["set"] == "olmocr"),
        "docs": seconds_per_page(lambda d: d["set"] == "docs"),
        "digital": seconds_per_page(lambda d: d.get("regime") == "digital"),
        "scan_ocr": seconds_per_page(lambda d: d.get("regime") == "scan_ocr"),
        "scan": seconds_per_page(lambda d: d.get("regime") == "scan"),
        "scanned": seconds_per_page(lambda d: d.get("regime") in ("scan_ocr", "scan")),
    }
    fig_overall(t, tables)
    fig_regimes(tk, tables)
    fig_metrics(tk["docs"], tables)
    fig_heatmap(tables, t)
    fig_representation()
    fig_settings(t, tables)
    fig_docling(t, tables)
    fig_hero(tk, tables)
    t.rename(LABEL).sort_values().round(2).to_csv(FIG / "seconds_per_page.csv", header=["seconds_per_page"])
    print("figures ->", FIG)


if __name__ == "__main__":
    main()
