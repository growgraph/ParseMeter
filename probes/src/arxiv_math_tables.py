"""arXiv 2608.15882 (CC BY 4.0) — 13 pages, REVTeX two-column, 5 tables, 8 numbered equations."""

from study.author import sub_re


def probes(p):
    # furniture: the arXiv side stamp; page numbers are bare digits (not testable as absent)
    p.absent("furniture", "arXiv:2608.15882v1 [cond-mat.mtrl-sci] 16 Aug 2026", 1, max_diffs=3, note="vertical arXiv stamp")

    # stitching across page breaks
    p.present("stitching", "Zhang et al. theoretically predicted the orthorhombic", 1, max_diffs=1)
    p.present("stitching", "quasiparticle corrections within the G", 2, note="p2->p3 starts mid-sentence; checks no furniture in between")
    p.regex("stitching", r"approach were per-?\s?formed\. A Γ-centered", 2, note="hyphenated word across the page break")
    p.present("stitching", "thereby confirming the excellent mechanical stability of these orthorhombic chalcogenide perovskites", 4)
    p.present("stitching", "which is valid in the low carrier-density regime", 9)

    # reading order / footnote splice: the author-email footnotes sit at the bottom of column 1
    p.present("footnotes", "Owing to their high structural stability, suitable band gaps, and excellent optoelectronic properties", 1, note="body sentence wraps around the p1 footnotes")
    p.present("footnotes", "sa731@snu.edu.in", 1)
    p.order("reading_order", "opening new pathways for next-generation optoelectronic materials", "Recently, chalcogenide perovskites have emerged", 1)
    p.order("reading_order", "INTRODUCTION", "COMPUTATIONAL DETAILS", 1)
    p.order("reading_order", "Polaronic Properties", "Feynman introduced a powerful variational approach", 9)

    # tables (neighbours, not row labels: the row labels carry subscripts)
    p.table("6.39 (6.27)", 4, right="7.02 (6.97)", note="Table I, PBEsol value in bold parentheses")
    p.table("-28.9 (-6.8)", 4, left="10.00 (9.79)")
    p.table("3745", 8, left="0.323", right="0.69", note="Table III")
    p.table("-19.41", 9, left="0.324", right="5.99", note="Table IV")
    p.table("10.72", 11, left="5.32", right="7.04", note="Table V, e/h sub-columns")
    p.table("39.94", 11, left="2.94", note="Table V last column")
    p.table("2.62e [18]", 7, max_diffs=2, note="Table II, superscript e + citation in a cell")

    # display equations
    p.math(r"\alpha=\frac{1}{4\pi\varepsilon_{0}}\frac{1}{2}\left(\frac{1}{\varepsilon_{\infty}}-\frac{1}{\varepsilon_{s}}\right)\frac{e^{2}}{\hbar\omega_{LO}}\left(\frac{2m^{*}\omega_{LO}}{\hbar}\right)^{1/2}", 10, note="eq 5")
    p.math(r"E_{p}=(-\alpha-0.0123\alpha^{2})\hbar\omega_{LO}", 10, note="eq 6")
    p.math(r"m_{p}=m^{*}\left(1+\frac{\alpha}{6}+\frac{\alpha^{2}}{40}+...\right)", 10, note="eq 7")
    p.math(r"\mu_{p}=\frac{(3\sqrt{\pi}e)}{2\pi c\omega_{LO}m^{*}\alpha}\frac{\sinh(\beta/2)}{\beta^{5/2}}\frac{w^{3}}{v^{3}}\frac{1}{K(a,b)}", 10, note="eq 8")
    p.math(r"r_{exc}=\frac{m_{0}}{\mu_{dir}^{*}}\varepsilon_{\mathrm{eff}}n^{2}r_{Ry}", 9, note="eq 3")
    p.math(r"|\phi_{n}(0)|^{2}=\frac{1}{\pi(r_{exc})^{3}n^{3}}", 9, note="eq 4")

    # inline
    p.regex("inline", sub_re("ABX", "3") + r"\s?\(A = Y, La", 1)
    p.regex("inline", r"G\s?(?:0|_\{?0\}?|<sub>0</sub>|₀)\s?\$?\s?W\s?(?:0|_\{?0\}?|<sub>0</sub>|₀)", 1, note="G0W0 with subscripts")
    p.regex("inline", r"cm\s?(?:\^\s*\{?2\}?|<sup>2</sup>|²)\s?\$?\s?V\s?(?:\^\s*\{?\s*-\s?1\}?|<sup>\s*-\s?1</sup>|⁻¹)", 1, note="mobility units with exponents")
    p.regex("inline", r"10\s?(?:\^\s*\{?\s*-\s?6|<sup>\s*-\s?6|⁻⁶)\s?\}?\s?(?:</sup>)?\$?\s?eV", 2, note="10^-6 eV")

    # characters
    p.present("chars", "Fröhlich model", 1)
    p.regex("chars", r"Γ-centered 7\s?×\s?7\s?×\s?5", 2)
    p.regex("chars", r"0\.01 eV/Å", 2)

    # headings
    for h, pg in [("Rare-earth chalcogenide perovskites: A promising class of materials for optoelectronic applications", 1), ("INTRODUCTION", 1),
                  ("COMPUTATIONAL DETAILS", 2), ("RESULTS AND DISCUSSIONS", 3), ("Polaronic Properties", 9), ("CONCLUSION", 11),
                  ("ACKNOWLEDGMENTS", 11), ("DATA AVAILABILITY", 11)]:
        p.heading(h, pg)

    # figures
    p.figure("FIG. 1. Crystal structures of rare-earth chalcogenide perovskites", 3)
    p.figure("FIG. 2. Phonon dispersion curves of the rare-earth chalcogenide perovskites", 5)
    p.figure("FIG. 3. Electronic band structures of the rare-earth chalcogenide perovskites", 6)
    p.figure("FIG. 4. Spatially averaged real", 7)
