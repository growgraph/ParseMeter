"""Run one converter arm over the document list. Stdlib only: it runs inside each arm's venv.

    uv run --project arms/<arm> python arms/_driver.py <arm> [--variant V] [--set docs|olmocr|all]
                                                           [--only id1,id2] [--budget-h 8] [--force]

The arm directory holds ``run.py`` exposing ``make(variant: str) -> convert`` where
``convert(pdf: Path, assets: Path) -> str`` returns markdown, and ``PACKAGES``: the
distributions whose versions are recorded. Outputs, resumable:

    out/<arm>[-<variant>]/docs/<id>.md
    out/<arm>[-<variant>]/olmocr/<category>/<stem>.md
    out/<arm>[-<variant>]/timing.jsonl     one row per conversion
    out/<arm>[-<variant>]/env.json         versions, variant, host
"""

import argparse
import importlib.metadata
import importlib.util
import json
import os
import platform
import resource
import sys
import time
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_arm(arm: str):
    spec = importlib.util.spec_from_file_location(f"arm_{arm.replace('-', '_')}", ROOT / "arms" / arm / "run.py")
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(ROOT / "arms" / arm))
    spec.loader.exec_module(mod)
    return mod


def _versions(packages: list[str]) -> dict[str, str]:
    out = {}
    for p in packages:
        try:
            out[p] = importlib.metadata.version(p)
        except importlib.metadata.PackageNotFoundError:
            out[p] = "?"
    return out


def _rss_mb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("arm")
    ap.add_argument("--variant", default="")
    ap.add_argument("--set", default="all", choices=["docs", "olmocr", "all"])
    ap.add_argument("--only", default="")
    ap.add_argument("--budget-h", type=float, default=8.0)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--core", action="store_true", help="only documents marked core (heavy arms)")
    args = ap.parse_args()

    mod = _load_arm(args.arm)
    name = args.arm + (f"-{args.variant}" if args.variant else "")
    out = ROOT / "out" / name
    out.mkdir(parents=True, exist_ok=True)
    docs = json.loads((ROOT / "out" / "doclist.json").read_text())
    if args.set != "all":
        docs = [d for d in docs if d["set"] == args.set]
    if args.core:
        docs = [d for d in docs if d.get("core")]
    if args.only:
        keep = set(args.only.split(","))
        docs = [d for d in docs if d["id"] in keep]

    t0 = time.perf_counter()
    convert = mod.make(args.variant)
    load_s = time.perf_counter() - t0
    env = {
        "arm": args.arm,
        "variant": args.variant,
        "packages": _versions(getattr(mod, "PACKAGES", [])),
        "extra": getattr(mod, "EXTRA", {}),
        "python": platform.python_version(),
        "cpu_count": os.cpu_count(),
        "setup_seconds": round(load_s, 2),
    }
    (out / "env.json").write_text(json.dumps(env, indent=2))

    started = time.perf_counter()
    with open(out / "timing.jsonl", "a") as log:
        for d in docs:
            md_path = out / ("docs" if d["set"] == "docs" else "olmocr") / f"{d['id']}.md"
            if md_path.exists() and not args.force:
                continue
            if time.perf_counter() - started > args.budget_h * 3600:
                log.write(json.dumps({"id": d["id"], "set": d["set"], "status": "budget"}) + "\n")
                log.flush()
                continue
            md_path.parent.mkdir(parents=True, exist_ok=True)
            assets = out / "assets" / d["id"]
            row = {"id": d["id"], "set": d["set"], "pages": d["pages"]}
            t = time.perf_counter()
            try:
                md = convert(ROOT / d["path"], assets)
                md_path.write_text(md)
                row["status"] = "ok"
            except Exception as e:  # noqa: BLE001 - a failure is a result
                row["status"] = "error"
                row["error"] = f"{type(e).__name__}: {e}"[:500]
                (out / "errors").mkdir(exist_ok=True)
                (out / "errors" / f"{d['id'].replace('/', '__')}.txt").write_text(traceback.format_exc())
            row["seconds"] = round(time.perf_counter() - t, 3)
            row["max_rss_mb"] = round(_rss_mb(), 1)
            log.write(json.dumps(row) + "\n")
            log.flush()
            print(f"[{name}] {d['id']} {row['status']} {row['seconds']}s", flush=True)


if __name__ == "__main__":
    main()
