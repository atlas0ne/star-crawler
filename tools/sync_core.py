# -*- coding: utf-8 -*-
"""Bring a game up to date with Crawler-Core, and say exactly what moved.

A game holds three things it does not own: `engine/ENGINE.md`,
`engine/vocabulary.yaml`, and every tool Core ships in `tools/`. It pins the
Core commit in `engine/VERSION`. Doing this by hand is `cp` plus remembering;
this is the same `cp` that also tells you what changed, refuses to touch a
file the game owns (`game_schema.py`, `generate.py`, `validate.py`, anything
Core does not ship), and writes the pin.

Usage, from the game's root:

  python tools/sync_core.py            show what would change
  python tools/sync_core.py --apply    copy, and write engine/VERSION

After --apply: read the diff of ENGINE.md against your DIVERGENCES.md, run
`python tools/check.py`, and commit with the new Core hash in the message.
Run inside Core itself it does nothing, on purpose.
"""
import io, os, sys, glob, filecmp, shutil, subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corepath

GAME = corepath.HERE
CORE = corepath.core_root()

if corepath.is_core(GAME):
    sys.exit("this is Crawler-Core; nothing to sync into")

# SELF-UPDATE FIRST. A fix to this file cannot help a game whose copy
# predates the fix (mail #8: the old copy overwrote check.py; the new one
# knew not to, and no game had the new one). So: pull Core, refresh this
# file and corepath.py from it, and if this file changed, re-run as the new
# version before touching anything else.
if "--no-self-update" not in sys.argv:
    subprocess.run(["git", "-C", CORE, "pull", "-q", "--ff-only"],
                   capture_output=True)
    _me = os.path.abspath(__file__)
    _changed = False
    for _f in ("sync_core.py", "corepath.py"):
        _src = os.path.join(CORE, "tools", _f)
        _dst = os.path.join(GAME, "tools", _f)
        if os.path.exists(_src) and not (os.path.exists(_dst)
                                         and filecmp.cmp(_src, _dst, shallow=False)):
            shutil.copyfile(_src, _dst)
            print("  updated  tools/%s (from Core, before anything else)" % _f)
            _changed = True
    if _changed:
        sys.exit(subprocess.call([sys.executable, _me, "--no-self-update"] + sys.argv[1:]))

PAIRS = [(os.path.join(CORE, "ENGINE.md"), os.path.join(GAME, "engine", "ENGINE.md")),
         (os.path.join(CORE, "vocabulary", "vocabulary.yaml"),
          os.path.join(GAME, "engine", "vocabulary.yaml"))]
CORE_ONLY = {"new_game.py", "fleet.py"}   # run inside Core; a game has no use for them

# A game may keep its own copy of a Core-shipped tool. It says so in
# tools/checks.yaml under `keep:`; those files are reported and never copied.
# (mail #8: the sync overwrote Stone & Spear's check.py and skirmish.py.)
KEEP = set()
_cy = os.path.join(GAME, "tools", "checks.yaml")
if os.path.exists(_cy):
    import yaml
    KEEP = set((yaml.safe_load(io.open(_cy, encoding="utf-8")) or {}).get("keep") or [])

for f in sorted(glob.glob(os.path.join(CORE, "tools", "*.py"))):
    if os.path.basename(f) not in CORE_ONLY:
        PAIRS.append((f, os.path.join(GAME, "tools", os.path.basename(f))))


def core_hash():
    return subprocess.check_output(["git", "-C", CORE, "rev-parse", "--short", "HEAD"]
                                   ).decode().strip()


def main():
    apply = "--apply" in sys.argv
    pin = os.path.join(GAME, "engine", "VERSION")
    old = io.open(pin, encoding="utf-8").read().strip() if os.path.exists(pin) else "(none)"
    new = core_hash()
    print("Core %s -> %s" % (old, new))
    changed = 0
    for src, dst in PAIRS:
        rel = os.path.relpath(dst, GAME).replace("\\", "/")
        if os.path.exists(dst) and filecmp.cmp(src, dst, shallow=False):
            continue
        if os.path.basename(dst) in KEEP:
            print("  %-8s %s  (game-owned per tools/checks.yaml; not copied)" % ("kept", rel))
            continue
        changed += 1
        print("  %-8s %s" % ("new" if not os.path.exists(dst) else "changed", rel))
        if apply:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)
    if apply:
        os.makedirs(os.path.dirname(pin), exist_ok=True)
        io.open(pin, "w", encoding="utf-8", newline="\n").write(new + "\n")
        print("%d file%s copied, engine/VERSION = %s" % (changed, "" if changed == 1 else "s", new))
    else:
        print("%d file%s would change; --apply to do it" % (changed, "" if changed == 1 else "s"))


if __name__ == "__main__":
    main()
