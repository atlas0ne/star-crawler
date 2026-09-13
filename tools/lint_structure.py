#!/usr/bin/env python3
"""Document structure linter.

Checks every markdown document in the project for the things that make a book
navigable and machine-readable, and that nothing else verifies:

  * exactly one H1 per document
  * no skipped heading levels (an H2 never jumps straight to an H4)
  * front matter present on every document meant to carry it
  * front matter carries the required fields

Heading skips are not pedantry. They break generated tables of contents, they
break screen readers, and they break any tool that infers structure from
depth - which includes an assistant deciding which part of a file to read.
"""
import io, os, re, sys, glob
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
HEAD = re.compile(r"^(#{1,6})\s+(.*)$", re.M)
FENCE = re.compile(r"```.*?```", re.S)
BANNED_TAGS = re.compile(r"\[(CHANGED|CORRECTED)\]")

# Documents that must carry front matter, and the fields they must carry.
REQUIRED = ["title", "status"]
RICH = ["title", "author", "date", "lang", "status", "version", "website", "repository"]

def targets():
    out = []
    out += sorted(glob.glob(os.path.join(ROOT, "book", "*.md")))
    out += sorted(glob.glob(os.path.join(ROOT, "quickstart", "*.md")))
    for f in ("QUICKSTART.md", "RULES_REFERENCE.md", "README.md", "OPEN_QUESTIONS.md"):
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            out.append(p)
    out += sorted(glob.glob(os.path.join(ROOT, "decisions", "*.md")))
    return out

def main():
    issues = []
    rows = []
    for path in targets():
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        raw = io.open(path, encoding="utf-8").read()
        m = FM.match(raw)
        fm = None
        if m:
            # A document may legitimately open with a --- horizontal rule, which
            # looks exactly like front matter to a regex. Only accept it if it
            # actually parses as a mapping.
            try:
                parsed = yaml.safe_load(m.group(1))
                fm = parsed if isinstance(parsed, dict) else None
            except yaml.YAMLError:
                fm = None
        body = FENCE.sub("", raw[m.end():] if (m and fm) else raw)

        levels = [(len(h), t.strip()) for h, t in HEAD.findall(body)]
        h1 = sum(1 for lv, _ in levels if lv == 1)
        skips = []
        prev = None
        for lv, txt in levels:
            if prev is not None and lv > prev + 1:
                skips.append(f"H{prev}->H{lv} at \"{txt[:40]}\"")
            prev = lv

        # generated + book documents are the ones that must be rich
        wants_fm = rel.startswith("book/") or rel in ("QUICKSTART.md", "RULES_REFERENCE.md")
        missing = []
        if wants_fm:
            if fm is None:
                missing = ["<no front matter at all>"]
            else:
                need = RICH if rel in ("QUICKSTART.md", "RULES_REFERENCE.md") else REQUIRED
                missing = [k for k in need if k not in fm]

        rows.append((rel, len(levels), h1, len(skips), "yes" if fm else "no"))
        if h1 > 1:
            issues.append((rel, f"{h1} H1 headings - a document should have exactly one"))
        if wants_fm and h1 == 0:
            issues.append((rel, "no H1 heading"))
        for s in skips:
            issues.append((rel, f"skipped heading level: {s}"))
        if missing:
            issues.append((rel, "front matter missing: " + ", ".join(missing)))

        # A confidence tag answers ONE question for the reader: how much should
        # I trust this rule? CHANGED and CORRECTED answer a different one -
        # what did an earlier draft say - which a reader who never saw that
        # draft cannot use, and which git records better. Eleven of them sat in
        # book prose until 2.4.4. They belong in design notes and tool
        # comments, which this linter does not read, and never in the book.
        # ...but a DECISION LOG is exactly where "this changed, and here is why"
        # belongs, so the ban covers the book and the views built from it only.
        for bad in (BANNED_TAGS.finditer(raw) if wants_fm else []):
            issues.append((rel, "changelog tag [%s] in book prose - a "
                                "confidence tag says how much to trust a rule, "
                                "not what an older draft said. Use the real "
                                "tier and let git hold the history."
                                % bad.group(1)))

    print("=" * 84)
    print("DOCUMENT STRUCTURE")
    print("=" * 84)
    print(f"\n{'file':44s}{'heads':>7s}{'H1':>4s}{'skips':>7s}{'front matter':>14s}")
    print("-" * 84)
    for rel, n, h1, sk, has in rows:
        print(f"{rel:44s}{n:7d}{h1:4d}{sk:7d}{has:>14s}")

    print("\n" + "=" * 84)
    if issues:
        print(f"{len(issues)} ISSUE(S)\n")
        for rel, msg in issues:
            print(f"  {rel}\n     {msg}")
    else:
        print("PASS - one H1 each, no skipped levels, front matter complete")
    print("=" * 84)
    return 1 if issues else 0

if __name__ == "__main__":
    sys.exit(main())
