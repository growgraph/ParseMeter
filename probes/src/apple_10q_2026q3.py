"""Apple Form 10-Q, Q3 FY2026 — 32 pages, EDGAR HTML rendered to PDF, ~20 financial tables.

Table probes use the row label (``left_heading``) plus a neighbour or the period header,
and never a cell sitting next to a ``$`` column (converters split or merge those freely).
"""


def probes(p):
    # furniture
    p.absent("furniture", "Apple Inc. | Q3 2026 Form 10-Q | 7", 10, max_diffs=2, note="running footer, every page")

    # tables — statements of operations / comprehensive income / balance sheet / equity / cash flows
    p.table("47,153", 4, left_heading="Products", top_heading="Three Months Ended", right="43,620")
    p.table("(171)", 4, left_heading="Other income/(expense), net", right="670")
    p.table("14,750,302", 4, left_heading="Diluted", top_heading="Nine Months Ended", right="15,051,726")
    p.table("(1,094)", 5, left_heading="Total change in unrealized gains/losses on derivative instruments", right="1,077")
    p.table("27,509", 6, left_heading="Vendor non-trade receivables", right="33,180")
    p.table("(14,264)", 6, left_heading="Retained earnings/(Accumulated deficit)", left="11,326")
    p.table("(25,949)", 7, left_heading="Common stock repurchased", right="(21,166)")
    p.table("(16,266)", 8, left_heading="Other current and non-current assets", right="(6,116)")
    # notes
    p.table("27,277", 9, left_heading="Wearables, Home and Accessories", top_heading="Nine Months Ended", right="26,673")
    p.table("(1,192)", 10, left_heading="Mortgage- and asset-backed securities", left="65", right="23,701", note="7-column, 3-row header")
    p.table("35,937", 11, left_heading="Corporate debt securities", left="10,623")
    p.table("(3,788)", 13, left_heading="Repayments of commercial paper", right="—")
    p.table("72,400", 14, left_heading="RSUs granted")
    p.table("6,406", 14, left_heading="2028")
    p.table("(10,771)", 15, left_heading="Cost of sales", left="(14,732)", right="(3,310)", note="segment table")
    p.table("(6)%", 18, left_heading="iPad", left="6,581", right="21,700")
    p.table("39.9%", 19, left_heading="Products", left="34.5%")
    p.table("17.9%", 20, left_heading="Effective tax rate", right="16.4%")
    p.table("AAPL", 1, left_heading="Common Stock, $0.00001 par value per share", top_heading="Trading symbol(s)", note="cover-page securities table")

    # footnotes
    p.present("footnotes", "The valuation techniques used to measure the fair values of the Company's Level 2 financial instruments, which generally have counterparties with high credit ratings", 11)
    p.order("footnotes", "The valuation techniques used to measure the fair values", "81% of the Company's non-current marketable debt securities", 11, note="table note stays with its table")

    p.present("footnotes", "In May 2026, the Company entered into new accelerated share repurchase agreements", 27)
    p.present("footnotes", "On April 30, 2026, the Company announced an additional program to repurchase up to $100 billion", 27)
    p.order("footnotes", "May 2026 ASRs", "In May 2026, the Company entered into new accelerated share repurchase agreements", 27)
    p.table("26,920", 27, left_heading="Open market and privately negotiated purchases", note="repurchase table, 5-row header")
    p.table("26,468", 27, left_heading="May 2026 ASRs")

    # reading order: statements in sequence, sections in sequence
    p.order("reading_order", "CONDENSED CONSOLIDATED STATEMENTS OF OPERATIONS", "CONDENSED CONSOLIDATED STATEMENTS OF COMPREHENSIVE INCOME", 4)
    p.order("reading_order", "CONDENSED CONSOLIDATED BALANCE SHEETS", "CONDENSED CONSOLIDATED STATEMENTS OF CASH FLOWS", 6)
    p.order("reading_order", "Note 9 - Commitments and Contingencies", "Note 10 - Segment Information", 14)

    # stitching: notes table split by a page break (June table p10, September table p11)
    p.order("stitching", "Mortgage- and asset-backed securities", "September 27, 2025", 10)
    p.present("stitching", "the Company had one customer that represented 10% or more of total trade receivables", 12)

    # headings
    for h, pg in [("PART I — FINANCIAL INFORMATION", 4), ("Item 1. Financial Statements", 4), ("Note 1 – Summary of Significant Accounting Policies", 9),
                  ("Note 2 – Revenue", 9), ("Note 4 – Financial Instruments", 10), ("Note 10 – Segment Information", 15),
                  ("Item 2. Management's Discussion and Analysis of Financial Condition and Results of Operations", 16),
                  ("Segment Operating Performance", 17), ("Gross Margin", 19), ("Liquidity and Capital Resources", 21),
                  ("Item 4. Controls and Procedures", 22), ("Item 1A. Risk Factors", 24)]:
        p.heading(h, pg)

    # characters
    p.regex("chars", r"(?:☒|\[x\]|\[X\]|☑|■)\s?QUARTERLY REPORT PURSUANT TO SECTION 13", 1, note="checked box")
    p.regex("chars", r"(?:☐|\[ \]|□)\s?TRANSITION REPORT PURSUANT", 1, note="unchecked box")
    p.regex("chars", r"iPhone\s?®", 9, note="registered sign")
    p.present("chars", "Intangibles—Goodwill and Other—Internal-Use Software", 21, max_diffs=2)
