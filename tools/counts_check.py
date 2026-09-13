# -*- coding: utf-8 -*-
"""Prose that asserts how much content exists, checked against the content.

THE FAULT THIS EXISTS FOR. Three times in two sessions a file has described an
older version of the corpus: 3.3 counted 83 Families the day the 84th landed,
humans.yaml called itself the only stock with an empty anatomy list, and the
glossary defined Stock as "your animal" long after Humans stopped being one.

Nothing caught any of them, because a wrong number is still valid YAML and
still passes every structural check. The corpus grows; the sentences about it
do not. That is a fault CLASS, so it gets a check rather than three fixes.

WHAT IT DOES. Finds sentences that put a number next to a countable noun and
compares the number to what is actually in content/. A number inside a range,
a price, a die or a section reference is not a count and is skipped.

WHAT THE NOUNS ARE is the game's business, not Core's. Until 2026-09-13 this
file carried Mutant's table - Families / Breeds / Variants / paid-pool traits -
and walked Mutant's YAML to count them, which meant every other game counted
nothing and said so silently. Now the game declares both in
`tools/game_schema.py` (see playbook/STARTING_A_NEW_GAME.md):

    NOUNS  = [(re.compile(r"\\bFamil(?:y|ies)\\b"), "family"), ...]
    def counts(): return {"family": 84, ...}

Without that file there is nothing to count. The check says so and passes;
it does not pretend. The self-test runs against a fixture schema, so the
mechanism is proven whether or not the game has declared anything.

WHAT IT DELIBERATELY DOES NOT DO. It does not check every integer in the book.
Most numbers are rules - damage, costs, tiers - and a checker that flagged them
would be noise nobody reads, which is worse than no checker.
"""
import io, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, "tools")

try:
    import game_schema as SCHEMA
except ImportError:
    SCHEMA = None

NUM = re.compile(r"(?<![\d.$–—-])(\d{2,4})"
                 r"(?![\d.']|\s*(?:-|–|—)\s*\d)")
# a number that is plainly not a count of content
# "19 Families OFFER Wing-Hands" counts a subset, not the corpus.
SUBSET = re.compile(r"^\s*(?:of them |of these |in the book )?"
                    r"(offer|use|sell|carry|share|have|has|include)s?\b", re.I)

SKIP = re.compile(r"(\$|\bd\d|\bp\.|\bhp\b|\bft\b|\bkg\b|\bAC\b|\bXP\b"
                  r"|\bSection\b|\bAppendix\b|\bTier\b|\byear|\btonne|\bmetre)",
                  re.I)

def scan(text, name, nouns, want, hits):
    for i, line in enumerate(text.split("\n"), 1):
        if SKIP.search(line):
            continue
        if len(re.findall(r"\d+", line)) >= 3:
            continue  # a table row or a worked sum, not a claim about content
        for pat, key in nouns:
            m = pat.search(line)
            if not m:
                continue
            for n in NUM.finditer(line):
                # only a number sitting just before the noun counts it
                gap = m.start() - n.end()
                if not (0 <= gap <= 12):
                    continue
                # a count immediately narrowed is a subset, not the corpus
                if SUBSET.match(line[m.end():m.end() + 30]):
                    continue
                v = int(n.group(1))
                if v != want[key]:
                    hits.append((name, i, v, key, want[key],
                                 " ".join(line.split())[:100]))
            break

def run(nouns, want, extra=None):
    hits = []
    files = sorted(glob.glob("book/*.md")) + sorted(glob.glob("content/**/*.yaml",
                                                              recursive=True))
    for f in files:
        scan(io.open(f, encoding="utf-8").read(), f, nouns, want, hits)
    if extra:
        scan(extra, "<self-test>", nouns, want, hits)
    return hits

# --------------------------------------------------------------- SELF-TEST
# A check that never fails is not a check. These are the three real sentences
# that got through, plus one that must NOT fire. They are Mutant's sentences
# and they run against a FIXTURE of Mutant's schema, not the game's: the test
# proves the number-next-to-noun mechanism, not any one game's table.
FIXTURE_NOUNS = [
    (re.compile(r"\bpaid[- ]pool traits?\b", re.I), "trait"),
    (re.compile(r"\bpool traits?\b", re.I),         "trait"),
    (re.compile(r"\bNamed Variants?\b", re.I),      "variant"),
    (re.compile(r"\bVariants?\b"),                  "variant"),
    (re.compile(r"\bFamil(?:y|ies)\b"),             "family"),
    (re.compile(r"\bBreeds?\b"),                    "breed"),
]
FIXTURE_WANT = {"family": 84, "breed": 288, "variant": 100, "trait": 900}

MUST_CATCH = [
    "* **Every trait carries a number.** 854 paid-pool traits across 83 Families,",
    "All six Class Pick lists, the 68-Family list, three worked Family drafts",
    "68 Families drafted with dual naming, a quarry to draw from over time",
]
MUST_PASS = [
    "anatomy Flaws in the shared list, at -2, and 19 Families offer it",
    "A Heavy Blade does 1d8 and costs $300, which is Cost Tier 3 for one Family",
    "See Section 3.3 for the 84 Families and what each Breed sells",
    # the four false positives that tightened this check. Each one is a number
    # sitting near a countable noun WITHOUT claiming how much content exists.
    "this book. Base Speed is 30'. Your Family's traits are what make you",
    "The 8-10 Family pool, the 3-4 Breed pool and the four-Breeds-per-spread",
    "Tiny 15 . Small 13 . Medium 11 . Large 9. A Family may state a modifier",
    # (the 288-arithmetic line was reworded instead: no wording of it could
    #  be told apart from a real claim, and "gives 288 of them" reads better)
]

def self_test():
    ok = True
    def probe(s):
        h = []
        scan(s, "<self-test>", FIXTURE_NOUNS, FIXTURE_WANT, h)
        return h
    for s in MUST_CATCH:
        if not probe(s):
            print("SELF-TEST FAILED - missed: %s" % s[:60])
            ok = False
    for s in MUST_PASS:
        if probe(s):
            print("SELF-TEST FAILED - false positive: %s" % s[:60])
            ok = False
    return ok

if __name__ == "__main__":
    if not self_test():
        raise SystemExit("counts_check refuses to report: its own tests fail")
    if SCHEMA is None or not getattr(SCHEMA, "NOUNS", None):
        print("no tools/game_schema.py declaring NOUNS: nothing to count "
              "(see playbook/STARTING_A_NEW_GAME.md)")
        sys.exit(0)
    want = SCHEMA.counts()
    hits = run(SCHEMA.NOUNS, want)
    print("corpus: " + ", ".join("%d %s" % (want[k], k)
                                 for k in sorted(want)))
    for f, i, got, key, exp, line in hits:
        print("  STALE  %-28s %4d  says %d %ss, corpus has %d\n         %s"
              % (f.replace("\\", "/"), i, got, key, exp, line))
    print("%d stale count%s" % (len(hits), "" if len(hits) == 1 else "s"))
    sys.exit(1 if hits else 0)
