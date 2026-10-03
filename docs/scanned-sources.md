# Scanned-document sourcing

Three public-domain **scanned** PDFs (page images, not born-digital), sourced
2026-10-02. Each file here is a contiguous page excerpt cut with
`qpdf --empty --pages <src>.pdf A-B -- <id>.pdf`. qpdf copies the pages
byte-for-byte: the page images and any OCR text layer are left as published.

| id | pages | text layer | main targets |
|----|------:|------------|--------------|
| `naca-rm-e7b11c` | 15 | **none** (CCITT G4 images only) | display and numbered equations, symbol list, table, typewritten |
| `nbs-rp1` | 14 | **OCR** (invisible text, Adobe Paper Capture) | numeric tables with table footnotes, page footnotes, running headers, photo plates |
| `usgs-b580j` | 14 | **OCR** (invisible text, SAFER Create) | dense page footnotes in two-column blocks, alternating verso/recto running headers, tables, foldout map |

---

## 1. `naca-rm-e7b11c`

- **Title:** Cooling of Gas Turbines. III — Analysis of Rotor and Blade Temperatures in Liquid-Cooled Gas Turbines
- **Authors / agency:** W. Byron Brown and John N. B. Livingood, National Advisory Committee for Aeronautics, Aircraft Engine Research Laboratory (Lewis), Cleveland, Ohio. NACA Research Memorandum **RM E7B11c**.
- **Year:** 1947 (dated February 11, 1947)
- **Direct PDF:** https://ntrs.nasa.gov/api/citations/20030064253/downloads/20030064253.pdf
- **Landing page:** https://ntrs.nasa.gov/citations/20030064253 (metadata API: https://ntrs.nasa.gov/api/citations/20030064253)
- **Public-domain evidence:**
  - A US federal government work (NACA staff authors acting in their official capacity), so not subject to copyright under 17 U.S.C. §105.
  - The NTRS record's copyright block reads `"determinationType":"GOV_PUBLIC_USE_PERMITTED"`, with `containsThirdPartyMaterial: false`, `distribution: PUBLIC` and export control `NO`.
  - NASA STI disclaimer (https://sti.nasa.gov/disclaimers/): *"Documents available from this Web site are not protected by copyright unless noted. If not copyrighted, documents may be reproduced and distributed, without further permission from NASA."*
- **Original page count:** 30 (cover, 14 text pages, then 15 figure pages).
- **Excerpt:** PDF pp. 1–15, i.e. the cover plus report pp. 1–14 (all of the text through the references). **15 pages.**
- **Text layer:** **none.** `pdftotext` returns only form feeds (0 non-whitespace characters) and `pdffonts` lists no fonts. Each page is a single 1-bit CCITT G4 image at 300 dpi. Producer: Image Alchemy v1.11.
- **What it exercises:**
  - Typewritten (IBM-typed) technical memo, single column.
  - Many display equations with sub- and superscripts, fractions, exponentials and hyperbolic functions; numbered equations (1), (2), … on report pp. 9–10.
  - A symbol list (report pp. 3–4) laid out as a two-column definition list.
  - A numeric table (report p. 12) that sits directly after a page break (*"…given in the following table:"* ends p. 11).
  - Sentences crossing page breaks (for example *"They were"* at the foot of p. 10).
  - A running header (`NACA RM No. E7B11c`) and page numbers.
  - A cover page with classification stamps (`RESTRICTED`, since cancelled), library stamps and a few handwritten annotations.
- **sha256 (excerpt):** `b81a69db6896e47e37b73ca543badc492a3a3acb3b91bebd776f911ef51d7abd`
- **sha256 (source as downloaded):** `03713997815853275d2ebfc259322a660fae26f0ea9b9107e75e232298f72ebe`

## 2. `nbs-rp1`

- **Title:** Accelerated Tests of Organic Protective Coatings (Research Paper RP1)
- **Authors / agency:** Percy H. Walker and E. F. Hickson, Bureau of Standards (US Department of Commerce). *Bureau of Standards Journal of Research*, vol. 1, no. 1, pp. 1–17.
- **Year:** 1928 (July 1928 issue)
- **Direct PDF:** https://nvlpubs.nist.gov/nistpubs/jres/1/jresv1n1p1_A1b.pdf
- **Landing / DOI:** https://doi.org/10.6028/jres.001.001 (resolves to the PDF above)
- **Public-domain evidence:**
  - A US federal government work by Bureau of Standards staff (17 U.S.C. §105), **and** published in the US in 1928, i.e. before 1930.
  - NIST statement (https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications): *"Works authored by NIST employees are not subject to Copyright protection within the United States; foreign rights are reserved. To the extent NIST may assert rights outside of the United States, the public is granted the non-exclusive, perpetual, paid-up, royalty-free, worldwide right to reprint works in all formats…"*
  - Suggested credit: "Republished courtesy of the National Institute of Standards and Technology."
- **Original page count:** 22 PDF pages: journal pp. 1–17, plus 4 unnumbered photographic plate pages (PDF 3–4 and 7–8) and a blank last page.
- **Excerpt:** PDF pp. 5–18, i.e. journal pp. 3–14 plus the two plate pages between pp. 4 and 5. **14 pages.**
- **Text layer:** **OCR.** It is invisible text (`3 Tr`) under each page image, which is 600 dpi grayscale JPEG; producer is Adobe Acrobat 9.13 Paper Capture. The scan is Internet Archive digitization hosted by NIST. Prose OCR is good; tables are garbled. Sample from excerpt p. 7 (journal p. 7):
  ```
  gallon. Triplicate panels were used for each spreading rate, making
  nin e panels for each paint. The panels were exposed in November,
  ```
  The footnote on that page comes out as `, 'r aken from Proc. A. S. T . M .• 10, pp. lOiH06; 1910.` The table caption comes out as `TABLE    2.- Rati ngs of 5 out of 19 pain ts i ns pected May 5,1910`.
- **What it exercises:**
  - About 8 numeric tables. The best is Table 2 (journal p. 7), a ruled grid of ratings with brace-grouped row blocks (A/B/C per paint) and a superscript table footnote (`¹ These values were not considered in computing the average…`), followed on the same page by a page footnote (`³ Taken from Proc. A.S.T.M.…`).
  - The exposure-cycle schedule table on journal p. 6.
  - Further tables on journal pp. 3, 8, 10, 12 and 14.
  - Alternating running headers (`Bureau of Standards Journal of Research [Vol. 1` / `Walker, Hickson] Tests of Organic Protective Coatings`).
  - Two full-page halftone photo plates with captions (`FIG. 4.—Cabinet for exposing to ozonized air`, and others). They interrupt a sentence that runs from journal p. 4 to p. 5, which is a page-break-across-inserts test.
  - Single column. Note the size: 13.8 MB because of the 600 dpi grayscale JPEGs.
- **sha256 (excerpt):** `ad9f6645373d930ab91399374937fd94d4d2d2b4a56ea5139e9db1068c80ae83`
- **sha256 (source as downloaded):** `6dc5d3cab9f86686c9b82848288f7f3ce665f002f32e1d407201454185b4e982`

## 3. `usgs-b580j`

- **Title:** The Phosphate Deposits of South Carolina
- **Author / agency:** G. S. Rogers, US Geological Survey (Department of the Interior). USGS **Bulletin 580-J**, in *Contributions to Economic Geology, 1913, Part I*, pp. 183–220.
- **Year:** 1915 (chapter published October 10, 1914; bulletin 1915)
- **Direct PDF:** https://pubs.usgs.gov/bul/0580j/report.pdf
- **Landing page:** https://pubs.usgs.gov/publication/b580J (DOI https://doi.org/10.3133/b580J)
- **Public-domain evidence:**
  - A US federal government work by a USGS geologist (17 U.S.C. §105). The Publications Warehouse record has `"noUsgsAuthors": false` and `"Publisher": "U.S. Geological Survey"`.
  - It was **also** published in the US in 1914–1915, before 1930.
  - USGS policy (https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits): *"USGS-authored or produced data and information are considered to be in the U.S. Public Domain."*
- **Original page count:** 39 PDF pages (bulletin pp. 183–220, plus Plate II, a foldout map).
- **Excerpt:** PDF pp. 1–14, i.e. bulletin pp. 183–195 plus Plate II. **14 pages.**
- **Text layer:** **OCR.** It is invisible text (`3 Tr`) under 400 dpi 1-bit CCITT page images; producer is SAFER Create 3.000. OCR is good on body text and noisier on footnote markers (superscript digits misread as `8`, `<`, `i`). Sample from excerpt p. 7 (bulletin p. 188):
  ```
  end of the Ecoene and that deposition may have continued for some
  time. If it did, then all the strata down to the present top of the
  ```
  The footnotes on that page come out as:
  ```
  2 Tuomey, Michael, op. cit., pp. 164-165.
  8 Am. Jour. Sci., 3d ser., vol. 48, pp. 300-301,1898.
  ```
- **What it exercises:**
  - Numbered page-bottom footnotes on nearly every page of the excerpt. Up to about 10 per page (bulletin p. 184), several set in a **two-column footnote block** beneath single-column body text. Many are `op. cit.` / `Idem` back-references.
  - Running headers that alternate between verso (`184 CONTRIBUTIONS TO ECONOMIC GEOLOGY, 1913, PART I.`) and recto (`PHOSPHATE DEPOSITS OF SOUTH CAROLINA. 185`), with the page number on the outer edge.
  - A ruled geologic-formations table (bulletin p. 186) and measured-section lists set as small tables (bulletin pp. 190–191).
  - A wide foldout map plate with caption (Plate II, landscape page, PDF p. 3).
  - Italic run-in headings (*Edisto marl.*—…) and sentences crossing page breaks.
- **sha256 (excerpt):** `3b74a682efc51e3e6a19a81984b15e0d66ae7d2c99ac5ce7de21d81569b5e8db`
- **sha256 (source as downloaded):** `5b7c054b4ae371a94bbab622a1dbb892e53a5821bccd0bca5c08963730350786`

---

## Rejected candidates

1. **NACA Report 496, Theodorsen, *General Theory of Aerodynamic Instability and the Mechanism of Flutter* (1935).**
   - Source: https://ntrs.nasa.gov/citations/19930090935, `GOV_PUBLIC_USE_PERMITTED`.
   - Strengths: typeset two-column, very dense math, page footnotes, running headers. It is the strongest equation document if a typeset one is wanted.
   - Why rejected: the NTRS file is an NTIS re-scan. It has an NTIS front page ("reproduced from the best copy… certain portions are illegible") and smudged regions, and it ships a very poor OCR layer. The image-only RM was chosen so that one of the three documents has no text layer.
   - It remains a good fourth candidate (26 pp.; PDF pp. 5–16 would be a clean excerpt).
2. **NACA TM-1433, Mushtari & Sachenkov, *Stability of Cylindrical and Conical Shells…* (1958).**
   - Source: NTRS 20030064289.
   - Why rejected: it is image-only like the RM, but it is a NACA translation of a Soviet Academy of Sciences paper. The underlying foreign work may have restored US copyright (URAA), so it is not unambiguously public domain.
3. **NACA TN 10 Part II, Prandtl, *Theory of Lifting Surfaces* (1920).**
   - Source: NTRS 20030082190.
   - Why rejected: it is pre-1930 and image-only, but it is typewritten with hand-inserted Greek and math symbols, so part of every equation is handwritten. It is also a translation and abstract of a German original, and only 10 pages long.
4. ***Olmstead v. United States*, 277 U.S. 438 (1928), Library of Congress U.S. Reports scan.**
   - Source: https://tile.loc.gov/storage-services/service/ll/usrep/usrep277/usrep277438/usrep277438.pdf
   - Strengths: an ideal footnote and running-header document (the Brandeis dissent).
   - Why rejected: the opinion text is public domain, but LOC's collection page says the scans were made under an agreement with William S. Hein & Co. and are *"provided for personal, educational, and research use. Hein has not made its materials available for commercial purposes"*. That is a terms-of-use restriction we should not carry into a commercial benchmark report.
5. **Old GAO reports (gao.gov/assets/…).** Scripted downloads return HTTP 403 (bot protection), so the source bytes cannot be pinned reproducibly.
6. **USGS Bulletin 720 (Summerfield and Woodsfield quadrangles, Ohio, 1922).** Clean scan with OCR, but it has very few footnotes (about one every 10–20 pages).
7. **BLS bulletins / Monthly Labor Review on FRASER.** The content is public domain, but FRASER's terms prohibit commercial use of the service without the Federal Reserve Bank of St. Louis's consent.

---

## YAML for `sources.yaml`

This block follows the existing field names (`license`, `license_url`, `license_evidence`, `landing_url`, `authors`, `layout`, `features`, `notes`) and adds `group`, `excerpt_of` and `text_layer`. Paste it under `documents:`.

```yaml
  - id: naca-rm-e7b11c
    path: scanned/naca-rm-e7b11c.pdf
    group: scanned
    title: "Cooling of Gas Turbines. III - Analysis of Rotor and Blade Temperatures in Liquid-Cooled Gas Turbines"
    authors: W. Byron Brown, John N. B. Livingood (NACA Aircraft Engine Research Laboratory)
    venue: NACA Research Memorandum RM E7B11c, 1947
    origin_url: https://ntrs.nasa.gov/api/citations/20030064253/downloads/20030064253.pdf
    landing_url: https://ntrs.nasa.gov/citations/20030064253
    license: "Public domain (US government work, 17 U.S.C. §105)"
    license_url: https://www.law.cornell.edu/uscode/text/17/105
    license_evidence: "NTRS record copyright.determinationType = GOV_PUBLIC_USE_PERMITTED, containsThirdPartyMaterial = false (https://ntrs.nasa.gov/api/citations/20030064253, checked 2026-10-02); NASA STI disclaimer https://sti.nasa.gov/disclaimers/: 'Documents available from this Web site are not protected by copyright unless noted.'"
    excerpt_ok: true
    pages: 15
    excerpt_of: "pp. 1-15 of 30 (cover + report pp. 1-14)"
    text_layer: none
    layout: single-column
    features:
    - typewritten
    - display-equations
    - numbered-equations
    - symbol-list
    - tables
    - running-header
    - page-break-table
    - cover-page
    - stamps
    notes: "Image-only scan (1-bit CCITT, 300 dpi, Image Alchemy); pdftotext returns nothing. Numbered equations (1), (2), ... on report pp. 9-10; table on report p. 12 directly after a page break; cover carries RESTRICTED stamps (since cancelled) and handwritten annotations"
    sha256: b81a69db6896e47e37b73ca543badc492a3a3acb3b91bebd776f911ef51d7abd
  - id: nbs-rp1
    path: scanned/nbs-rp1.pdf
    group: scanned
    title: "Accelerated Tests of Organic Protective Coatings"
    authors: Percy H. Walker, E. F. Hickson (Bureau of Standards)
    venue: Bureau of Standards Journal of Research 1(1), 1-17 (1928), RP1
    origin_url: https://nvlpubs.nist.gov/nistpubs/jres/1/jresv1n1p1_A1b.pdf
    landing_url: https://doi.org/10.6028/jres.001.001
    license: "Public domain (US government work, 17 U.S.C. §105; published in the US 1928)"
    license_url: https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications
    license_evidence: "NIST: 'Works authored by NIST employees are not subject to Copyright protection within the United States'; Bureau of Standards staff authors; US publication 1928 (pre-1930)"
    excerpt_ok: true
    pages: 14
    excerpt_of: "pp. 5-18 of 22 (journal pp. 3-14 incl. 2 photo plates)"
    text_layer: ocr
    layout: single-column
    features:
    - tables
    - table-footnotes
    - grouped-table-rows
    - footnotes
    - running-header
    - figures
    - photo-plates
    notes: "Internet Archive scan hosted by NIST, 600 dpi grayscale JPEG with invisible Paper Capture OCR (good on prose, garbled in tables). Table 2 (journal p. 7) has brace-grouped rows, a table footnote and a page footnote on the same page; two full-page photo plates interrupt a sentence crossing journal pp. 4-5; ~13.8 MB"
    sha256: ad9f6645373d930ab91399374937fd94d4d2d2b4a56ea5139e9db1068c80ae83
  - id: usgs-b580j
    path: scanned/usgs-b580j.pdf
    group: scanned
    title: "The Phosphate Deposits of South Carolina"
    authors: G. S. Rogers (US Geological Survey)
    venue: USGS Bulletin 580-J (Contributions to Economic Geology, 1913, Part I), pp. 183-220, 1915
    origin_url: https://pubs.usgs.gov/bul/0580j/report.pdf
    landing_url: https://pubs.usgs.gov/publication/b580J
    license: "Public domain (US government work, 17 U.S.C. §105; published in the US 1915)"
    license_url: https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits
    license_evidence: "USGS: 'USGS-authored or produced data and information are considered to be in the U.S. Public Domain.'; Publications Warehouse record b580J: publisher U.S. Geological Survey, noUsgsAuthors=false, year 1915 (pre-1930)"
    excerpt_ok: true
    pages: 14
    excerpt_of: "pp. 1-14 of 39 (bulletin pp. 183-195 + Plate II)"
    text_layer: ocr
    layout: single-column
    features:
    - footnotes
    - two-column-footnotes
    - running-header
    - alternating-running-header
    - tables
    - figures
    - foldout-plate
    notes: "400 dpi 1-bit CCITT scan with invisible SAFER OCR (good body text, noisy footnote markers). Numbered page-bottom footnotes on nearly every page (up to ~10 on bulletin p. 184), many op. cit./Idem; verso/recto running headers with outer page numbers; landscape foldout map plate at PDF p. 3"
    sha256: 3b74a682efc51e3e6a19a81984b15e0d66ae7d2c99ac5ce7de21d81569b5e8db
```
