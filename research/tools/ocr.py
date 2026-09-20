# -*- coding: utf-8 -*-
"""OCR image-only PDFs into text sidecars the extractors can read.

The source PDFs are never modified. Output goes to research/corpora/_ocr/<slug>/
as one file per page (p0001.txt ...) so a run can be interrupted and resumed,
plus <slug>.txt with all pages joined by form-feeds once the run is complete.

Tesseract 5 (winget UB-Mannheim.TesseractOCR), page rendered at 300 dpi with
PyMuPDF, --psm 1 (automatic page segmentation with orientation) which handles
the two-column rulebook layouts.

Usage:  python research/tools/ocr.py <slug> [<slug> ...]      slugs from BOOKS
        python research/tools/ocr.py --all
"""
import io, os, sys, time
import pymupdf
import pytesseract
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
OUT = os.path.join(os.path.dirname(__file__), "..", "corpora", "_ocr")

BOOKS = {
    "uaa": paths.D20_UAA,
    "rcr": paths.D20_RCR,
    "ffg_eote": paths.FFG_EDGE,
    "ffg_fad": paths.FFG_FORCE_DESTINY,
    # WEG scans without a text layer
    "gg4_alien_races": paths.WEG_GG + "/WEG40094.pdf",
    "gg8_scouts": paths.WEG_GG + "/WEG40061.pdf",
    "gg6_tramp_freighters": paths.WEG_GG + "/WEG40095.pdf",
    "alien_encounters": paths.WEG_SUPP + "/WEG40166.pdf",
    # Saga Edition scans
    "saga_core": paths.SAGA_CORE,
    "saga_starships": paths.SAGA_STARSHIPS,
    "saga_jedi_academy": paths.SAGA_JEDI_ACADEMY,
}


def ocr_book(slug, pdf):
    d = os.path.join(OUT, slug)
    os.makedirs(d, exist_ok=True)
    doc = pymupdf.open(pdf)
    n = len(doc)
    t0 = time.time()
    done = 0
    for i in range(n):
        p = os.path.join(d, "p%04d.txt" % (i + 1))
        if os.path.exists(p):
            continue
        pix = None
        for dpi in (300, 200, 120):                   # a huge scanned page trips
            try:                                      # MuPDF's pixmap limit
                pix = doc[i].get_pixmap(dpi=dpi); break
            except Exception as e:
                print("  %s p%d: %s at %d dpi, retrying lower" % (slug, i + 1, type(e).__name__, dpi), flush=True)
        if pix is None:
            io.open(p, "w", encoding="utf-8").write(""); continue
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        txt = pytesseract.image_to_string(img, config="--psm 1")
        with io.open(p + ".tmp", "w", encoding="utf-8", newline="\n") as f:
            f.write(txt)
        os.replace(p + ".tmp", p)
        done += 1
        if done % 25 == 0:
            rate = (time.time() - t0) / done
            print("  %s %d/%d  %.1fs/page  ~%d min left" % (slug, i + 1, n, rate, rate * (n - i - 1) / 60), flush=True)
    pages = []
    for i in range(n):
        pages.append(io.open(os.path.join(d, "p%04d.txt" % (i + 1)), encoding="utf-8").read())
    with io.open(os.path.join(OUT, slug + ".txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\f".join(pages))
    print("%s: %d pages -> %s.txt (%d new this run, %.0f min)" % (slug, n, slug, done, (time.time() - t0) / 60), flush=True)


if __name__ == "__main__":
    slugs = list(BOOKS) if "--all" in sys.argv else [a for a in sys.argv[1:] if a in BOOKS]
    if not slugs:
        sys.exit("give slugs from: " + ", ".join(BOOKS))
    for s in slugs:
        ocr_book(s, BOOKS[s])
