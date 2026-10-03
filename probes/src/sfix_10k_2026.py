"""Stitch Fix Form 10-K, FY2026 — 110 pages; a "Table of Contents" link heads every page,
paragraphs run across page breaks throughout the risk factors and notes."""


def probes(p):
    # furniture
    p.absent("furniture", "STITCH FIX, INC. | 2026 FORM 10-K | 35", 38, max_diffs=2, note="running footer")
    p.regex("furniture", r"(?i)table of contents\s+(?:\S+\s+){0,3}(?:respectively, representing a year-over-year decrease|internal-use software is capitalized|revenue until the performance obligation)", 38, absent=True,
            note="'Table of Contents' page header spliced at the top of a continuing paragraph")

    # stitching: sentences that cross a page break
    for pg, text in [
        (8, "control the use of our proprietary technology and intellectual property through provisions in both our client terms"),
        (12, "expectations, our business, financial condition, operating results, and reputation could be adversely affected"),
        (17, "Additional changes in our management team and senior leadership could cause retention and morale concerns"),
        (21, "Additionally, the launch of new client experiences or offerings requires investments in"),
        (26, "may be materially impacted by sudden or unforeseen changes in tax laws"),
        (29, "limit the opportunity for our stockholders to receive a premium for their shares of our common stock"),
        (37, "as of August 1, 2026, and August 2, 2025, respectively, representing a year-over-year decrease of 1.4%"),
        (42, "base our estimates on historical experience and other assumptions that we believe to be reasonable"),
        (49, "Accrued interest receivable was $1.4 million and $1.1 million as of August 1, 2026, and August 2, 2025, respectively"),
        (50, "A subsequent addition, modification, or upgrade to internal-use software is capitalized to the extent"),
        (51, "Style Pass annual fee are included in deferred revenue until the performance obligation is satisfied"),
        (102, "mobile telephones, tablets, handheld devices, and servers), credit cards, entry cards"),
    ]:
        p.present("stitching", text, pg, max_diffs=1)

    # tables
    p.table("4,223", 37, left_heading="Non-ordinary course legal fees (2)", right="229", note="adjusted EBITDA reconciliation")
    p.table("(8,661)", 37, left_heading="Interest income", right="(10,709)")
    p.table("2,277", 37, left_heading="Active clients (in thousands)", right="2,309")
    p.table("(2.8)%", 41, left_heading="Effective tax rate", right="(2.9)%")
    p.table("122,707", 47, left_heading="Inventory, net", right="118,370", note="balance sheet")
    p.table("(508,598)", 47, left_heading="Accumulated deficit", right="(495,992)")
    p.table("109,767", 47, left_heading="Accrued liabilities", right="76,348")
    p.table("79,981", 58, left_heading="Corporate bonds (1)", note="fair-value hierarchy, 8 value columns")
    p.table("(320)", 58, left_heading="Corporate bonds", right="79,981")
    p.table("9,170", 59, left_heading="2029", note="lease maturity table")
    p.table("75,239", 59, left_heading="Total undiscounted future minimum lease payments(1)")
    p.table("77.2 %", 67, left_heading="Research and development tax credits", left="(9,468)", note="tax rate reconciliation")
    p.table("5,511", 67, left_heading="Excess Officer's Compensation", right="(44.9)%")
    p.table("3 years", 50, left_heading="Computer equipment and capitalized software")

    # footnotes under tables
    p.present("footnotes", "Non-ordinary course legal fees include costs related to a specific class action lawsuit.", 37)
    p.present("footnotes", "State taxes in California made up the majority (greater than 50 percent) of the tax effect in this category.", 67)
    p.present("footnotes", "In fiscal 2024, the Company recorded an impairment charge related to a portion of its corporate office space of $16.6 million.", 59)
    p.order("footnotes", "Non-ordinary course legal fees include costs related to a specific class action lawsuit.", "Net cash provided by operating activities from continuing operations", 37,
            note="note under its table, before the next table")
    p.order("footnotes", "State taxes in California made up the majority", "Taxes at federal statutory rate", 67)

    # reading order
    p.order("reading_order", "CONSOLIDATED BALANCE SHEETS", "DESCRIPTION OF BUSINESS", 47)
    p.order("reading_order", "FAIR VALUE MEASUREMENTS", "INVENTORY, NET", 53)

    # headings
    for h, pg in [("FACTORS AFFECTING OUR PERFORMANCE", 38), ("MACROECONOMIC ENVIRONMENT", 38), ("PROVISION FOR INCOME TAXES", 41),
                  ("LIQUIDITY AND CAPITAL RESOURCES", 41), ("SHARE REPURCHASES", 41), ("ITEM 7A. QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK", 44),
                  ("1. DESCRIPTION OF BUSINESS", 52), ("2. SIGNIFICANT ACCOUNTING POLICIES", 52), ("REVENUE RECOGNITION", 54),
                  ("IMPAIRMENT OF LONG-LIVED ASSETS", 54), ("KEY FINANCIAL AND OPERATING METRICS", 36), ("SUPPLEMENTAL CASH FLOW INFORMATION", 59)]:
        p.heading(h, pg)

    # characters
    p.regex("chars", r"(?:☒|\[x\]|\[X\]|☑|■)\s?ANNUAL REPORT PURSUANT TO SECTION 13", 1, note="checked box; cover lines wrap badly in the text layer")
    p.present("chars", "first-in-first-out (FIFO) method", 53)
    p.regex("chars", r"Selling, general, and administrative expenses \(\"SG&A\"\)", 38, note="ampersand and quotes")
