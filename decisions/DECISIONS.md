---
title: "Decisions"
status: SCAFFOLD
---

# DECISIONS

Settled calls, with the reason. **Check here before relitigating anything.**

Format: what was decided, when, why, and what it blocks or unblocks. A decision
marked *proposed* is a starting position awaiting Dan's call; it is written down
so the alternative is argued against something, not against nothing.

---

## 2026-09-13 — The five decisions every game on Core has to make

`STARTING_A_NEW_GAME.md` says a new game decides five things and nothing else at
first. These are the five, for Star Crawler. All *proposed*, all SCAFFOLD.

### 1. The origin system — what does a player spend points on?

**Proposed:** Three layers, inherited from Project Mutant with the names changed.

| Layer | Mutant has | Star Crawler has | Bought or rolled |
|---|---|---|---|
| Anatomy | Family / Breed / Variant, bought with Biogen | **Species** — a fixed pool, no currency | fixed by species |
| Training | six attribute Classes, three Picks at L1 | the same six Classes | chosen |
| Strangeness | twelve Strains, 240 perks, **rolled** | **the Force** — the Strains re-read, **rolled** | rolled, never bought |

**Why:** The thing that makes the genre is not the ship or the blaster, it is that
some people are *touched* and most are not, and the ones who are did not choose
it. That is exactly Mutant's mutation model: rolled, not bought, with a cost on
every perk. A Force power is a Strain perk with a `reads_as` of "the Force". No
Force point pool, no light/dark meter as a resource — the d4 cost table on each
perk is what the dark side is.

Species is fixed rather than point-bought because the source material's aliens
are *types*, not builds: a player picks the big hairy one, they do not tune it.
That removes the whole Biogen economy from day one. What is lost is Mutant's
enormous build variety; what is gained is a character in five minutes, which the
genre wants more.

**What this blocks:** no `cost_check`, `free_check` or ladders until a currency
exists — and one may never. `mutation_audit` is needed unchanged.

### 2. The Dose — how strange is the galaxy?

**Proposed:** **Clean 0** by default. Nobody rolls on the Strain table at
character creation unless they take the *Sensitive* background, and then they
roll once. The referee may raise it to Standard 1 for an era where the knights
still walk around.

**Why:** The era below is the one where the Force is a rumour. A party of six
where one is Sensitive matches the fiction; a party where all six are is a
different, later genre. The Dose is the one dial, and it is set low so it can be
turned up.

### 3. The setting — one, named or nameless?

**Proposed:** One era, **the Dark Times** — the years after the old order fell
and before the rebellion was more than a rumour. The empire is the dungeon. The
knights are dead, hunted, or hiding. Player characters are the people at the
edge: smugglers, deserters, bounty hunters, the last apprentice.

**The names are placeholders — Dan's call, 2026-09-13.** Star Wars names are
used as-is while the game is built (the same ruling as Mutant's placeholder
Class names: they read well and nothing is gained by inventing now). Dan's
own names replace them before release. Every placeholder is logged in
`content/placeholders.yaml` on first use so the rename is a lookup, not a
hunt; the check that fails on any placeholder in a printed field is written
now and switched on at the rename pass. Mutant's `reads_as` field runs the
other way here: it will carry the *original* placeholder once the real name
lands, so a reader who knows the source can still find the thing.

**Why this era:** it is the one where OSR lethality, scarce magic, and a
crawl-shaped structure (an imperial facility *is* a dungeon) all fit without
bending anything. Modules can add the Clone Wars or the High Republic later.

### 4. Classes — are there any?

**Proposed:** **Yes, Mutant's six**, unchanged: Strong, Fast, Tough, Smart,
Wise, Charismatic, three Picks at first level. The Force is **not** a class.
A knight is a Wise (or any) character who rolled Sensitive.

**Why:** Making the knight a class puts the whole game's magic behind one door
and makes every other class the one that is not the knight. Making it a Strain
means a Charismatic smuggler can turn out to be Sensitive, which is the better
story and the one the source tells. It also means the Class layer is already
tested — Mutant's — and this game does not have to re-derive it.

### 5. Does the never-list bend?

**No.** Deflecting a blaster bolt is a *resistance* on the ladder. A mind trick
is a save, target 15, and a natural 20 shrugs it off. A cloaked ship is a bonus
to a stealth check, not undetectability. Nobody comes back from 0 hit points
without a rule that says so and prices it. If a power cannot be written as one
of the 55 shapes in `engine/vocabulary.yaml`, it is not a power in this engine.

**Why:** the never-list is what keeps the game OSR. A character who cannot be hit
is not a character in a game with a round.

---

## 2026-09-13 — Three Core tools were wrong on an empty book

**Decided:** Fixed here, to be sent upstream to Crawler-Core.

* `citation_check.py` self-tested against the *real* book, expecting "Rests
  Rough" in section 6.5 — Project Mutant's content, baked into a Core tool. It
  refused to run on any book that was not Mutant's. Now self-tests against a
  synthetic fixture. Proven to fire when the fixture is broken.
* `register_check.py` hardcoded `content/mutations.yaml` and crashed if absent.
  Now skips content files that do not exist, and knows `powers.yaml`.
* `check.py` listed fourteen checks; Core ships five. Now runs the ones that
  exist and prints the ones it is still waiting for.
* `register_check.py` **never set an exit code.** It printed "N fields to
  rewrite" and exited 0, so `check.py` could not fail on it — in Mutant too.
  A check that never fails is not a check. Now exits 1 on any hit (guarded
  by `__main__`, because `check.py` imports the module). Proven: a probe
  chapter with "older than the argument" now takes the gate to 4 of 5.
* `register_check.py` and `counts_check.py` indexed `g["id"]`, `g["breeds"]`,
  `d["name"]` on any file under `content/families/` and `content/classes/` —
  Mutant's schema, hard-crashing on any other. Now `.get()` with a filename
  fallback. **What this hides:** a species file with no `breeds` counts zero
  Breeds silently. This game's own `validate.py` owns the schema; until it
  exists, the counts check only counts Mutant-shaped data.

Every check was then proven to fail on a probe chapter — two H1s and a
skipped level (`lint_structure`), a citation to a section that does not
exist (`citation_check`), an evocative construction (`register_check`) —
and the gate returned 1 each time. `skirmish.py` imports `generate`, which
does not exist yet; it is not in the gate and stays dead until the generator
is written, per the first-week plan.

**Why it matters:** `STARTING_A_NEW_GAME.md` §"first hour" step 5 says the gate
should pass on an empty book. It did not, three ways. A game that started
writing content first would have had a gate that never ran.

---

## 2026-09-13 — Repository structure and pin

**Decided:** `engine/` pinned to Crawler-Core `4c37d48` (0.1.0-draft).
`book/`, `content/`, `tools/`, `decisions/` per the recipe. Version
`0.1.0-scaffold` until played.
