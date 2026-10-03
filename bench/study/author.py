"""Helpers for writing probe files: ``probes/src/<doc>.py`` defines ``probes(p: Probes)``.

Conventions the helpers encode:
- a subscript may be written plainly (``CsPbBr3``) or marked (``_3``, ``<sub>3</sub>``, ``₃``),
  but never split off by a space (``CsPbBr 3``);
- a superscript exponent must be marked (``10^2``, ``<sup>2</sup>``, ``²``) — written plainly it
  changes the value (``102``);
- a citation marker must be marked or dropped, never left as a bare number fused to a word;
- a symbol counts in Unicode or in equivalent markup (``°`` / ``$^\\circ$`` / ``<sup>o</sup>``,
  ``μ`` / ``$\\mu$``, ``¾`` / ``$\\frac{3}{4}$``): use ``DEG``, ``MU``, ``frac_re`` in regex probes.
"""

import importlib.util
import json
import re
import sys

from study.paths import PROBES

_SUBS = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
_SUPS = str.maketrans("0123456789-−", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁻")


def _alts(*xs: str) -> str:
    return "(?:" + "|".join(xs) + ")"


DEG = r"(?:°|º|℃|℉|\$?\s?\^\s?\{?\s?\\circ\s?\}?\s?\$?\s?|<sup>\s?[o°]\s?</sup>)"
MU = r"(?:μ|µ|\$?\s?\\mu\s?\$?\s?)"
_VULGAR = {(1, 2): "½", (1, 4): "¼", (3, 4): "¾", (1, 3): "⅓", (2, 3): "⅔", (1, 8): "⅛", (3, 8): "⅜", (5, 8): "⅝", (7, 8): "⅞"}


def frac_re(num: int, den: int, whole: int | None = None) -> str:
    """Regex for the (mixed) fraction ``whole num/den`` as a vulgar fraction, ``n/d``, or LaTeX ``\\frac``."""
    forms = [rf"{num}\s?[/⁄]\s?{den}", rf"\$?\s?\\[dt]?frac\s?\{{?{num}\}}?\s?\{{?{den}\}}?\s?\$?"]
    if (num, den) in _VULGAR:
        forms.insert(0, _VULGAR[(num, den)])
    frac = _alts(*forms)
    if whole is None:
        return frac
    return rf"\$?\s?{whole}" + _alts(rf"\s?{frac}", rf"\s+{num}\s?/\s?{den}")


def sub_re(base: str, sub: str) -> str:
    """Regex accepting ``base`` followed by subscript ``sub`` in any marked or plain form."""
    s = re.escape(sub)
    form = _alts(
        s,
        rf"\$?_\{{?{s}\}}?\$?",
        rf"\$?_\{{?\\mathrm\{{{s}\}}\}}?\$?",
        rf"<sub>\s*{s}\s*</sub>",
        re.escape(sub.translate(_SUBS)),
        rf"~{s}~",
    )
    return re.escape(base) + r"(?:\$\s*)?" + form


def sup_re(base: str, sup: str) -> str:
    """Regex accepting ``base`` followed by MARKED superscript ``sup`` (a plain digit run fails)."""
    s = re.escape(sup).replace(r"\-", "[-−–]")
    form = _alts(
        rf"\$?\s*\^\s*\{{?\s*{s}\s*\}}?\s*\$?",
        rf"<sup>\s*{s}\s*</sup>",
        re.escape(sup.translate(_SUPS)),
        rf"\^{s}\^",
    )
    return re.escape(base) + r"\s?(?:\$\s*)?(?:\\mathrm\{[^}]*\}\s*)?" + form


class Probes:
    def __init__(self, doc: str):
        self.doc = doc
        self.rows: list[dict] = []
        self._n = 0

    def _add(self, category: str, type_: str, page: int, note: str | None, **kw) -> None:
        self._n += 1
        row = {"pdf": self.doc, "page": page, "id": f"{self.doc}_{self._n:03d}", "type": type_, "category": category}
        row.update({k: v for k, v in kw.items() if v is not None})
        if note:
            row["note"] = note
        self.rows.append(row)

    # text
    def present(self, category: str, text: str, page: int = 1, max_diffs: int = 0, note: str | None = None, case_sensitive: bool = True):
        self._add(category, "present", page, note, text=text, max_diffs=max_diffs, case_sensitive=case_sensitive)

    def absent(self, category: str, text: str, page: int = 1, max_diffs: int = 0, note: str | None = None, case_sensitive: bool = False):
        self._add(category, "absent", page, note, text=text, max_diffs=max_diffs, case_sensitive=case_sensitive)

    def order(self, category: str, before: str, after: str, page: int = 1, max_diffs: int = 0, note: str | None = None):
        self._add(category, "order", page, note, before=before, after=after, max_diffs=max_diffs)

    def regex(self, category: str, pattern: str, page: int = 1, absent: bool = False, note: str | None = None):
        re.compile(pattern)
        self._add(category, "regex_absent" if absent else "regex_present", page, note, pattern=pattern)

    # structure
    def heading(self, text: str, page: int = 1, note: str | None = None):
        self._add("headings", "heading", page, note, text=text)

    def figure(self, caption: str, page: int = 1, note: str | None = None):
        self._add("figures", "figure", page, note, caption=caption)

    def table(self, cell: str, page: int = 1, note: str | None = None, max_diffs: int = 0, **rel):
        self._add("tables", "table", page, note, cell=cell, max_diffs=max_diffs, **rel)

    def math(self, latex: str, page: int = 1, note: str | None = None):
        self._add("math", "math", page, note, math=latex)

    # shorthands
    def sub(self, base: str, sub: str, page: int = 1, note: str | None = None):
        self.regex("inline", sub_re(base, sub), page, note=note or f"{base}_{sub}")

    def sup(self, base: str, sup: str, page: int = 1, note: str | None = None):
        self.regex("inline", sup_re(base, sup), page, note=note or f"{base}^{sup}")


def compile_doc(doc: str) -> list[dict]:
    src = PROBES / "src" / f"{doc.replace('-', '_')}.py"
    spec = importlib.util.spec_from_file_location(f"probes_{doc}", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    p = Probes(doc)
    mod.probes(p)
    p.regex("chars", r"&(?:amp|lt|gt|quot|apos|#\d+);", absent=True, note="HTML entity left in the text")
    return p.rows


def main() -> None:
    docs = sys.argv[1:] or sorted(f.stem.replace("_", "-") for f in (PROBES / "src").glob("*.py"))
    for doc in docs:
        rows = compile_doc(doc)
        (PROBES / f"{doc}.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
        cats: dict[str, int] = {}
        for r in rows:
            cats[r["category"]] = cats.get(r["category"], 0) + 1
        print(doc, len(rows), cats)


if __name__ == "__main__":
    main()
