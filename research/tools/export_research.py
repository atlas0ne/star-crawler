# -*- coding: utf-8 -*-
"""Export research/RESEARCH.md as EPUB and PDF for the author's tablet.

WHY THIS EXISTS SEPARATELY FROM tools/reading_copy.py. Core's reading_copy builds
the *book* - it concatenates `book/*.md`. Star Crawler has no book yet and will
not for a while; what there is to read is the research. This reuses Core's
converter detection and its output folder convention (`_Reading copies/<Title>/`,
one current export per title, superseded ones deleted) and changes only the
input. Reported to Core as mail; if Core generalises reading_copy to take a
source document, this file goes away.

Usage:  python research/tools/export_research.py             EPUB + PDF
        python research/tools/export_research.py --epub-only
        python research/tools/export_research.py --out DIR
"""
import argparse, datetime, glob, io, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import reading_copy as RC           # Core's: which(), PANDOC/CALIBRE candidates, CARD

TITLE = "Star Crawler Research"
SRC = os.path.join(ROOT, "research", "RESEARCH.md")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out")
    ap.add_argument("--epub-only", action="store_true")
    a = ap.parse_args()

    # always rebuild the markdown first: an export of a stale document is worse
    # than no export, because it looks current on the tablet
    sys.path.insert(0, os.path.join(ROOT, "research", "tools"))
    import build_research
    io.open(SRC, "w", encoding="utf-8", newline="\n").write(build_research.build())

    pandoc = RC.which(RC.PANDOC_CANDIDATES)
    if not pandoc:
        sys.exit("pandoc not found; see tools/reading_copy.py for where it looks")

    out_dir = a.out or (os.path.join(RC.CARD, "Star Crawler")
                        if os.path.isdir(RC.CARD) else os.path.join(ROOT, "build"))
    os.makedirs(out_dir, exist_ok=True)
    import yaml
    ver = yaml.safe_load(io.open(os.path.join(ROOT, "project.yaml"), encoding="utf-8"))["version"]
    stem = "%s v%s (%s)" % (TITLE, ver, datetime.date.today().isoformat())
    epub = os.path.join(out_dir, stem + ".epub")

    cmd = [pandoc, SRC, "-o", epub, "--toc", "--toc-depth=2",
           "--metadata", "title=" + TITLE, "--standalone"]
    subprocess.run(cmd, check=True, cwd=os.path.join(ROOT, "research"))
    made = [epub]

    if not a.epub_only:
        calibre = RC.which(RC.CALIBRE_CANDIDATES)
        if calibre:
            pdf = os.path.join(out_dir, stem + ".pdf")
            subprocess.run([calibre, epub, pdf, "--paper-size", "a4",
                            "--pdf-page-margin-left", "48", "--pdf-page-margin-right", "48",
                            "--base-font-size", "11"],
                           check=True, capture_output=True)
            made.append(pdf)
        else:
            print("note: Calibre's ebook-convert not found - EPUB only")

    # one current export per title, as Core's tool does
    for old in glob.glob(os.path.join(out_dir, "*.epub")) + glob.glob(os.path.join(out_dir, "*.pdf")):
        if old not in made and TITLE in os.path.basename(old):
            os.remove(old)
            print("removed superseded %s" % os.path.basename(old))
    for f in made:
        print("wrote %s (%.1f MB)" % (f, os.path.getsize(f) / 1048576.0))


if __name__ == "__main__":
    main()
