"""Apple Form 10-K, FY2025 — 80 pages, EDGAR HTML rendered to PDF; statements, notes, exhibits."""


def probes(p):
    # furniture
    p.absent("furniture", "Apple Inc. | 2025 Form 10-K | 37", 40, max_diffs=2, note="running footer, every page")

    # stitching: sentences across page breaks (exhibit 4.1 pages)
    p.present("stitching", "the most recent U.S. dollar/euro exchange rate published in The Wall Street Journal on", 65)
    p.present("stitching", "on not less than 10 nor more than 60 days' prior notice, in each case at a redemption price", 67, max_diffs=1)
    p.present("stitching", "with the advice of three brokers of, and/or market makers in, United Kingdom government bonds selected by us", 68)
    p.order("stitching", "Mortgage- and asset-backed securities", "Total (2)(3)", 40, note="two-year table pair on one page")

    # tables
    p.table("194,116", 32, left_heading="Products", right="185,233", note="statement of operations")
    p.table("(321)", 32, left_heading="Other income/(expense), net", right="269")
    p.table("15,004,697", 32, left_heading="Diluted", right="15,408,095")
    p.table("33,180", 34, left_heading="Vendor non-trade receivables", right="32,833")
    p.table("(14,264)", 34, left_heading="Accumulated deficit", right="(19,154)")
    p.table("33,708", 26, left_heading="Mac", right="12 %", note="% change columns")
    p.table("(4)%", 26, left_heading="Wearables, Home and Accessories", left="35,686")
    p.table("109,158", 26, left_heading="Services (1)", note="footnote marker in the row label")
    p.table("(1,252)", 40, left_heading="Mortgage- and asset-backed securities", left="126", right="23,004")
    p.table("(1,953)", 40, left_heading="Corporate debt securities", left="270", right="63,939")
    p.table("64,377", 51, left_heading="China (1)", right="66,952")
    p.table("3,617", 51, left_heading="China (1)", right="4,797")
    p.table("28,986", 22, left_heading="Open market and privately negotiated purchases", note="repurchase table, 5-row header")
    p.table("287", 23, left_heading="Dow Jones U.S. Technology Total Stock Market Index", top_heading="September 2025", max_diffs=1, note="every cell carries $; allow it merged")

    # footnotes under tables
    p.present("footnotes", "Services net sales include amortization of the deferred value of services bundled in the sales price of certain products.", 26)
    p.present("footnotes", "As of September 28, 2024, current marketable securities included $13.2 billion held in escrow and restricted from general use.", 40)
    p.present("footnotes", "China includes Hong Kong and Taiwan.", 51)
    p.present("footnotes", "On May 2, 2024, the Company announced a program to repurchase up to $110 billion of the Company's common stock.", 22)
    p.order("footnotes", "Total (2)(3)", "As of September 28, 2024, cash and cash equivalents included $2.6 billion held in escrow", 40)
    p.order("footnotes", "China includes Hong Kong and Taiwan.", "Report of Independent Registered Public Accounting Firm", 51, note="note stays before the next section")

    # reading order
    p.order("reading_order", "CONSOLIDATED STATEMENTS OF OPERATIONS", "CONSOLIDATED BALANCE SHEETS", 32)
    p.order("reading_order", "Note 3 – Earnings Per Share", "Note 4 – Financial Instruments", 39)

    # figures: the stock performance graph (a chart, drawn as an image)
    p.figure("The following graph shows a comparison of five-year cumulative total shareholder return", 23)

    # headings
    for h, pg in [("Item 1. Business", 4), ("Item 1A. Risk Factors", 8), ("Item 1C. Cybersecurity", 20),
                  ("Item 5. Market for Registrant's Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities", 22),
                  ("Item 7. Management's Discussion and Analysis of Financial Condition and Results of Operations", 24),
                  ("Item 8. Financial Statements and Supplementary Data", 31), ("Note 2 – Revenue", 38), ("Note 7 – Income Taxes", 43),
                  ("Note 9 – Debt", 46), ("Item 9A. Controls and Procedures", 55), ("Item 15. Exhibit and Financial Statement Schedules", 57),
                  ("DESCRIPTION OF DEBT SECURITIES", 64)]:
        p.heading(h, pg)

    # characters
    p.regex("chars", r"(?:☒|\[x\]|\[X\]|☑|■)\s?ANNUAL REPORT PURSUANT TO SECTION 13", 1)
    p.regex("chars", r"S&P 500 Index", 23, note="ampersand, not an HTML entity")
