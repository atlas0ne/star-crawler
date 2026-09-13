# -*- coding: utf-8 -*-
"""Where Crawler-Core is on this machine, and which game this is.

Every game copies tools/ from Core, so a tool can be running inside Core or
inside any game. Two questions, answered once here:

  core_root()  - the Crawler-Core checkout. Looked for, in order: the
                 CRAWLER_CORE environment variable; a sibling directory named
                 Crawler-Core; a path written in ~/.crawler-core; the current
                 repo itself if it IS Core (has ENGINE.md at the root).
  game_name()  - the slug this repo signs messages with: the last path segment
                 of `repository:` in project.yaml, lower-cased, else the
                 directory name. Core is "crawler-core".
"""
import io, os, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def is_core(path):
    return os.path.exists(os.path.join(path, "ENGINE.md")) and \
        os.path.isdir(os.path.join(path, "vocabulary"))


def core_root():
    cands = []
    if os.environ.get("CRAWLER_CORE"):
        cands.append(os.environ["CRAWLER_CORE"])
    if is_core(HERE):
        cands.append(HERE)
    cands.append(os.path.join(os.path.dirname(HERE), "Crawler-Core"))
    rc = os.path.expanduser("~/.crawler-core")
    if os.path.exists(rc):
        cands.append(io.open(rc, encoding="utf-8").read().strip())
    for c in cands:
        if c and is_core(c):
            return os.path.abspath(c)
    sys.exit("cannot find Crawler-Core: set CRAWLER_CORE, or write its path "
             "to ~/.crawler-core, or check it out beside this repo")


def game_name(root=HERE):
    if is_core(root):
        return "crawler-core"
    p = os.path.join(root, "project.yaml")
    if os.path.exists(p):
        import yaml
        d = yaml.safe_load(io.open(p, encoding="utf-8")) or {}
        repo = str(d.get("repository") or "").rstrip("/")
        if repo:
            return repo.split("/")[-1].lower().replace(".git", "")
    return os.path.basename(root).lower().replace(" ", "-")


if __name__ == "__main__":
    print("core:", core_root())
    print("game:", game_name())
