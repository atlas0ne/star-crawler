# -*- coding: utf-8 -*-
"""The game's engine copy matches its pin, and the pin is not ancient.

THE FAULT THIS EXISTS FOR. A game holds a verbatim copy of Core's ENGINE.md
and vocabulary.yaml and a pin in engine/VERSION. Nothing checked that the
copy was still the pinned version - a session could edit engine/ENGINE.md
in the game by mistake, or copy a newer Core file without moving the pin,
and the book would print rules Core never agreed to. README has said since
the seed that "a check in the game repo asserts the copy matches the pinned
tag". This is that check, five commits late.

WHAT IT DOES. For each pinned file, `git show <pin>:<file>` in Core and
compare. Any difference is a FAIL: fix it with `python tools/sync_core.py
--apply` (which moves the pin too) or by restoring the file. It also counts
Core commits since the pin and prints them as a WARNING - not a failure,
because re-pinning is a decision, but a game twenty commits behind is a
game whose DIVERGENCES.md is describing a Core that no longer exists.

Without Core on this machine (CI, a fresh clone) it says so and passes:
it cannot check, and it will not pretend to.
"""
import io, os, sys, subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corepath

GAME = corepath.HERE
os.chdir(GAME)

if corepath.is_core(GAME):
    print("this is Core; nothing is pinned")
    sys.exit(0)

try:
    CORE = corepath.core_root()
except SystemExit:
    print("Core is not on this machine: pin not checked (not a failure)")
    sys.exit(0)

PINNED = (("ENGINE.md", "engine/ENGINE.md"),
          ("vocabulary/vocabulary.yaml", "engine/vocabulary.yaml"))


def git(*a):
    # bytes, decoded as UTF-8 ourselves: text=True would decode as cp1252 on
    # Windows and every en dash in ENGINE.md would read as a difference
    r = subprocess.run(["git", "-C", CORE] + list(a), capture_output=True)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else None


def norm(s):
    return s.replace("\r\n", "\n").strip()


def main():
    pinf = "engine/VERSION"
    if not os.path.exists(pinf):
        print("FAIL  engine/VERSION missing: this game is not pinned to Core")
        sys.exit(1)
    pin = io.open(pinf, encoding="utf-8").read().strip()
    if git("cat-file", "-e", pin + "^{commit}") is None:
        print("FAIL  pin %s is not a commit in Core (pull Core?)" % pin)
        sys.exit(1)
    bad = 0
    for core_rel, game_rel in PINNED:
        want = git("show", "%s:%s" % (pin, core_rel))
        if want is None:
            print("FAIL  %s does not exist in Core at %s" % (core_rel, pin))
            bad += 1
            continue
        if not os.path.exists(game_rel):
            print("FAIL  %s missing" % game_rel)
            bad += 1
            continue
        have = io.open(game_rel, encoding="utf-8").read()
        if norm(want) != norm(have):
            print("FAIL  %s differs from Core %s:%s - sync_core.py --apply, or restore it"
                  % (game_rel, pin, core_rel))
            bad += 1
        else:
            print("ok    %s == Core %s" % (game_rel, pin))
    n = git("rev-list", "--count", "%s..HEAD" % pin)
    n = int(n) if n else 0
    if n:
        print("WARN  Core is %d commit%s ahead of the pin: python tools/sync_core.py"
              % (n, "" if n == 1 else "s"))
        for line in (git("log", "--oneline", "%s..HEAD" % pin) or "").strip().split("\n")[:8]:
            print("        " + line)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
