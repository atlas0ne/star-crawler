# -*- coding: utf-8 -*-
"""Extract every WEG d6 droid from the rancorpit Droids_Stats compilation.

Source: <library>/Star Wars/d6/The Rancor Pit/Droids_Stats.pdf (see paths.py)
        ("Droids Stats" by Thiago S. Aranha). The table of contents is organised
        Degree -> category -> model, which IS the WEG droid taxonomy (from the
        1988 *Droids* sourcebook); it is preserved on every record.

Output: research/corpora/weg/droids.yaml - one record per droid: name, degree,
        category, type line, attributes (with skills listed under each), the
        "Equipped With" list, move, size, cost, source, PDF page. Raw; nothing
        interpreted. Canon: Legends.

Usage:  python research/tools/extract_weg_droids.py
"""
import io, os, re, sys, yaml
import pypdf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths

PDF = paths.WEG_DROIDS
OUT = os.path.join(os.path.dirname(__file__), "..", "corpora", "weg", "droids.yaml")
ATTRS = ["DEXTERITY", "KNOWLEDGE", "MECHANICAL", "PERCEPTION", "STRENGTH", "TECHNICAL"]
ATTR_RE = re.compile(r"^(%s)\s*([\dD+ ]*)$" % "|".join(ATTRS))
DEGREE_RE = re.compile(r"^(\d)(?:st|nd|rd|th) Degree Droids$")
TOC_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$")
LABEL_RE = re.compile(r"^(Type|Move|Size|Cost|Source|Equipped With|Special Abilities|Story Factors|Game Notes|Capsule|Special)\s*:?\s*(.*)$")


def fix(s):
    return (s.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("’", "'")
             .replace("“", '"').replace("”", '"').replace("–", "-"))


def toc(pages):
    out, degree, cat, pending = [], None, None, None
    for i in (3, 4):
        for line in pages[i].split("\n"):
            s = line.strip()
            if not s or s in ("Table of Contents",) or re.match(r"^\d+$", s):
                continue
            m = DEGREE_RE.match(s)
            if m:
                degree = int(m.group(1)); continue
            m = TOC_RE.match(s)
            if m:
                out.append([degree, cat, m.group(2)]); pending = out[-1]; continue
            if s.endswith("Droids") or s in ("Individual Droids",):
                cat = s.replace(" Droids", ""); continue
            if pending and not s[0].isdigit():          # wrapped name continuation
                pending[2] = (pending[2] + " " + s).strip()
    return [tuple(x) for x in out]


def heads(line, name):
    s = line.strip().lower(); n = name.lower()
    return s == n or (s.startswith(n) and len(s) - len(n) < 12)


def split(pages, names):
    body = []
    for i, p in enumerate(pages[5:], start=5):
        for line in p.split("\n"):
            body.append((i + 1, line.rstrip()))
    entries, cur, want, missed = [], None, 0, []
    k = 0
    while k < len(body):
        page, line = body[k]
        two = (line.strip() + " " + body[k + 1][1].strip()) if k + 1 < len(body) else line
        hit = None
        for look in range(0, 4):                     # a TOC name the body lacks: skip it
            if want + look < len(names):
                nm = names[want + look][2]
                if heads(line, nm):
                    hit = (look, 0); break
                if heads(two, nm) and len(line.strip()) < len(nm):
                    hit = (look, 1); break           # heading wrapped over two lines
        if hit:
            look, extra = hit
            missed += [names[want + j][2] for j in range(look)]
            d, c, n = names[want + look]
            cur = {"name": n, "degree": d, "category": c, "pdf_page": page, "lines": []}
            entries.append(cur); want += look + 1; k += 1 + extra
            continue
        if cur is not None:
            cur["lines"].append(line.strip())
        k += 1
    if missed:
        print("TOC names not found in body (%d): %s" % (len(missed), "; ".join(missed[:12])))
    return entries, want


def parse(e):
    rec = {k: e[k] for k in ("name", "degree", "category", "pdf_page")}
    rec["attributes"] = {}
    rec["equipped_with"] = []
    section, attr = None, None
    for s in e["lines"]:
        if not s or re.match(r"^\d{1,3}$", s):
            continue
        m = ATTR_RE.match(s)
        if m:
            attr = m.group(1); rec["attributes"][attr] = {"dice": m.group(2).strip(), "skills": []}
            section = "attr"; continue
        m = LABEL_RE.match(s)
        if m:
            k = m.group(1).lower().replace(" ", "_")
            if k == "equipped_with":
                section = "equip"
            elif k in ("special_abilities", "story_factors", "game_notes", "capsule", "special"):
                section = k; rec.setdefault(k, [])
                if m.group(2): rec[k].append(m.group(2))
            else:
                rec[k] = m.group(2).strip(); section = k
            continue
        if section == "attr" and attr:
            rec["attributes"][attr]["skills"].append(s)
        elif section == "equip":
            if s.startswith("-"):
                rec["equipped_with"].append(s.lstrip("- ").strip())
            elif rec["equipped_with"]:
                rec["equipped_with"][-1] += " " + s
        elif section in ("type", "source", "cost", "size", "move") and section in rec:
            rec[section] = (rec[section] + " " + s).strip()
        elif section and isinstance(rec.get(section), list):
            rec[section].append(s)
    return rec


def main():
    pages = [fix(p.extract_text() or "") for p in pypdf.PdfReader(PDF).pages]
    names = toc(pages)
    entries, found = split(pages, names)
    recs = [parse(e) for e in entries]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    from collections import Counter
    meta = {"corpus": "WEG Star Wars d6 droids", "source_pdf": PDF,
            "compiler": "Thiago S. Aranha (rancorpit 'Droids Stats')", "canon": "legends",
            "taxonomy": "WEG Degree (1-5) -> category -> model, as the compilation's TOC",
            "extracted_by": "research/tools/extract_weg_droids.py",
            "toc_entries": len(names), "extracted": len(recs),
            "by_degree": dict(sorted(Counter(r["degree"] for r in recs).items())),
            "by_category": dict(Counter("%s/%s" % (r["degree"], r["category"]) for r in recs))}
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump({"meta": meta, "droids": recs}, f, sort_keys=False, allow_unicode=True, width=100)
    print("TOC %d, extracted %d, with attributes %d, with equipment %d" % (
        len(names), len(recs), sum(1 for r in recs if r["attributes"]),
        sum(1 for r in recs if r["equipped_with"])))
    print(meta["by_degree"])
    if found < len(names):
        print("not found:", [n for _, _, n in names[found:found + 8]])


if __name__ == "__main__":
    main()
