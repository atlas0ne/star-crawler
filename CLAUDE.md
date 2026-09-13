# Star Crawler — working conventions

A space-opera OSR game on the Crawler Core engine. Read `README.md` for what it
is; this file is how to work on it. **Everything here is a standing rule, not a
suggestion.** It is Project Mutant's `CLAUDE.md` with the names changed, on
purpose: the method is inherited, only the game is new.

## The one architectural rule

**Rules are prose. Content is data.**

`book/*.md` is hand-written chapters with YAML front matter. `content/*.yaml` is
machine-readable species, classes, Force powers, equipment, starships and
monsters. If you find yourself typing something in two places, it is data you
have not extracted yet.

## The engine is not ours

`engine/ENGINE.md` and `engine/vocabulary.yaml` are **copied verbatim** from
Crawler-Core at the commit in `engine/VERSION`. Never edit them here. A rule
this game does differently goes in `engine/DIVERGENCES.md` with the reason, or
it is a bug. A change the engine itself needs goes to the Crawler-Core repo.

## Never edit generated files

Every `*.md` in the root is **generated** once the builders exist. Edit
`content/` or `book/`, then run the builders.

```bash
python tools/check.py             # every check that exists; exit 1 on any failure
python tools/check.py --quick     # the structural ones
```

**The check is the gate.** Run `python tools/check.py` before every commit;
the commit message says "N checks pass" and it should be true.

## Validation discipline

* **Errors must be zero at all times.** Warnings may sit indefinitely.
* **A new check must be proven to fail before it is trusted.** Break something
  deliberately, watch it fire, then fix it. Three Core tools were silently
  wrong on this game's first empty run — see `decisions/DECISIONS.md`.
* **A check with an exemption hides a category.** List what each one hides.
* **Anything found by eye should become a check**, or it will be found by eye
  again.

## Writing traits

* **Mechanical text is terse.** Say what it does and stop. Flavour in a
  mechanical field hides duplication from the validator.
* Flavour lives in `identity`, `blurb`, `reads_as` and `behaviour` — nowhere else.
* **Every trait has a `shape` from `engine/vocabulary.yaml`.** If it cannot be
  written as one of the 55, it is a referee ruling, not a trait. That includes
  every Force power and every piece of Jedi fiction: no automatic hits, no broad
  immunity, no permanent undetectability, no undo. A lightsaber that deflects
  blaster bolts is a *resistance*, priced.
* **Cost attaches to shapes, not to traits.**
* **Names are unique unless the text is identical.**

## The IP rule

The genre is Star Wars. The published text will not be. **Star Wars names are
placeholders** — Wookiee, Jedi, Empire, lightsaber — used freely in `book/` and
`content/` while the game is being built, because writing "the big hairy one"
for six months helps nobody. Dan's own names replace them before anything
leaves the repo. Every placeholder goes in `content/placeholders.yaml` as it is
first used, with its eventual `reads_as` blank until the real name exists;
the check that reads that list and fails on any placeholder in a printed
field is the release gate, and it is switched off until the rename pass.

## Player-facing vs internal text

The generators print `identity`, `blurb`, trait `text`, `behaviour` and any
`player_note`. They **never** print `note`, `design_note`, `reads_as`, `open`
or `changelog`.

## Shell scripting

**Do not write Python or a regex through a shell heredoc.** Write the script
to a file and run the file. **Batch edits report per item and do not abort on
the first miss.**

## Recording decisions

Every non-obvious decision goes in `decisions/DECISIONS.md` with the reasoning.
Reversals are marked `[CORRECTED]`. Confidence tiers on every chapter:
`TESTED` / `REASONED` / `SCAFFOLD`.

## Versioning

`project.yaml` is the single source of metadata. MAJOR stays 0 until the game
has been played. MINOR when a playtester would have to re-learn a rule. PATCH
for content.
