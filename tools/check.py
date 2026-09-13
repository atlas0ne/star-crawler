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

# THE LIST IS THE GAME'S. Core ships the runner; the game owns which checks
# run, in tools/checks.yaml:
#
#     checks: [validate, banned, shape_check, lint_structure, ...]
#     quick:  [lint_structure, xref, banned]
#
# Without that file the runner falls back to the list below - the four Core
# checks plus the names Mutant proved a game ends up writing. Until 2026-09-13
# the list was hard-coded here, and syncing Core's runner into Stone & Spear
# would have silently dropped its `banned` check from the run (mail #8). A
# check that stops running looks exactly like a check that passes.
DEFAULT_CHECKS = [
    "pin_check", "validate", "register_check", "shape_check", "cost_check", "free_check",
    "complexity_check", "structure_check", "rules_check", "xref",
    "lint_structure", "mutation_audit", "counts_check", "bestiary_check",
    "citation_check",
]
DEFAULT_QUICK = ["pin_check", "validate", "structure_check", "xref", "lint_structure",
                 "counts_check", "citation_check"]


def check_lists():
    p = os.path.join("tools", "checks.yaml")
    if not os.path.exists(p):
        return DEFAULT_CHECKS, DEFAULT_QUICK
    import yaml
    d = yaml.safe_load(io.open(p, encoding="utf-8")) or {}
    checks = list(d.get("checks") or DEFAULT_CHECKS)
    quick = list(d.get("quick") or [c for c in DEFAULT_QUICK if c in checks])
    return checks, quick


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
    checks, quick = check_lists()
    names, missing = present(quick if "--quick" in sys.argv else checks)
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
    # The gate runs before every commit, so it is where mail gets noticed.
    # Not a failure: a message is work, not a fault.
    try:
        import corepath, mail
        me = corepath.game_name()
        waiting = mail.open_for(me)
        if waiting:
            print("\n  MAIL: %d open message%s for %s - python tools/mail.py list --open --to %s"
                  % (len(waiting), "" if len(waiting) == 1 else "s", me, me))
            for m in waiting:
                print("     #%d  from %-16s %s" % (m["id"], m["from"], m.get("title", "")[:60]))
    except SystemExit:
        pass                    # no Core on this machine (CI): nothing to report
    except Exception as e:
        print("  (mail check skipped: %s)" % e)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
