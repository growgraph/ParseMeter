"""arXiv 2609.39072 (CC BY 4.0) — 15 pages, ACL two-column, 11 results tables incl. two-level headers."""


def probes(p):
    p.absent("furniture", "arXiv:2609.39072v1", 1, max_diffs=1, note="arXiv stamp")

    # tables
    p.table("60.299", 6, left_heading="Zero-shot", top_heading="LLaMA-3.3-70B", note="Table 1, fully ruled grid")
    p.table("73.196", 6, left_heading="LoRA", top_heading="LLaMA-2-7B")
    p.table("0.4778", 6, left="0.4406", right="0.4653", top_heading="3.1-8B", note="Table 2, two-level header")
    p.table("0.6311", 6, left_heading="Valence", top_heading="Few-shot")
    p.table("0.2990", 6, left_heading="Dominance", left="0.1235", right="0.3046")
    p.table("0.736", 7, left="0.603", right="0.604", note="Table 3")
    p.table("84", 7, left_heading="FT LLaMA-3.1-8B", left="66", right="74", note="Table 4, small font")
    p.table("38", 7, left_heading="LLaMA-3.1-8B FS", top_heading="Angry")

    # table notes
    p.present("footnotes", "The proposed here is LLaMA-3.3-70B with LoRA fine-tuning", 7, note="note line under Table 3")
    p.present("footnotes", "ZS: zero-shot; FS: few-shot; FT: fine-tuned.", 7, note="note under Table 4")
    p.order("footnotes", "Table 3: Comparison with Prior Work on VAD Evaluation on IEMOCAP", "Annotator Reliability", 7)

    # captions: Table 1 caption sits below its table, Table 2 caption above
    p.present("figures", "Table 1: Discrete ER Performance of All Models (Weighted F1 score)", 6)
    p.present("figures", "Table 2: VAD Evaluation Performance Comparison Across Different Models", 6)
    p.order("reading_order", "Table 2: VAD Evaluation Performance Comparison Across Different Models", "Error Analysis for Discrete ER", 6)

    # reading order around full-width tables
    p.present("reading_order", "which assigns a single categorical label(e.g. happiness, frustration, etc.) to an utterance", 1, max_diffs=2)
    p.present("reading_order", "the confusion rates of 46.5-75.3 for GPT models on misinterpreting anger as frustration", 6)
    p.present("reading_order", "while GPT-4o-mini, in contrast, is more conservative about the positive levels", 6)
    p.order("reading_order", "Annotator Reliability", "Ablation Studies", 7)
    p.order("reading_order", "The Impact of Acoustic Feature Descriptions", "The Impact of Past VAD Context", 7)

    # stitching
    p.present("stitching", "rhythm, and speaking rate all carry affective signals that text transcriptions discard", 1)
    p.present("stitching", "best represents the dominant emotion of the target utterance", 13, note="prompt text crossing p13->p14")

    # characters / inline
    p.regex("chars", r"Krippendorff['’]s\s?\$?\s?(?:α|\\alpha)", 6)
    p.regex("chars", r"Happy\s?(?:→|\\rightarrow|\$\\rightarrow\$)\s?Excite", 6)
    p.regex("chars", r"(?:α|\\alpha)\s?\$?\s?=\s?\$?\s?0\.680", 6)

    # headings
    for h, pg in [("Beyond Text: LLM-Based Dimensional Emotion Evaluation in Multimodal Dialogue", 1), ("Abstract", 1), ("Introduction", 1),
                  ("Error Analysis for Discrete ER", 6), ("VAD Evaluation Performance Analysis", 6), ("Annotator Reliability", 7),
                  ("Ablation Studies", 7), ("The Impact of Past VAD Context", 7), ("GPT Models with Prompting", 7), ("Conclusion", 9)]:
        p.heading(h, pg)
