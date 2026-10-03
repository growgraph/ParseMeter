"""Bureau of Standards Journal of Research RP1 (1928), "Accelerated Tests of Organic Protective Coatings"
(US government work) — 14-page excerpt, journal pp. 3-14 plus two photo plates (PDF pp. 3-4) that
interrupt a sentence crossing journal pp. 4-5. 600 dpi scan with a hidden OCR layer. Seven numeric
tables (brace-grouped row blocks in Tables 2, 3 and 5), table and page footnotes, alternating running
headers. Page numbers below are PDF pages of the excerpt; decimals are printed with a thin space
after the point ("8. 5") and are expected as plain decimals ("8.5")."""

from study.author import DEG, MU, frac_re, sub_re, sup_re

# running headers: verso "N Bureau of Standards Journal of Research [Vol. 1",
# recto "Walker, Hickson] Tests of Organic Protective Coatings N"; plates carry "B. S. Journal of Research, RP1"
_HDR = r"(?:Journal of Research|Organic Protective Coatings|Walker,? Hickson)"


def _between(end: str, start: str, w: int = 900) -> str:
    """Header text found between the two halves of a sentence that crosses a page break."""
    return rf"{end}(?:(?!{start}).){{0,{w}}}?{_HDR}(?:(?!{end}).){{0,{w}}}?{start}"


def probes(p):
    # furniture: running header (or plate label) left between the halves of a body sentence
    p.regex("furniture", _between(r"placed in the bottom of this", r"glass chamber to moisten"), 3, absent=True,
            note="j. p4 -> two plates -> j. p5; plate label 'B. S. Journal of Research, RP1' + recto header")
    p.regex("furniture", _between(r"square feet per", r"gallon\. Triplicate"), 7, absent=True, note="recto header j. p7")
    p.regex("furniture", _between(r"the only one who collaborated", r"with any other member"), 8, absent=True,
            note="verso header j. p8, page footnote 3 also between the halves")
    p.regex("furniture", _between(r"exposed to the same high", r"humidity condition showed"), 10, absent=True,
            note="verso header j. p10, footnotes 6-8 also between")
    p.regex("furniture", _between(r"disintegration by visual inspection that they were", r"removed from the test"), 12, absent=True,
            note="verso header j. p12")
    p.absent("furniture", "B. S. Journal of Research, RP1", 3, max_diffs=1, note="plate label on both plate pages")

    # stitching: sentences crossing a page break (dehyphenated)
    p.present("stitching", "Some water is placed in the bottom of this glass chamber to moisten the ozonized air.", 5, max_diffs=2,
              note="two full-page photo plates (Figs. 4-7) sit between the halves")
    p.present("stitching", "Each of these paints was applied in three spreading rates—600, 900, and 1,200 square feet per gallon.", 7, max_diffs=2)
    p.present("stitching", "A. H. Sabin was the only one who collaborated with any other member of the subcommittee;", 8, max_diffs=2,
              note="page footnote 3 sits between the halves")
    p.present("stitching", "one of the greatest needs for the study of paint and similar coatings is a method or methods for determining the time of breakdown of the coatings.", 9, max_diffs=4,
              note="footnotes 4 and 5 sit between the halves")
    p.present("stitching", "A similar sieve uncoated and exposed to the same high humidity condition showed an average passage of about 7.4 g of water.", 10, max_diffs=3,
              note="footnotes 6-8 sit between the halves")
    p.present("stitching", "showed such complete disintegration by visual inspection that they were removed from the test and kept in a clean, dry container.", 12, max_diffs=3)

    # footnotes: page and table footnotes present; markers not left as bare numbers in the body
    p.present("footnotes", "Proc. Am. Soc. Test. Mtls., 22, Pt. II, p. 485; 1922", 1, max_diffs=1, note="page footnote 2")
    p.regex("footnotes", r"Nelson and others\s?2\s+has not been used", 1, absent=True, note="footnote marker 2 left as a bare number")
    p.present("footnotes", "These values were not considered in computing the average of paint No. 2.", 7, max_diffs=1, note="Table 2 footnote")
    p.present("footnotes", "Taken from Proc. A. S. T. M., 10, pp. 105-106; 1910.", 7, max_diffs=1, note="page footnote 3, same page as the table footnote")
    p.order("footnotes", "These values were not considered in computing the average of paint No. 2.", "Taken from Proc. A. S. T. M.", 7, max_diffs=1,
            note="table footnote stays with its table, ahead of the page footnote")
    p.present("footnotes", "The divergent opinions of competent observers mentioned above are well illustrated in the following selection of 5 of these 19 paints.", 7, max_diffs=3,
              note="body sentence carrying marker 3, intact")
    p.regex("footnotes", r"June 28, 1911\.\s?5\s+Three of the four", 8, absent=True, note="marker 5 fused into the year (reads 1911.5)")
    p.order("footnotes", "A. S. T. M. Proceedings, 10, p. 73; 1910.", "A. S. T. M. Proceedings, 11, p. 192; 1911.", 8, max_diffs=1,
            note="footnotes 4 and 5 printed side by side on one line")
    p.regex("footnotes", r"No\. 100\s?8\s+wire sieves", 9, absent=True, note="marker 8 fused into 'No. 100' (reads No. 1008)")
    p.present("footnotes", "These panels were exposed exactly 1 month and then discontinued, because under the microscope the coating was cracked all over.", 12, max_diffs=3,
              note="Table 6 footnote")

    # tables: cell relations (brace-grouped row blocks in Tables 2, 3, 5)
    p.table("22.1", 1, up="16.5", down="31.6", note="Table 1")
    p.table("112", 6, up="32", down="165", note="exposure-cycle summary (Hours / Per cent)")
    p.table("6.44", 7, up="10", right="6", top_heading="Aiken", note="Table 2, paint 2 row C")
    p.table("4.66", 7, left="4.33", right="5.3", top_heading="Hume", note="Table 2, paint 2 row C")
    p.table("9.66", 7, left="7.14", right="8.4", left_heading="11", note="Table 2, paint label 11 printed on the B row of its brace")
    p.table("8.55", 7, up="10", right="7", top_heading="Aiken", note="Table 2, paint 13 row C")
    p.table("9.8", 7, up="8.8", down="8.6", top_heading="Average", left_heading="14", note="Table 2, paint 14 row B")
    p.table("8.5", 8, up="10", left="5", right="4", note="Table 3, paint 100 June 28, 1911 row")
    p.table("0", 8, left="1", right="3", top_heading="Gardner", note="Table 3, paint 5555 Apr. 15, 1910 row")
    p.table("35", 10, up="31", down="39", note="Table 4, 30-gallon varnish column")
    p.table("0.07", 10, left="0.06", right="0.08", top_heading="48 days", note="Table 5, white lead first row; two-level header")
    p.table("76", 12, up="122.5", down="119.5", note="Table 6")
    p.table("16", 12, left="Titanium zinc paint, F. S. B. specification No. 278", max_diffs=1, note="Table 6, dot leaders after the label")
    p.table("92", 14, left="100", up="2", down="2", note="Table 7")
    p.table("58", 14, left="100", up="0", down="32", note="Table 7")

    # table titles and figure captions
    for pg, title in [
        (7, "Table 2.—Ratings of 5 out of 19 paints inspected May 5, 1910"),
        (10, "Table 4.—Permeability to water vapor of coatings on wire mesh exposed to weather"),
        (12, "Table 6.—Permeability of various paints after four months in accelerated cycle"),
        (14, "Table 7.—Tests of olive green oleoresinous automobile enamels"),
    ]:
        p.present("figures", title, pg, max_diffs=2, case_sensitive=False, note="small-caps TABLE")
    p.figure("Cabinet for exposing to ozonized air", 3)
    p.figure("Apparatus for determining breakdown of film by passing air through it", 4)
    p.figure("Photograph and wiring diagram of Wilson's apparatus for determining end point of paint failures", 4)
    p.present("figures", "A, Steel wool contact frame. B, Buzzer. C, Switch. D, Head phones. E, Dry cell.", 4, max_diffs=2, note="Fig. 6 legend")
    p.present("figure_text", "Head Phones", 4, note="Fig. 7 wiring diagram label")
    p.present("figure_text", "Test Surface", 4, note="Fig. 7 wiring diagram label")

    # reading order
    p.order("reading_order", "hours (9.30 to 1).", "Water (tap water at about", 5, max_diffs=1,
            note="two-column schedule: a column split puts all labels before all durations")
    p.order("reading_order", "17 hours (4 to 9 Sunday).", "Sunday:", 6, note="schedule rows kept in row order")
    p.order("reading_order", "determining end point of paint failures", "A, Steel wool contact frame.", 4, max_diffs=1, note="legend under the Fig. 6 caption")

    # characters
    p.regex("chars", rf"warm \(100 ?{DEG} ?F\.\) water", 2, note="degree sign (Unicode or markup); the thin space before F is optional")
    p.regex("chars", rf"cooled to \$?\s?[-−]\s?25 ?{DEG} ?C\. \(\s?\$?\s?[-−]\s?13 ?{DEG} ?F\.\)", 2,
            note="minus and degree signs as printed (Unicode or markup)")
    p.regex("chars", rf"{frac_re(1, 2, whole=3)} hours \(9\.30 to 1\)\.", 5)
    p.regex("chars", rf"95 mm \({frac_re(3, 4, whole=3)} inches\)", 9)
    p.regex("chars", rf"radiation in the moderate ultra-violet \(350 to 400 m\s?{MU}\)", 1)
    p.present("chars", "investigations—determining the progressive change in permeability on weathering—the writers", 9, note="em dashes, line-end hyphen in deter-mining")
    p.regex("chars", r"\b1(?:18|22|19)\. 5\b", 12, absent=True, note="Table 6 decimals printed with a thin space after the point")

    # inline sub/superscripts
    p.regex("inline", sup_re("0.075 watt per cm", "2"), 1, note="cm^2")
    p.regex("inline", sup_re("(71.26 cm", "2") + r"\s?area", 9, note="cm^2")
    p.sub("dishes containing dry CaCl", "2", 9)

    # headings
    for h, pg in [
        ("4. TEMPERATURE CHANGES (REFRIGERATION)", 2),
        ("III. METHODS OF DETERMINING EXTENT TO WHICH DISINTEGRATION HAS TAKEN PLACE", 6),
        ("2. PERMEABILITY TO WATER VAPOR", 9),
        ("3. PERMEABILITY TO AIR", 11),
        ("5. USE OF MILLIAMMETER", 14),
    ]:
        p.heading(h, pg)
