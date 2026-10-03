#!/usr/bin/env bash
# The measurement as published: every arm configuration, one after another (each gets the whole
# machine). Text-layer and layout-model arms run on all documents; slow arms on the core set
# (our documents minus the two 10-Ks, plus 10 olmOCR-Bench pages per category).
# Resumable: the driver skips documents whose markdown already exists in out/.
#   ./run_benchmark.sh [fast|slow|all]          (default: all)
# Keep the machine awake and detach for long runs, e.g.
#   setsid nohup systemd-inhibit --what=sleep:idle ./run_benchmark.sh all > out/run.log 2>&1 < /dev/null & disown
cd "$(dirname "$0")"
stage=${1:-all}
if [[ $stage == fast || $stage == all ]]; then
  ./run_queue.sh pdftotext docling:default docling:textlayer docling:noocr docling:fast docling:layoutonly \
    docling:native docling:lean pymupdf4llm:default pymupdf4llm:layout \
    kreuzberg:default marker:nocr mineru:basic unstructured:hires
  bash arms/grobid/serve.sh && SET=docs ./run_queue.sh grobid:default; docker stop grobid-bench
fi
if [[ $stage == slow || $stage == all ]]; then
  CORE=1 ./run_queue.sh docling:fullocr docling:formula docling:tuned marker:fast mineru:standard
  CORE=1 BUDGET_H=10 ./run_queue.sh paddle:vl paddle:structurev3
fi
# Built but not part of the published run (CPU cost; cite published numbers instead):
#   CORE=1 BUDGET_H=10 ./run_queue.sh docling:granite docling:glmocr docling:lightonocr marker:balanced
