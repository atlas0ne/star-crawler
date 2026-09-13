# Star Crawler

**Draft stage — nothing about character creation is decided.** See `decisions/DECISIONS.md`.

**A space-opera OSR game on the [Crawler Core](https://github.com/atlas0ne/Crawler-Core)
engine.** Blasters, starships, a fallen order of mystic knights and the empire that
hunted them. Same rules as Stone & Spear and Project Mutant: a player who has rolled in
one has rolled in all of them.

*Version 0.1.0-scaffold. Nothing here has been played.*

## Where things are

| | |
|---|---|
| `engine/` | Crawler Core, copied verbatim at the commit in `VERSION`. Never edited here. `DIVERGENCES.md` is what this game switches on and off. |
| `book/` | The rules. Prose, hand-written, with front matter. |
| `content/` | The data: species, classes, Force powers, gear, ships, monsters. |
| `tools/` | The checks. `python tools/check.py` is the gate. |
| `decisions/` | Every non-obvious call, with the reason. Read before arguing. |

## The five decisions

The engine leaves a new game five things to decide. Star Crawler's answers, all
proposed and unplayed, are in `decisions/DECISIONS.md`: species are fixed, the Force is
Project Mutant's Strains rolled not bought, the galaxy is Clean 0, the era is the Dark
Times, the six Classes stay, and the never-list does not bend.

## Working on it

Read `CLAUDE.md`. Rules are prose, content is data, and the check runs before every commit.

```bash
python tools/check.py
```
