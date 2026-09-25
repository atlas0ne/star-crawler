# -*- coding: utf-8 -*-
"""Build RESEARCH.md - the five comparison files as one document to read.

Generated. Never edit RESEARCH.md; edit the files in research/ and rebuild.

The reading order is the order the design questions block in: races, droids, the
Force, classes, generators - then the sources and the corpus inventory as
appendices. Each source file's own front matter and its "Still to do" section are
dropped from the reading copy (they are working notes, not reading), and its
headings are demoted one level so the whole thing has one H1.

Usage:  python research/tools/build_research.py
        python research/tools/build_research.py --check   exit 1 if out of date
"""
import io, os, re, sys, glob, datetime, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(ROOT)
RESEARCH = os.path.join(ROOT, "research")
OUT = os.path.join(RESEARCH, "RESEARCH.md")

# (file, part title) in reading order
PARTS = [
    ("Options.md", "The options — read this part"),
    ("Race_Models_Compared.md", "Races"),
    ("Droid_Models_Compared.md", "Droids"),
    ("Force_Models_Compared.md", "The Force"),
    ("Class_Models_Compared.md", "Classes"),
    ("Generators_Compared.md", "Generators: planets, ships, droids"),
    ("SOURCES.md", "Appendix A: the sources"),
    ("README.md", "Appendix B: the research programme"),
]
FM = re.compile(r"\A---\n.*?\n---\n", re.S)
STILL = re.compile(r"\n## (?:Still to do|Still to do in this file)\b.*?(?=\n## |\Z)", re.S)


def load(name):
    raw = io.open(os.path.join(RESEARCH, name), encoding="utf-8").read()
    raw = FM.sub("", raw)
    raw = STILL.sub("\n", raw)
    raw = raw.strip()
    raw = re.sub(r"^# .*\n", "", raw, count=1)          # drop the file's own H1
    raw = re.sub(r"^(#{2,5}) ", r"#\1 ", raw, flags=re.M)  # demote the rest
    return raw.strip()


def corpora():
    """A table of what has been extracted, read from the YAML rather than restated."""
    import yaml
    rows = []
    for f in sorted(glob.glob(os.path.join(RESEARCH, "corpora", "*", "*.yaml"))):
        d = yaml.safe_load(io.open(f, encoding="utf-8")) or {}
        m = d.get("meta", {})
        body = next((v for k, v in d.items() if k != "meta" and isinstance(v, list)), [])
        rel = os.path.relpath(f, RESEARCH).replace("\\", "/")
        canon = str(m.get("canon", "-"))
        canon = canon.split(" - ")[0].split(";")[0].strip()   # the tag, not its essay
        rows.append("| `%s` | %s | %d | %s |" % (
            rel, m.get("corpus", "-"), len(body), canon))
    ocr = sorted(os.path.basename(p)[:-4] for p in
                 glob.glob(os.path.join(RESEARCH, "corpora", "_ocr", "*.txt")))
    out = ["## %d. Appendix C: what has been extracted" % (len(PARTS) + 1), "",
           "*Generated from the corpus files themselves.*", "",
           "| File | Corpus | Records | Canon |", "|---|---|---|---|"] + rows
    if ocr:
        out += ["", "**OCR'd to text** (sidecars, not committed): " +
                ", ".join("`%s`" % o for o in ocr) + ".", "",
                "Rebuild any corpus with `python research/tools/extract_*.py`; "
                "re-OCR with `python research/tools/ocr.py <slug>`."]
    return "\n".join(out)


def build():
    import yaml
    p = yaml.safe_load(io.open(os.path.join(ROOT, "project.yaml"), encoding="utf-8"))
    try:
        commit = subprocess.check_output(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"],
                                        stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        commit = "unknown"
    head = [
        "---",
        'title: "Star Crawler — Research"',
        'subtitle: "How other games do races, droids, the Force, classes and generators"',
        "author: [%s]" % p["author"]["name"],
        "date: %s" % datetime.date.today().isoformat(),
        "lang: %s" % p["language"],
        "status: SCAFFOLD",
        "version: %s" % p["version"],
        "generated_by: research/tools/build_research.py",
        "source_commit: %s" % commit,
        "---",
        "",
        "# Star Crawler — Research",
        "",
        "**Generated. Do not edit.** Edit the files in `research/` and run",
        "`python research/tools/build_research.py`.",
        "",
        "**Draft stage. Nothing here is a decision.** Every numbered finding at the end",
        "of a part is a *reading* — what the evidence appears to support — not a ruling.",
        "Star Crawler's own draft positions live in `decisions/DECISIONS.md` and are",
        "also not decisions. Where a claim has a number, the number came from a corpus",
        "in `research/corpora/` and can be recounted; where it does not, it is a reading",
        "of a book and should be argued with.",
        "",
        "Nothing in this document is Star Crawler's design. It is eleven other games'.",
        "",
        "**Part 1 is the one to read.** It reduces all of it to the choices actually in",
        "front of the game, each with what it costs, who else does it, and a",
        "recommendation to argue with. Parts 2-6 are the evidence behind those",
        "choices, to skim or to check. You can answer part 1 with a list of letters.",
        "",
        "## Contents",
        "",
    ]
    for i, (_, title) in enumerate(PARTS, 1):
        head.append("%d. %s" % (i, title))
    head += ["%d. Appendix C: what has been extracted" % (len(PARTS) + 1), ""]

    body = []
    for i, (name, title) in enumerate(PARTS, 1):
        body += ["", "---", "", "## %d. %s" % (i, title), "",
                 "*Source: `research/%s`*" % name, "", load(name)]
    body += ["", "---", "", corpora(), ""]
    return "\n".join(head) + "\n".join(body) + "\n"


if __name__ == "__main__":
    text = build()
    if "--check" in sys.argv:
        old = io.open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        # ignore the date and commit lines, which move on their own
        norm = lambda s: re.sub(r"^(date|source_commit):.*$", "", s, flags=re.M)
        if norm(old) != norm(text):
            sys.exit("RESEARCH.md is out of date: run python research/tools/build_research.py")
        print("RESEARCH.md up to date")
    else:
        io.open(OUT, "w", encoding="utf-8", newline="\n").write(text)
        print("wrote %s (%d lines, %.0f KB)" % (
            os.path.relpath(OUT, ROOT).replace("\\", "/"),
            text.count("\n"), len(text.encode("utf-8")) / 1024.0))
