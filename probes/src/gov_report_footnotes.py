"""CRS Report R47872 (US government work) — 18 pages, footnotes at the bottom of nearly every page,
running header/footer, a table whose notes continue onto the next page."""


def probes(p):
    # furniture: running header text glued to the first line of the next page's body
    p.regex("furniture", r"Inflation Reduction Act\s+(?:Selected Drug Negotiation Provisions of the IRA|Secretary announced that all manufacturers|Enbrel, Stelara, and Fiasp)", 5,
            absent=True, note="running header between pages")
    p.regex("furniture", r"Congressional Research Service\s+\d{1,2}\s+(?:Medicare Drug Price|Selected Drug|Secretary announced|Enbrel)", 4, absent=True, note="footer + page number")

    # stitching across pages, with a block of footnotes between the halves
    p.present("stitching", "In October 2023, the Secretary announced that all manufacturers of the selected drugs had agreed to participate in negotiations", 5,
              note="footnotes 8-12 and the page header sit between the halves")
    p.present("stitching", "Enbrel, Stelara, and Fiasp are biologics.", 7, note="table notes continue on the next page")
    p.order("stitching", "Notes: According to HHS, from June 1, 2022 to May 31, 2023", "The designation also covers the products", 6, max_diffs=1)

    # footnotes: present, and kept out of body sentences
    for pg, text in [
        (4, "Pub. L. No. 117-169, tit. I, subtit. B, pt. 1, 136 Stat. 1818"),
        (4, "For the ASP methodology, see 42 U.S.C. § 1395w-3a."),
        (5, "Biologics are pharmaceuticals derived from a living organism"),
        (7, "Starting in 2030, the IRA includes a third MFP ceiling, which is to be 65% of the non-FAMP"),
    ]:
        p.present("footnotes", text, pg)
    p.present("footnotes", "Overall, Medicare accounts for about 32% of U.S. retail drug spending, with much of the spending concentrated in higher-cost brand name and specialty drugs.", 4,
              note="body sentence carrying marker 7, intact")
    p.regex("footnotes", r"169\),\s?1\s+including", 4, absent=True, note="footnote marker 1 left as a bare number in the sentence")
    p.regex("footnotes", r"\$200 million;\s+indexed for inflation", 5, note="list item not broken by footnotes")
    p.order("footnotes", "would be set as a percentage of the sum", "Industry Responses to IRA Negotiation Program", 7)

    # reading order
    p.present("reading_order", "This report provides information related to several topics of recent congressional concern", 4, note="drop cap T")
    p.order("reading_order", "Kevin J. Hickey", "In accordance with the statute, the Secretary must negotiate MFPs", 2, note="summary sidebar")

    # table
    p.table("3,706,000", 6, left="$16,482,621,000", note="Table 1, multi-line cells")
    p.table("869,000", 6, left="$4,087,081,000")
    p.table("$2,663,560,000", 6, right="20,000")
    p.table("Novo Nordisk Inc.", 6, right="Diabetes")
    p.present("figures", "Table 1. Part D Selected Drugs for Negotiation for the Initial 2026 Price Year", 6)

    # characters
    p.regex("chars", r"42 U\.S\.C\. §§ 1320f-1 to f-7", 4)
    p.regex("chars", r"Crohn['’]s disease", 6)
    p.regex("chars", r"Centers for Medicare & Medicaid Services", 7)

    # headings
    for h, pg in [("Medicare Coverage of Prescription Drugs", 4), ("Selected Drug Negotiation Provisions of the IRA", 5),
                  ("Drugs Eligible for Negotiation", 5), ("MFP Ceiling", 7), ("Industry Responses to IRA Negotiation Program", 7), ("Contents", 3)]:
        p.heading(h, pg)
