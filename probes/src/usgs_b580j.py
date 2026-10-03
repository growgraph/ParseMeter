"""USGS Bulletin 580-J (1915, public domain) — 14-page scan with a hidden OCR layer: bulletin pp. 183-195
plus a foldout map plate (PDF p3). Numbered page-bottom footnotes on nearly every page (ten on p184,
two-column blocks on pp188-191), alternating verso/recto running headers with outer page numbers,
a ruled formations table (p186) and measured-section tables (pp190-191).

Ground truth read from the page images. Structure probes carry ~1 diff per 40 chars for OCR noise."""

from study.author import frac_re

# verso header "184 CONTRIBUTIONS TO ECONOMIC GEOLOGY, 1913, PART I." (number before it)
VERSO = r"(?i)economic\s+geology,?\s+1913,?\s+pa\S{2}\s+\S{1,2}\s*(?:\d{3}\s*)?"
# recto header "PHOSPHATE DEPOSITS OF SOUTH CAROLINA. 185" (number after it)
RECTO = r"(?i)deposits\s+of\s+south\s+carolina\.?\s*(?:\d{3}\s*)?"
# an optional footnote marker in any form (bare, ^n, <sup>n</sup>, ¹), then a space
MARK = r"(?:\s?\S{0,14})?\s"


def md(n: int) -> int:
    """~1 diff per 40 characters, min 1."""
    return max(1, n // 40)


def probes(p):
    # ---- furniture: running header glued in front of the continuation of a body sentence
    for pg, head in [
        (2, "published the most complete"),
        (5, "or less extended descriptions"),
        (7, "end of the Ec"),
        (11, "lacking in the area between"),
        (13, "places this material contains"),
    ]:
        p.regex("furniture", VERSO + head, pg, absent=True, note="verso running header + page number inside a split sentence")
    for pg, head in [(4, "In previous years a large amount"), (6, "hard when dry"), (12, "concentrated on the river bottom")]:
        p.regex("furniture", RECTO + head, pg, absent=True, note="recto running header + page number inside a split sentence")
    p.regex("furniture", r"(?i)#+\s*phosphate\s+deposits\s+of\s+south\s+carolina", 10, absent=True,
            note="recto running header promoted to a heading (the title heading starts with THE)")
    p.regex("furniture", r"(?i)#+\s*(?:\d{3}\s*)?contributions\s+to\s+economic\s+geology", 9, absent=True,
            note="verso running header promoted to a heading")
    p.regex("furniture", r"53317", 1, absent=True, note="printer's signature line '53317°—Bull. 580—15——13' at the foot of p183")

    # ---- stitching: sentences continuing across a page break (footnote block + header between halves)
    p.regex("stitching", r"Shepard, jr\.," + MARK + r"published the most complete and valuable", 2,
            note="p183->184; marker 4 sits at the break, footnotes 1-4 and the verso header between the halves")
    for pg, text in [
        (4, "the former being the center of the phosphate and fertilizer industry. In previous years a large amount of phosphate rock was shipped from these points"),
        (5, "all give more or less extended descriptions of the geology"),
        (6, "but lighter colored and fairly hard when dry. It commonly contains about 75 per cent lime carbonate"),
        (7, "there may have been no marked break at the end of the Ecoene and that deposition may have continued for some time."),
        (8, "found in irregular deposits in the beds of many of the rivers. This river rock generally consists of rounded pebbles"),
        (9, "the Pleistocene generally rests directly on the Edisto within the phosphate-bearing area and constitutes the overburden which must be removed in mining."),
        (11, "This formation thus appears to be entirely lacking in the area between Ashepoo and Combahee rivers and in several smaller districts."),
        (12, "in part of fragments derived from the land deposits and concentrated on the river bottom, the whole deposit having been more or less worked over by river action."),
        (13, "Its color appears to depend largely on that of the rock with which it is associated. In places this material contains quartz pebbles"),
    ]:
        note = None
        if pg == 4:
            note = ("p184 -> p185 across the foldout map plate (PDF p3) and footnotes 1-10; a paragraph, not a sentence, continues "
                    "(p185 opens flush left, no indent) — every arm leaves footnotes between the two sentences")
        elif pg == 7:
            note = "'Ecoene' is the printed typo; a corrected 'Eocene' costs 2 diffs, inside the tolerance"
        elif pg == 8:
            note = ("p188 -> p189: a paragraph, not a sentence, continues (p189 opens flush left, no indent); "
                    "every arm leaves the two-column footnote block between the two sentences")
        p.present("stitching", text, pg, max_diffs=md(len(text)), note=note)

    # ---- footnotes: texts present
    for pg, text in [
        (1, "On the phosphate beds of South Carolina: Boston Soc. Nat. Hist. Proc., vol. 13, pp. 222-235, 1870: U. S. Coast Survey Rept., pp. 182-189, 1870."),
        (2, "Nature and origin of deposits of phosphate of lime: U. S. Geol. Survey Bull. 46, pp. 60-70, 1888."),
        (2, "Description of vertebrate remains, chiefly from the phosphate beds of South Carolina: Jour. Acad. Nat. Sci. Philadelphia"),
        (4, "A good account of the configuration of the coast, the submarine topography, etc., is given by N. S. Shaler in U. S. Coast Survey Rept., 1870, pp. 182-185."),
        (5, "For discussion by Vaughan see Willis, Bailey, Index to the stratigraphy of North America: U. S. Geol. Survey Prof. Paper 71, pp. 806-813, 1912."),
        (6, "Shepard, C. U., jr., Rural Carolinian, August, 1873. See also Chazal, P. E., loc. cit., and Waggaman, W. H., loc. cit."),
        (9, "Sloan, Earle, op. cit., pp. 480-484."),
        (14, "Waggaman, W. H., Report on the phosphate fields of South Carolina: U. S. Dept. Agr. Bull. 18, p. 6, 1913."),
    ]:
        p.present("footnotes", text, pg, max_diffs=md(len(text)))

    # footnote markers left as a bare number fused into the body sentence
    for pg, pat, n in [
        (2, r"Penrose, jr\.,\s?\d{1,2}\s+wrote", 1),
        (2, r"Dall\s?\d{1,2}\s+in 1894", 10),
        (4, r"Ruffin,\s?\d\s+Tuomey,", 2),
        (7, r"Vaughan\s?\d\s+to be middle Miocene", 1),
        (12, r"Edisto marl,\s?\d\s+and there seems little doubt", 2),
        (14, r"Waggaman\s?\d\s+states that isolated", 1),
    ]:
        p.regex("footnotes", pat, pg, absent=True, note=f"footnote marker {n} left as a bare number in the sentence")

    # two-column footnote block (p188): left column 1-3, right column 4-5 — column order, not row order
    p.order("footnotes", "Tuomey, Michael, op. cit., pp. 164-165.", "Sloan, Earle, op. cit., p. 470.", 7, max_diffs=1,
            note="two-column footnote block read row-wise interleaves 1,4,2,5,3")
    p.order("footnotes", "Am. Jour. Sci., 3d ser., vol. 48, pp. 300-301, 1898.", "Idem, p. 299.", 7, max_diffs=1)

    # ---- reading order
    p.order("reading_order", "following classification has been adopted by the United States Geological Survey",
            "Geologic formations related to the phosphate deposits of the Charleston region", 5, max_diffs=2, note="table title follows the lead-in")
    p.order("reading_order", "Sand, gravel, loam, etc.", "is the lowest formation here considered", 5, max_diffs=1, note="table before the next section")
    p.order("reading_order", "Sea Island loams. Fine, glauconitic sand and silt", "Wadmalaw marl. Greenish-gray sandy marl", 9, max_diffs=1,
            note="numbered list printed 5..1, top to bottom")

    # ---- tables
    p.table("100+", 5, left="Cooper marl.", note="p186 ruled formations table")
    p.table("Eocene.", 5, right="Cooper marl.")
    p.table("Pliocene.", 5, top_heading="Series.")
    p.table("Cooper marl.", 5, top_heading="Formation.")
    p.table("5", 9, up="4", down="3", note="Section at Bolton mine (dotted leaders)")
    p.table("6", 10, up="1", down="1", note="Section near Lambs; no arm emits the p191 sections as tables (mineru: leader lines)")
    p.table("6", 10, right="0", down="1", note="Section at Simmons Bluff, Ft./in. columns; no arm emits a table here")

    # ---- headings
    for h, pg in [
        ("THE PHOSPHATE DEPOSITS OF SOUTH CAROLINA.", 1),
        ("INTRODUCTION.", 1),
        ("GEOGRAPHY AND TOPOGRAPHY.", 2),
        ("SEQUENCE OF THE STRATA.", 4),
        ("OLIGOCENE SERIES.", 6),
        ("GEOLOGIC HISTORY.", 10),
        ("CHEMICAL COMPOSITION.", 14),
    ]:
        p.heading(h, pg)

    # ---- figures
    p.figure("MAP SHOWING APPROXIMATE ORIGINAL DISTRIBUTION OF SOUTH CAROLINA PHOSPHATE DEPOSITS.", 3, note="Plate II, landscape foldout")
    p.present("figures", "Geologic formations related to the phosphate deposits of the Charleston region, S. C.", 5, max_diffs=2, note="table title")
    p.present("figure_text", "Density of pattern indicates value of deposit", 3, max_diffs=1, note="map legend")
    p.present("figure_text", "Deposits mostly exhausted", 3, note="map legend")

    # ---- characters
    p.regex("chars", r"exceeding\s?" + frac_re(1, 2, whole=2) + r"\s?\$?\s?feet", 7, note="mixed fraction 2½ (glyph, n/d or \\frac)")
    p.present("chars", "sharks' teeth and vertebræ", 7, note="æ ligature as printed; the OCR layer and every arm transliterate to 'vertebrae'")
    p.present("chars", "Charleston & Western Carolina Railway", 4)
    p.present("chars", "Cooper marl.—The Cooper marl is the lowest formation", 5, note="em dash after the italic run-in heading")
    p.present("chars", "middle Miocene—about equivalent", 7)
    p.present("chars", "Sand, white, brownish at top (Wando (?) of Sloan)", 10)
