"""Nat. Commun. 11, 329 (2020) — 7 pages, two-column, figures only on p5, no tables/equations."""


from study.author import DEG


def probes(p):
    # furniture
    p.absent("furniture", "NATURE COMMUNICATIONS | (2020)11:329 | https://doi.org/10.1038/s41467-019-14078-1 | www.nature.com/naturecommunications", 1, max_diffs=8, note="running footer")
    p.absent("furniture", "NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-019-14078-1", 2, max_diffs=3, note="running header")
    p.absent("furniture", "1234567890():,;", 1, note="vertical glyph strip on p1")

    # stitching across page breaks
    p.present("stitching", "and the field distributions of the resonant modes in the microcavities", 3, max_diffs=2, note="p3->p4, figure on top of p4")
    p.present("stitching", "The surplus ratio after the CESF process is close to this noise limit.", 4, note="p4->p6 across figure-only p5")
    p.order("stitching", "has never been reported", "Here, we develop a novel microstructure", 2)
    p.order("stitching", "with high-quality-factor terahertz cavity photons", "Self-organization of CdSe", 6, max_diffs=2, note="reference list p6->p7")

    # reading order (columns, text around figures)
    p.present("reading_order", "Perovskites are an excellent optical candidate for achieving large oscillator strength", 2, note="drop cap P rejoined")
    p.present("reading_order", "these samples remain stable in the ambient atmospheric environment for several months", 3, note="left->right column")
    p.present("reading_order", "were mixed in a 50 ml four-neck flask and dried under", 6, max_diffs=2, note="Methods: left column -> right column")
    p.order("reading_order", "an ultrafast control of many-body quantum ensemble in a perovskite core", "Here, we develop a novel microstructure", 2)
    p.order("reading_order", "Preparation of Cs-oleate", "Synthesis of CsPbBr", 6)
    p.order("reading_order", "Synthesis of CsPbBr", "Characterization techniques", 6)
    p.order("reading_order", "photoelectric-compatible quantum processors", "are an excellent optical candidate for achieving", 1)
    p.order("reading_order", "Results", "Optical properties of QDSM", 3)
    p.order("reading_order", "Dynamics of SF and CESF", "Cooperative ensemble breaks population-inversion limitation", 4)
    p.order("reading_order", "In summary, we propose the ultrafast control", "Data availability", 6)

    # footnotes (affiliations block on p1)
    p.present("footnotes", "Key Laboratory of Materials for High-Power Laser, Shanghai Institute of Optics and Fine Mechanics, Chinese Academy of Sciences", 1)
    p.present("footnotes", "These authors contributed equally: Chun Zhou, Yichi Zhong", 1)
    p.order("footnotes", "photoelectric-compatible quantum processors", "Key Laboratory for Micro-Nano Physics and Technology of Hunan Province", 1, note="affiliations after the abstract, not inside it")

    # inline: sub/superscripts and citation markers
    p.sub("CaTiO", "3", 1)
    p.sub("CsPbBr", "3", 3)
    p.sup("~10", "2", 4, note="N_eff ~ 10^2, plain '~102' changes the value")
    p.sup("μJ cm", "-2", 5, note="Fig. 4 caption, cm^-2")
    p.regex("inline", r"absorption\s?1\s?-\s?4\b", 2, absent=True, note="citation 1-4 fused to a word")
    p.regex("inline", r"superlattice\s?10,\s?11\b", 2, absent=True, note="citation 10,11 fused")
    p.regex("inline", r"cooperation\s?6\s?-\s?9\b", 2, absent=True, note="citation 6-9 fused")
    p.regex("inline", r"carriers\s?30\s?\(", 6, absent=True, note="citation 30 fused before (<1 ps)")
    p.regex("inline", r"N\s?(?:_\{?ph\}?|<sub>ph</sub>|ph)\s?/\s?N\s?(?:_\{?dp\}?|<sub>dp</sub>|dp) ratio", 4, note="N_ph/N_dp ratio")

    # characters
    p.present("chars", "highly efficient light absorption", 2, note="fi ligature")
    p.present("chars", "Rainò, G. et al.", 6)
    p.present("chars", "Bose-Einstein condensation in a gas of sodium atoms", 6)
    p.regex("chars", rf"\(10\s?{DEG}\s?C?\)", 6, note="degree sign (Unicode or markup)")
    p.regex("chars", r"NA\s?=\s?0\.42,\s?×\s?50", 6, note="multiplication sign")

    # headings
    p.heading("Cooperative excitonic quantum ensemble in perovskite-assembly superlattice microcavities", 1)
    for h, pg in [("Results", 3), ("Discussion", 6), ("Methods", 6), ("Data availability", 6), ("References", 6),
                  ("Acknowledgements", 7), ("Author contributions", 7), ("Competing interests", 7), ("Additional information", 7)]:
        p.heading(h, pg)
    for h, pg in [("Structural characterizations", 3), ("Optical properties of QDSM", 3), ("Dynamics of SF and CESF", 4),
                  ("Cooperative ensemble breaks population-inversion limitation", 4), ("Preparation of Cs-oleate", 6),
                  ("Characterization techniques", 6), ("PL spectra and dynamical measurements", 6)]:
        p.heading(h, pg, note="run-in subsection head")

    # figures
    p.figure("Fig. 1 Linking “self-assembly of QDs” to “phase transitions of exciton ensemble”", 2)
    p.figure("Fig. 2 Dynamic tracing and optical characterization of perovskite QDSMs.", 3)
    p.figure("Fig. 3 Dynamics of SF and CESF under different pumping densities.", 4)
    p.figure("Fig. 4 Surplus dipoles after the CESF process vs. the case of a classical laser.", 5)
    p.figure("Fig. 5 Terahertz conversion based on a CsPbBr", 5)
    p.present("figures", "The whiskers around the cubic QD are oleylamine and oleic acid ligands. b Phase transitions of exciton ensemble", 2, max_diffs=2, note="caption contiguous")
    p.present("figures", "Multimode lasing can be obtained and the spacing between two adjacent modes decreases with the increasing of cavity size.", 3, note="caption tail")

    # text inside figures (reported separately)
    for t, pg in [("Superlattice microcavity", 2), ("Cavity-enhanced cooperative excitons", 2), ("Pumping density", 3),
                  ("Fast-radiation dipoles", 5), ("Two identified status in", 5)]:
        p.present("figure_text", t, pg)
