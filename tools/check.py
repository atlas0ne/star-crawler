# -*- coding: utf-8 -*-
"""Run every check, in order, and say which failed.

There are fourteen checks and for weeks they have been run as a shell loop
typed out by hand. This is that loop, kept once, with two things the loop
could not do: it runs the scenario folder through the checks that apply to
prose (citations, register), and it exits non-zero if anything failed, so it
can gate a commit.

Usage:  python tools/check.py            everything
        python tools/check.py --quick    the fast structural ones only
"""
import io
import glob
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
PY = sys.executable
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")

CHECKS = [
    "validate", "register_check", "shape_check", "cost_check", "free_check",
    "complexity_check", "structure_check", "rules_check", "xref",
    "lint_structure", "mutation_audit", "counts_check", "bestiary_check",
    "citation_check",
]
QUICK = ["validate", "structure_check", "xref", "lint_structure",
         "counts_check", "citation_check"]


# Core ships five of these; a game adds the rest as it writes them. A name with
# no file is not a failure, it is a check this game has not written yet - but
# it is printed, so the gap stays visible.
def present(names):
    have, missing = [], []
    for n in names:
        (have if os.path.exists(os.path.join("tools", n + ".py")) else missing).append(n)
    return have, missing


def run_tool(name):
    r = subprocess.run([PY, os.path.join("tools", name + ".py")],
                       capture_output=True, text=True, env=ENV)
    return r.returncode == 0, (r.stdout + r.stderr)


def scenario_prose():
    """The scenario folder is prose that cites the book. It gets the two
    checks that read prose: every citation must resolve, and the register
    must hold. Returns a list of (file, message)."""
    sys.path.insert(0, "tools")
    import citation_check as C
    import register_check as R
    secs = C.sections()
    bad = []
    for f in sorted(glob.glob("scenario/*.md")) + sorted(glob.glob("genre/*.md")):
        txt = io.open(f, encoding="utf-8").read()
        for _, why in C.run([(f, txt)], secs):
            bad.append((f, why))
        for i, line in enumerate(txt.split("\n"), 1):
            hit = R.check(line, "rules")
            if hit:
                bad.append((f, "line %d: %s - %s" % (i, hit[0], line.strip()[:60])))
    return bad


def main():
    names, missing = present(QUICK if "--quick" in sys.argv else CHECKS)
    if missing:
        print("  not yet written: " + ", ".join(missing))
    failed = []
    for n in names:
        ok, out = run_tool(n)
        print("  %-18s %s" % (n, "OK" if ok else "FAIL"))
        if not ok:
            failed.append((n, out))
    # register_check prints its own banner when imported; swallow it here
    _o, sys.stdout = sys.stdout, io.StringIO()
    try:
        prose = scenario_prose()
    finally:
        sys.stdout = _o
    print("  %-18s %s" % ("scenario prose", "OK" if not prose else "FAIL"))
    for f, why in prose:
        print("      %s: %s" % (f, why))
    print()
    if failed:
        for n, out in failed:
            print("=" * 66)
            print(n)
            print("=" * 66)
            print("\n".join(out.strip().split("\n")[-12:]))
    total = len(names) + 1
    bad = len(failed) + (1 if prose else 0)
    print("%d of %d passed" % (total - bad, total))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
