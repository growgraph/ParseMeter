"""Shared locations; everything is relative to the repository root."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUT = ROOT / "out"
PROBES = ROOT / "probes"
ARMS = ROOT / "arms"
SOURCES = ROOT / "sources.yaml"
