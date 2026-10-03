"""NACA RM E7B11c (1947, US government work) — 15 scanned pages, no text layer: stamped cover plus a
typewritten research memorandum with display equations, numbered equations (1)-(2), a two-column
symbol list, a table directly after a page break, running header ``NACA RM No. E7B11c`` + page number."""

from study.author import DEG, sub_re

# running header as printed, with OCR latitude on "RM" and the "11" of the report number
HDR = r"NACA\s+R\S{0,2}\s+No\.?\s*E7B\S{2}c"
DEGF = rf"(?:{DEG}\s?\$?\s?(?:F|\\mathrm\{{F\}}|\\text\{{F\}})\s?\$?|℉)"
# stacked 1/16 in a mixed number
FRAC = r"\$?\s?(?:1\s?/\s?16|\\frac\s?\{?1\}?\s?\{?16\}?|\\tfrac\s?\{?1\}?\s?\{?16\}?|¹⁄₁₆|1⁄16|¹/₁₆)\s?\$?"
LAM = r"\$?\s?(?:λ|\\lambda)\s?\$?"


def _sandwich(end: str, start: str = "") -> str:
    """End of one page's text, the running header within 40 chars, then (optionally) the next page's text."""
    tail = rf"[\s\S]{{0,40}}?{start}" if start else ""
    return rf"{end}[\s\S]{{0,40}}?(?:{HDR}|RESTRICTED){tail}"


def probes(p):
    # furniture: running header / page number / struck classification stamp between the halves of a sentence
    p.regex("furniture", _sandwich(r"and a sharp", r"temperature rise to the blade tip"), 3, absent=True,
            note="report p.1 -> p.2: struck RESTRICTED stamp + '2 NACA RM No. E7B11c'")
    p.regex("furniture", _sandwich(r"possibilities of much", r"larger increases"), 4, absent=True, note="report p.2 -> p.3")
    p.regex("furniture", _sandwich(r"sections\.\s+They were"), 12, absent=True,
            note="report p.10 -> p.11: 'They were' continues with the list of p_o q_o values")
    p.regex("furniture", _sandwich(r"given in the following table:?"), 13, absent=True,
            note="report p.11 -> p.12: the table sits directly after the page break")
    p.regex("furniture", _sandwich(r"about equal to the coolant", r"temperature, a steady"), 15, absent=True,
            note="report p.13 -> p.14, inside conclusion 2")

    # stitching: sentences crossing a page break (and line-end hyphenation inside a page)
    p.present("stitching", "a nearly constant or prevalent blade temperature through most of the liquid-cooled part of the blade, "
              "and a sharp temperature rise to the blade tip", 3, max_diffs=3, note="crosses PDF p.2 -> p.3")
    p.present("stitching", "and of the possibilities of much larger increases in cooling with liquid cooling suggested in reference 4, "
              "a theoretical analysis was made", 4, max_diffs=3, note="crosses p.3 -> p.4; 'ref-erence' dehyphenated")
    p.present("stitching", "were found to show a rotor temperature about equal to the coolant temperature, a steady temperature rise "
              "through the rim and a small part of the blades", 15, max_diffs=3, note="crosses p.14 -> p.15")
    p.present("stitching", "The analysis was applied to obtain the rotor and blade temperatures of a specific turbine", 2,
              max_diffs=2, note="'anal-ysis' hyphenated at a line end")
    p.present("stitching", "The shorter the blade cooling passages, the less effective is the cooling.", 14, max_diffs=1,
              note="'effec-tive' hyphenated at a line end")
    p.present("stitching", "the prevalent blade temperature F is about one-fifth the effective gas temperature when the turbine is "
              "cooled by water", 13, max_diffs=3, note="'tempera-ture' hyphenated at a line end")

    # reading order: cover before body, symbol list kept as symbol -> definition, table between its lead-in and the prose after it
    p.order("reading_order", "This document contains classified information", "A theoretical analysis of the radial temperature distribution",
            1, max_diffs=1, note="cover classification block precedes the body")
    p.regex("reading_order", r"\bB\s*[|:\-]?\s*number of blades", 4, note="symbol list: symbol next to its definition")
    p.order("reading_order", "thermal conductivity of turbine metal", "perimeter of blade-heating surface", 5, max_diffs=1,
            note="symbol list continues across p.4 -> p.5")
    p.order("reading_order", "are given in the following table", "Kerosene", 13, max_diffs=1)
    p.order("reading_order", "Kerosene", "The large flow of heat near the cooling fluid may produce considerable", 13, max_diffs=1)
    p.regex("reading_order", r"6\s?4\s?9\b(?:(?!5\s?1\s?0\b|2\s?3\s?7\s?0\b)[\s\S]){0,80}?ethylene glycol", 11,
            note="value column paired with its coolant label column")

    # display equations (report pp. 6-9); those carrying the script-l subscript T_l are left out
    for pg, tex, what in [
        (7, r"\frac{d^{2}T}{dz^{2}}-\nu^{2}T=-\nu^{2}T_{e}", "section 1 ODE; Greek nu, subscript e"),
        (7, r"\nu^{2}=\frac{p_{i}q_{i}}{kA_{1}}", "p_i q_i (dotted i, hot-gas side) over kA_1 (digit one); checked at 400 dpi"),
        (7, r"T=T_{e}-C\cosh\nu(z+\lambda)", "section 1 solution"),
        (7, r"\tanh\nu(z_{1}+\lambda)=\frac{q_{i}}{k\nu}=\sqrt{\frac{q_{i}A_{1}}{p_{i}k}}", "tip condition"),
        (8, r"\frac{d^{2}T}{dx^{2}}-\mu^{2}T=-\gamma^{2}", "section 2 ODE"),
        (8, r"\mu^{2}=\frac{p_{i}q_{i}+p_{o,2}q_{o,2}}{kA_{2}}", "mu^2; subscripts i and letter o"),
        (8, r"T=F-He^{\mu x}-Je^{-\mu x}", "section 2 solution"),
        (8, r"\beta^{2}=\frac{4\pi\bar{r}_{3}q_{o}'+p_{o,3}q_{o,3}}{kA_{3}}", "beta^2; r-bar as \\bar, q_o prime, letter-o subscripts"),
        (9, r"T=L+Ke^{\beta y}+Me^{-\beta y}", "section 3 solution"),
        (9, r"\frac{d^{2}T}{dr^{2}}-\alpha^{2}T=-\zeta^{2}", "section 4 ODE"),
        (10, r"F-He^{\mu x_{2}}-Je^{-\mu x_{2}}=L+Ke^{\beta y_{1}}+Me^{-\beta y_{1}}", "junction 2-3; both exponents carry the minus and beta y_1"),
        (10, r"k\beta(-Ke^{\beta y_{2}}+Me^{-\beta y_{2}})=nk\alpha G\sinh\alpha r_{1}", "junction 3-4; nk alpha G (Greek alpha)"),
    ]:
        p.math(tex, pg, note=what)
    p.regex("math", r"(?:\(1\)|\\tag\{1\})[\s\S]{0,40}?Equation \(1\) equates", 10, note="equation number (1) kept, before its gloss")
    p.regex("math", r"(?:\(2\)|\\tag\{2\})[\s\S]{0,40}?Equation \(2\) equates", 10, note="equation number (2) kept, before its gloss")

    # inline: subscripted symbols in running text
    p.regex("inline", rf"values of \$?{sub_re('q', 'i')}\$?\s+and\s+\$?{sub_re('T', 'e')}\$?\s+over the blade tip", 6, note="q_i, T_e")
    p.regex("inline", rf"value of \$?{sub_re('q', 'i')}\$?\s+was attributed to radiation", 6, note="q_i")
    p.regex("inline", rf"section is denoted by \$?{sub_re('A', 'r')}\$?\s?\.", 10, note="A_r")
    p.regex("inline", rf"An average value for \$?{sub_re('p', 'o,3')}\$?\s?\$?{sub_re('q', 'o,3')}\$?\s+was used", 8, note="p_{o,3} q_{o,3}: subscript is the letter o (coolant side), not zero")
    p.regex("inline", rf"values of \$?{sub_re('p', 'o')}\$?\s?\$?{sub_re('q', 'o')}\$?\s+for the rim", 11, note="p_o q_o: letter o, not zero")
    p.regex("inline", rf"hot gases \$?{sub_re('T', 'e')}\$?\s+was regarded", 12, note="T_e")
    p.regex("inline", rf"\(\s?\$?\s?z\s?=\s?{sub_re('z', '2')}\$?\s+and\s+\$?\s?x\s?=\s?{sub_re('x', '1')}", 10, note="z = z_2 and x = x_1")
    p.regex("inline", rf"lengths in blades \$?\s?4\s?{FRAC}\s?inches long", 4, note="mixed number 4 1/16 (stacked fraction)")

    # characters: degree signs, Greek letters, fractions-with-hyphens
    p.regex("chars", rf"average coolant temperature of \$?\s?200\s?{DEGF}", 2)
    p.regex("chars", rf"varied from \$?\s?2000\s?{DEG}\s?to \$?\s?5000\s?{DEGF}", 2)
    p.regex("chars", rf"temperature drop of \$?\s?450\s?{DEGF} occurred", 9)
    p.regex("chars", rf"Air at \$?\s?0\s?{DEGF} cooled the rim", 12)
    p.regex("chars", rf"where C and {LAM} are integration constants and {LAM} is evaluated", 7, note="lambda in prose")
    p.present("chars", "two 1/4-inch-diameter passages in each blade", 11)
    p.regex("chars", r"3\s?0\s?,\s?3\s?6\s?0\s*(?:\\mathrm\s?\{|\\text\s?\{)?\s*Btu", 12,
            note="thousands comma kept; LaTeX digit spacing tolerated")

    # tables: the coolant table at the top of report p.12, right after a page break
    p.table("Kerosene", 13, left="4", right="2000-5000", note="own row below the two-line Ethylene glycol cell")
    p.table("Kerosene", 13, top_heading="Coolant")
    p.table("5", 13, right="Water", note="first data row")
    p.table("3", 13, up="4", down="2", note="row 4 1/16 | 3 | Water")
    p.table("1", 13, down="3", right="Water", note="row 4 1/16 | 1 | Water")

    # headings: centred all-caps section titles as typed
    for h, pg in [("SUMMARY", 2), ("INTRODUCTION", 3), ("SYMBOLS", 4), ("THEORETICAL ANALYSIS", 6),
                  ("APPLICATION OF ANALYSIS", 11), ("RESULTS AND DISCUSSION", 12), ("CONCLUSIONS", 14), ("REFERENCES", 15)]:
        p.heading(h, pg)
