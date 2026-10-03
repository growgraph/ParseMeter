"""Text completeness: word-multiset precision/recall of an arm's markdown against the PDF text layer.

Born-digital documents only (all of ours). The reference is ``pdftotext`` minus page furniture.
Both sides are NFKC-normalised (ligatures and super/subscript digits fold to plain text), markup
is stripped, and words are lower-cased alphanumeric runs. Recall drops when a converter loses
text; precision drops when it repeats or invents text. Text drawn inside vector figures is in
the reference, so a converter that skips figure labels loses a little recall here too.
"""

import re
import subprocess
import unicodedata
from collections import Counter

import yaml

from study.paths import ROOT, SOURCES

FURNITURE = {
    "natcomm-2020": [r"NATURE COMMUNICATIONS \|.*", r"^\s*ARTICLE\s*$", r"^\s*\d\s*$", r"1234567890\(\):,;"],
    "apple-10k-2025": [r"Apple Inc\. \| 2025 Form 10-K \| \d+"],
    "apple-10q-2026q3": [r"Apple Inc\. \| Q3 2026 Form 10-Q \| \d+"],
    "sfix-10k-2026": [r"STITCH FIX, INC\. \| 2026 FORM 10-K \| \d+", r"^\s*Table of Contents\s*$"],
}

_MARKUP = [
    (re.compile(r"<!--.*?-->", re.S), " "),
    (re.compile(r"<[^>]+>"), " "),
    (re.compile(r"!\[[^\]]*\]\([^)]*\)"), " "),
    (re.compile(r"\]\([^)]*\)"), " "),
    (re.compile(r"\\(?:mathrm|text|mathbf|mathit|operatorname|left|right|hat|vec|bar|tilde|frac|sqrt|cdot|times|quad|,|;|!)\b"), " "),
    (re.compile(r"&(?:amp|lt|gt|quot|#\d+);"), lambda m: {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"'}.get(m.group(0), " ")),
]
_WORD = re.compile(r"[^\W_]+", re.U)


def words(text: str) -> Counter:
    text = unicodedata.normalize("NFKC", text)
    for pat, rep in _MARKUP:
        text = pat.sub(rep, text)
    return Counter(w.lower() for w in _WORD.findall(text) if len(w) > 1 or w.isdigit())


def reference(doc_id: str, pdf_path: str) -> Counter:
    raw = subprocess.run(["pdftotext", "-enc", "UTF-8", str(ROOT / pdf_path), "-"], capture_output=True, text=True, check=True).stdout
    pats = [re.compile(p, re.M) for p in FURNITURE.get(doc_id, [])]
    lines = []
    for ln in raw.splitlines():
        for p in pats:
            ln = p.sub(" ", ln)
        lines.append(ln)
    return words("\n".join(lines))


def score(ref: Counter, hyp: Counter) -> dict:
    overlap = sum((ref & hyp).values())
    r = overlap / max(1, sum(ref.values()))
    p = overlap / max(1, sum(hyp.values()))
    return {"recall": round(r, 4), "precision": round(p, 4), "f1": round(2 * p * r / max(1e-9, p + r), 4)}


def docs() -> list[dict]:
    return yaml.safe_load(SOURCES.read_text())["documents"]
