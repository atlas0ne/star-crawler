# -*- coding: utf-8 -*-
"""Extract every species from the Ultimate Alien Anthology (WotC 2003, d20 RCR).

Source: the Tesseract sidecars in research/corpora/_ocr/uaa/ (from
        <library>/99_INBOX/d20_star_wars-ultimate_alien_anthology.pdf, see paths.py).
        Run research/tools/ocr.py uaa first.

Output: research/corpora/uaa/species.yaml - one record per "<Name> Species Traits"
        block: name, pdf_page, the bulleted traits as (label, text), and the
        Homeworld / Language / Personality lines from the entry above it.

The OCR renders the bullet glyph as one of a few characters (G, @, ©, ®, e, •);
a trait line is any of those followed by "Label: text". Nothing is interpreted.
Canon: every UAA species is Legends (WotC line ended 2010).

Usage:  python research/tools/extract_uaa.py
"""
import io, os, re, glob, yaml

HERE = os.path.dirname(os.path.abspath(__file__))
OCR = os.path.join(HERE, "..", "corpora", "_ocr", "uaa")
OUT = os.path.join(HERE, "..", "corpora", "uaa", "species.yaml")

# name = the last one-to-three capitalised words before "Species Traits"; the OCR
# sometimes glues a stray glyph to the front ("_Mrissi") or merges the line with
# the previous paragraph ("... are stocky Elom Species Traits")
HEAD = re.compile(r"[^A-Za-z]?([A-Z][A-Za-z'’-]+(?: [A-Z][A-Za-z'’-]+){0,2})\s+Species Traits\s*[—:\-]?\s*$")
BULLET = re.compile(r"^\s*(?:[G@©®e•¢*o0S]{1,2}|\(\w\))\s*([A-Z][A-Za-z' /()-]{2,40}):\s*(.*)$")
STOP = re.compile(r"^\s*(.{2,40}?)\s+(Commoner|Thug|Diplomat|Expert)\s*:")
PRE = re.compile(r"^(Homeworld|Language|Personality|Physical Description|Example Names|Adventurers):\s*(.*)$")


def pages():
    out = []
    for f in sorted(glob.glob(os.path.join(OCR, "p*.txt"))):
        n = int(os.path.basename(f)[1:5])
        out.append((n, io.open(f, encoding="utf-8").read().split("\n")))
    return out


def main():
    lines = []
    for n, ls in pages():
        for l in ls:
            lines.append((n, l.rstrip()))
    recs = []
    i = 0
    while i < len(lines):
        n, l = lines[i]
        m = HEAD.search(l)
        if not m or "section" in l:
            i += 1
            continue
        name = m.group(1).strip()
        rec = {"name": name, "pdf_page": n, "canon": "legends", "traits": []}
        # the prose above: walk back up to 80 lines for the labelled paragraphs
        j = i - 1
        while j >= max(0, i - 80):
            pm = PRE.match(lines[j][1].strip())
            if pm and pm.group(1).lower().replace(" ", "_") not in rec:
                k = pm.group(1).lower().replace(" ", "_")
                txt = pm.group(2)
                jj = j + 1
                while jj < i and lines[jj][1].strip() and not PRE.match(lines[jj][1].strip()):
                    txt += " " + lines[jj][1].strip(); jj += 1
                rec[k] = " ".join(txt.split())[:400]
            if HEAD.search(lines[j][1]) or STOP.match(lines[j][1]):
                break
            j -= 1
        # the traits below
        i += 1
        cur = None
        while i < len(lines):
            n2, l2 = lines[i]
            s = l2.strip()
            if HEAD.search(l2) or STOP.match(l2):
                break
            bm = BULLET.match(l2)
            if bm:
                cur = {"name": bm.group(1).strip(), "text": bm.group(2).strip()}
                rec["traits"].append(cur)
            elif cur and s and not re.match(r"^\d{1,3}$", s):
                cur["text"] = (cur["text"] + " " + s).strip()
            i += 1
        recs.append(rec)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    meta = {"corpus": "Ultimate Alien Anthology species (WotC 2003, d20 Revised)",
            "source": "OCR sidecars from d20_star_wars-ultimate_alien_anthology.pdf (see paths.py)",
            "extracted_by": "research/tools/extract_uaa.py", "canon": "legends",
            "extracted": len(recs),
            "note": "OCR text; spelling faults possible. Ability Modifiers use an OCR em-dash for minus."}
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump({"meta": meta, "species": recs}, f, sort_keys=False, allow_unicode=True, width=100)
    from collections import Counter
    print("species %d, traits %d, with ability modifiers %d" % (
        len(recs), sum(len(r["traits"]) for r in recs),
        sum(1 for r in recs if any(t["name"].startswith("Ability Modifier") for t in r["traits"]))))
    print(Counter(len(r["traits"]) for r in recs))
    print(Counter(t["name"] for r in recs for t in r["traits"]).most_common(25))


if __name__ == "__main__":
    main()
