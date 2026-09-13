# -*- coding: utf-8 -*-
"""Extract every WEG d6 species from the rancorpit Aliens_Stats compilation.

Source: H:/RPG/Game Systems/Star Wars d6/rancorpit/Aliens_Stats.pdf
        ("Aliens Stats" by Thiago S. Aranha - a fan compilation of every
        species statted for WEG Star Wars d6, each entry citing its own
        original book and page in a "Source:" line where known).

Output: research/corpora/weg/species.yaml - one record per species with the
        raw labelled blocks split out and the special abilities broken into
        (name, text) pairs. Every record carries the PDF page it came from.
        Nothing here is interpreted; that is Species_Shape_Fit.md's job.

Usage:  python research/tools/extract_weg_species.py
"""
import io, os, re, sys, yaml
import pypdf

PDF = "H:/RPG/Game Systems/Star Wars d6/rancorpit/Aliens_Stats.pdf"
OUT = os.path.join(os.path.dirname(__file__), "..", "corpora", "weg", "species.yaml")

ATTRS = ["DEXTERITY", "KNOWLEDGE", "MECHANICAL", "PERCEPTION", "STRENGTH", "TECHNICAL"]
LABELS = ["Home Planet", "Attribute Dice", "Special Skills", "Special Abilities",
          "Story Factors", "Move", "Size", "Source", "Personality",
          "Physical Description", "Language", "Example Names"]
LABEL_RE = re.compile(r"^(%s)\s*:?\s*(.*)$" % "|".join(LABELS))
ATTR_RE = re.compile(r"^(%s)\s*([\dD+/ ]+)$" % "|".join(ATTRS))
DICE_RE = re.compile(r"^Attribute Dice\s*:?\s*(\d+D)")
# an ability line: "Name: text" where Name is short and title-ish
ABIL_RE = re.compile(r"^([A-Z(][^:]{1,60}):\s*(.*)$")


def fix(s):
    return (s.replace("\ufb01", "fi").replace("\ufb02", "fl").replace("\u2019", "'")
             .replace("\u201c", '"').replace("\u201d", '"').replace("\u2013", "-"))


def read_pages():
    r = pypdf.PdfReader(PDF)
    return [fix(p.extract_text() or "") for p in r.pages]


def toc_names(pages):
    """The TOC (pages 3-4, 0-based) lists 'NN. Name' - the names split the body."""
    names = []
    for i in (3, 4):
        for line in pages[i].split("\n"):
            m = re.match(r"^\s*(\d+)\.\s+(.+?)\s*$", line)
            if m:
                names.append((int(m.group(1)), m.group(2).rstrip("* ").strip()))
            elif names and line.strip().startswith("("):
                pass                                   # wrapped parenthetical
    return names


def heads(line, name):
    """A heading line is the name alone, or the name plus a short parenthetical."""
    s = line.strip().lower()
    n = name.lower()
    return s == n or (s.startswith(n) and len(s) - len(n) < 20 and "(" in s[len(n):])


def split_entries(pages, names):
    """Walk the body pages; a line equal to the next TOC name starts an entry."""
    body = []
    for i, p in enumerate(pages[5:], start=5):
        for line in p.split("\n"):
            body.append((i + 1, line.rstrip()))          # 1-based PDF page
    entries, cur, want = [], None, 0
    for page, line in body:
        if want < len(names) and heads(line, names[want][1]):
            cur = {"name": names[want][1], "pdf_page": page, "lines": []}
            entries.append(cur)
            want += 1
            continue
        if cur is not None:
            cur["lines"].append(line)
    return entries, want


def parse(entry):
    rec = {"name": entry["name"], "pdf_page": entry["pdf_page"],
           "attributes": {}, "special_abilities": [], "special_skills": [],
           "story_factors": []}
    section, buf = "description", []
    sections = {}

    def flush():
        if buf:
            sections.setdefault(section, []).extend(buf)
            buf.clear()

    for line in entry["lines"]:
        s = line.strip()
        if not s or re.match(r"^\d{1,3}$", s):         # page number
            continue
        m = ATTR_RE.match(s)
        if m:
            rec["attributes"][m.group(1)] = m.group(2).strip()
            continue
        m = DICE_RE.match(s)
        if m:
            rec["attribute_dice"] = m.group(1)
            continue
        m = LABEL_RE.match(s)
        if m and m.group(1) in ("Special Skills", "Special Abilities", "Story Factors"):
            flush(); section = m.group(1); buf.extend([m.group(2)] if m.group(2) else [])
            continue
        if m and m.group(1) in ("Move", "Size", "Source", "Home Planet"):
            flush()
            rec[m.group(1).lower().replace(" ", "_")] = m.group(2).strip()
            section = "after_" + m.group(1)
            continue
        if m:                                             # prose labels
            flush(); section = m.group(1); buf.append(m.group(2))
            continue
        buf.append(s)
    flush()

    def pairs(lines):
        out, cur = [], None
        for l in lines:
            m = ABIL_RE.match(l)
            if m:
                cur = {"name": m.group(1).strip(), "text": m.group(2).strip()}
                out.append(cur)
            elif cur:
                cur["text"] = (cur["text"] + " " + l).strip()
            else:
                out.append({"name": "", "text": l})
        return out

    rec["special_abilities"] = pairs(sections.get("Special Abilities", []))
    rec["special_skills"] = pairs(sections.get("Special Skills", []))
    rec["story_factors"] = pairs(sections.get("Story Factors", []))
    desc = sections.get("description", []) + sections.get("Physical Description", [])
    if desc:
        rec["description"] = " ".join(desc)[:600]
    for k in ("Personality", "Language"):
        if k in sections:
            rec[k.lower()] = " ".join(sections[k])[:400]
    return rec


def main():
    pages = read_pages()
    names = toc_names(pages)
    entries, found = split_entries(pages, names)
    recs = [parse(e) for e in entries]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    head = {"corpus": "WEG Star Wars d6 species",
            "source_pdf": PDF,
            "compiler": "Thiago S. Aranha (rancorpit 'Aliens Stats')",
            "canon": "legends",
            "canon_note": "WEG d6 (1987-1999) predates the 2014 Legends split entirely; "
                          "every entry is Legends. Entries whose source line cites a WotC "
                          "book are also Legends (WotC line ended 2010).",
            "extracted_by": "research/tools/extract_weg_species.py",
            "toc_entries": len(names), "extracted": len(recs),
            "note": "Raw extraction. Each record cites its PDF page; each entry's "
                    "own 'source' line names the original WEG/WotC book where the "
                    "compiler gave one."}
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump({"meta": head, "species": recs}, f, sort_keys=False,
                       allow_unicode=True, width=100)
    n_ab = sum(len(r["special_abilities"]) for r in recs)
    missing = [n for _, n in names[found:]]
    print("TOC %d, extracted %d, abilities %d, with attribute_dice %d, with source %d"
          % (len(names), len(recs), n_ab,
             sum(1 for r in recs if "attribute_dice" in r),
             sum(1 for r in recs if "source" in r)))
    if missing:
        print("not found: %s" % ", ".join(missing[:20]))


if __name__ == "__main__":
    main()
