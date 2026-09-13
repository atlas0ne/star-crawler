# -*- coding: utf-8 -*-
"""A citation must point at a section that exists, and that says the thing.

WHAT xref ALREADY DOES: resolves "Section 6.3b" style pointers against the
actual headings. What it does not do is either half of this:

  1. BARE PARENTHETICAL REFERENCES. The corpus is full of "(6.5)", "(7.13)",
     "(9.7)" - 176 of them across the book and content/ - and none were checked
     by anything, because xref only matches the word "Section" followed by a
     number. Traits use the bare form almost exclusively.

  2. WHETHER THE TARGET SAYS THE THING. 3.2 cited "the general ability-check
     system (Section 7.0)" for a long time. 7.0 exists, so xref passed it. But
     7.0 is the B/X-minimalism PRINCIPLE - it says effects state themselves
     locally and there is no skill list. It never said what to roll. The
     pointer resolved to a real section that did not contain the rule, which is
     the same fault as flanking and grappling wearing a cross-reference.

So when the corpus says "**Rests Rough** (6.5)", this checks that the phrase
"Rests Rough" actually appears in section 6.5. Eleven traits make that exact
citation and it is correct - which is the point: a citation that names its
target is checkable, and this makes naming it worth doing.

Usage:  python tools/citation_check.py
"""
import io
import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

HEADING = re.compile(r"^#{1,6}\s+(?:\[[A-Z]+[^\]]*\]\s*)?"
                     r"(\d+(?:\.\d+)?[a-z]?)\b", re.M)
# ...and chapter 10 introduces 10.1a-10.1g as bold leads instead.
BOLDSEC = re.compile(r"^\*\*(?:\[[A-Z]+[^]]*] *)?"
                     r"(\d+(?:\.\d+)?[a-z]?)\b", re.M)
BARE = re.compile(r"\((\d+(?:\.\d+)?[a-z]?)\)")
NAMED = re.compile(r"\*\*([^*\n]{3,40}?)\*\*[ ]*\((\d+(?:\.\d+)?[a-z]?)\)")
# A citation is a pointer to a rule. These parentheses are not.
NOT_A_REF = re.compile(r"^\d+$")
# A cited TERM is a short noun phrase. A bolded sentence that happens to be
# followed by a reference is prose, and checking its words against the target
# section reports the checker's own confusion as a fault in the book.
NOT_A_TERM = re.compile(r"\b(a|an|the|you|your|it|is|are|on|in|and|"
                        r"under|with|for|that|this)\b", re.I)


def sections():
    """Section number -> its text, from the heading to the next heading."""
    out = {}
    for path in sorted(glob.glob("book/*.md")):
        raw = io.open(path, encoding="utf-8").read()
        marks = sorted([(m.group(1), m.start()) for m in HEADING.finditer(raw)] + [(m.group(1), m.start()) for m in BOLDSEC.finditer(raw)], key=lambda t: t[1])
        for i, (num, at) in enumerate(marks):
            end = marks[i + 1][1] if i + 1 < len(marks) else len(raw)
            out.setdefault(num, "")
            out[num] += raw[at:end]
    return out


def corpus():
    """Every string in the project that might carry a citation, with a label."""
    items = []
    for path in sorted(glob.glob("book/*.md")):
        items.append((os.path.basename(path), io.open(path, encoding="utf-8").read()))
    for path in (sorted(glob.glob("content/*.yaml"))
                 + sorted(glob.glob("content/families/*.yaml"))
                 + sorted(glob.glob("content/classes/*.yaml"))):
        name = os.path.basename(path)
        found = []

        def walk(o):
            if isinstance(o, dict):
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
            elif isinstance(o, str):
                found.append(o)

        walk(yaml.safe_load(io.open(path, encoding="utf-8")))
        items.append((name, "\n".join(found)))
    return items


def normalise(s):
    return re.sub(r"[^a-z0-9 ]", " ", s.lower())


def run(items, secs):
    bad = []
    for name, text in items:
        for num in set(BARE.findall(text)):
            if num not in secs and "." in num:
                bad.append((name, "cites (%s), which is not a section" % num))
        for term, num in set(NAMED.findall(text)):
            if num not in secs:
                continue          # the bare check above already reported it
            if NOT_A_REF.match(term.strip()) or NOT_A_TERM.search(term):
                continue
            if len(term.split()) > 3:
                continue
            want = normalise(term).split()
            body = normalise(secs[num])
            # every word of the named term must appear in the cited section
            # stem-match: "Borrows" satisfies a section called "Borrowing"
            words = body.split()
            missing = [w for w in want if len(w) > 2
                       and not any(x.startswith(w[:5]) for x in words)]
            if missing:
                bad.append((name, 'cites "%s" (%s), but %s does not mention %s'
                            % (term.strip(), num, num, ", ".join(missing[:3]))))
    return bad


# --------------------------------------------------------------- SELF-TEST
# The real fault this was built for, plus the citation that is correct.
BREAKS = [
    ("**Flanking** (7.13)", "does not mention"),
    ("see the rule at (99.9) for details", "not a section"),
]
CLEAN = "**Rests Rough** (6.5), wedged in any branch fork"

# The self-test runs against a synthetic book, not the real one, so it proves
# the checker and not the corpus. On an empty book the real sections() is {}
# and every citation is "not a section", which is correct and still fails a
# self-test that expected to find a real 6.5 - it did, for a whole first hour.
SELF_TEST_SECS = {
    "6.5": "## 6.5 Camping\n\nA character who **Rests Rough** recovers nothing.",
    "7.13": "## 7.13 Surprise\n\nRoll a d6 at the start of the encounter.",
}


def self_test(secs):
    secs = SELF_TEST_SECS
    ok = True
    for text, want in BREAKS:
        hits = " ".join(m for _, m in run([("<self-test>", text)], secs))
        if want not in hits:
            print("SELF-TEST FAILED - missed %r, got %r" % (want, hits[:70]))
            ok = False
    if run([("<self-test>", CLEAN)], secs):
        print("SELF-TEST FAILED - false positive on a correct citation")
        ok = False
    return ok


if __name__ == "__main__":
    secs = sections()
    if not self_test(secs):
        raise SystemExit("citation_check refuses to report: its own tests fail")
    items = corpus()
    bad = run(items, secs)
    total = sum(len(set(BARE.findall(t))) for _, t in items)
    print("%d sections; %d distinct citations checked" % (len(secs), total))
    for name, why in bad:
        print("  %-26s %s" % (name, why))
    print("%d bad citation%s" % (len(bad), "" if len(bad) == 1 else "s"))
    sys.exit(1 if bad else 0)
