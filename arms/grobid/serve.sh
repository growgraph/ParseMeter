#!/usr/bin/env bash
# Start the GROBID server for the grobid arm and wait until it answers /api/isalive.
#   arms/grobid/serve.sh          start (no-op if already up)
#   docker stop grobid-bench      stop
set -euo pipefail
IMAGE="${GROBID_IMAGE:-grobid/grobid:0.9.1-full}"
NAME=grobid-bench
if ! curl -sf http://localhost:8070/api/isalive >/dev/null 2>&1; then
  docker run -d --rm --init --ulimit core=0 --name "$NAME" -p 8070:8070 "$IMAGE" >/dev/null
fi
for _ in $(seq 1 300); do
  if [ "$(curl -sf http://localhost:8070/api/isalive 2>/dev/null)" = "true" ]; then
    echo "grobid up: $IMAGE ($(curl -s http://localhost:8070/api/version))"
    exit 0
  fi
  sleep 2
done
echo "grobid did not come up within 600 s" >&2
docker logs --tail 50 "$NAME" >&2 || true
exit 1
