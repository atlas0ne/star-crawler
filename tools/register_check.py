# -*- coding: utf-8 -*-
"""The register check: describe, do not evoke.

Dan, after two passes that both missed the point:

    "You have seen them asleep. / opened the thing and is holding the piece
    that came loose. / you touch everything you look at before you have
    decided to. / and older than the argument. / that reads as a helmet
    nobody can take off / anything trading on being impressive. / and the
    only person present who is not surprised by how things turn out. / older
    on land than either (ew)

    hate this style. disgusting. weird. try hard. obviously AI. exactly NOT
    what i want"

WHAT THE FIRST TWO PASSES GOT WRONG. Pass one chased length variance, which
was measurable and irrelevant. Pass two cut the JOKES, which was closer and
still wrong. Not one of the eight lines above is a joke. They are a writer
being LITERARY - implication, atmosphere, uncanniness, and the vocabulary of
somebody reviewing a thing rather than describing it.

THE RULE, and it is five lines because a rule nobody can apply is a mood:

  1. Every sentence states a fact about the animal. If it implies something
     instead, cut it.
  2. No critic's vocabulary - "reads as", "somehow", "quietly", "and it knows
     it".
  3. Concrete nouns. "A black mask across the eyes." Not "a helmet nobody can
     take off".
  4. No sentence exists for atmosphere. If deleting it loses no information,
     delete it.
  5. Nothing addresses the reader. Never "you have seen them asleep".

This checker is the fourth and fifth rules made mechanical, plus the specific
constructions Dan named. Rules one and three are human judgement and always
will be; what a script can do is stop the same phrases coming back.

WHAT THIS MISSED FOR WEEKS, and the reason it is worth saying out loud: it
scanned `content/families/*.yaml` and nothing else. Not the Classes, not the
mutations, not the equipment, and not one word of the 41,000-word rules prose
in `book/`. It reported "15 fields to rewrite" every run and read as a clean
bill of health for a book it had never opened. A check that only looks at a
quarter of the corpus passes for the wrong reason.

Dan: "we did a pass on the classes as well... We've checked checked
everything. Have we?" No. The Classes turned out genuinely clean - 0 of 111 -
but nobody had ever asked the question of the other three corpora.

SCOPE MATTERS, which is why widening it is not just a wider glob. Two of the
patterns are only faults in FLAVOUR:

  * Second person is the house voice of the rules. "Take the exact shape of a
    person you have seen" is correct rules writing and wrong in a Family
    identity line. Flagging it everywhere buries the real hits under hundreds
    of correct sentences.
  * "Reads as" is a printed TABLE COLUMN - the reskin column on the Size
    table, the Wealth table and the Strains. Banned in prose, legitimate as a
    heading.

Usage:  python tools/register_check.py [--list] [--scope flavour|rules|all]
"""
import io, os, sys, glob, re, yaml
from collections import Counter

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# (id, pattern, what is wrong with it) - every one drawn from a line Dan
# rejected or from the fault class it belongs to.
BAD = [
 ("critic",   r"\breads as\b|\breads like\b",            "critic's vocabulary"),
 ("adverb",   r"\bsomehow\b|\bquietly\b|\bfaintly\b",    "atmosphere adverb"),
 ("abstract", r"\btrading on\b|\bin the business of\b",  "abstraction instead of a thing"),
 ("reader",   r"\byou have (seen|already)\b",            "addresses the reader"),
 ("reader",   r"\bbefore you (have|had|finished|even)\b", "addresses the reader"),
 ("flourish", r"(than|is) the argument\b|\bthe conversation\b|"
              r"\bthe question is settled\b",
                                                         "abstract flourish"),
 ("aware",    r"\band (it|they) knows? it\b|\bentirely aware\b|\bnever once\b",
                                                         "claimed self-awareness"),
 ("ranking",  r"\bthe only (person|thing) (present|here) who\b",
                                                         "ranking claim"),
 ("crowd",    r"\bnobody (has ever|notices|minds)\b|\beveryone knows\b|"
              r"\bnobody can (take|see|tell|say|remember|hear)\b",
                                                         "appeals to the crowd"),
 ("signoff",  r"\bwhich is the whole (point|problem|tension|conceit|thing|idea)\b|"
              r"\band that is that\b|\bin any respect\b",
                                                         "sign-off"),
 ("notxbuty", r"\bnot lazy\b|\bnot a \w+ so much as\b|\bless a \w+ than\b",
                                                         "not-X-but-Y"),
 ("attitude", r"\bhas (never|not) (once |ever )?(needed|regretted|minded|bothered)\b",
                                                         "an attitude about its own body"),
]
PATS = [(pid, re.compile(p, re.I), why) for pid, p, why in BAD]

# Faults in flavour, correct in rules text. See SCOPE MATTERS above.
FLAVOUR_ONLY = set(["reader"])
TABLE_ROW = re.compile(r"^\s*[|]")
# "Reads as" is also a printed bold label above the reskin lists.
LABEL = re.compile(r"^[*]{2}Reads as:")

# An atmosphere adverb is only a fault when it modifies something that is not
# physical. "faintly luminous" is a degree of light; "faintly disapproving" is
# a mood attributed to a face. What the adverb modifies is the tell.
PHYSICAL = re.compile(
    r"(faintly|quietly)\s+(luminous|wet|tacky|damp|visible|patterned|steaming|"
    r"striped|ridged|warm|cool|blue|green|glowing|of|from|through|under|against)"
    r"|(moves?|moving|walks?|walking|breathes?|breathing|spoken|speaking|said)"
    r"\s+quietly", re.I)

# THE REGRESSION CORPUS. Every line Dan actually rejected, and the pattern that
# has to keep catching it. Asserted on every run: narrow the patterns as far as
# you like, but the moment one of these gets through, the tool refuses to
# report. A check that can be quietly weakened is not a check.
REJECTED = [
    ("You have seen them asleep.", "addresses the reader"),
    ("you touch everything you look at before you have decided to.",
     "addresses the reader"),
    ("and older than the argument.", "abstract flourish"),
    ("that reads as a helmet nobody can take off", "critic's vocabulary"),
    ("anything trading on being impressive.",
     "abstraction instead of a thing"),
    ("and the only person present who is not surprised by how things turn out.",
     "ranking claim"),
]
# These two are caught by no pattern and never were. They are rules one and
# three - a sentence implying instead of stating, and an abstraction where a
# noun belongs - which are human judgement. Recorded rather than pretended.
UNCAUGHT = ["opened the thing and is holding the piece that came loose.",
            "older on land than either"]


def check(text, scope):
    """Return (why, matched fragment, flattened text) for the first fault."""
    t = " ".join(str(text).split())
    for pid, pat, why in PATS:
        if scope == "rules" and pid in FLAVOUR_ONLY:
            continue
        if pid == "critic" and (TABLE_ROW.match(str(text))
                                or LABEL.match(str(text).strip())):
            continue          # a printed column heading, not prose
        m = pat.search(t)
        if m:
            if pid == "adverb" and PHYSICAL.search(t[max(0, m.start() - 12):
                                                     m.start() + 30]):
                continue      # a degree of a physical property, not a mood
            return why, m.group(0), t
    return None


def self_test():
    """Refuse to report if a line Dan rejected now gets through."""
    bad = []
    for line, why in REJECTED:
        got = check(line, "flavour")
        if not got or got[0] != why:
            bad.append((line, why, got[0] if got else "NOTHING"))
    if bad:
        print("REGRESSION - the checker no longer catches what it was built for:")
        for line, want, got in bad:
            print("   want %-32s got %-20s | %s" % (want, got, line[:60]))
        raise SystemExit("register_check refuses to run")
    return len(REJECTED)


PASSED = self_test()


# ------------------------------------------------------------ the four corpora
rows = []          # (corpus, where, scope, text)


def add(corpus, where, scope, text):
    if text and str(text).strip():
        rows.append((corpus, where, scope, text))


for f in sorted(glob.glob("content/families/*.yaml")):
    g = yaml.safe_load(io.open(f, encoding="utf-8")) or {}
    gid = g.get("id") or os.path.basename(f)
    add("families", "%s/identity" % gid, "flavour", g.get("identity"))
    add("families", "%s/silhouette" % gid, "flavour", g.get("silhouette"))
    add("families", "%s/behaviour" % gid, "flavour",
        (g.get("behaviour") or {}).get("text"))
    for b in (g.get("breeds") or []):
        add("families", "%s/%s/blurb" % (gid, b["name"]), "flavour", b.get("blurb"))
        add("families", "%s/%s/look" % (gid, b["name"]), "flavour", b.get("look"))

for f in sorted(glob.glob("content/classes/*.yaml")):
    d = yaml.safe_load(io.open(f, encoding="utf-8")) or {}
    n = d.get("name") or os.path.basename(f)
    for k in ("blurb", "identity", "summary", "description"):
        add("classes", "%s/%s" % (n, k), "flavour", d.get(k))
    for p in (d.get("picks") or []):
        add("classes", "%s/%s" % (n, p["name"]), "rules", p.get("text"))
        add("classes", "%s/%s.flavour" % (n, p["name"]), "flavour", p.get("flavour"))

# Mutations and equipment: `text` is a rule, everything else is flavour.
FLAV_KEYS = ("blurb", "flavour", "reads_as", "identity", "look", "description")
# artefacts.yaml joined this list the day it was written, rather than
# weeks later like the other three. A corpus this checker does not know
# about is a corpus nobody is checking.
for f in ("content/mutations.yaml", "content/powers.yaml",
          "content/equipment.yaml", "content/artefacts.yaml"):
    if not os.path.exists(f):
        continue
    base = os.path.basename(f)

    def walk(node, name):
        if isinstance(node, dict):
            here = node.get("name") or name
            for k, v in node.items():
                if isinstance(v, str):
                    if k == "text":
                        add(base, "%s:%s" % (base, here), "rules", v)
                    elif k in FLAV_KEYS:
                        add(base, "%s:%s/%s" % (base, here, k), "flavour", v)
                else:
                    walk(v, here)
        elif isinstance(node, list):
            for x in node:
                walk(x, name)

    walk(yaml.safe_load(io.open(f, encoding="utf-8")), "top")

for f in sorted(glob.glob("book/*.md")):
    s = io.open(f, encoding="utf-8").read()
    for para in s.split("\n\n"):
        if not para.strip():
            continue
        ln = s[:s.find(para)].count("\n") + 1
        add("book", "%s:%d" % (os.path.basename(f), ln), "rules", para)

# ------------------------------------------------------------------- the scan
want = "all"
if "--scope" in sys.argv:
    want = sys.argv[sys.argv.index("--scope") + 1]
if want != "all":
    rows = [r for r in rows if r[2] == want]

hits = []
for corpus, where, scope, text in rows:
    r = check(text, scope)
    if r:
        hits.append((corpus, where, scope, r[0], r[1], r[2]))

print("=" * 74)
print("  REGISTER CHECK  -  describe, do not evoke")
print("  self-test: %d rejected lines still caught, %d beyond any pattern"
      % (PASSED, len(UNCAUGHT)))
print("=" * 74)
print("\n  %d fields across 4 corpora, %d carrying an evocative construction (%.1f%%)"
      % (len(rows), len(hits), 100.0 * len(hits) / max(1, len(rows))))

print("\n  by corpus:")
for c in ("families", "classes", "mutations.yaml", "equipment.yaml",
          "artefacts.yaml", "book"):
    tot = sum(1 for r in rows if r[0] == c)
    n = sum(1 for h in hits if h[0] == c)
    if tot:
        print("     %-18s %3d of %4d  (%.0f%%)" % (c, n, tot, 100.0 * n / tot))

print("\n  by fault:")
for why, n in Counter(h[3] for h in hits).most_common():
    print("     %-34s %d" % (why, n))

if "--list" in sys.argv:
    print("\n" + "=" * 74)
    for h in sorted(hits):
        i = h[5].lower().find(h[4].lower())
        print("   %-32s %-24s ...%s"
              % (h[1][:32], h[3], h[5][max(0, i - 40):][:100]))

print("\n" + "=" * 74)
print("  %s" % ("PASS" if not hits else "%d fields to rewrite" % len(hits)))
print("=" * 74)

# Until 2026-09-13 this file reported and then exited 0 whatever it found, so
# check.py could never fail on it. Guarded so that check.py, which imports
# this module for the scenario prose, is not killed by the import.
if __name__ == "__main__" and hits:
    sys.exit(1)
