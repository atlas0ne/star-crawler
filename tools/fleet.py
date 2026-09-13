# -*- coding: utf-8 -*-
"""Every game on the engine, in one screen: pin, drift, gate, mail.

Run from Core. Reads games.yaml, and for each game that is checked out on
this machine: the Core commit it pins, how many Core commits it is behind,
whether its engine files still match that pin, whether its gate passes, and
how many open messages are addressed to it. A game that is not on this
machine gets its pin from GitHub if `gh` is available, and "not here" if not.

  python tools/fleet.py            the table
  python tools/fleet.py --gate     also run each game's check.py (slow)

This is the view Core did not have on 2026-09-13, when finding the games
meant grepping a drive.
"""
import io, os, sys, glob, subprocess, yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corepath, mail

CORE = corepath.core_root()
os.chdir(CORE)


def git(*a, cwd=CORE):
    try:
        return subprocess.check_output(["git", "-C", cwd] + list(a),
                                       stderr=subprocess.DEVNULL).decode("utf-8", "replace").strip()
    except Exception:
        return None


def behind(pin):
    n = git("rev-list", "--count", "%s..HEAD" % pin)
    return int(n) if n is not None else None


def drift(game_path, pin):
    """Which of the pinned files differ from Core at the pin."""
    bad = []
    for core_rel, game_rel in (("ENGINE.md", "engine/ENGINE.md"),
                               ("vocabulary/vocabulary.yaml", "engine/vocabulary.yaml")):
        want = git("show", "%s:%s" % (pin, core_rel))
        p = os.path.join(game_path, game_rel)
        if want is None or not os.path.exists(p):
            bad.append(game_rel + " missing")
            continue
        have = io.open(p, encoding="utf-8").read()
        if want.replace("\r\n", "\n").strip() != have.replace("\r\n", "\n").strip():
            bad.append(game_rel)
    return bad


def gate(game_path):
    r = subprocess.run([sys.executable, os.path.join(game_path, "tools", "check.py")],
                       capture_output=True, text=True, cwd=game_path,
                       env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    last = [l for l in r.stdout.strip().split("\n") if l.strip()]
    return ("OK " if r.returncode == 0 else "FAIL") + " " + (last[-1] if last else "")


def main():
    games = (yaml.safe_load(io.open("games.yaml", encoding="utf-8")) or {}).get("games") or []
    msgs = mail.load()
    head = git("rev-parse", "--short", "HEAD")
    print("Core %s   %s" % (head, git("log", "-1", "--format=%s")[:50]))
    print()
    print("%-16s %-9s %-8s %-7s %-22s %s" % ("game", "status", "pin", "behind", "drift", "open mail"))
    for g in games:
        path = g.get("path") or ""
        name = g["name"]
        open_to = [m["id"] for m in msgs if m.get("status") == "open" and name in m["to"]]
        open_from = [m["id"] for m in msgs if m.get("status") == "open" and m["from"] == name]
        mail_s = "to it: %s" % (",".join("#%d" % i for i in open_to) or "-")
        if open_from:
            mail_s += "  from it: %s" % ",".join("#%d" % i for i in open_from)
        if not os.path.isdir(path):
            print("%-16s %-9s %-8s %-7s %-22s %s" % (name, g.get("status", ""), "?", "", "not on this machine", mail_s))
            continue
        pinf = os.path.join(path, "engine", "VERSION")
        pin = io.open(pinf, encoding="utf-8").read().strip() if os.path.exists(pinf) else None
        if not pin:
            print("%-16s %-9s %-8s %-7s %-22s %s" % (name, g.get("status", ""), "none", "", "not on Core", mail_s))
            continue
        b = behind(pin)
        d = drift(path, pin)
        row = "%-16s %-9s %-8s %-7s %-22s %s" % (
            name, g.get("status", ""), pin,
            "-" if b is None else str(b),
            "clean" if not d else ", ".join(d), mail_s)
        print(row)
        if "--gate" in sys.argv:
            print("%-16s   gate: %s" % ("", gate(path)))
    print()
    print("behind = Core commits since the pin; run tools/sync_core.py in the game.")
    print("drift  = the game's engine copy no longer matches its pin: a bug in the game.")


if __name__ == "__main__":
    main()
