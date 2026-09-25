# -*- coding: utf-8 -*-
"""Build a reading copy of the game's book - EPUB, and PDF where a converter exists.

THE FAULT THIS EXISTS FOR. Every game is a book kept as numbered Markdown in
`book/`, and until now there was no way to read one away from a screen with a
checkout on it. The author's tablet syncs
`RPG_NEW/08_PERSONAL_PROJECTS/_Reading copies/<Title>/` to its card; the folder
was made weeks ago with a README that says "drop the current PDF export of each
game here", and every game's folder is still empty, because nothing exported
anything. The author asked (2026-09-26) that each game build its own, since each
game knows its own chapter order and front matter and Core does not.

WHAT IT DOES. Concatenates `book/*.md` in filename order, puts Pandoc-standard
front matter on top (from `tools/meta.py` if the game has `project.yaml`, else
the directory name), and runs Pandoc to EPUB. If Calibre's `ebook-convert` is
on the machine it makes a PDF from that EPUB as well - Pandoc's own PDF writer
needs a LaTeX install, which no machine here has.

SCHEMA-BLIND, like every Core tool: it reads no content file and knows no
game's vocabulary. On Core, which has no `book/`, it says so and passes - it
cannot build, and it will not pretend to.

Usage:  python tools/reading_copy.py               build into the tablet folder if present, else build/
        python tools/reading_copy.py --out DIR     build somewhere else
        python tools/reading_copy.py --root DIR    build another checkout (Core can build any game on this machine)
        python tools/reading_copy.py --epub-only   skip the PDF
        python tools/reading_copy.py --self-test   build a synthetic book; used by CI
"""
import argparse
import datetime
import glob
import io
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The author's tablet reading-copies folder. Absent on CI and on any other
# machine, and that is not an error: the build falls back to build/.
CARD = r"H:\RPG_NEW\08_PERSONAL_PROJECTS\_Reading copies"
PANDOC_CANDIDATES = ["pandoc", r"C:\Users\Dan\AppData\Local\Pandoc\pandoc.exe",
                     r"C:\Program Files\Pandoc\pandoc.exe", "/usr/bin/pandoc"]
CALIBRE_CANDIDATES = ["ebook-convert", r"C:\Program Files\Calibre2\ebook-convert.exe",
                      "/usr/bin/ebook-convert"]


def which(candidates):
    for c in candidates:
        p = shutil.which(c) if os.sep not in c else (c if os.path.exists(c) else None)
        if p:
            return p
    return None


def metadata(root):
    """Title/author/version for the front matter. project.yaml when the game has one."""
    try:
        sys.path.insert(0, os.path.join(root, "tools"))
        import meta                                            # noqa: E402  (Core's shared builder)
        meta.ROOT = root
        p = meta.project()
        return {"title": p["title"], "subtitle": p.get("subtitle", ""),
                "author": p["author"]["name"] if isinstance(p.get("author"), dict) else p.get("author", ""),
                "version": str(p.get("version", "")), "lang": p.get("language", "en-GB")}
    except Exception:
        return {"title": os.path.basename(root), "subtitle": "", "author": "", "version": "", "lang": "en-GB"}


def build(root, out_dir=None, epub_only=False, quiet=False):
    """Returns the list of files written. Empty list when there is no book to build."""
    chapters = sorted(glob.glob(os.path.join(root, "book", "*.md")))
    if not chapters:
        if not quiet:
            print("no book/*.md here - nothing to build (this is normal in Core)")
        return []
    pandoc = which(PANDOC_CANDIDATES)
    if not pandoc:
        print("FAIL: pandoc not found. winget install JohnMacFarlane.Pandoc")
        sys.exit(1)
    m = metadata(root)
    stamp = datetime.date.today().isoformat()
    if out_dir is None:
        out_dir = os.path.join(CARD, m["title"]) if os.path.isdir(CARD) else os.path.join(root, "build")
    os.makedirs(out_dir, exist_ok=True)

    body = []
    for c in chapters:
        body.append(io.open(c, encoding="utf-8").read().rstrip() + "\n")
    fm = ["---", 'title: "%s"' % m["title"].replace('"', "'")]
    if m["subtitle"]:
        fm.append('subtitle: "%s"' % m["subtitle"].replace('"', "'"))
    if m["author"]:
        fm.append('author: "%s"' % m["author"].replace('"', "'"))
    fm += ['date: "%s"' % stamp, 'lang: %s' % m["lang"]]
    if m["version"]:
        fm.append('version: "%s"' % m["version"])
    fm.append("---\n")
    combined = "\n".join(fm) + "\n" + "\n".join(body)

    tmp = os.path.join(tempfile.gettempdir(), "reading_copy_%d.md" % os.getpid())
    io.open(tmp, "w", encoding="utf-8").write(combined)
    stem = "%s%s (%s)" % (m["title"], (" v" + m["version"]) if m["version"] else "", stamp)
    stem = "".join(ch for ch in stem if ch not in '\\/:*?"<>|')
    epub = os.path.join(out_dir, stem + ".epub")
    written = []
    try:
        subprocess.run([pandoc, tmp, "-o", epub, "--toc", "--toc-depth=2", "--standalone",
                        "--metadata", "title=" + m["title"]], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        written.append(epub)
        if not epub_only:
            calibre = which(CALIBRE_CANDIDATES)
            if calibre:
                pdf = os.path.join(out_dir, stem + ".pdf")
                subprocess.run([calibre, epub, pdf, "--paper-size", "a4", "--pdf-page-margin-top", "36",
                                "--pdf-page-margin-bottom", "36"], check=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                written.append(pdf)
            elif not quiet:
                print("note: Calibre's ebook-convert not found - EPUB only")
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass
    # One current copy per game: older exports of the same book are removed, so the
    # tablet never shows three versions of the same rules and no one has to guess.
    for old in glob.glob(os.path.join(out_dir, "*.epub")) + glob.glob(os.path.join(out_dir, "*.pdf")):
        if old not in written and os.path.basename(old).startswith(m["title"]):
            os.remove(old)
            if not quiet:
                print("  removed superseded %s" % os.path.basename(old))
    if not quiet:
        for w in written:
            print("  %s  (%.1f MB)" % (w, os.path.getsize(w) / 1e6))
    return written


def self_test():
    """A synthetic two-chapter book builds. Proven to fail if Pandoc is missing."""
    d = tempfile.mkdtemp(prefix="reading_copy_selftest_")
    os.makedirs(os.path.join(d, "book"))
    io.open(os.path.join(d, "book", "01-one.md"), "w", encoding="utf-8").write("# One\n\nFirst chapter.\n")
    io.open(os.path.join(d, "book", "02-two.md"), "w", encoding="utf-8").write("# Two\n\nSecond chapter.\n")
    out = os.path.join(d, "out")
    got = build(d, out_dir=out, epub_only=True, quiet=True)
    ok = len(got) == 1 and os.path.getsize(got[0]) > 1000
    text = subprocess.run([which(PANDOC_CANDIDATES), got[0], "-t", "plain"],
                          stdout=subprocess.PIPE).stdout.decode("utf-8", "replace") if ok else ""
    ordered = text.find("First chapter") < text.find("Second chapter") if "First chapter" in text else False
    shutil.rmtree(d, ignore_errors=True)
    print("self-test: %s" % ("PASS" if (ok and ordered) else "FAIL"))
    return 0 if (ok and ordered) else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out")
    ap.add_argument("--root", default=ROOT, help="the checkout to build; defaults to this repo")
    ap.add_argument("--epub-only", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    build(a.root, out_dir=a.out, epub_only=a.epub_only)
