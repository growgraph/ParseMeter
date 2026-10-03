"""Authoring aid: show the text either side of every page break whose last line looks unfinished.

    PYTHONPATH=. uv run python -m study.breaks <pdf> '<furniture regex>'
"""

import re
import subprocess
import sys


def page_lines(pdf: str, page: int, furniture: re.Pattern) -> list[str]:
    out = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), pdf, "-"], capture_output=True, text=True).stdout
    return [ln.strip() for ln in out.splitlines() if ln.strip() and not furniture.search(ln) and not re.fullmatch(r"\s*\d+\s*", ln)]


def main() -> None:
    pdf, fur = sys.argv[1], re.compile(sys.argv[2])
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    prev = page_lines(pdf, 1, fur)
    for i in range(2, n + 1):
        cur = page_lines(pdf, i, fur)
        if prev and cur and not re.search(r"[.:;!?”\"]\s*$", prev[-1]) and cur[0][:1].islower():
            print(f"p{i - 1}->{i}: ...{' '.join(prev[-1].split()[-9:])} || {' '.join(cur[0].split()[:9])}...")
        prev = cur


if __name__ == "__main__":
    main()
