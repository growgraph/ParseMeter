#!/usr/bin/env bash
# Fetch the llama.cpp CPU build used by the marker and paddle arms (llama-server, b11324, ubuntu x64).
set -euo pipefail
cd "$(dirname "$0")"
URL=https://github.com/ggml-org/llama.cpp/releases/download/b11324/llama-b11324-bin-ubuntu-x64.tar.gz
for arm in marker paddle; do
  mkdir -p "$arm/bin"
  [ -x "$arm/bin/llama-b11324/llama-server" ] || curl -sL "$URL" | tar xz -C "$arm/bin"
done
