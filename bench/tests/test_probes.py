"""The scorer on hand-made markdown: a clean conversion passes every probe, and each
deliberate corruption fails exactly the category it targets."""

import pytest

from study.author import Probes, sub_re, sup_re
from study.probes import build_test, run_test

GOLD = """# Cooperative excitons in superlattices

## Results

Perovskites are an excellent optical candidate for achieving large oscillator strength<sup>1-4</sup>.
The samples remain stable in the ambient atmospheric environment for several months.
Dense CsPbBr<sub>3</sub> superlattices give N<sub>eff</sub> ~10<sup>2</sup> cooperative dipoles at 70 μJ cm$^{-2}$.

<!-- image -->

Fig. 1 Linking self-assembly of QDs to phase transitions of exciton ensemble.

| Item | 2026 | 2025 |
|---|---|---|
| Products | 47,153 | 43,620 |
| Other income/(expense), net | (171) | 572 |

(1) Services net sales include amortization of deferred value.

$$E = mc^2$$

## Methods

Highly efficient light absorption was measured.
"""


def _probes() -> list[dict]:
    p = Probes("synthetic")
    p.absent("furniture", "NATURE COMMUNICATIONS | (2020)11:329 | www.nature.com", max_diffs=4)
    p.present("stitching", "remain stable in the ambient atmospheric environment for several months")
    p.order("reading_order", "Results", "Methods")
    p.present("footnotes", "Services net sales include amortization of deferred value.")
    p.table("47,153", left_heading="Products", right="43,620")
    p.table("(171)", left_heading="Other income/(expense), net")
    p.math("E = mc^2")
    p.sub("CsPbBr", "3")
    p.sup("~10", "2")
    p.sup("μJ cm", "-2")
    p.regex("inline", r"strength\s?1\s?-\s?4\b", absent=True)
    p.heading("Results")
    p.heading("Methods")
    p.figure("Fig. 1 Linking self-assembly of QDs")
    p.present("chars", "Highly efficient light absorption")
    return p.rows


def _failing(md: str) -> set[str]:
    return {row["category"] for row in _probes() if not run_test(build_test(row), md)[0]}


def test_gold_passes_everything():
    assert _failing(GOLD) == set()


@pytest.mark.parametrize(
    ("corrupt", "category"),
    [
        (lambda s: s.replace("several months.", "several\n\nNATURE COMMUNICATIONS | (2020)11:329 | www.nature.com\n\nmonths."), {"furniture", "stitching"}),
        (lambda s: s.replace("ambient atmospheric", "ambient\n\n<!-- page break -->\n\nZZZ atmospheric"), {"stitching"}),
        (lambda s: s.replace("| 47,153 | 43,620 |", "| 47,153 | 99,999 |"), {"tables"}),
        (lambda s: s.replace("strength<sup>1-4</sup>", "strength 1-4"), {"inline"}),
        (lambda s: s.replace("~10<sup>2</sup>", "~102"), {"inline"}),
        (lambda s: s.replace("CsPbBr<sub>3</sub>", "CsPbBr 3"), {"inline"}),
        (lambda s: s.replace("## Methods", "Methods"), {"headings"}),
        (lambda s: s.replace("<!-- image -->", ""), {"figures"}),
        (lambda s: s.replace("$$E = mc^2$$", "E = mc2"), {"math"}),
        (lambda s: s.replace("efficient", "eﬃcient"), {"chars"}),
        (lambda s: s.replace("(1) Services net sales include amortization of deferred value.", ""), {"footnotes"}),
    ],
)
def test_corruption_fails_its_category(corrupt, category):
    assert _failing(corrupt(GOLD)) == category


@pytest.mark.parametrize("form", ["CsPbBr3", "CsPbBr$_3$", "CsPbBr$_{3}$", "CsPbBr<sub>3</sub>", "CsPbBr₃", "CsPbBr_{\\mathrm{3}}"])
def test_subscript_forms_accepted(form):
    import re

    assert re.search(sub_re("CsPbBr", "3"), form)


@pytest.mark.parametrize("form", ["10^2", "10$^{2}$", "10<sup>2</sup>", "10²", "10^{2}"])
def test_superscript_forms_accepted(form):
    import re

    assert re.search(sup_re("10", "2"), form)


@pytest.mark.parametrize("form", ["102", "10 2", "CsPbBr 3"])
def test_flattened_forms_rejected(form):
    import re

    assert not re.search(sup_re("10", "2"), form) or form == "CsPbBr 3"
    assert not re.search(sub_re("CsPbBr", "3"), "CsPbBr 3")


def test_output_without_text_counts_as_no_output():
    from study.score import has_text

    assert not has_text("")
    assert not has_text("<!-- image -->\n\n![](_page_1_Figure_0.jpeg)\n<img src='x.png'>\n")
    assert has_text("<!-- image -->\nPage one.")
