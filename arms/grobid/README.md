# grobid arm

- Version: GROBID 0.9.1, docker image `grobid/grobid:0.9.1-full` (22.3 GB unpacked, ~14.8 GB compressed pull). Client deps: requests 2.32.5, lxml 6.0.2 (Python 3.12).
- Install: `docker pull grobid/grobid:0.9.1-full`; `uv sync` in this dir.
- Server: `arms/grobid/serve.sh` (runs `docker run -d --rm --init --ulimit core=0 --name grobid-bench -p 8070:8070 grobid/grobid:0.9.1-full`, waits for `/api/isalive`; ~50 s to come up). Stop with `docker stop grobid-bench`. `GROBID_IMAGE` overrides the image (e.g. `grobid/grobid:0.9.1-crf`, 0.5 GB, CRF-only models); `GROBID_URL` overrides the endpoint for `run.py`.
- Models: baked into the image (CRF + DeLFT deep-learning models); nothing in `~/.cache`.
- License: Apache-2.0 (code and models).
- Request: `POST /api/processFulltextDocument` with `consolidateHeader=0 consolidateCitations=0 consolidateFunders=0 includeRawCitations=1` (no external Crossref/glutton calls). The raw TEI is kept as `assets/<id>/grobid.tei.xml`.
- TEI → markdown (in `run.py`, fixed, no tuning): title `#`; author names; abstract paragraphs; body/back `div` heads `##` (prefixed with GROBID's section number when it gives one); paragraphs; formulas as plain text + label (GROBID emits no LaTeX); figures/tables as `head [label] figDesc` paragraphs, table cells as a pipe table; references as raw strings under `## References`; footnotes as a list at the end. Figures appear where GROBID places them in TEI (end of body), not inline.
- CPU: the full image runs its DL models on CPU (container used ~4.3 GB RAM). Requests are serialized by the arm (one PDF at a time).
- Smoke (natcomm-2020, 7 pages, machine shared with another arm, first request after start): 47.4 s (6.8 s/page).
- Output notes: clean title, authors, abstract and section structure; running headers/footers removed (one footer line surfaces as a "footnote"); drop-cap first letter becomes a section head (`## P` then `erovskites…`); figure captions sometimes duplicated/mislabelled (`Fig. 2 Fig. 2 …`, `Fig. 4 Fig. 5 45 …`); no equations in this paper; references clean, one per line.
