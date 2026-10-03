#!/usr/bin/env bash
# Run arms one after another (each gets the whole machine): ./run_queue.sh arm[:variant] ...
# Env: CORE=1 (core subset), SET=docs|olmocr, ONLY=id1,id2, BUDGET_H=<hours per arm>
set -u
cd "$(dirname "$0")"
unset VIRTUAL_ENV
export OMP_NUM_THREADS=${OMP_NUM_THREADS:-12} TOKENIZERS_PARALLELISM=false
for spec in "$@"; do
  arm=${spec%%:*}; variant=""; [[ $spec == *:* ]] && variant=${spec#*:}
  name=$arm${variant:+-$variant}
  mkdir -p out/$name
  echo "=== $(date -Is) $name"
  /usr/bin/time -v -o out/$name/time.txt \
    uv run --project arms/$arm python arms/_driver.py $arm ${variant:+--variant $variant} ${BUDGET_H:+--budget-h $BUDGET_H} ${CORE:+--core} ${SET:+--set $SET} ${ONLY:+--only $ONLY} \
    >> out/$name/run.log 2>&1
  echo "=== $(date -Is) $name exit=$?"
done
