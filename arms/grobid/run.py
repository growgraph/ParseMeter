"""GROBID full-text TEI rendered to markdown by a small fixed converter.

The server must already be running (``arms/grobid/serve.sh``); ``GROBID_URL`` overrides
http://localhost:8070. Consolidation is off (no Crossref/biblio-glutton calls), raw
reference strings are requested so the bibliography renders as printed.

TEI -> markdown: title ``#``; author names on one line; abstract paragraphs; body ``div``
heads ``##`` (with GROBID's section number when present); paragraphs; formulas as text
(GROBID emits no LaTeX) with their label; figures and tables as ``head label figDesc``
paragraphs (table cells as a pipe table); back-matter divs (acknowledgements, annexes,
availability) as ``##`` sections; references as a list of raw strings; footnotes at the end.
"""

import os
import re
from pathlib import Path

import requests
from lxml import etree

PACKAGES = ["requests", "lxml"]
URL = os.environ.get("GROBID_URL", "http://localhost:8070")
NS = {"t": "http://www.tei-c.org/ns/1.0"}
T = "{http://www.tei-c.org/ns/1.0}"


def _server_version() -> str:
    try:
        return requests.get(f"{URL}/api/version", timeout=5).text.strip()
    except requests.RequestException:
        return "?"


EXTRA = {
    "grobid_version": _server_version(),
    "image": os.environ.get("GROBID_IMAGE", "grobid/grobid:0.9.1-full"),
    "license": "Apache-2.0 (code and models)",
    "params": "consolidateHeader=0 consolidateCitations=0 consolidateFunders=0 includeRawCitations=1",
}


def _text(el) -> str:
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip() if el is not None else ""


def _cell(el) -> str:
    return _text(el).replace("|", "\\|")


def _figure(fig) -> list[str]:
    head = _text(fig.find(f"{T}head"))
    label = _text(fig.find(f"{T}label"))
    desc = _text(fig.find(f"{T}figDesc"))
    cap = " ".join(x for x in (head, label if label and label not in head else "", desc) if x)
    out = [cap] if cap else []
    table = fig.find(f"{T}table")
    if table is not None:
        rows = [[_cell(c) for c in r.findall(f"{T}cell")] for r in table.findall(f"{T}row")]
        rows = [r for r in rows if r]
        if rows:
            width = max(len(r) for r in rows)
            rows = [r + [""] * (width - len(r)) for r in rows]
            lines = ["| " + " | ".join(rows[0]) + " |", "|" + " --- |" * width]
            lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
            out.append("\n".join(lines))
    for note in fig.findall(f"{T}note"):
        if _text(note):
            out.append(_text(note))
    return out


def _formula(f) -> str:
    label = _text(f.find(f"{T}label"))
    body = re.sub(r"\s+", " ", "".join(f.text or "") + "".join(
        "".join(c.itertext()) + (c.tail or "") for c in f if c.tag != f"{T}label"
    )).strip()
    return f"{body} {label}".strip()


def _block(el, level: int) -> list[str]:
    tag = etree.QName(el).localname
    if tag == "head":
        n = el.get("n")
        h = _text(el)
        return [f"{'#' * level} {n + ' ' if n and not h.startswith(n) else ''}{h}"] if h else []
    if tag == "p":
        return [_text(el)] if _text(el) else []
    if tag == "formula":
        return [_formula(el)]
    if tag == "figure":
        return _figure(el)
    if tag == "list":
        return ["\n".join(f"- {_text(i)}" for i in el.findall(f"{T}item"))]
    if tag == "div":
        out = []
        for c in el:
            out += _block(c, level)
        return out
    if tag == "note":
        return [_text(el)] if _text(el) else []
    return [_text(el)] if _text(el) else []


def tei_to_markdown(tei: bytes) -> str:
    root = etree.fromstring(tei)
    out: list[str] = []
    title = root.find(".//t:teiHeader/t:fileDesc/t:titleStmt/t:title", NS)
    if _text(title):
        out.append(f"# {_text(title)}")
    authors = []
    for pers in root.findall(".//t:teiHeader/t:fileDesc/t:sourceDesc//t:analytic/t:author/t:persName", NS):
        name = " ".join(_text(x) for x in pers if etree.QName(x).localname in ("forename", "surname"))
        if name:
            authors.append(name)
    if authors:
        out.append(", ".join(authors))
    for el in root.findall(".//t:teiHeader/t:profileDesc/t:abstract//t:p", NS):
        if _text(el):
            out.append(_text(el))

    body = root.find(".//t:text/t:body", NS)
    footnotes: list[str] = []
    if body is not None:
        for el in body:
            if el.tag == f"{T}note":
                footnotes.append(_text(el))
                continue
            out += _block(el, 2)

    back = root.find(".//t:text/t:back", NS)
    if back is not None:
        refs: list[str] = []
        for el in back:
            if el.tag != f"{T}div":
                continue
            if el.get("type") == "references":
                for b in el.iter(f"{T}biblStruct"):
                    raw = b.find(".//t:note[@type='raw_reference']", NS)
                    refs.append(_text(raw) if raw is not None else _text(b))
            else:
                out += _block(el, 2)
        if refs:
            out.append("## References")
            out.append("\n".join(f"- {r}" for r in refs if r))
        for note in back.iter(f"{T}note"):
            if note.get("place") == "foot":
                footnotes.append(_text(note))
    footnotes = [f for f in footnotes if f]
    if footnotes:
        out.append("\n".join(f"- {f}" for f in footnotes))
    return "\n\n".join(x for x in out if x) + "\n"


def make(variant: str):
    if variant != "default":
        raise ValueError(f"unknown variant {variant!r}")
    if requests.get(f"{URL}/api/isalive", timeout=5).text.strip() != "true":
        raise RuntimeError(f"GROBID not alive at {URL}; run arms/grobid/serve.sh")
    session = requests.Session()

    def convert(pdf: Path, assets: Path) -> str:
        with open(pdf, "rb") as fh:
            r = session.post(
                f"{URL}/api/processFulltextDocument",
                files={"input": (pdf.name, fh, "application/pdf")},
                data={
                    "consolidateHeader": "0",
                    "consolidateCitations": "0",
                    "consolidateFunders": "0",
                    "includeRawCitations": "1",
                    "segmentSentences": "0",
                },
                timeout=1800,
            )
        r.raise_for_status()
        assets.mkdir(parents=True, exist_ok=True)
        (assets / "grobid.tei.xml").write_bytes(r.content)
        return tei_to_markdown(r.content)

    return convert
