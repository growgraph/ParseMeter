"""PLOS ONE 10.1371/journal.pone.0346024 (CC BY 4.0) — 20 pages, single column with a left
sidebar on p1-2, 8 tables (some spanning pages), superscript table notes, per-table DOI lines."""


from study.author import DEG


def probes(p):
    # furniture
    p.absent("furniture", "PLOS One | https://doi.org/10.1371/journal.pone.0346024 March 27, 2026", 2, max_diffs=3, note="running footer")
    p.regex("furniture", r"\b(?:6|12|16) / 20\b", 6, absent=True, note="page counter in the footer")

    # stitching: the abstract continues on p2 after the license sidebar
    p.present("stitching", "particularly using herbal biomass, presents a promising strategy for the comprehensive and high-value utilization", 1)
    p.present("stitching", "a new wave of \"Low carbon\" trends", 2, max_diffs=1)
    p.present("stitching", "field emission scanning electron microscopy (FESEM)", 3)
    p.present("stitching", "lignin decomposition produces mainly biochar and some volatile matters", 14)
    p.order("reading_order", "Competing interests: The authors have declared that no competing interests exist.", "Introduction", 2,
            note="sidebar (license, funding) kept apart from the abstract")

    # tables
    p.table("679.256", 6, left_heading="Tubers biomass", left="39.4", right="5.42", note="Table 1, units row under the header")
    p.table("29.2", 6, left_heading="Herbal biomass", top_heading="Cellul-ose", max_diffs=1)
    p.table("188.89", 16, left="0.04", right="0.97", note="Table 7, two-level header Langmuir/Freundlich/...")
    p.table("125.63", 16, left_heading="HB-Cd2+", max_diffs=2)
    p.table("000497-23-4", 13, left="2(5H)-Furanone", right="C4H4O2", note="Table 3, long compound list")
    p.table("6.412", 13, left="C31H37N7O7", right="2.07")

    # table notes
    p.present("footnotes", "This means the default CAS data.", 13)
    p.regex("footnotes", r"(?:\^\{?a\}?|<sup>a</sup>|\ba)\s?\$?\s?This means the default CAS data", 13, note="note keeps its marker")
    p.order("footnotes", "This means the default CAS data.", "pore structure becoming dense and diverse", 13, note="note follows its table")

    # inline / units
    p.regex("inline", r"Cd\s?(?:\^\s*\{?2\+\}?|<sup>2\+</sup>|²⁺)", 16, note="Cd2+ charge as superscript")
    p.regex("inline", r"mg\s?·\s?g\s?(?:\^\s*\{?\s*-\s?1\}?|<sup>\s*-\s?1</sup>|⁻¹)", 16)
    p.regex("inline", r"R\s?(?:\^\s*\{?2\}?|<sup>2</sup>|²)\s?\$?\s?≥\s?\$?\s?0\.98", 1)
    p.regex("inline", r"CaCO\s?(?:3|_\{?3\}?|<sub>3</sub>|₃)", 6)

    # characters
    p.regex("chars", r"2θ angles", 6)
    p.regex("chars", rf"24\.4\s?{DEG}, 26\.4\s?{DEG} and 29\.4\s?{DEG}", 6)
    p.present("chars", "α-D-glucose", 14)
    p.regex("chars", rf"280\s?[-–]\s?500\s?{DEG}\s?C?", 14)

    # headings
    for h, pg in [("Abstract", 1), ("Introduction", 2), ("Materials and methods", 4), ("Results and discussions", 5)]:
        p.heading(h, pg)

    # figures
    p.figure("Fig 3. XRD patterns of the prepared materials.", 8)
    p.figure("Fig 5. Adsorption-desorption isotherm of TB (a) and HB (b).", 10)
    p.figure("Fig 7. Isotherm adsorption curves of Cd2+ by TB and HB.", 16)
