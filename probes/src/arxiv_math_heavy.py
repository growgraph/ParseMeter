"""arXiv 2609.28992 (CC BY 4.0) — 19 pages, single-column hep-th, ~68 numbered equations, page footnotes."""


def probes(p):
    p.absent("furniture", "arXiv:2609.28992v1 [hep-th] 24 Sep 2026", 1, max_diffs=3, note="vertical arXiv stamp")

    # stitching
    p.present("stitching", "the promotion of global symmetries to local gauge symmetries introduces profound conceptual", 1, note="footnote sits between the halves")
    p.present("stitching", "To define the path integral and eliminate the redundancies associated with gauge invariance", 7)
    p.present("stitching", "describing the gauge symmetry on a curved internal field space", 14)

    # footnotes: present, and not spliced into the sentence that wraps past them
    p.present("footnotes", "To review the some results of this section, we have based this part of the text on the reference", 3)
    p.present("footnotes", "An involutive distribution is a set of tangent directions closed under Lie brackets", 4)
    p.present("footnotes", "Corresponding author. email:ancastillo42@uan.edu.co", 1, max_diffs=2)
    p.present("footnotes", "the Killing vectors define an involutive distribution", 4, note="marker kept or dropped, sentence intact")
    p.order("footnotes", "whose integral manifolds are the local group orbits by the Frobenius theorem", "An involutive distribution is a set of tangent directions", 4, max_diffs=1)

    # display equations
    for pg, tex, n in [
        (3, r"\mathcal{L}_{\mathrm{NL}\sigma\mathrm{M}}=\frac{1}{2}g_{ab}(\pi)\partial_{\mu}\pi^{a}\partial^{\mu}\pi^{b}", 1),
        (3, r"g_{ab}(\pi)=\delta_{ab}+\frac{\pi_{a}\pi_{b}}{v^{2}-|\pi|^{2}}", 2),
        (3, r"g_{ab}=\delta_{ab}+\frac{\pi_{a}\pi_{b}}{v^{2}-|\pi|^{2}}=\delta_{ab}+\frac{\pi_{a}\pi_{b}}{v^{2}}\left(1+\frac{|\pi|^{2}}{v^{2}}+\frac{|\pi|^{4}}{v^{4}}+\cdots\right)", 3),
        (3, r"\mathcal{L}_{\zeta_{i}}g_{ab}=0", 4),
        (3, r"\delta_{\epsilon}\pi^{a}=\epsilon^{i}\zeta_{i}^{a}(\pi)", 5),
        (4, r"[\zeta_{i},\zeta_{j}]^{a}=\zeta_{i}^{b}\partial_{b}\zeta_{j}^{a}-\zeta_{j}^{b}\partial_{b}\zeta_{i}^{a}=f_{ij}{}^{k}\zeta_{k}^{a}", 6),
        (4, r"D_{\mu}\pi^{a}=\partial_{\mu}\pi^{a}-gA_{\mu}^{I}\zeta_{I}^{a}(\pi)", 7),
        (4, r"\mathcal{L}_{\pi}=\frac{1}{2}g_{ab}(\pi)D_{\mu}\pi^{a}D^{\mu}\pi^{b}", 8),
        (4, r"F_{\mu\nu}^{I}=\partial_{\mu}A_{\nu}^{I}-\partial_{\nu}A_{\mu}^{I}+gf_{JK}{}^{I}A_{\mu}^{J}A_{\nu}^{K}", 10),
        (4, r"\mathcal{L}_{\mathrm{YM}}=-\frac{1}{4}F_{\mu\nu}^{I}F_{I}^{\mu\nu}", 11),
        (4, r"\mathcal{L}_{GB}=\frac{1}{2}g_{ab}(\pi)D_{\mu}\pi^{a}D^{\mu}\pi^{b}-\frac{1}{4}F_{\mu\nu}^{I}F_{I}^{\mu\nu}", 12),
    ]:
        p.math(tex, pg, note=f"eq {n}")
    p.regex("math", r"Q\s?(?:\^\s*\{?2\}?|<sup>2</sup>|²)\s?\$?\s?=\s?\$?\s?0", 2, note="inline Q^2 = 0")

    # characters
    p.present("chars", "Departamento de Física, Universidad Nacional de Colombia, Bogotá D.C.", 1)
    p.present("chars", "Frobeniüs theorem", 4, max_diffs=1)

    # headings
    for h, pg in [("Geometrical BRST Quantization of Gauged Nonlinear Sigma Models: Killing Fields and Physical Cohomology", 1),
                  ("Abstract", 1), ("Introduction", 1), ("Extended Dynamics of GBs", 3),
                  ("Geometrical formalism of the GBs dynamics in the internal field space", 3)]:
        p.heading(h, pg)
