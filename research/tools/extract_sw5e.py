# -*- coding: utf-8 -*-
"""Extract species and Force powers from the SW5e Player's Handbook.

Source: H:/RPG/Game Systems/Star Wars 5e/SW5e - Player's Handbook.pdf
        (fan-made 5e conversion, sw5e.com; the PDF's own outline gives the
        page of every species and chapter).

Outputs:
  research/corpora/sw5e/species.yaml       - every Chapter 2 species with its
                                             trait block split into (name, text)
  research/corpora/sw5e/force_powers.yaml  - every Chapter 11 power with level,
                                             side, casting fields and text

Extraction uses pdftotext (poppler): pypdf drops this PDF's fi/ff ligatures.

CANON. SW5e is post-2014 fan work and draws on both continuities. Species and
powers here are tagged per record by a lookup table at the bottom of this
file (`CANON`), which is a judgement kept in one place so it can be argued
with. Default is "both" (exists in Legends and in Disney canon); "legends"
or "disney" where the thing exists in only one. Unknown stays "untagged".

Usage:  python research/tools/extract_sw5e.py
"""
import io, os, re, subprocess, yaml
import pypdf

PDF = "H:/RPG/Game Systems/Star Wars 5e/SW5e - Player's Handbook.pdf"
OUTDIR = os.path.join(os.path.dirname(__file__), "..", "corpora", "sw5e")


def text(first, last):
    r = subprocess.run(["pdftotext", "-f", str(first), "-l", str(last), PDF, "-"],
                       capture_output=True)
    return r.stdout.decode("utf-8", "replace").replace("\f", "\n")


def outline():
    r = pypdf.PdfReader(PDF)
    out = []

    def walk(o, depth):
        for x in o:
            if isinstance(x, list):
                walk(x, depth + 1)
            else:
                out.append((depth, x.title, r.get_destination_page_number(x) + 1))
    walk(r.outline, 0)
    return out


# ----------------------------------------------------------------- species
TRAIT_SPLIT = re.compile(r"(?:(?<=\.)|(?<=:)|^)\s+(?=([A-Z][A-Za-z'/-]+(?: (?:[A-Z][A-Za-z'/-]+|of|the|and|or|in|to))*)\. [A-Z])")
TRAIT_HEAD = re.compile(r"^([A-Z][A-Za-z'/-]+(?: (?:[A-Z][A-Za-z'/-]+|of|the|and|or|in|to))*)\. (.*)$", re.S)


def species(ol):
    items = [(t, p) for d, t, p in ol if d == 1]
    idx = [i for i, (t, p) in enumerate(items)]
    ch2 = [(t, p) for d, t, p in ol]
    # the species are the depth-1 entries between CHAPTER 2 and CHAPTER 3
    start = next(i for i, (d, t, p) in enumerate(ol) if t.startswith("CHAPTER 2"))
    end = next(i for i, (d, t, p) in enumerate(ol) if t.startswith("CHAPTER 3"))
    sp = [(t, p) for d, t, p in ol[start + 1:end] if d == 1]
    recs = []
    for i, (name, page) in enumerate(sp):
        last = sp[i + 1][1] if i + 1 < len(sp) else ol[end][2]
        t = text(page, max(page, last))
        flat = " ".join(t.split())
        key = name.replace("DROID, CLASS ", "CLASS ") + " DROID TRAITS" if name.startswith("DROID") \
            else name + " TRAITS"
        j = flat.find(key)
        block = flat[j + len(key):] if j >= 0 else ""
        # the block ends at the next species heading or the next all-caps section
        m = re.search(r" (?:[A-Z][A-Z',-]+ ){0,3}(?:TRAITS|EXPANDED CONTENT|CHAPTER \d)", block)
        if m:
            block = block[:m.start()]
        block = re.sub(r"As an? [^.]{1,40}, you have the following special traits\.\s*", "", block)
        block = re.sub(r"\s+\d{1,3} EXPANDED CONTENT \| SPECIES\s*", " ", block)
        traits = []
        for piece in TRAIT_SPLIT.split(block):
            if not piece or not piece.strip():
                continue
            m2 = TRAIT_HEAD.match(piece.strip())
            if m2 and not traits and m2.group(1) != "Ability Score Increase":
                pass
            if m2:
                traits.append({"name": m2.group(1), "text": " ".join(m2.group(2).split())})
            elif traits:
                traits[-1]["text"] += " " + piece.strip()
        # dedupe: TRAIT_SPLIT yields captured group AND remainder alternately
        seen, clean = set(), []
        for tr in traits:
            k = tr["name"]
            if k in seen:
                continue
            seen.add(k); clean.append(tr)
        for a, b in zip(clean, clean[1:]):          # "... Age" trailing next name
            if a["text"].endswith(" " + b["name"]):
                a["text"] = a["text"][:-len(b["name"]) - 1].rstrip()
        rec = {"name": name.title().replace("'S", "'s"), "pdf_page": page,
               "canon": CANON.get(name.title(), "untagged"), "traits": clean}
        recs.append(rec)
    return recs


# -------------------------------------------------------------- force powers
LEVEL = re.compile(r"^(?P<name>[A-Z][A-Z0-9' ,/-]+?)\s+(?P<lvl>At-will|\d(?:st|nd|rd|th)-level) "
                   r"(?P<side>universal|light side|dark side) power\s*$")
LEVEL2 = re.compile(r"^(?P<lvl>At-will|\d(?:st|nd|rd|th)-level) (?P<side>universal|light side|dark side) power\s*$")
FIELDS = re.compile(r"^(Prerequisite|Casting Time|Range|Duration|Force Potency|Overcharge Tech)\s*[:.]\s*(.*)$")


def powers(ol):
    start = next(p for d, t, p in ol if t.startswith("CHAPTER 11"))
    end = next(p for d, t, p in ol if t.startswith("CHAPTER 12"))
    lines = [l.rstrip() for l in text(start, end - 1).split("\n")]
    recs, cur, prev = [], None, ""
    for l in lines:
        s = l.strip()
        if not s:
            continue
        m = LEVEL.match(s)
        m2 = LEVEL2.match(s) if not m else None
        if m or (m2 and re.match(r"^[A-Z][A-Z0-9' ,/-]+$", prev)):
            name = m.group("name") if m else prev
            g = m or m2
            cur = {"name": name.title().replace("'S", "'s"), "level": g.group("lvl"),
                   "side": g.group("side"), "text": ""}
            recs.append(cur)
            prev = s
            continue
        prev = s
        if cur is None:
            continue
        if re.match(r"^[A-Z][A-Z0-9' ,/-]+$", s):
            continue                                  # a heading (next power's name)
        if re.match(r"^\d{1,3}$", s) or "CHAPTER 11" in s or "FORCE POWERS" in s:
            continue
        f = FIELDS.match(s)
        if f:
            # several fields may share one line: split on the next field name
            parts = re.split(r" (?=(?:Prerequisite|Casting Time|Range|Duration)\s*[:.])", s)
            for part in parts:
                g = FIELDS.match(part)
                if g:
                    cur[g.group(1).lower().replace(" ", "_")] = g.group(2).strip()
        else:
            cur["text"] = (cur["text"] + " " + s).strip()
    for r in recs:
        r["canon"] = "n/a"                            # a power is a rule, not a thing
    return recs


CANON = {
    # species in Legends only, Disney only, or both. Judgement, kept in one place.
    "Bith": "both", "Bothan": "both", "Cathar": "legends", "Cerean": "both",
    "Chiss": "both", "Devaronian": "both", "Duros": "both", "Ewok": "both",
    "Gamorrean": "both", "Gungan": "both", "Human": "both", "Ithorian": "both",
    "Jawa": "both", "Kel Dor": "both", "Mon Calamari": "both", "Nautolan": "both",
    "Rodian": "both", "Sith Pureblood": "legends", "Togruta": "both",
    "Trandoshan": "both", "Tusken": "both", "Twi'Lek": "both", "Weequay": "both",
    "Wookiee": "both", "Zabrak": "both",
    "Droid, Class I": "both", "Droid, Class Ii": "both", "Droid, Class Iii": "both",
    "Droid, Class Iv": "both", "Droid, Class V": "both",
}


def main():
    ol = outline()
    os.makedirs(OUTDIR, exist_ok=True)
    sp = species(ol)
    pw = powers(ol)
    meta = {"corpus": "SW5e Player's Handbook", "source_pdf": PDF,
            "publisher": "sw5e.com (fan, 5e SRD-based)", "extracted_by":
            "research/tools/extract_sw5e.py (pdftotext)",
            "canon": "mixed - see per-record canon field; droid classes I-V are the "
                     "Legends droid classification (Droids sourcebook, WEG 1988) and "
                     "survive in Disney canon"}
    with io.open(os.path.join(OUTDIR, "species.yaml"), "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump({"meta": dict(meta, extracted=len(sp)), "species": sp}, f,
                       sort_keys=False, allow_unicode=True, width=100)
    with io.open(os.path.join(OUTDIR, "force_powers.yaml"), "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump({"meta": dict(meta, extracted=len(pw)), "powers": pw}, f,
                       sort_keys=False, allow_unicode=True, width=100)
    from collections import Counter
    print("species %d, traits %d" % (len(sp), sum(len(s["traits"]) for s in sp)))
    print("  ", [(s["name"], len(s["traits"])) for s in sp][:8])
    print("powers %d" % len(pw), Counter(p["side"] for p in pw), Counter(p["level"] for p in pw))


if __name__ == "__main__":
    main()
