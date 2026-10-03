"""Classify a PDF as born-digital, scanned with a hidden OCR layer, or scanned without text.

    digital   real text layer (text drawn visibly, no page-sized image under it)
    scan_ocr  page-sized image with text that is invisible or sits under the image
    scan      no usable text layer

Measured from the file, not from a category name: olmOCR's ``old_scans_math`` mixes
the last two, and a few pages in other categories are scans.
"""

import pypdfium2 as pdfium
import pypdfium2.raw as pdfium_c

MIN_CHARS = 200  # per document: less than this is "no text layer"
COVER = 0.85  # an image covering this share of the page is a scanned page


def _page(page: pdfium.PdfPage) -> tuple[int, bool, int, int]:
    """(non-space chars, page-sized image, visible text objects, invisible text objects)."""
    w, h = page.get_size()
    tp = page.get_textpage()
    chars = sum(not c.isspace() for c in tp.get_text_range())
    cover = vis = invis = 0
    for obj in page.get_objects():
        if obj.type == pdfium_c.FPDF_PAGEOBJ_IMAGE:
            left, bottom, right, top = obj.get_bounds()
            cover = max(cover, (right - left) * (top - bottom) / (w * h))
        elif obj.type == pdfium_c.FPDF_PAGEOBJ_TEXT:
            if pdfium_c.FPDFTextObj_GetTextRenderMode(obj.raw) == pdfium_c.FPDF_TEXTRENDERMODE_INVISIBLE:
                invis += 1
            else:
                vis += 1
    return chars, cover >= COVER, vis, invis


def classify(path) -> str:
    pdf = pdfium.PdfDocument(path)
    chars = scanned = vis = invis = 0
    for page in pdf:
        c, full_image, v, i = _page(page)
        chars += c
        scanned += full_image
        vis += v
        invis += i
    if chars < MIN_CHARS:
        return "scan"
    if invis > vis or scanned * 2 > len(pdf):
        return "scan_ocr"
    return "digital"
