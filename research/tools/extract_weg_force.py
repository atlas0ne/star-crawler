# -*- coding: utf-8 -*-
"""Extract every WEG d6 Force power from the rancorpit Force_Powers compilation.

Source: H:/RPG/Game Systems/Star Wars d6/rancorpit/Force_Powers.pdf
        (compiled by Cheshire, edited by Thiago S. Aranha - every Force
        power published for WEG Star Wars d6, grouped by the Control / Sense /
        Alter axis and by light / dark side).

Output: research/corpora/weg/force_powers.yaml - one record per power:
        name, group (which skills it needs), side, the difficulty lines,
        required powers, time to use, effect text, example text, PDF page.
        Nothing interpreted; Force_Models_Compared.md does that.

Usage:  python research/tools/extract_weg_force.py
"""
import io, os, re, yaml
import pypdf

PDF = "H:/RPG/Game Systems/Star Wars d6/rancorpit/Force_Powers.pdf"
OUT = os.path.join(os.path.dirname(__file__), "..", "corpora", "weg", "force_powers.yaml")

GROUPS = ["Control Powers", "Sense Powers", "Alter Powers", "Control and Sense Powers",
          "Control and Alter Powers", "Sense and Alter Powers",
          "Control, Sense and Alter Powers"]
SIDES = ["Jedi Powers", "Dark Side Powers", "Special Powers", "Converted Powers",
         "Fan-Made Powers"]
FIELD_RE = re.compile(r"^(Control Difficulty|Sense Difficulty|Alter Difficulty|"
                      r"Required Powers?|Time to Use|Effect|Example|Warning|Note|"
                      r"This power may be kept up)\s*:?\s*(.*)$", re.I)


def fix(s):
    return (s.replace("\ufb01", "fi").replace("\ufb02", "fl").replace("\u2019", "'")
             .replace("\u201c", '"').replace("\u201d", '"').replace("\u2013", "-")
             .replace("\u2014", "-"))


def toc(pages):
    """The TOC is the page(s) after the title: power names in order under group headings.
    Returns the ordered list of (side, group, name)."""
    out, side, group = [], None, None
    for i in (3, 4):
        for line in pages[i].split("\n"):
            s = line.strip()
            if not s or re.match(r"^x?\d*\s*$", s) or s == "s":
                continue
            if s == "Appendix":
                return out
            if s in SIDES:
                side = s; continue
            if s in GROUPS:
                group = s; continue
            if s.lower().startswith(("force powers", "table of contents")):
                continue
            if side and group:
                out.append((side, group, s))
    return out


def split(pages, names):
    body = []
    for i, p in enumerate(pages[5:], start=5):
        for line in p.split("\n"):
            body.append((i + 1, line.rstrip()))
    entries, cur, want = [], None, 0
    for page, line in body:
        s = line.strip()
        if want < len(names) and s.lower() == names[want][2].lower():
            side, group, name = names[want]
            cur = {"name": name, "side": side, "group": group, "pdf_page": page, "lines": []}
            entries.append(cur); want += 1
            continue
        if s in SIDES or s in GROUPS or re.match(r"^\d+ Force Powers$", s):
            continue
        if cur is not None:
            cur["lines"].append(s)
    return entries, want


def parse(e):
    rec = {"name": e["name"], "side": e["side"], "group": e["group"],
           "pdf_page": e["pdf_page"]}
    field, buf, fields = "lead", [], {}

    def flush():
        if buf:
            fields.setdefault(field, []).append(" ".join(x for x in buf if x))
            buf.clear()

    for s in e["lines"]:
        if not s:
            continue
        m = FIELD_RE.match(s)
        if m:
            flush()
            field = m.group(1).lower().replace(" ", "_").rstrip("s")
            if field == "required_power":
                field = "required_powers"
            buf.append(m.group(2))
            continue
        buf.append(s)
    flush()
    for k, v in fields.items():
        rec[k] = " ".join(v).strip()
    skills = []
    for k in ("control_difficulty", "sense_difficulty", "alter_difficulty"):
        if k in rec:
            skills.append(k.split("_")[0])
    rec["skills_used"] = skills
    return rec


def main():
    pages = [fix(p.extract_text() or "") for p in pypdf.PdfReader(PDF).pages]
    names = toc(pages)
    entries, found = split(pages, names)
    recs = [parse(e) for e in entries]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    meta = {"corpus": "WEG Star Wars d6 Force powers", "source_pdf": PDF,
            "compiler": "Cheshire, ed. Thiago S. Aranha (rancorpit 'Force Powers')",
            "canon": "legends",
            "provenance_by_side": {
                "Jedi Powers": "WEG published (2e R&E, Tales of the Jedi Companion, etc.)",
                "Dark Side Powers": "WEG published (Dark Side Sourcebook and others)",
                "Special Powers": "WEG published, one-off",
                "Converted Powers": "fan conversions to d6 from other systems (WotC d20/Saga); "
                                    "Legends content, not WEG rules text",
                "Fan-Made Powers": "fan inventions; no canon standing - keep, tag, never cite as source"},
            "extracted_by": "research/tools/extract_weg_force.py",
            "toc_entries": len(names), "extracted": len(recs)}
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump({"meta": meta, "powers": recs}, f, sort_keys=False,
                       allow_unicode=True, width=100)
    from collections import Counter
    print("TOC %d, extracted %d, with effect %d" %
          (len(names), len(recs), sum(1 for r in recs if "effect" in r)))
    print(Counter(r["side"] for r in recs))
    print(Counter(r["group"] for r in recs))
    if found < len(names):
        print("not found:", [n for _, _, n in names[found:found + 10]])


if __name__ == "__main__":
    main()
