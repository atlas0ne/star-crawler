# -*- coding: utf-8 -*-
"""Mail between the games and Core. One directory, one file per message.

WHY. Until 2026-09-13 a game that had something to tell Core wrote an
INBOX_FROM_<GAME>_N.md into Core's root by hand, and Core answered with an
OUTBOX file, and the numbering was whatever the session remembered. Four
games, all talking, and no way to ask "what is still unanswered?". This is
that, made mechanical: `mail/` in Crawler-Core is the one mailbox every
session reads, and every message is a markdown file with front matter that
says who, to whom, about what, and whether it has been answered.

Core is the hub. A game does not write into another game's repo; it writes
to Core, and Core's `mail/` is pushed, so every session on every machine
sees the same thread after a pull.

Usage (from Core or from any game that copied tools/):

  python tools/mail.py list [--open] [--to NAME] [--from NAME]
  python tools/mail.py read N
  python tools/mail.py send --to a,b --title "..." [--re N] [--body FILE]
  python tools/mail.py close N            mark N answered without a reply
  python tools/mail.py check              every file parses; used by CI

`send` with no --body reads the body from stdin. --from defaults to this
repo's name (project.yaml `repository`, or "crawler-core" inside Core).
Add --commit to git-commit the new file in Core and push it in the same
step (--no-push to skip the push). list/read/send pull Core first, so what
you read is what the hub has; MAIL_NO_PULL=1 skips that when offline.

Names: crawler-core, star-crawler, project-mutant, stone-and-spear, ccag.
"""
import io, os, re, sys, glob, datetime, subprocess

# Messages carry en dashes and a Unicode minus; a Windows console is cp1252
# and `read` crashed on message #9 (mail #9, 2026-09-13).
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corepath

CORE = corepath.core_root()
BOX = os.path.join(CORE, "mail")


def pull():
    """Core is read through git. A stale checkout is stale mail; pull first.
    Quiet on success, one line on failure, never fatal (offline is allowed)."""
    if os.environ.get("MAIL_NO_PULL"):
        return
    r = subprocess.run(["git", "-C", CORE, "pull", "-q", "--ff-only"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("(could not pull Core: %s)" % (r.stderr.strip().split("\n")[-1] if r.stderr else "?"))


def push():
    r = subprocess.run(["git", "-C", CORE, "push", "-q"], capture_output=True, text=True)
    if r.returncode != 0:
        print("PUSH FAILED - the other sessions cannot see this until you push Core:")
        print("   " + (r.stderr.strip().split("\n")[-1] if r.stderr else "?"))
    else:
        print("pushed")


def open_for(name):
    """Open messages addressed to `name`. Used by check.py so the gate says so."""
    return [m for m in load() if m.get("status") == "open" and name in m["to"]]
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse(path):
    s = io.open(path, encoding="utf-8").read()
    m = FM.match(s)
    if not m:
        raise ValueError("%s: no front matter" % path)
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    meta["to"] = [x.strip() for x in meta.get("to", "").split(",") if x.strip()]
    meta["id"] = int(meta["id"])
    meta["path"] = path
    meta["body"] = s[m.end():]
    return meta


def load():
    msgs = [parse(f) for f in sorted(glob.glob(os.path.join(BOX, "[0-9]*.md")))]
    return sorted(msgs, key=lambda m: m["id"])


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]


def write(meta, body):
    keys = ["id", "from", "to", "date", "title", "re", "status"]
    fm = ["---"]
    for k in keys:
        if k in meta and meta[k] not in (None, "", []):
            v = ", ".join(meta[k]) if isinstance(meta[k], list) else meta[k]
            fm.append("%s: %s" % (k, v))
    fm.append("---")
    io.open(meta["path"], "w", encoding="utf-8", newline="\n").write(
        "\n".join(fm) + "\n\n" + body.strip() + "\n")


def cmd_list(args):
    pull()
    msgs = load()
    want_open = "--open" in args
    to = opt(args, "--to")
    frm = opt(args, "--from")
    rows = [m for m in msgs
            if (not want_open or m.get("status") == "open")
            and (not to or to in m["to"])
            and (not frm or m["from"] == frm)]
    for m in rows:
        print("%3d  %-8s %-14s -> %-28s %s%s" % (
            m["id"], m.get("status", "?"), m["from"], ", ".join(m["to"]),
            m.get("title", ""), ("  (re %s)" % m["re"]) if m.get("re") else ""))
    print("%d message%s" % (len(rows), "" if len(rows) == 1 else "s"))


def find(n):
    for m in load():
        if m["id"] == int(n):
            return m
    sys.exit("no message %s" % n)


def cmd_read(args):
    pull()
    m = find(args[0])
    print(io.open(m["path"], encoding="utf-8").read())


def opt(args, flag, default=None):
    if flag in args:
        return args[args.index(flag) + 1]
    return default


def cmd_send(args):
    to = opt(args, "--to")
    title = opt(args, "--title")
    if not to or not title:
        sys.exit("send needs --to and --title")
    frm = opt(args, "--from", corepath.game_name())
    body_file = opt(args, "--body")
    body = io.open(body_file, encoding="utf-8").read() if body_file \
        else sys.stdin.read()
    if not body.strip():
        sys.exit("empty body")
    pull()                      # so the id is the next one on the hub, not on a stale copy
    msgs = load()
    n = (msgs[-1]["id"] + 1) if msgs else 1
    tos = [x.strip() for x in to.split(",")]
    meta = {
        "id": n, "from": frm, "to": tos,
        "date": datetime.date.today().isoformat(),
        "title": title, "status": "open",
        "path": os.path.join(BOX, "%03d-%s-to-%s-%s.md"
                             % (n, slug(frm), slug("-".join(tos)), slug(title))),
    }
    re_n = opt(args, "--re")
    if re_n:
        meta["re"] = str(int(re_n))
        parent = find(re_n)
        parent["status"] = "answered"
        write(parent, parent["body"])
    write(meta, body)
    rel = os.path.relpath(meta["path"], CORE).replace("\\", "/")
    print("wrote %s" % rel)
    if "--commit" in args:
        subprocess.check_call(["git", "-C", CORE, "add", "mail"])
        subprocess.check_call(["git", "-C", CORE, "commit", "-q", "-m",
                               "mail #%d: %s -> %s: %s" % (n, frm, ", ".join(tos), title)])
        print("committed in %s" % CORE)
        if "--no-push" not in args:
            push()
    else:
        print("commit it in Core: git -C \"%s\" add mail && git -C \"%s\" commit"
              % (CORE, CORE))


def cmd_close(args):
    pull()
    m = find(args[0])
    m["status"] = "answered"
    write(m, m["body"])
    print("closed #%d" % m["id"])


def cmd_check(args):
    bad = 0
    seen = set()
    for f in sorted(glob.glob(os.path.join(BOX, "[0-9]*.md"))):
        try:
            m = parse(f)
        except Exception as e:
            print("BAD  %s: %s" % (os.path.basename(f), e))
            bad += 1
            continue
        for k in ("from", "to", "date", "title", "status"):
            if not m.get(k):
                print("BAD  %s: missing %s" % (os.path.basename(f), k))
                bad += 1
        if m.get("status") not in ("open", "answered"):
            print("BAD  %s: status must be open|answered" % os.path.basename(f))
            bad += 1
        if m["id"] in seen:
            print("BAD  %s: duplicate id %d" % (os.path.basename(f), m["id"]))
            bad += 1
        seen.add(m["id"])
        if m.get("re") and int(m["re"]) not in seen:
            print("BAD  %s: re %s is not an earlier message" % (os.path.basename(f), m["re"]))
            bad += 1
    n_open = sum(1 for m in load() if m.get("status") == "open")
    print("%d messages, %d open, %d malformed" % (len(seen), n_open, bad))
    sys.exit(1 if bad else 0)


CMDS = {"list": cmd_list, "read": cmd_read, "send": cmd_send,
        "close": cmd_close, "check": cmd_check}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        print(__doc__)
        sys.exit(2)
    CMDS[sys.argv[1]](sys.argv[2:])
