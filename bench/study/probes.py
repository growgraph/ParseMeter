"""Probe tests: olmOCR-Bench test types plus ``heading``, ``figure``, ``regex_present``, ``regex_absent``.

A probe row is an olmOCR-Bench test dict plus ``category`` (and an optional ``note``).
Tests run over the WHOLE-document markdown, which is what makes page stitching testable.
"""

import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from olmocr.bench.tests import BasePDFTest, load_single_test, normalize_text
from rapidfuzz import fuzz

CATEGORIES = [
    "furniture",  # running headers/footers, page numbers, watermarks absent
    "stitching",  # text continuing across a page break is joined
    "reading_order",  # column order, text flowing around figures
    "footnotes",  # footnotes present, attached, not spliced into sentences
    "tables",  # cell relations
    "math",  # display equations (KaTeX render match)
    "inline",  # sub/superscripts, chemical formulae, units, citation markers not fused
    "headings",  # section titles emitted as markdown headings
    "figures",  # figure detected next to its caption; caption intact
    "chars",  # ligatures, symbols, junk glyphs
]
SEPARATE = ["figure_text"]  # text inside figures (axis labels): reported apart, not in the macro score

_EXTRA_KEYS = {"category", "note"}
_HEADING_LINE = re.compile(r"^\s{0,3}#{1,6}\s+(.*?)\s*#*\s*$|<h[1-6][^>]*>(.*?)</h[1-6]>", re.M | re.I)
_NUMBERING = re.compile(r"^((\d+(\.\d+)*|[IVXLC]+|[A-Z])[.)]?\s+)")
_IMAGE = re.compile(r"<!--\s*image\s*-->|!\[[^\]]*\]\([^)]*\)|<img\b|<figure\b|\[image\]|<!--\s*figure", re.I)


_DASHES = str.maketrans({"–": "-", "−": "-", "—": "-", "‑": "-", "‒": "-", "‘": "'", "’": "'", "“": '"', "”": '"', "µ": "μ"})


def light_norm(md: str) -> str:
    """Whitespace, dashes, quotes and NFC only — keeps ``_``/``^``/``$`` so LaTeX survives."""
    md = re.sub(r"<br/?>", " ", md)
    md = re.sub(r"\s+", " ", md)
    return unicodedata.normalize("NFC", md).translate(_DASHES)


def _clean_heading(s: str) -> str:
    s = normalize_text(re.sub(r"<[^>]+>", "", s)).strip().rstrip(".:").strip()
    return _NUMBERING.sub("", s).lower()


@dataclass
class HeadingTest:
    id: str
    text: str
    threshold: float = 90.0

    def run(self, md: str) -> tuple[bool, str]:
        want = _clean_heading(self.text)
        best = 0.0
        for m in _HEADING_LINE.finditer(md):
            got = _clean_heading(m.group(1) or m.group(2) or "")
            best = max(best, fuzz.ratio(want, got))
            if best >= self.threshold:
                return True, ""
        return False, f"no heading line matching {self.text!r} (best {best:.0f})"


@dataclass
class FigureTest:
    """Caption found, and an image element within ``window`` characters of it."""

    id: str
    caption: str
    window: int = 1500
    threshold: float = 90.0

    def run(self, md: str) -> tuple[bool, str]:
        want = normalize_text(self.caption)
        al = fuzz.partial_ratio_alignment(want, md, score_cutoff=self.threshold)
        if al is None:
            return False, f"caption {self.caption[:40]!r} not found"
        lo, hi = max(0, al.dest_start - self.window), min(len(md), al.dest_end + self.window)
        if _IMAGE.search(md, lo, hi):
            return True, ""
        return False, "caption found but no image element nearby"


@dataclass
class RegexTest:
    id: str
    pattern: str
    absent: bool

    def run(self, md: str) -> tuple[bool, str]:
        found = re.search(self.pattern, light_norm(md)) is not None
        if found == self.absent:
            return False, f"pattern {self.pattern!r} {'found' if found else 'not found'}"
        return True, ""


def build_test(row: dict):
    t = row["type"]
    if t == "heading":
        return HeadingTest(row["id"], row["text"])
    if t == "figure":
        return FigureTest(row["id"], row["caption"])
    if t in ("regex_present", "regex_absent"):
        return RegexTest(row["id"], row["pattern"], t == "regex_absent")
    data = {k: v for k, v in row.items() if k not in _EXTRA_KEYS}
    data.setdefault("pdf", data.get("doc", "doc"))
    data.setdefault("page", 1)
    data.pop("doc", None)
    return load_single_test(data)


def load_probes(path: Path) -> list[tuple[dict, object]]:
    out = []
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("//"):
            continue
        row = json.loads(line)
        if row.get("category") not in CATEGORIES + SEPARATE:
            raise ValueError(f"{path.name}:{n}: bad category {row.get('category')!r}")
        out.append((row, build_test(row)))
    ids = [r["id"] for r, _ in out]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise ValueError(f"{path.name}: duplicate ids {sorted(dup)}")
    return out


def run_test(test, md: str) -> tuple[bool, str]:
    try:
        return test.run(md) if not isinstance(test, BasePDFTest) else test.run(md)
    except Exception as e:  # noqa: BLE001 - a crashing test is a failed test
        return False, f"{type(e).__name__}: {e}"
