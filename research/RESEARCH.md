---
title: "Star Crawler — Research"
subtitle: "How other games do races, droids, the Force, classes and generators"
author: [Dan Amos]
date: 2026-09-26
lang: en-GB
status: SCAFFOLD
version: 0.1.0-scaffold
generated_by: research/tools/build_research.py
source_commit: 4d26f19
---

# Star Crawler — Research

**Generated. Do not edit.** Edit the files in `research/` and run
`python research/tools/build_research.py`.

**Draft stage. Nothing here is a decision.** Every numbered finding at the end
of a part is a *reading* — what the evidence appears to support — not a ruling.
Star Crawler's own draft positions live in `decisions/DECISIONS.md` and are
also not decisions. Where a claim has a number, the number came from a corpus
in `research/corpora/` and can be recounted; where it does not, it is a reading
of a book and should be argued with.

Nothing in this document is Star Crawler's design. It is eleven other games'.

**Part 1 is the one to read.** It reduces all of it to the choices actually in
front of the game, each with what it costs, who else does it, and a
recommendation to argue with. Parts 2-6 are the evidence behind those
choices, to skim or to check. You can answer part 1 with a list of letters.

## Contents

1. The options — read this part
2. Races
3. Droids
4. The Force
5. Classes
6. Generators: planets, ships, droids
7. Appendix A: the sources
8. Appendix B: the research programme
9. Appendix C: what has been extracted

---

## 1. The options — read this part

*Source: `research/Options.md`*

*Everything the research turned up, reduced to the choices actually in front of
Star Crawler. Nothing here is decided. For each question: the real options, what
each one costs and buys, who else does it, and a recommendation you can disagree
with. The evidence for every claim is in the parts that follow.*

*Read this part; skim the rest. Written 2026-09-26, draft stage.*

**How to use it:** each option has a letter. You can answer this document with
nothing but letters — "1B, 2A, 3C…" — and that is enough for me to start building.
Where you disagree with a recommendation, the reason matters more than the letter.

---

### 1. What is a species, mechanically?

The single biggest decision, because everything else hangs off it.

**Option A — the fixed package.** A species is a small printed block: an attribute
shift, size, speed, one or two abilities, a flaw, a behaviour line. Player picks
one and moves on.
*Buys:* a character in five minutes; matches every licensed Star Wars game; the
referee's homemade species is the same shape as the book's.
*Costs:* every Wookiee is identical; no build variety at the species layer.
*Who:* WEG (449 species, median 1–2 abilities), Saga (14+), FFG, SW5e, Star
Frontiers, Star Adventurer.

**Option B — the package plus a small pool.** The fixed block, plus 2–3 points to
spend inside a short species-specific list (a Wookiee picks two of: climb, rage,
bowcaster familiarity, thick hide…).
*Buys:* two Wookiees differ; keeps chargen under ten minutes; the pool is where
sub-species (Breeds) would live later.
*Costs:* a currency exists, so it has to be priced — `cost_check` becomes necessary.
*Who:* nobody in the genre exactly; closest is Mutant's Breed pool shrunk.

**Option C — Mutant's full build.** Family pool 8+, Breed 3+, Variant, bought with
a currency, per character.
*Buys:* enormous variety; the tooling is inherited and tested.
*Costs:* 15–20 minutes of chargen and a whole economy to balance; the genre's
aliens are *types*, and this makes them builds.
*Who:* Project Mutant only.

**Option D — the archetype.** No named species at all: "Brute", "Contemplative",
"Little Green Men", each ±1/−1 and one quirk. The player names their own alien.
*Buys:* infinite species with no content debt; sidesteps IP entirely; 15 lines of
rules total.
*Costs:* no Wookiee on the page — the recognisable thing the genre sells.
*Who:* Star Adventurer (15 archetypes, d20).

> **Recommendation: A, with the option-B pool held as the first expansion.** Three
> unrelated designs (WEG's corpus, WEG's own builder, Star Adventurer, SWN's menu)
> independently land on *a species is two things plus a note*. Start there, print
> 20–30 species that size, and add the pool only if the table finds them flat.
> **D is worth stealing from even if you pick A**: the archetype list makes a fine
> *generator* prompt (see 2) and a fine answer for background aliens.

---

### 2. The species builder — how does a referee or player make a new one?

Every game that answers this at all uses one of two shapes.

**Option A — the menu.** "Pick two benefits from this list of nine." One price,
paid once, identical for every species.
*Buys:* ten minutes, impossible to break, trivially checkable.
*Costs:* results feel same-ish; no texture unless you write it.
*Who:* Stars Without Number — and its robot PC uses the *same* menu.

**Option B — the table sequence.** Roll or choose down a fixed order: environment →
body plan → diet → size → senses → attributes → **number of abilities (weighted so
1–2 is typical)** → natural weapons → armour → skill bonus → penalties → story
factor → move/size.
*Buys:* the most complete builder in the genre, and its weighting reproduces the
published corpus; rollable for surprise or pickable for intent.
*Costs:* a dozen tables to write and balance.
*Who:* **WEG Alien Encounters ch. 1** (from Galaxy Guide 8) — this is the one real
Star Wars race builder that exists.

**Option C — the near-human swap.** Start from human, trade the human's one perk for
one non-human trait from a table.
*Buys:* five minutes; guaranteed balance.
*Costs:* only makes near-humans, not a Hutt.
*Who:* Saga, *Unknown Regions*.

**Option D — all three, layered.** A d20 archetype prompt (D above) for the concept,
the menu for the mechanics, the table sequence as the long form for a referee who
wants to roll a whole species.
*Buys:* one procedure at each level of effort.
*Costs:* three things to write instead of one.

> **Recommendation: B, presented as A.** Write the WEG table sequence — it is proven
> and its numbers match its own corpus — but put the *menu* at the front of the
> chapter as the ten-minute path, and the tables behind it for the referee who wants
> to roll. That is one chapter with a fast lane, not three procedures.

---

### 3. Where does the droid go?

**Option A — droid is a species.** Five or eight chassis, each a species block:
ability shift, size, speed, shared droid traits, bonus equipment, one hardwired skill.
*Buys:* the race builder does double duty; a droid PC is picked as fast as a Wookiee.
*Costs:* a droid is more equipment-shaped than a body, and equipment wants prices.
*Who:* SW5e (5 Degrees as species), Saga's Scavenger's Guide ("each chassis treated
as a species" — 8 chassis), SWN (an origin focus, same menu as aliens).

**Option B — droid is a class.** Metal body, scanners, self-repair, restricted
weapons, no armour; the model sets the class skill.
*Buys:* one entry, very OSR, no new layer.
*Costs:* a droid can then only be one thing; a droid *mechanic* and a droid
*assassin* are the same character.
*Who:* White Star, Mothership.

**Option C — droid is a build.** Chassis plus a parts catalogue with credit costs.
*Buys:* the fiction (droids are *modified* constantly); the same procedure as ship
modification.
*Costs:* slow chargen; needs a priced catalogue.
*Who:* WEG Cynabar's, Saga option 1.

> **Recommendation: A for the character, C for the catalogue.** Every game that lets
> you play a droid ends up treating it like a race, and Saga proves the two halves
> coexist: chassis-as-species to *make* one, parts catalogue to *change* one. Use
> the Degree taxonomy — it has survived three editions and sorts 319 WEG droids
> cleanly — but split it the way Saga did (Astromech / Mechanic / Protocol / Service
> / Battle / Probe / Medical / Labor), because "4th Degree" is not a character and
> "battle droid" is.
>
> **Steal Saga's Droid Quirks table regardless of which option you pick.** It is the
> droid's behaviour note, it is free, and it is the only place personality enters a
> droid build in any system.

---

### 4. The Force — how is it acquired?

**Option A — rolled.** The Strains model: you roll what you get, each power carries
a d4 table of what it costs you.
*Buys:* the fiction — nobody chooses to be sensitive; 240 tested powers already
exist; no pool, no bookkeeping between sessions; the dark side *is* the cost table.
*Costs:* a player who wants to be a knight may not get to be one; no licensed game
does this, so no reference points.
*Who:* Project Mutant, Star Adventurer (d20, one power at level 1).

**Option B — a feat-gated list that refills on a short rest.** A flag makes you
sensitive; a second pick gives you *1 + WIS* powers; using one spends it; a minute's
rest gets them all back.
*Buys:* the least bookkeeping of any licensed model; a Force user of any class;
scales cleanly.
*Costs:* a pool by another name; needs a power list with DCs.
*Who:* Saga Edition.

**Option C — three skills and a difficulty ladder.** Control / Sense / Alter; each
power states its own difficulty; no points at all; coercive powers are opposed by
the target.
*Buys:* the source's own model; 76 published powers to convert; the never-list is
*already* respected (all 13 coercive powers are opposed; 60 of 76 are against a
fixed number).
*Costs:* Core has no skills — this needs translating to x-in-6 or the 2d6 check.
*Who:* WEG d6, and RCR with vitality-point costs bolted on.

**Option D — failure is the cost.** Roll to use; on a failure the power is gone until
you rest four hours.
*Buys:* one sentence of rules, no resource tracking, instantly OSR.
*Costs:* nothing scales; a bad roll ends your contribution.
*Who:* Star Adventurer.

> **Recommendation: A for acquisition, D for use, C for the power list's shape.**
> Roll what you have (it is the fiction and the tooling exists); pay for a use with
> the roll itself and lose the power on a failure (no pool, no slots, one sentence);
> and write the powers in WEG's shape — each states its own chance, coercion is
> opposed, everything else is against a stated difficulty. **B is the fallback** if
> the table finds rolled powers frustrating.

---

### 5. Is the Force-user a class?

**Option A — no; it is a layer on any class.** A smuggler can turn out to be
sensitive.
*Who:* Saga (a feat), WEG (a flag), SWN (half a class), Mutant (a rolled layer).

**Option B — yes, and there are three of them.** Consular / Guardian / Sentinel, or
Adept / Mystic / Warrior.
*Who:* RCR (3 of 9), SW5e (3 of 10), Star Adventurer (3 of 7).

**Option C — yes, one class.** The Star Knight.
*Who:* White Star.

> **Recommendation: A.** Every game that makes it a class discovers it needs three,
> because one "Jedi" class is either the whole game or nothing. A layer also means
> the Class layer can be Mutant's, tested, unchanged.

---

### 6. What are the classes?

**Option A — Mutant's six, unchanged** (Strong, Fast, Tough, Smart, Wise,
Charismatic; three Picks at first level).
*Buys:* tested, priced, inherited with its tooling; zero design work.
*Costs:* nobody in the genre uses attribute-linked classes; the names don't evoke
the setting.

**Option B — Mutant's six, renamed to roles** (Soldier, Scoundrel, Pilot, Scholar,
Mystic-ish, Noble) with the same attribute links and the same Picks.
*Buys:* the genre's own axis — every Star Wars game uses roles — at the cost of a
renaming pass and nothing else.
*Costs:* a name can imply a Pick list it doesn't have; the link to the attribute
has to stay visible or the pricing drifts.

**Option C — five roles from scratch** (Saga's Jedi/Noble/Scoundrel/Scout/Soldier).
*Costs:* a whole class layer to design and price.

**Option D — no classes; templates.** A printed page that *is* species + role +
background + gear + a line of character. "Failed Jedi." "Retired Captain."
*Buys:* the genre's own answer, and the fastest possible chargen — pick a page, play.
*Costs:* only works once species, backgrounds and gear exist to assemble from.
*Who:* WEG (26 in the core, a build-your-own chapter in *Heroes & Rogues*).

> **Recommendation: B now, D as a printed layer on top later.** Keep the tested
> six and the Picks; give them the genre's names. Then, once species and gear exist,
> *generate* templates from them — WEG's 26 templates are the single best onboarding
> device in any Star Wars game and cost nothing new to make if the parts exist.

---

### 7. Skills — the problem that shows up twice

Core has **no skill list**; traits state their own chance. But the genre's "good at
piloting" is a skill in nine of eleven games, and **183 of WEG's 831 species
abilities are skill bonuses** — the single most common thing a species does.

**Option A — no skills, ever.** Every species ability becomes an x-in-6 chance or a
+1 to the 2d6 check. "Wookiees climb 5-in-6."
*Buys:* stays Core-native; nothing new to learn.
*Costs:* a long translation pass; some WEG abilities won't translate cleanly.

**Option B — a small named list** (8–12: Pilot, Repair, Medicine, Stealth,
Perception, Lore, Persuade…), each a +1-per-rank on the 2d6 check.
*Buys:* the genre's texture; makes Backgrounds and Origins easy to write; makes
importing WEG and Saga content mechanical rather than interpretive.
*Costs:* a Core divergence, and it must be declared in `DIVERGENCES.md`; Mutant's
7.0 principle argues against a shared skill list.

**Option C — skills only as traits.** No list, but a trait may *be* "Pilot +1", so
the effect exists without a system.
*Buys:* both, sort of.
*Costs:* the thing a validator hates — an implicit list nobody declared.

> **Recommendation: A, and say so out loud in the conversion notes.** This is the
> one place I'd hold the Core line hardest: the moment a skill list exists, every
> Class Pick and every species ability starts being written as +1 to a skill, and
> the game stops being this engine. The cost is a slow translation pass — that is
> exactly what `Species_Shape_Fit.md` (next) is for.

---

### 8. The generators

**Planets.** The fields have been settled since 1991 and nobody has changed them:
type, terrain, temperature, gravity, atmosphere (None/I–IV), hydrosphere, day, year,
species, starport, population, tech level, exports. Saga already bolted d20 tables
onto exactly those fields.
*The only real choice:* **do we add SWN-style tags?** A d100 list where each entry
carries Enemies / Friends / Complications / Things / Places. No Star Wars game has
this; it is what makes a rolled planet an adventure instead of a weather report.
> **Recommendation: yes — the fields from GG8/Saga, rolled, plus a tag list written
> for this setting.** The fields are a day's work; the tags are the content, and
> they are the best value-for-effort in the whole project.

**Ships.** Two families: **build** (hull + budgets: SWN's power/mass/hardpoints,
Traveller's tonnage) or **modify** (a stock hull, changed, each modification a
skill difficulty + a cost + a design limit — WEG's *Tramp Freighters*).
> **Recommendation: modify, stored as build.** Star Wars fiction is modification —
> nobody designs the *Falcon*. WEG's version is engine-native (a roll and a limit).
> Keep SWN's three-number budget underneath in `content/ships.yaml` so a stock ship
> is data and a from-scratch builder stays possible later.

**Droids.** Covered in 3: chassis (the race builder) + parts catalogue (the ship
modification chapter). No third procedure needed anywhere.

---

### 9. The two things I'd ask you to decide first

Everything above can wait except these, because the next work depends on them:

1. **Question 1 (what a species is)** — A, B, C or D. `Species_Shape_Fit.md` and
   the first 20 species files both depend on it.
2. **Question 7 (skills)** — A or B. It changes how *every* imported ability is
   written, and changing it later is a rewrite of all content, not a patch.

The rest — the Force model, classes, droids, generators — can be decided after the
shape-fit pass, and will be better decided then.

---

## 2. Races

*Source: `research/Race_Models_Compared.md`*

*How eleven games build a playable species, asked the same questions. Draft stage:
this file produces evidence, not rulings. Numbers come from `corpora/`; a claim with
no number behind it is a reading. Written 2026-09-20, all systems covered 2026-09-26.*

### The questions

1. How many races, and are they *species* (Wookiee) or *archetypes* (Brute)?
2. Fixed package or built? If built, with what currency?
3. What does a race give — attribute shifts · size · speed · senses · special
   abilities · a drawback · a story hook · languages?
4. Is there a **race builder** for new species, and what does it look like?
5. How is one race priced against another?
6. Do the abilities fit Core's 55 shapes? Which do not?
7. Where does the robot / droid go?

### The systems

#### WEG Star Wars d6 (1987–99) — *corpus: 449 species, 421 statted*

| | |
|---|---|
| How many | 449 in the fan compilation; the 2e core had ~20; GG4 + Alien Encounters ~150 |
| Species or archetype | species, named, with homeworld |
| Fixed or built | **fixed** — but the fixed thing is a *range*, not a number |
| What it gives | **Attribute Dice** (total, 333 of 421 at 12D) and per-attribute **min/max** (e.g. STR 2D/4D); 0–6 **Special Abilities** (median 1–2; 72 species have none); **Story Factors** (201 of 421 — a named line with no mechanic or a soft one); Move; Size; occasionally **Special Skills** (40) |
| Race builder | **Yes — Alien Encounters ch. 1 (1998), "loosely based on GG8 ch. 7"**, read from OCR. A table-driven template, rollable or chosen: environment (2D: barren … exotic) → biological origin (2D, weighted to mammal/reptile/insect) → diet, senses, size, tech level (nomadic … space) → **attribute dice** (12D average; sum of minimums ≤ total, sum of maximums ≥ total + 6D) → per-attribute range (3D table, 1D/2D at 3 up to 4D/6D at 18) → special skills (optional; "the majority of aliens in this book lack special skills") → **number of special abilities: 3D → 0 (15–18) / 1 (10–14) / 2 (7–9) / 3 (4–6) / 4 (3)** → natural weapons (1D: claws, fangs, tail, tusks… all STR+1D), natural armour (1D: +1 to +2D physical), skill bonus table (3D: +2D to a skill), beginning-character abilities, constant abilities (glide, see in dark, breathe water) → **penalty abilities** (delicate build, breath mask, technological ignorance, light gravity, poor vision, voice box) → story factors → move/size (3D table). GG4 2e has no procedure, only the format definition. |
| Pricing | none stated; the attribute total is the only lever, and 79% of species sit at 12D — priced by *not moving the total* |
| Shape fit | of 831 abilities: skill bonus +xD 183 · natural weapon 166 · sense 118 · movement 36 · communication 34 · armour/resistance 33 · environment/immunity 16 · Force-related 15 · other 227. Skill bonuses are the modal shape and Core has no skills — that is the translation problem. |
| Droids | statted as characters in `Droids_Stats` (corpus to extract); the Degree taxonomy (1st–5th) is WEG's |

**What the corpus says:** a WEG species is *narrow*. The attribute range is the
body; one or two abilities are the hook; the Story Factor is the culture. Most of
what a Wookiee *is* in play lives in the range (STR 3D/6D) and the Story Factor,
not in a list of powers. **And the builder says the same thing on purpose:** its
number-of-abilities roll is weighted so that 1–2 is the modal result (18 of 36 on
3D), 0 is common (10 of 36) and 4 is a 1-in-216. The corpus median of 1–2 is not an
accident of authorship; it is the design's stated intent. The builder also states
the one balance rule WEG has: "be reluctant to go above 6D … players will start
with 6D in every skill under that attribute" — the cap is on the *maximum*, not
the total.

#### SW5e (fan, 5e) — *corpus: 30 species, 360 traits*

| | |
|---|---|
| How many | 30 in the PHB incl. **five droid classes as species** |
| Fixed or built | fixed, 5e-style |
| What it gives | 12 traits each, always: Ability Score Increase · Age · Alignment · Size · Speed · Languages, plus 4–8 specials (Wookiee: Claws, Darkvision, Hide, Menacing, Powerful Build, Treeclimber) |
| Race builder | none in the PHB |
| Pricing | 5e's implicit budget (+2/+1, one or two "ribbons", one real ability) |
| Shape fit | all 5e shapes: proficiency, advantage, natural weapon, darkvision, climb speed. Advantage does not exist in Core (Module, off); proficiency does not exist in Core. |
| Droids | **species**, one per Degree, with shared Droid traits (resistances, no eat/breathe, ion vulnerability, Force-insensitive) + per-class differences |

#### Star Adventurer (RPGPundit, OSR) — *read in full*

| | |
|---|---|
| How many | 15, rolled on **d20** (Human 8–11) |
| Species or archetype | **archetypes** — Brute, Contemplative, Engineer, Giant, Hunter, Little Green Men, Methane-Breather, Warrior… "rather than provide descriptions for specific races, they are described as archetypes" |
| Fixed or built | fixed |
| What it gives | ±1 to two attributes (one +, one −); 1–2 skill bonuses; **one quirk** (breathes underwater; nightvision; needs breathing apparatus; +2 AC) |
| Race builder | the archetype list *is* the builder: pick the archetype, name the species, "generate specific appearances and homeworlds" |
| Pricing | every package is +1/−1 plus a small quirk; Human gets +1/+1 with no quirk |
| Shape fit | everything fits Core: attribute shift, skill bonus (→ x-in-6 or +1), sense, environment. The cleanest fit of any system read. |
| Droids | not a race; robots are equipment / NPCs |

**Also:** psychic powers are **rolled on a d20**, one at level 1, more by the
level-up chart — the same rolled-not-bought model as Mutant's Strains.

#### White Star Galaxy Edition (S&W WhiteBox) — *read: classes, mysticism*

| | |
|---|---|
| How many | race = class: Alien Brute, Alien Mystic, Robot (standard); Brimling, Uttin, Yabnab, Star Squirrel… (optional) |
| Species or archetype | archetype classes with a **species sub-table** — Alien Brute picks Falcon-Men / Procyon / Qinlon / Rawrarr / Space Duck / Wolfling, each one line |
| Fixed or built | fixed, as a class |
| What it gives | a full class (HD, BHB, saves, XP table) + class abilities + one species line |
| Race builder | one sentence: "the referee may allow other species… and should design the benefits… to suit their campaign" |
| Pricing | the class XP table |
| Shape fit | fits; the species lines are single shapes (fly 12; +1 to-hit with lasers; battle rage) |
| Droids | **Robot is a class** — metal body (+3 AC), scanners, self-repair, no armour, restricted weapons; models set the class skill |

#### Stars Without Number Revised — *read: pp. 199, 209*

| | |
|---|---|
| How many | none by default; humans |
| Fixed or built | **built by the GM, from a menu** |
| What it gives | an alien race is an **Origin Focus**: GM picks **two** from — Aptitude for Violence (+1 attack) · Environmental Native · Innate Ability (2–3 items' worth, or one psionic technique) · Natural Defenses (AC 15 + ½ level) · Origin Skill · Psychic Aptitude · Shapeshifting · Strong Attribute (+1 mod) · Tough (first HD maxed) — "or three if a couple are minor" |
| Race builder | **yes, this is one**, a page long |
| Pricing | the race **costs the player's free focus pick** — one price, paid once, same for every race. Flaws explicitly *not* a balance tool ("players pick classes unhindered by the flaw") |
| Shape fit | every menu item is a Core shape |
| Droids | VI PCs are the **same mechanism**: an origin focus, with the VI special rules (no sleep/eat, vacuum-immune, poison-immune, no Psychic class) |

#### Hulks & Horrors — *read: contents*

Races are classes (Hovering Squid, Omega Reticulan, Bearman) beside the human
classes (Pilot, Scientist, Soldier, Psyker). Race-as-class, White Star's model.

#### X-Plorers — *read: p. 28*

Humans only as PCs. "Alien Races" is a creature-building section: standard stat
blocks plus a special-abilities list (Swallow, Swarm, Web…). The race builder is
for monsters. Nothing for us on the PC side; the monster builder is the same shape
as Saga's *Creating New Beasts*.

#### Star Frontiers (TSR 1982) — *to read; from memory, to verify*

Four races, fixed: Human, Dralasite, Vrusk, Yazirian. Each: ability-score
adjustments, one or two special abilities (Dralasite lie detection + elasticity,
Vrusk comprehension + ambidexterity, Yazirian battle rage + gliding + night vision).
The earliest "race as a small fixed package" in the genre.

#### OSE — *via Mutant's `OSE_Race_Abilities_Analysis.md`*

21 races. The two-free-traits parity rule, the Light Sensitivity drawback template,
the Gargantua size finding. Race-as-class in B/X; Advanced splits them. Reuse as-is.

#### Project Mutant — *the sibling*

Family (8+ priced pool) → Breed (3+) → Named Variant; bought with Biogen; every
trait has a shape and a price; every Family a behaviour note; free traits at 3 or
under; Signatures may exceed if pre-paid. **The most built model on this list**,
and the one whose tooling this game inherits.

#### Saga Edition core (2007) — *read from OCR*

| | |
|---|---|
| How many | **14** in the core (Human, Bothan, Cerean, Duros, Ewok, Gamorrean, Gungan, Ithorian, Kel Dor, Mon Calamari, Quarren, Rodian, Sullustan, Trandoshan, Twi'lek, Wookiee, Zabrak); campaign guides add ~10 each; *Threats* and *Unknown Regions* more |
| Fixed or built | fixed |
| What it gives | Ability Modifiers (Wookiee +4 STR +2 CON −2 DEX −2 WIS −2 CHA) · Size · Speed · 2–4 specials (Extraordinary Recuperation; Rage — once/day, +2 melee, then −1 persistent condition step; Weapon Familiarity) · **Skills** (take 10 on Climb; reroll Persuasion to intimidate) · Automatic Languages. Human: bonus feat + bonus trained skill — **the baseline every species is priced against** |
| Race builder | *Unknown Regions* **Near-Humans**: "substantially the same as Humans … one or more differences" — swap the human bonus feat or bonus skill for one near-human trait from a table (extra arms, darkvision, quick healing …), plus a physical-variation table. A one-trait builder on a human chassis. Also *Creating New Beasts* for monsters |
| Pricing | against the human's feat + skill; a species' package is "worth" about those two |
| Shape fit | ability shifts, natural healing rate, a once-a-day surge with a hangover, take-10 and reroll (which are 3.5 skill mechanics Core lacks) |
| Droids | ch. 12: droid heroes with a standard score package; the five Degrees named in prose; Scavenger's Guide makes the chassis a species |

#### UAA (d20 RCR format) — *corpus: 161 species, 1,033 traits*

Every entry: Ability Modifiers (152 of 161) · size (Medium 109, Small 23, Large 12)
· Speed (147) · Free Language Skills (140) · then 1–5 specials. Modal specials:
Bonus Feat 54 · Natural Armor 32 · Skill Bonus(es) 52 · Natural Weapon(s) 23 ·
Low-Light Vision 14 · Darkvision 10 · Extra Limbs 10 · Breathe Underwater 8 ·
Damage Reduction 6 · **Primitive** 15 (a drawback: no proficiency with modern gear)
· Xenophobic 4. Median 5–6 traits, of which three are the boilerplate (mods, size,
speed, languages) — so **2–3 real abilities per species**, one more than WEG's
1–2, with d20's bonus feat doing the work WEG's skill bonus did.

#### FFG Edge of the Empire (2013) — *read from OCR; characteristic values are icons and did not OCR*

| | |
|---|---|
| How many | 8 in the EotE core (Bothan, Droid, Gand, Human, Rodian, Trandoshan, Twi'lek, Wookiee); ~50 across the three lines |
| Fixed or built | fixed |
| What it gives | a **characteristic spread** (Brawn, Agility, Intellect, Cunning, Willpower, Presence — 1 to 3, Human all 2) · Wound Threshold 10 + Brawn · Strain Threshold 10 + Willpower · **Starting XP** (Rodian 100, Human 110, **Droid 175**) · **Special Abilities**: one line — a free skill rank (Rodian: Survival) and/or one talent (Expert Tracker); Human: two free skill ranks |
| Race builder | none published; the format is a template |
| Pricing | **explicit** — starting XP *is* the price: a strong spread costs XP up front (Wookiee 90), a weak one refunds it (Droid 175, all characteristics 1). The only licensed game where the species price is a number on the sheet |
| Shape fit | attribute spread, a skill rank, a talent — all Core-shaped; the FFG species is the *smallest* package of any licensed game: a spread and one line |
| Droids | **a species**, with all-1 characteristics and 175 XP to spend — the race builder's menu applied to a robot |

### Side by side

| System | Count | Species or archetype | Built? | Builder | Price of a race | Droid |
|---|---|---|---|---|---|---|
| WEG d6 | 449 | species | fixed range | format-as-template | attribute total, 79% at 12D | character stat block |
| SW5e | 30 | species | fixed | none | 5e's implicit | **species** (5 classes) |
| Star Adventurer | 15 | **archetype** | fixed, rolled | archetype list | +1/−1 + quirk | none |
| White Star | ~10 | archetype **class** | fixed | one sentence | XP table | **class** |
| SWN | 0 | GM-built | **menu** | **yes — 2 perks** | one focus pick | same menu |
| Hulks & Horrors | 3 | class | fixed | none | XP table | — |
| X-Plorers | 0 | — | — | monsters only | — | — |
| Star Frontiers | 4 | species | fixed | none | parity by eye | none |
| OSE | 21 | class / species | fixed | none | two free traits | — |
| Mutant | 84 | species | **bought** | the whole system | Biogen | — |
| Saga | 14+ | species | fixed | Near-Human (1 trait) | vs human's feat + skill | chassis-as-species |
| RCR / UAA | 161+ | species | fixed | none | implicit | — |
| FFG | ~50 | species | fixed | none | **starting XP** | **species**, 175 XP |

### What the evidence points at (readings, not rulings)

1. **Every game that lets the referee make a race does it one of two ways:** a
   *menu* (SWN: pick two perks) or a *template with tables* (WEG Alien Encounters:
   roll or pick down a fixed sequence of tables; Star Adventurer: pick an archetype
   and name it). WEG's is the most complete in the genre, and it is explicitly
   both — "we recommend using the system as a guideline … though it is set up to
   produce random results." Nobody uses a point-buy at the race level except
   Mutant, and Mutant's is per-character.
2. **The measured WEG species is small.** 1–2 abilities, one Story Factor, a
   range. Star Adventurer independently lands at the same size (+1/−1, one quirk).
   SWN's "two perks" is the same size again. Three unrelated designs agree that a
   race is about **two things plus a note**.
3. **The attribute range is WEG's real race mechanic**, and Core has a rule for it:
   "a game may add a rule that moves scores off the 3d6 range; the table extends
   the same curve." A species as a *shift* on 3d6 — Wookiee STR +2, CHA −1 — is
   ENGINE-native and is what Star Adventurer does.
4. **Skill bonuses are the modal WEG ability (183 of 831) and Core has no skills.**
   Any WEG import has to translate +1D Sneak into something: an x-in-6 chance, a
   +1 on the 2d6 check, or a trait that states its own roll. This is the single
   biggest conversion question and it is a *vocabulary* question, not a race one.
5. **Droid placement splits three ways** — species (SW5e), class (White Star,
   Mothership), or the race-builder's own menu (SWN). SWN's is the only one where
   droid and alien share a procedure, which is what a droid-race category wants.
6. **Nobody prices a flaw.** SWN says outright that flaws do not balance because
   players route around them. Mutant prices them (−2 anatomy flaws) but on a
   per-character build. A race-level flaw is a story factor, not a cost.
7. **The archetype question is real.** Star Adventurer's "Brute / Contemplative /
   Little Green Men" is a race builder that produces *recognisable* results with
   IP filed off — which is exactly the placeholder-then-rename problem this game
   has. Worth holding next to the species list rather than instead of it.

---

## 3. Droids

*Source: `research/Droid_Models_Compared.md`*

*Where the droid goes — species, class, build, or equipment — in eight games, and
which taxonomy each uses. Draft stage: evidence, not rulings. Written 2026-09-20.*

### The questions

1. Is a player droid a **species**, a **class**, a **build**, or **equipment**?
2. What is the **taxonomy** — how does the game sort droids?
3. Is there a **droid builder**, and does it share a procedure with the race builder?
4. What do all droids share (the "droid traits"), and what does the type add?

### The systems

#### WEG d6 — *corpus: 319 droids*

| | |
|---|---|
| Player droid | a character: full attributes and skills; a template ("Failed Jedi"-style templates exist for droids in some sourcebooks) |
| Taxonomy | **Degree** (1st–5th) → category → model. Corpus: 1st 37 (Information, Utilitarian, Cooking, Medical) · 2nd 78 (Astromech, Repair, Slicer, Surveillance, Exploration) · 3rd 48 (Protocol, Servant, Caretaker) · 4th 100 (Military, Assassin, Security, Training) · 5th 56 (Cargo, Mining, Labor, Messenger, Service) — 26 categories, plus "Individual" named droids per Degree |
| Builder | **Cynabar's Fantastic Technology: Droids** (1997), "Designing, Upgrading, Customizing and Maintaining Droids": three skills (droid programming, droid repair, (A) droid engineering), then a systems catalogue — the droid is built like a vehicle, part by part, with a cost |
| Shared traits | the stat block: six attributes as a character, an **Equipped With** list (locomotion, appendages, sensors, tools, weapons), Move, Size, Cost. 316 of 319 have attributes; 312 have an equipment list |
| Adds | the type is the attribute spread + the equipment list; there is no separate "droid trait" block — everything a droid *is* is on its list |

#### SW5e — *corpus: 30 species, 5 droid*

| | |
|---|---|
| Player droid | **a species** — one per Degree (Class I–V) |
| Taxonomy | the five Degrees, renamed Classes |
| Builder | none; "work with your GM to find suitable traits" |
| Shared traits | Armor Integration · Droid Resistances (necrotic/poison/psychic; immune to poison, disease) · Droid Systems (no eat/drink/breathe) · Droid Vulnerabilities (ion; disadvantage vs ion/lightning) · Force-Insensitive · Maintenance Mode |
| Adds | per Class: ability shift (IV: +2 CON, +1 STR/DEX), size, one or two specials |

#### Saga Edition — *Scavenger's Guide to Droids, read; core ch. 12 pending OCR*

| | |
|---|---|
| Player droid | **three options**: (1) custom — build from scratch, systems and accessories bought individually (core p. 186); (2) a standard model — an existing stat block, usually with nonheroic levels, ≤ 5,000 credits; (3) **a stock chassis, "treated as a species"** |
| Taxonomy | Degree → **chassis**: 1st Medical · 2nd Astromech, Mechanic · 3rd Protocol, Service · 4th Battle, Probe · 5th Labor — eight chassis for five Degrees |
| Builder | option 1 *is* one, and ch. 3 is its catalogue: locomotion, appendages, processors, ~50 accessories, armour, with credit costs and "Adjudicating Droid Modifications" (unbalancing, redundant, "taking away toys") |
| Shared traits | droid immunities + "typical droid traits" (core pp. 187–8); no Constitution score |
| Adds | a chassis gives: ability modifiers (Astromech +2 INT −2 CHA; Battle +2 DEX −2 INT; Labor +2 STR −2 INT), size, speed + locomotion, **bonus equipment** (the systems every droid of that chassis has), a hardwired skill, a conditional bonus feat, languages. Also **Droid Quirks** (a d% table of persistent conditions) and droid-only feats and talents |

#### White Star — *read*

Robot is **a class**: metal body (+3 AC), scanners, self-repair, no armour, restricted
weapons, shut down 1 hour a day; the *model* sets the class skill. Novomachina and
Cypher are further robot-adjacent optional classes.

#### Stars Without Number — *read, p. 199*

VI (robot) PC is **an origin focus**, the same mechanism as an alien species: spend
the free focus pick; then the VI rules (no sleep/eat/drink, Type B cell weekly,
vacuum-immune, poison/disease-immune, reprogrammable in a month, no Psychic class).
"They may have been built to be a particular type of bot, but they use their own
statistics, not those for their type." The type is fiction.

#### Mothership — *not on disk; from memory*

Android is **one of four classes**; the others are human. Class gives stat bonuses,
a save bonus, and one rule (Androids: fear saves cause nearby humans to panic).

#### Star Adventurer · X-Plorers · Hulks & Horrors · Star Frontiers

No player droid. Robots are equipment or NPCs.

### Side by side

| System | Player droid is | Taxonomy | Builder | Shares a procedure with the race builder? |
|---|---|---|---|---|
| WEG | a character | Degree → 26 categories | Cynabar's, parts catalogue | no — vehicle-style |
| SW5e | **a species** | Degree (5) | none | yes, trivially — it *is* a species |
| Saga | species (chassis) / model / build | Degree → 8 chassis | ch. 3 catalogue + core p. 186 | option 3 yes; option 1 no |
| White Star | **a class** | model → class skill | none | race is also a class, so yes |
| SWN | **an origin focus** | none (type is fiction) | the same menu | **yes, identical** |
| Mothership | a class | — | none | — |

### What the evidence points at (readings, not rulings)

1. **Every game that lets you play a droid ends up treating it the way it treats a
   race.** SW5e: a species. Saga: a chassis "treated as a species". White Star: a
   class, like the aliens. SWN: an origin focus, like the aliens. The one exception
   is WEG, which has no race layer at all — a droid is just a character with an
   equipment list — and Cynabar's builds it like a speeder.
2. **The Degree taxonomy survives every edition** — WEG 1988, SW5e, Saga — and the
   corpus shows why: 26 categories in 319 droids sort cleanly under five headings,
   and 4th Degree (combat) is the biggest at 100. Saga's move from five Degrees to
   eight *chassis* (splitting 2nd into Astromech/Mechanic, 3rd into Protocol/Service,
   4th into Battle/Probe) is the only refinement anyone has made, and it is the one
   a player-facing list needs: "battle droid" and "probe droid" are different
   characters; "4th Degree" is not a character.
3. **The shared droid trait block is the same in every game**, which means it is a
   Core-shape question already answered: *resistance* (poison, disease, vacuum),
   *vulnerability* (ion), *no rest / different rest*, *cannot use the Force* — four
   shapes, priced once, inherited by every chassis.
4. **The builder splits into two jobs**: (a) *chassis* — ability shift + size +
   locomotion + a bonus-equipment list + one hardwired skill (Saga's format is the
   cleanest and is exactly a WEG species entry with "Equipped With" in place of
   Special Abilities); (b) *modification* — a parts catalogue with prices (Cynabar's,
   Saga ch. 3). (a) is the race builder with a different menu. (b) is the ship
   modification chapter with a different menu. Neither is a third procedure.
5. **Quirks.** Saga's d% Droid Quirks table is the droid equivalent of WEG's Story
   Factor and Mutant's behaviour note — a free, no-mechanic-or-soft-mechanic line
   that makes a droid *this* droid. It is the only place personality enters a
   droid build in any system, and it is a table, which is what a builder wants.

---

## 4. The Force

*Source: `research/Force_Models_Compared.md`*

*How nine games give a character the Force (or its stand-in), asked the same
questions. Draft stage: evidence, not rulings. Numbers come from `corpora/`; FFG and
Saga are placeholders until their text is in. Written 2026-09-20.*

### The questions

1. A class, a skill, a pool, a power list, a feat tree?
2. Bought, rolled, or granted?
3. What does a power cost to *use* — points, a roll, hit points, nothing?
4. What resolves it — the user's roll against a fixed number, or against the target?
5. Is there a dark side, and is it a resource, a meter, a cost, or fiction?
6. How many powers, and how many break the never-list (automatic hit, broad
   immunity, undetectability, undo)?
7. What does the game do about lightsabers?

### The systems

#### WEG d6 — *corpus: 122 powers, 76 WEG-published*

| | |
|---|---|
| Model | **three skills** — Control, Sense, Alter — under a Force-sensitive flag; powers are *things you can do with the skills you have* |
| Acquired | learned from a teacher, one at a time; 48 of 76 list prerequisite powers (a tree) |
| Cost to use | a **roll** against a difficulty; no points spent; using a power is the round's action; 14 powers may be "kept up" (a running −1D on everything else) |
| Resolution | **60 of 76 against a fixed difficulty**, set by the user's conditions (weight, distance, relationship). Only **13** are resolved against the target's own Control or Perception roll — and those are the coercive ones: Affect Mind, Injure/Kill, Force Lightning, Inflict Pain, Control Mind, Memory Wipe, Receptive/Projective Telepathy |
| Dark side | **a meter**: Dark Side Points, one per evil act or dark power used; at ≥ 1d6 roll the character falls. 19 of 76 published powers are Dark Side. Plus **Force Points**: a spendable double-everything, refunded for heroic use, lost for selfish use |
| Never-list | almost clean: 3 of 76 match a pattern (Control Mind, Telekinetic Kill, one false positive). *Absorb/Dissipate Energy* is a resistance — it fails on a bad roll |
| Lightsaber | **a power** — *Lightsaber Combat* (Control+Sense), kept up, adds Sense to hit and Control to damage; without it a lightsaber is a dangerous stick |
| Shape of the corpus | Control 18 · Sense 18 · Control+Alter 15 · all three 13 · Alter 4 · Control+Sense 4 · Sense+Alter 3. The single-skill powers are the small ones; the big ones need all three. |

**What the corpus says:** WEG's Force is a **skill system with a difficulty ladder**,
and its safety valve is that coercion is opposed while everything else is not. The
dark side is bookkeeping, not fuel.

#### d20 Revised Core Rulebook (WotC 2002) — *read from OCR*

| | |
|---|---|
| Model | **19 Force skills**, gated by **feats**: *Force-Sensitive* opens the "Force" skills (Empathy, Enhance Ability, Friendship…); *Alter / Control / Sense* each open their family, and are exclusive to Force-using classes (Force Adept, Jedi Consular, Jedi Guardian) |
| Acquired | skill ranks, bought with skill points like any skill |
| Cost to use | **vitality points**, paid on every attempt, success or not — the Force literally burns hit points |
| Resolution | skill check vs DC, or opposed |
| Dark side | Dark Side Points (from dark-side skills, marked in the table) and **Force Points** (a d6 added to a roll; more for Force-sensitives) |
| Lightsaber | a weapon with exotic proficiency; Jedi classes get it free; deflect/redirect are class features |

#### SW5e — *corpus: 200 powers*

| | |
|---|---|
| Model | **spellcasting**: forcecasting classes (Consular, Guardian, Sentinel) with force points and power levels 0–9; 33 at-will, 37 1st… 9 9th |
| Acquired | known powers by class level, chosen from the list; prerequisites chain them |
| Cost to use | **force points** (a mana pool), plus casting time and concentration |
| Resolution | saving throw against the caster's DC, or a force attack roll |
| Dark side | **an alignment tag on the power**: 88 universal, 52 light, 60 dark; a character's alignment gates which lists |
| Never-list | 5 of 200 match a pattern (Kill, Control Pain, Improved Restoration, Will of the Force, Improved Feedback) |
| Lightsaber | a weapon; Guardian forms and Sentinel paths are the fighting styles |

#### Star Adventurer (Pundit) — *read*

| | |
|---|---|
| Model | three **psychic classes** (Adept, Mystic, Warrior); powers work like skills |
| Acquired | **rolled on a d20 from 20**, one at level 1, more from the level-up chart ("gain one new psychic power" 2-in-12) |
| Cost to use | a roll (d20 + CHA + power bonus + level) vs DC; **on a failure the power is lost until 4 hours' rest** — failure is the cost |
| Dark side | a specialisation (Dark Psychic), not a meter; the Psychic Knight and Dark Psychic have the *same* deflection ability |
| Lightsaber | the "Psychic Laser Sword"; deflection is an **opposed attack roll**, rebounds on a beat-by-5, cumulative −2 per extra deflection in a round — a resistance, priced in actions |

#### White Star Galaxy Edition — *read*

| | |
|---|---|
| Model | **Vancian**: Star Knights (and Star Pilots, Untrained Initiates, Alien Mystics) prepare **Meditations** by level after 15 rounds of exercise; ~35 Meditations across five levels (Charm Person, Detect Thoughts, Telekinesis, Missile Redirection…); Alien Mystics get *Gifts*, Star Squirrels *Chitterings* |
| Acquired | class level table; a 1st-level Star Knight has **no** Meditations |
| Cost to use | the prepared slot |
| Dark side | none mechanical |
| Lightsaber | the star sword; Star Knight +2 to hit, free at level 1 |

#### Stars Without Number — *psionics; to verify from ch. 5*

Psychic class; six disciplines as skills 0–4; techniques bought per level; an
**Effort** pool committed per use, scene or day; overuse is the cost. Not the Force,
but the most-copied OSR psionics and the model for "a pool that comes back".

#### Project Mutant — *the sibling: `content/mutations.yaml`*

Twelve Strains, 240 perks, **rolled** on the Strain table (Dose sets how often);
each perk has a d4 table of what it costs *you* and four Manifestations of what
it looks like. No use cost, no pool; the price is on the character permanently.
Audited against the never-list; passes. This is the system the draft proposes to
re-read as the Force.

#### Saga Edition (2007) — *read from OCR*

| | |
|---|---|
| Model | **a feat, a skill, and a hand of cards.** *Force Sensitivity* (any class) → the *Use the Force* skill (CHA) → each *Force Training* feat adds **1 + WIS modifier** powers to your **suite**; "using a Force power is like playing a card and putting it in a discard pile" |
| Acquired | chosen from the list per Force Training; a permanent WIS change adds or removes powers |
| Cost to use | the card. **Regain all after 1 minute's rest out of combat**, or on a natural 20 on Use the Force, or one per Force Point spent as a reaction |
| Resolution | a Use the Force check against a DC ladder printed on the power, or against a target's Defense |
| Dark side | **Dark Side Score**, max = Wisdom; +1 per major transgression — which *includes* using any power with the [dark side] descriptor (Force Lightning, Dark Rage); at Score = WIS the character is the GM's. Plus Force Points (5 + ½ level per level, lost if unspent) |
| Never-list | powers are DC-laddered and mostly "vs Will/Fortitude Defense"; *Sever Force* blocks a Force-user's access — a shutdown, not an undo |
| Lightsaber | **Block / Deflect** talents: a reaction, Use the Force check vs the attack roll, **cumulative −5 per use since your last turn**; *Lightsaber Defense*: +1 Reflex as a swift action — a priced resistance, escalating |

**What it adds to the picture:** Saga is the licensed game that made the Force a
*layer on any class* and made its resource a **short-rest** one (1 minute), which is
the least bookkeeping of the four licensed games. Its Block/Deflect is Star
Adventurer's deflection with −5 instead of −2.

#### FFG Force and Destiny (2015) — *read from OCR; structure confirmed, tables are graphics*

| | |
|---|---|
| Model | **a rating and a shop.** A Force-sensitive character has **Force rating 1** (from a career or the Force Sensitive Exile/Emergent specialisation); each Force power is a **tree**: a basic power bought with XP, then upgrades (Range, Magnitude, Strength, Duration, Control…) bought down the tree |
| Acquired | XP, like everything else; a Force user *spends their talent XP on powers* — the non-Force character's relevance is that they spent the same XP on talents |
| Cost to use | **roll Force dice** equal to rating; the pips you get are the budget for that use; light-side pips are free, **dark-side pips cost strain and Conflict** to use |
| Resolution | the pips; no target number, no save — the power does what the pips buy, and a target may get an opposed check for some |
| Dark side | **Morality**: a 0–100 score; **Conflict** accrues per session from dark-pip use and bad acts, rolled against at session end; below 30 the character is dark side and the dice read the other way |
| Never-list | Move (telekinesis) scales to starships with enough pips; *Influence* is a mind trick with a Discipline opposed check; nothing is automatic — everything is bought with pips the dice may not give |
| Lightsaber | a skill (Lightsaber, keyed to Brawn or by form talent to Agility/Intellect/Cunning/Willpower/Presence); **Reflect / Parry** talents spend strain to reduce damage — a resistance priced in strain |

**What it adds:** FFG's is the only Force where *the same XP* buys a Jedi's powers
and a smuggler's talents — relevance by construction. And its Morality is the only
dark-side meter that is *rolled against* rather than counted up.

### Side by side

| System | Model | Acquired | Use cost | Resolves vs | Dark side | Lightsaber |
|---|---|---|---|---|---|---|
| WEG | 3 skills + power list | taught, tree | a roll; kept-up penalty | fixed diff (60/76); target's roll for coercion (13) | DSP meter + Force Points | a **power** |
| RCR | 19 skills, feat-gated | skill ranks | **vitality points** | DC / opposed | DSP + Force Points | weapon + class features |
| SW5e | spell levels | class list | force points (mana) | save vs DC | tag on the power | weapon + forms |
| Star Adventurer | psychic classes | **rolled d20** | roll; **fail = lost till rest** | DC | a subclass | opposed deflect |
| White Star | Vancian meditations | class level | a slot | save | none | +2 weapon |
| SWN | disciplines + techniques | bought | Effort pool | skill check | none | — |
| Mutant | Strains, 240 perks | **rolled** | none; permanent d4 cost | per shape | the d4 cost | — |
| Saga | feat → suite | chosen | spent till rest | Use the Force vs Defense | Dark Side Score | weapon + talents |
| FFG | rating + trees | XP | Force dice; dark pips cost strain + Conflict | pips buy the effect | **Morality**, rolled | Reflect/Parry (strain) |

### What the evidence points at (readings, not rulings)

1. **Every licensed game makes the Force a *resource*** — vitality (RCR), force
   points (SW5e), a suite that empties (Saga), Force dice (FFG). WEG alone makes it a
   *roll*, and pays for it with a kept-up penalty and the dark-side meter. The two
   OSR knockoffs split: White Star copies the cleric; Star Adventurer makes failure
   the cost. Core has no mana and no spell slots; the WEG and Star Adventurer models
   are the ones that fit the engine without adding a pool.
2. **The source's own coercion rule is the never-list's rule.** WEG resolves 60 of
   76 powers against a fixed number, but *every* mind-affecting or killing power is
   opposed by the target. That is "a save, target 15" with the serial numbers filed
   off — Star Crawler's draft position 5 is what WEG already did.
3. **Rolled powers exist in the genre twice** — Star Adventurer (d20, one at L1)
   and Mutant (Strains). Both are OSR. Both make the Force something that *happens
   to* a character. No licensed game does it; all of them are shopping.
4. **The lightsaber is the one thing every system treats differently**, and only
   WEG makes it a Force power. Star Adventurer's deflection — opposed attack roll,
   rebound on a beat-by-5, −2 per extra deflect — is a *resistance* with a price in
   actions and fits a Core shape exactly. WEG's Absorb/Dissipate Energy is the same
   idea one step more general.
5. **Never-list hits are rare in the source** (3/76 WEG, 5/200 SW5e by pattern —
   a reviewed pass will find more). The fiction's "invulnerable" moments are
   mostly *resistances with a roll* already. The audit Mutant ran on its Strains
   would run on a WEG-derived list almost unchanged.
6. **The dark side is a meter in two games, a tag in one, a subclass in one, and
   absent in three.** Mutant's "the d4 cost on each perk" is a fourth answer none
   of the licensed games use, and it is the only one with no bookkeeping between
   sessions.
7. **WEG's power count is small.** 76 published, ~50 of them light-side and
   non-coercive. A Star Crawler Force list of that size, each entry a Core shape with
   a Mutant-style cost table, is a week's data entry, not a design problem.

---

## 5. Classes

*Source: `research/Class_Models_Compared.md`*

*What a Star Wars or sci-fi OSR character* is *before they are a race or a Force
user: the class layer, in eleven systems. Draft stage: evidence, not rulings.
Project Mutant's `Class_Models_Compared.md` already compares fifteen general
class models against eight criteria and chose ACKS-style; this file does not redo
that. It asks only the genre's questions. Written 2026-09-20.*

### The questions

1. Are there classes? How many, and what is the **axis** — role, attribute,
   archetype, career, template?
2. Is the Force-user a class, a layer on any class, or a separate class set?
3. What does a level give, and when does the first differentiating feature arrive?
4. How does a **non-Force character stay relevant** next to a Force user?
5. Where do skills live — a list, the class, or nowhere?

### The systems

#### WEG d6 — *REUP: 26 templates*

| | |
|---|---|
| Classes | **none**. Characters are attributes + skills; a **template** is a pre-built, pre-flavoured sheet: Alien Student of the Force, Armchair Historian, Arrogant Noble, Bounty Hunter, Brash Pilot, Ewok, Failed Jedi, Gambler, Laconic Scout, Loyal Retainer, Merc, Minor Jedi, Mon Calamari, Old Senatorial, Outlaw, Pirate, Protocol Droid, Quixotic Jedi, Retired Captain, Smuggler, Tongue-Tied Engineer, Tough Native, Wookiee, Young Jedi, Young Senatorial (+ Heroes & Rogues: dozens more, with a build-your-own-template chapter) |
| Force user | a flag (Force-sensitive) and three skills; four of the 26 templates are Jedi of some kind |
| Level gives | no levels; Character Points buy skill pips |
| Non-Force relevance | structural: a Jedi's Force skills are three more skills; the smuggler has the ship |
| Skills | the whole game — ~50 skills under six attributes |

**Note the template as a design object.** A WEG template is exactly a *species +
class + background + gear + a personality line*, printed as one page. "Failed Jedi"
and "Quixotic Jedi" are the same class with different behaviour notes. It is the
closest thing in any Star Wars game to Mutant's "Family page".

#### d20 RCR (2002) — *read from OCR*

| | |
|---|---|
| Classes | **nine**: Fringer, Noble, Scoundrel, Scout, Soldier, Tech Specialist, **Force Adept, Jedi Consular, Jedi Guardian**. Prestige classes above 7th |
| Force user | **three of the nine classes**; a Jedi who leaves the path before 7th "must return his lightsaber to his master" |
| Level gives | d20 3.0: BAB, saves, feats, class features by level, skill points |
| Non-Force relevance | the 3.0 answer — skills and feats; the Force skills cost vitality, so a Jedi is a caster who bleeds |
| Skills | 3.0 skill list with ranks; Force skills are skills |

#### Saga Edition (2007) — *read from OCR*

**Five** heroic classes — Jedi, Noble, Scoundrel, Scout, Soldier — each with
**talent trees** (the Jedi's: Consular, Guardian, Sentinel, **Lightsaber Combat**
— where Block, Deflect and Lightsaber Defense live); a talent at every odd level,
a feat at every even. **Force Sensitivity is a feat any class can take**; Force
Training (1 + WIS powers) likewise; so a Force-using Scoundrel is a first-level
build, and the Jedi *class* is the one with the lightsaber talents and a Force
Point boost ("5 + one-half character level"). Prestige classes at 7th (Jedi Knight,
Ace Pilot, Bounty Hunter, Crime Lord…). Humans: a bonus feat and a bonus trained
skill. Droid heroes: ch. 12, any class, a "standard score package".

#### SW5e — *PHB ch. 3, outline read*

**Ten** classes, each with four archetypes: Berserker · Consular · Engineer · Fighter
· Guardian · Monk · Operative · Scholar · Scout · Sentinel. The Force users are
**three classes** (Consular, Guardian, Sentinel — the Saga Jedi trees promoted to
classes); Engineer and Scholar are *tech*-casters. 5e chassis: subclass at 3rd,
ASI at 4th/8th/12th…

#### Star Adventurer — *read*

**Seven**: Brute, Explorer, Psychic Adept, Psychic Mystic, Psychic Warrior, Rogue,
Technician, Warrior — each with 2–4 **specialisations** (Warrior: Gang Enforcer,
Hit-Man, Officer, Stormtrooper; Psychic Warrior: Dark Psychic, Psychic Knight).
Attribute requirement per class. **Three of eight are psychic classes.** Plus 20
**Origins** (Aristocrat, Criminal, DriveTech, Gunner, MedTech, Pilot, Smuggler-
shaped "Scoundrel", Soldier, Spacer…), each three skill bonuses. Level-up is a
**random roll on a class chart** (d12: hit die, save, attack, skills, a new psychic
power). Skills are a list of ~28 with d20 + mod vs DC 10/15/20/25.

#### White Star — *read*

**Five** standard: Aristocrat, Mercenary, Pilot, Robot, **Star Knight**; ~20
optional (Alien Brute, Bounty Hunter, Combat Medic, Gunslinger, Two-Fisted
Technician, Alien Mystic, Star Pilot, Untrained Initiate…). The Star Knight is the
cleric; Star Pilot and Untrained Initiate are the paladin/ranger (Meditations late
and few). S&W WhiteBox chassis: HD, BHB, save, one class skill. **Serials** —
an optional lifepath (homeworld, family, youth, first adventure, adversaries,
allies, critical event).

#### Stars Without Number — *read: ch. 2*

**Four**: Warrior, Expert, Psychic, **Adventurer** (any two halves). Backgrounds
(a d6 growth/learning table each) + **Foci** (Sniper, Die Hard, Gunslinger… two
levels each). The Psychic is one of four; the Adventurer can be Partial Psychic.
Skills level 0–4. The non-psychic answer: Foci and the Expert's reroll.

#### Traveller — *on disk, to verify*

**Careers**, not classes: Navy, Marines, Army, Scouts, Merchants, Other; four-year
terms, survival rolls, skills from career tables, mustering-out benefits. The
character is their history. No Force-analogue in the core (psionics in a supplement).

#### Star Frontiers — *on disk, to verify*

No classes; skills in three areas (Military, Technological, Biosocial) bought with
experience; a *PSA* (primary skill area) is the nearest thing to a class.

#### Mothership — *not on disk; from memory*

**Four**: Teamster, Scientist, Android, Marine — a stat spread, a save spread, one
rule each. No powers of any kind.

#### X-Plorers · Hulks & Horrors

X-Plorers: four (Scientist, Soldier, Scout, Technician). H&H: Pilot, Scientist,
Soldier, Psyker + three race-classes.

#### Project Mutant — *the sibling*

Six attribute-linked classes (Strong, Fast, Tough, Smart, Wise, Charismatic), three
Picks at 1st, ACKS-style picks after; every class has features from level 1 (the
"undifferentiated to 7th" problem was found and fixed). Mutations are a *layer* on
any class, rolled.

### Side by side

| System | Classes | Axis | Force user is | Skills |
|---|---|---|---|---|
| WEG | 0 (26+ templates) | template = species+class+background | a flag + 3 skills | ~50, the game |
| RCR | 9 | role | **3 classes** | 3.0 list |
| Saga | 5 (+prestige) | role, talent trees | **a feat on any class** (+ Jedi class) | 3.5-lite |
| SW5e | 10 ×4 | role | **3 classes** (+2 tech-casters) | 5e |
| Star Adventurer | 7 ×2–4 | role; 20 Origins | **3 classes** | 28, d20 |
| White Star | 5 (+~20) | archetype/class-as-race | **1 class** (+3 lesser) | one class skill |
| SWN | 4 | role; backgrounds + foci | **1 class** (+ half) | 0–4 |
| Traveller | careers | history | — | career tables |
| Mothership | 4 | stat spread | — | skills |
| Mutant | 6 | **attribute** | **a layer**, rolled | none — traits state their roll |

### What the evidence points at (readings, not rulings)

1. **Two answers to "is the Jedi a class", and the licensed games split evenly.**
   *Class*: RCR (3 of 9), SW5e (3 of 10), Star Adventurer (3 of 7), White Star (1).
   *Layer on any class*: Saga (a feat), WEG (a flag), SWN (half a class), Mutant.
   The layer games are the ones where "the smuggler turns out to be Force-sensitive"
   is a rules-legal event; the class games make that a multiclass.
2. **Every game that makes the Jedi a class makes it three classes** — Consular /
   Guardian / Sentinel, Adept / Mystic / Warrior — because one "Jedi" class is
   either the whole game or nothing. The layer games don't have this problem: the
   Force adds to whatever the character already was.
3. **The WEG template is the genre's own answer to "what does a player pick up
   and play".** Species + role + background + a line of character, one page. Every
   game since has some version: Star Adventurer's Origins, White Star's Serials,
   SWN's Backgrounds, Saga's prestige archetypes. Mutant's Family page is the
   same object. A Star Crawler that has Species and Classes and Backgrounds could
   *print* templates without designing a new thing.
4. **Non-Force relevance is solved by skills in every game but Mutant's**, and
   Core has no skill list — traits state their own roll. That is the same
   translation problem `Race_Models_Compared.md` found for WEG's +xD species
   abilities: the genre's "smuggler is good at piloting" is a skill in nine games
   and a trait-with-a-chance in this engine. It is one question, asked twice.
5. **Star Adventurer's random level-up chart is the class analogue of rolled
   mutations** and the only one of its kind here. It is small, and it is exactly
   Mutant's method applied to advancement.
6. **Nobody uses attribute-linked classes but Mutant.** Every genre game's axis is
   role (soldier, scoundrel, pilot). Whether Star Crawler's six are "Strong, Fast…"
   or "Soldier, Scoundrel, Pilot…" is a naming question if the Picks are the same —
   and the draft already keeps Mutant's Class-name placeholders precedent.

---

## 6. Generators: planets, ships, droids

*Source: `research/Generators_Compared.md`*

*Planet, ship and droid generators across the systems on disk: what the unit of
build is, what comes out, and how long it takes. Draft stage: evidence, not
rulings. Written 2026-09-20; Saga Starships and core pending OCR.*

### The questions

1. **Unit of build** — tables you roll down? a classification you fill in? a hull
   plus fittings with a budget? points?
2. **Output** — a stat block the engine can use (Core can fight a ship? a planet
   has a number a check is made against?), or a description?
3. **Time** — one roll, ten rolls, an hour?
4. **Where the hooks are** — what makes the result *this* planet / ship / droid
   rather than a stat line?

---

### A. Planets

#### Traveller (1977) — the ancestor; *Traveller Book on disk, to verify pages*

**Unit:** the Universal World Profile — eight digits, each a 2D roll modified by the
one before: Starport (A–E, X) · Size · Atmosphere · Hydrographics · Population ·
Government · Law Level · Tech Level. Plus trade classifications derived from the
digits (Agricultural, Industrial, Poor, Rich…) and bases.
**Output:** a code (`A788899-C`) that *is* the stat block — starport quality gates
what you can buy, law level is a number you roll against for weapons, tech level
gates equipment.
**Time:** eight rolls; a subsector of 40 worlds in an evening.
**Hooks:** none built in; the digits imply them and the referee reads them.

#### Stars Without Number Revised — *read: pp. 132–169*

**Unit:** attributes by 2d6 table (atmosphere, temperature, biosphere, population,
tech level) **plus two World Tags from a d100 list of 100** (Abandoned Colony, Alien
Ruins, Altered Humanity, Anarchists, … Zombies). Each tag carries Enemies /
Friends / Complications / Things / Places — five lists of adventure material.
**Output:** a short stat line and two tags that *are* the adventure hooks.
**Time:** ~7 rolls; a sector of 20–30 worlds in an evening.
**Hooks:** the whole point — the tags are the generator's product; the numbers are
scaffolding.

#### WEG Galaxy Guide 8: Scouts / Planets Collection — *read from OCR*

**Unit:** a **classification template**, not dice: Type · Terrain (14 kinds) ·
Temperature (5) · Gravity (4) · Atmosphere (None, Type I–IV) · Hydrosphere (5) ·
Length of day / year · Sapient species · Starport (5 classes) · Population · Tech
level (Stone → Space, 6) · Major exports/imports. GG8 ch. 9 defines every field and
its values; the Planets Collection is 30 worlds in that format. GG8 ch. 7's alien
and creature tables *are* dice-driven and became Alien Encounters ch. 1.
**Output:** the template filled in — which is exactly a Star Wars planet as the
films present one ("desert world, Type I, standard gravity, limited starport").
**Time:** as long as you take; there is nothing to roll.
**Hooks:** none mechanical; the sourcebook entries carry them as prose.

#### Saga: The Unknown Regions — "Creating New Worlds", *read*

Two methods, stated: **build from scratch** (start with a basic idea → key themes
and features → name → adventure use — a design essay, not a procedure) or the
**planet generator**: d20 tables — 3-1 System type · 3-2 Number of planets · 3-3
Planet type · 3-4 (gravity) · 3-5 Atmosphere (None / Breathable / Breath mask /
Environment suit / Hazardous suit, "based on Human compatibility") · 3-6 Hours per
day · 3-7 Local days per year · 3-8 Climate (Arid, Temperate, Tropical,
Subarctic, Superheated) · 3-9 Dominant environment (14 kinds, each with 3–6
named subtypes) · and on through population, tech, government, points of interest
(tables past p. 86, to read). "Roll on each table to create a completely random
world, or pick and choose."
**Output:** WEG's template, filled by dice. The subtypes ("Desert: arid, dusty,
frozen, hot, sandy, searing, rocky") are the texture.
**Time:** ~12 rolls.
**Hooks:** points of interest tables (to verify).

#### Star Adventurer · White Star · X-Plorers · Hulks & Horrors

No planet generator in Star Adventurer or White Star (both assume the referee
brings a galaxy). X-Plorers and H&H have creature tables only.

#### Planets — side by side

| System | Unit | Output | Rolls | Hooks |
|---|---|---|---|---|
| Traveller | 8 chained 2D digits | a code that gates play | 8 | implied |
| SWN | 2d6 stats + **2 of 100 tags** | stat line + adventure lists | ~7 | **the product** |
| WEG GG8 | classification, no dice | the Star Wars template | 0 | prose |
| Saga UR | d20 tables → the WEG template | template + subtypes | ~12 | POI tables |

**Reading:** the Star Wars template (GG8) and the OSR generator (SWN) are not rivals;
Saga UR already bolted dice onto the WEG fields. What none of the Star Wars games
have is SWN's **tag** — the thing that makes a planet an adventure rather than a
weather report. A Star Crawler planet generator is the WEG/Saga fields, rolled, plus
a tag list written for the genre; the fields are settled, the tags are the work.

---

### B. Ships

#### Traveller — *Traveller Book on disk*

**Unit:** **tonnage**: pick a hull (100–5,000 tons), allocate tons and credits to
jump drive, manoeuvre drive, power plant, fuel, bridge, computer, staterooms,
cargo, weapons (turrets by hull size). A checklist procedure with a spreadsheet's
worth of arithmetic.
**Output:** a full stat block for the Traveller space-combat game.
**Time:** an hour for a new design; standard designs are provided so most tables
never do it.

#### Stars Without Number — *read: pp. 94–103*

**Unit:** **hull + fittings**. Twelve hulls in four classes (Strike Fighter, Shuttle,
Free Merchant, Patrol Boat, Corvette, Heavy Frigate, Bulk Freighter, Fleet Cruiser,
Battleship, Carrier, Small/Large Station), each with Cost / Speed / Armor / HP /
Crew / AC / **Power / Mass / Hardpoints**. Fittings (weapons, defenses, drives,
workshop, cargo…) each cost power, mass and sometimes a hardpoint; a hull's
budget is its three numbers. Modifying a ship later = the same fittings list.
**Output:** a stat block the SWN ship combat runs on directly.
**Time:** ten minutes; the three budgets make it a checklist, not arithmetic.

#### WEG GG6: Tramp Freighters — *read from OCR, ch. 8*

**Unit:** **a stock hull, modified**. No building from scratch: start with a stock
ship (Stock Ships, 40150, is a catalogue of them), then *modify or replace* a
system — hull, manoeuvrability, space, shields, hyperdrive, weapons, sensors, cargo
— each modification a repair-skill **difficulty** and a **cost** (as a percentage
of the ship's value), with **design limits** on how far a given hull can go. Used
parts cost less and fail more. Maintenance overhauls and a 2D hyperdrive-
malfunction roll for neglected ships.
**Output:** a WEG ship stat block, changed.
**Time:** minutes per modification; the campaign is *paying* for them.

#### SW5e Starships of the Galaxy — *on disk, to read*

5e-shaped: ship "tiers", deployments (roles for crew), ship sizes; a construction
chapter (to read).

#### Saga Starships of the Galaxy — *OCR in progress*

Templates by size class; a modification system with emplacement points; ship
"quality". Section when the text is in.

#### White Star — *read: contents*

Stock ships (20) and a **Starship Modifications** section (p. 147); a mecha builder
(hard points, programs, chassis modifications, ch. 8) that is the most build-like
thing in the book.

#### Star Frontiers: Knight Hawks — *on disk, to verify*

Hull sizes 1–20; engines, weapons, defences and cargo bought per hull size against a
credit budget; the earliest hull-plus-fittings builder in the genre (1983).

#### Ships — side by side

| System | Unit | Budget | Output | Time |
|---|---|---|---|---|
| Traveller | tonnage | tons + credits | full combat block | an hour |
| SWN | **hull + fittings** | power, mass, hardpoints | full combat block | 10 min |
| WEG GG6 | **stock hull, modified** | credits + difficulty + design limits | WEG block | minutes each |
| Star Frontiers KH | hull size + systems | credits | KH block | 30 min |
| White Star | stock + mods; mecha hard points | credits | S&W block | minutes |
| Saga | templates + emplacement points | — | — | pending |

**Reading:** two families. **Build** (Traveller, SWN, Knight Hawks): a hull with
budgets, fill it. **Modify** (WEG, White Star): a stock ship, change it, pay. Star
Wars fiction is the second — nobody designs the *Falcon*, they *modify* it — and
WEG's version has the two things Core wants: a difficulty (a roll) and a limit. SWN's
three-number budget is the cleaner data model for a catalogue, and it is what a
`content/ships.yaml` would want underneath either presentation.

---

### C. Droids

See `Droid_Models_Compared.md`. In one line each: **WEG Cynabar's** — build like a
vehicle, part by part, three skills, a cost; **Saga Scavenger's** — a chassis
"treated as a species" (eight, by Degree) plus a parts catalogue with ~50
accessories and adjudication rules; **SWN** — an origin focus (the race menu) and a
type that is fiction; **White Star** — a class. The chassis half is the race
builder; the parts half is the ship-modification chapter. There is no third
procedure anywhere.

---

### What the evidence points at (readings, not rulings)

1. **Every generator here is one of two shapes: roll-down-a-list, or
   stock-then-modify.** Planets are the first (Traveller, SWN, Saga UR); ships in
   Star Wars are the second (WEG); droids are both halves at once (chassis, then
   parts). A game needs *two* generator mechanisms, not five.
2. **The Star Wars planet fields are settled since 1991 and never changed** — GG8's
   template is Saga UR's table list. Star Crawler does not design the fields; it
   writes the tags.
3. **WEG's ship chapter is the only one that prices a modification as a *roll*.**
   That is the engine-native version, and it is what a tramp-freighter campaign
   spends its money on. The build-from-scratch models exist for referees, and SWN's
   hull budgets are the data shape to store a stock ship in either way.
4. **The tag is the missing piece in every Star Wars generator**, and it is the one
   piece that is pure content — a d100 list, in this game's voice, with Enemies /
   Friends / Complications / Things / Places under each. That is a week of writing
   and no rules.

---

## 7. Appendix A: the sources

*Source: `research/SOURCES.md`*

*2026-09-20 (rev. 2: library moved to `H:\RPG_NEW`; paths in `tools/paths.py`). Organised by the research axes in `README.md`. "Chapter" means the
part of the book I actually need; the rest can stay closed. Every item says why.*

### A. Already on disk — no action

The WEG library at `H:\RPG_NEW_GAME_SYSTEMS\Star Wars\d6\` covers every axis (`The Rancor Pit`, `Galaxy Guides`, `supplements`, `companions and sourcebooks`). Product
codes resolved against the WEG catalogue; scans without a text layer are marked
**(scan)** and will need OCR or reading by eye.

| Axis | Book | File | Chapter needed |
|---|---|---|---|
| Races — corpus | rancorpit *Aliens Stats* (every WEG species) | `The Rancor Pit/Aliens_Stats.pdf` | **extracted**: 449 species |
| Races — the builder | **Galaxy Guide 4: Alien Races, 2e** (40094) | `Galaxy Guides/WEG40094.pdf` (scan) | the intro chapter on creating alien species; the "Story Factors" convention |
| Races — corpus 2 | **Alien Encounters** (40166) | `supplements/WEG40166.pdf` (scan) | the species format; near-human guidance |
| Races — worked examples | GG12 Aliens: Enemies and Allies (prob. 40087) | `Galaxy Guides/WEG40087.pdf` (scan) | skim |
| Classes / chargen | **Heroes and Rogues** (40086) | `supplements/WEG40086.pdf` | the template-building and background chapters |
| Classes / chargen | REUP (R&E core) | `REUP.pdf` | ch. 2 Characters, the Templates section |
| Force — corpus | rancorpit *Force Powers* | `The Rancor Pit/Force_Powers.pdf` | **extracted**: 122 powers |
| Force — the rules | **Tales of the Jedi Companion** (40082) | `companions and sourcebooks/WEG40082.pdf` | the Force chapter: learning, Force Points, Dark Side Points |
| Force — the rules | REUP | `REUP.pdf` | the Force chapter |
| Force — dark side | GG14 The Dark Side (fan) | `Galaxy Guides/gg14tds.pdf` | skim; fan work, tag as such |
| Droids — corpus | rancorpit *Droids Stats* | `The Rancor Pit/Droids_Stats.pdf` | **extracted**: 319 droids, Degree → category preserved |
| Droids — builder | **Cynabar's Fantastic Technology: Droids** (40116) | `supplements/WEG40116.pdf` | the droid construction / modification chapter |
| Planets — generator | **Galaxy Guide 8: Scouts** (40061) | `Galaxy Guides/WEG40061.pdf` (scan) | the world-generation system, the whole thing |
| Planets — examples | **The Planets Collection** (40100) | `supplements/WEG40100.pdf` | the planet template format only |
| Ships — builder | **GG6: Tramp Freighters, 2e** (40095) | `Galaxy Guides/WEG40095.pdf` (scan) | ship modification and customisation |
| Ships — examples | **Stock Ships** (40150) | `supplements/WEG40150.pdf` | format only |
| Ships — corpus | rancorpit *Starships Stats R&E* | `The Rancor Pit/Starships_Stats_R&E_censored.pdf` | to extract if a ship corpus is wanted |
| SW5e — all | Player's Handbook | `../5e/SW5e - Player's Handbook.pdf` | **extracted**: 30 species, 200 powers; classes ch. 3 still to read |
| SW5e — ships | Starships of the Galaxy | `../5e/SW5e - Starships of the Galaxy - 20210316.pdf` | ship construction chapter |
| OSE races | Mutant's `OSE_Race_Abilities_Analysis.md` | `H:\Project Mutant\research\` | reuse as-is |

### B. OSR and sci-fi — on disk as of 2026-09-20

Found in `01_GAME_SYSTEMS` and the `07_COLLECTIONS_AND_ARCHIVES/O-S-R archive`.
Paths in `research/tools/paths.py`. Chapters I need, and why:

| System | Where | Chapters | Why |
|---|---|---|---|
| **Star Adventurer** (RPGPundit) | `RPGPundit/Star Adventurer/` | all of it — it is short | the OSR Star Wars knockoff by the author whose "medieval-authentic" method is closest to Core's; races, the Force-analogue, ships |
| **White Star Galaxy Edition** + *Walking the Way* | `White Star/` | Classes (Star Knight, Alien Brute, Alien Mystic, Robot); Meditations; Starships; *Walking the Way* whole | the Star Knight is the "Jedi as class" test case; *Walking the Way* is a whole book on the Force-analogue |
| **Stars Without Number Revised** (Deluxe) | `O-S-R archive/Stars Without Number/` | ch. 2 Character Creation; ch. 5 Psionics; ch. 7 Starships; ch. 8 Sector Creation | the modern OSR standard for ship builder and planet generator |
| **Worlds Without Number** | `Worlds Without Number/` | Character creation (Foci); the world-building tags | SWN's sibling; Foci are a class-free build worth seeing |
| **Classic Traveller Book** | `Traveller/` | Character Generation; Worlds (UWP); Starships (design) | the ancestor of every world and ship generator |
| **Star Frontiers** Alpha Dawn + Knight Hawks | `O-S-R archive/Star Frontiers/` | AD: Races; KH: ship construction | four fixed-package races, 1982; earliest "race as package" |
| **X-Plorers** | `O-S-R archive/X-Plorers/` | Classes | four-class minimal end |
| **Hulks & Horrors** | `O-S-R archive/Hulks & Horrors/` | Classes, Races | races as classes |
| **Starships & Spacemen 2e** | `O-S-R archive/Starships & Spacemen/` | Classes, Races, Ships | Trek-shaped, but a Labyrinth Lord-based race and ship model |
| **Star Dogs**, **Space Dungeon**, **BX-Space**, **Machinations of the Space Princess** | `O-S-R archive/` | skim: races and psionics chapters | the long tail; each gets a line in the comparison, not a section |

### B2. Arrived in `99_INBOX`, 2026-09-20

| Book | File | Text layer | Chapters I need |
|---|---|---|---|
| **FFG Force and Destiny** | `Force_and_Destiny.pdf` | **scan — needs OCR** | ch. 8 The Force; Morality and Conflict |
| **FFG Edge of the Empire** | `Edge_of_the_Empire.pdf` | **scan — needs OCR** | ch. 2 Character Creation (species, careers); ch. 7 Starships; ch. 8 The Force |
| **d20 Revised Core Rulebook** | `d20_star_wars-revised_core_rulebook.pdf` | OCR'd 2026-09-20 | ch. 2 Species; ch. 9 The Force |
| **Ultimate Alien Anthology** | `d20_star_wars-ultimate_alien_anthology.pdf` | OCR'd 2026-09-20 | **extracted**: 161 species, 1,033 traits → `corpora/uaa/species.yaml` |
| **Saga: Scum and Villainy** | `d20_star_wars-scum_and_villainy.pdf` | yes | ch. 1 Character Options (species, talents) |

**OCR:** no engine on this machine. Cheapest route is `pip install winocr` (uses the
OCR built into Windows 10, no system install); best quality is Tesseract via
`winget install UB-Mannheim.TesseractOCR`. Either is Dan's call. Until then the four
scans can be read page-by-page as images, which is fine for a rules chapter and not
fine for a 180-species corpus.

### C. Not free — still to source

Ordered by how much the research depends on them.

| # | Book | Chapters I need | Why |
|---|---|---|---|
| 1 | **Star Wars Saga Edition Core Rulebook** (WotC 2007) | ch. 2 Species; ch. 3 Heroic Classes; ch. 6 The Force (Use the Force, Force powers, Dark Side Score); ch. 12 Droid Heroes | the best-regarded d20 Star Wars; species are fixed packages with a **priced** format; droids are a species-with-systems; the Force is a *feat-gated power list* |
| 2 | **Saga: The Unknown Regions** | the Near-Human species builder; Creating New Beasts; **Creating New Worlds** | Saga's only race builder and its planet generator, in one book |
| 3 | **Saga: Scavenger's Guide to Droids** | Droid construction; systems and accessories | the fullest droid builder in any Star Wars game |
| 4 | **Saga: Starships of the Galaxy** | Starship construction; modifications | the Saga ship builder |
| 8 | **Scum and Villainy** (Evil Hat, FitD) | Playbooks; Ship playbooks | the modern SW knockoff; ship-as-character is worth seeing even though the engine is different |
| 8b | **Mothership 1e Player's Survival Guide** (free from Tuesday Knight) | Classes | four classes, one is the robot: "droid as class" — the only free item still missing |
| 9 | **WEG Galaxy Guide 4: Alien Races, 1e** (40041) — only if 40094 scan is unreadable | species creation guidance | backup |
| 10 | **Cynabar's** is on disk; **Gundark's Fantastic Technology** (40158) optional | gear format | low priority |

### D. Wookieepedia — reference, not corpus

Wookieepedia's Legends pages are the canon-tagging authority (every Legends article
carries the tab). I cannot fetch Fandom pages from here (they return a paywall
response), so canon disputes get resolved by you reading the page. The corpora
carry `canon:` per record so the disputes are findable.

### What happens when the books arrive

Each book gets a corpus extraction where it is a corpus (Saga species, UAA
species, FFG species; droids from Cynabar's and Scavenger's) and a section in the
comparison file where it is a model. The comparison files are written axis by axis
in this order: **Races → Droids → Force → Classes → Generators**, because that is
the order the design questions are blocking in.

---

## 8. Appendix B: the research programme

*Source: `research/README.md`*

*How other games do the three things Star Crawler has to decide — races, classes,
the Force — before Star Crawler decides them. Draft stage: this folder produces
evidence, not rulings. A file here is the provenance a later decision points at.*

*Method is Project Mutant's `research/`: the same questions asked of every system,
a comparison table, then a synthesis that says what the evidence supports. Where a
source is a corpus (WEG's 435 species, 133 Force powers), it is extracted to data
and counted, not summarised from memory.*

### The three axes and the questions asked of every system

**Races.** How many? Fixed package or built? What does a race give — attribute
shifts, size, speed, senses, special abilities, a drawback, a story hook? Is there
a *race builder* for new species, and what does it look like? How is a race priced
against another? Do racial abilities fit Core's 55 shapes, and which do not?

**Classes.** Are there any? How many, and what is the axis — role, attribute,
archetype, career? Is the Force-user a class or a layer? Multi/prestige? What does a
level give? How does a non-Force character stay relevant next to one?

**The Force.** A class, a skill, a pool, a power list? Bought, rolled, or granted?
What does a power cost to use — points, a roll, nothing? Is there a dark side and is
it a resource, a meter, a cost, or fiction? How many powers, and what *shapes* are
they — how many are automatic hits, immunities, undetectability, undo (the
never-list)? What does the game do about lightsabers?

**Droids.** A species, a class, a build, or equipment? SW5e makes the five Legends
droid classes (I–V, from WEG's *Droids* sourcebook, 1988) into species; WEG stats
droids like characters; Saga has droid *systems* bought like gear. Which taxonomy, and
is there a droid *builder* — and does it share a procedure with the race builder?

**Generators.** Three the game needs and every sci-fi OSR game has an answer to:
a **planet** generator (Traveller's UWP is the ancestor; SWN's world tags are the
modern standard; WEG's *Planets Collection* and *Galaxy Guide 8: Scouts* are the
Star Wars ones), a **ship** builder (SWN, Traveller, WEG *Tramp Freighters* /
*Starships of the Galaxy*, SW5e *Starships of the Galaxy*), and a **droid**
builder (WEG *Cynabar's Fantastic Technology: Droids*, Saga *Scavenger's Guide to
Droids*). The questions: what is the unit of build (hull + fittings? points?
tables?), does it produce a stat block Core can fight with, and how long does it take.

### Canon

**Dan's working position: Star Crawler is Legends.** Every corpus record carries
`canon:` — `legends`, `disney`, `both`, or `n/a` for a rule rather than a thing.
WEG (1987–99) and WotC (2000–10) are Legends by definition. SW5e and anything
post-2014 is tagged per record, in one lookup table per extractor so the judgement
can be argued with. Nothing enters `content/` without the tag.

### Systems

| System | Kind | Where | Status |
|---|---|---|---|
| WEG Star Wars d6 (REUP, 2e R&E) | licensed, 1987–99 | `<library>/Star Wars/d6/` — REUP, The Rancor Pit compilations, Galaxy Guides, supplements (paths in `tools/paths.py`) | **read; 3 corpora extracted** |
| WotC Star Wars RCR (d20, 2002) + Ultimate Alien Anthology | licensed | `99_INBOX` (scans, OCR'd) | **read; UAA extracted** |
| WotC Saga Edition (2007) + Unknown Regions, Scavenger's Guide | licensed | `D:/RPG DOWNLOAD/Star Wars Saga Edition` (OCR'd) | **read** |
| FFG Edge of the Empire / Force and Destiny | licensed | `99_INBOX` (scans, OCR'd) | **read** |
| SW5e (fan, 5e) | fan | `H:\RPG\Game Systems\Star Wars 5e\` — PHB, Scum & Villainy | on disk |
| White Star (S&W-based) | OSR knockoff | web | to find |
| Stars Without Number (rev.) | OSR sci-fi, psionics | web | to find |
| Star Adventurer / Star Crawl / X-plorers / Hulks & Horrors | OSR sci-fi | web | to find |
| Mothership | OSR-adjacent sci-fi, no powers | web | for classes only |
| Scum and Villainy (FitD) | SW knockoff | web; a d6 conversion is in rancorpit | to find |
| Star Frontiers / Traveller (Cepheus) | pre-OSR sci-fi, race and career models | web | to find |
| OSE (via Mutant's `OSE_Race_Abilities_Analysis.md`) | the vocabulary's source | `H:\Project Mutant\research\` | done, reuse |
| Project Mutant | the sibling: Family pool + Strains | `H:\Project Mutant\` | done, reuse |

### Outputs

| File | What it establishes |
|---|---|
| `corpora/weg/species.yaml` | **done** — 449 WEG species, 831 special abilities, Legends |
| `corpora/weg/force_powers.yaml` | **done** — 122 WEG Force powers by C/S/A axis and side, with provenance tiers (published / converted / fan) |
| `corpora/sw5e/species.yaml` | **done** — 30 SW5e species incl. droid classes I–V, 360 traits, canon-tagged |
| `corpora/sw5e/force_powers.yaml` | **done** — 200 SW5e Force powers by level and side |
| `corpora/weg/droids.yaml` | **done** — 319 WEG droids with the Degree → category taxonomy (5 Degrees, 26 categories) |
| `corpora/uaa/species.yaml` | **done** — 161 UAA species (d20 RCR format), 1,033 traits, from OCR; Legends |
| `Race_Models_Compared.md` | **drafted, all systems** — WEG measured + its builder (Alien Encounters), UAA measured, Saga, FFG, Star Adventurer, White Star, SWN |
| `Class_Models_Compared.md` | **drafted, all systems** — WEG templates, RCR, Saga, SW5e, Star Adventurer, White Star, SWN, Mutant |
| `Force_Models_Compared.md` | **drafted, all systems** — WEG measured (60/76 fixed, 13 opposed), RCR, Saga (suite), FFG (rating + trees), SW5e, Star Adventurer, White Star |
| `Species_Shape_Fit.md` | **next** — WEG's 831 + UAA's 1,033 species abilities mapped to the 55 shapes. Which do not fit, and why. |
| `Droid_Models_Compared.md` | **drafted, all systems** — WEG corpus, SW5e, Saga Scavenger's (chassis-as-species), White Star, SWN |
| `Generators_Compared.md` | **drafted** — planets (Traveller, SWN, GG8, Saga UR), ships (Traveller, SWN, GG6, White Star), droids cross-ref |
| `RESEARCH.md` | **generated** — all five comparisons as one reading copy (`tools/build_research.py`) |
| `Synthesis.md` | **after `Species_Shape_Fit`** — what the evidence supports for Star Crawler. Draft positions, not decisions. |

---

## 9. Appendix C: what has been extracted

*Generated from the corpus files themselves.*

| File | Corpus | Records | Canon |
|---|---|---|---|
| `corpora/sw5e/force_powers.yaml` | SW5e Player's Handbook | 200 | mixed |
| `corpora/sw5e/species.yaml` | SW5e Player's Handbook | 30 | mixed |
| `corpora/uaa/species.yaml` | Ultimate Alien Anthology species (WotC 2003, d20 Revised) | 161 | legends |
| `corpora/weg/droids.yaml` | WEG Star Wars d6 droids | 319 | legends |
| `corpora/weg/force_powers.yaml` | WEG Star Wars d6 Force powers | 122 | legends |
| `corpora/weg/species.yaml` | WEG Star Wars d6 species | 449 | legends |

**OCR'd to text** (sidecars, not committed): `alien_encounters`, `ffg_eote`, `ffg_fad`, `gg4_alien_races`, `gg6_tramp_freighters`, `gg8_scouts`, `rcr`, `saga_core`, `saga_jedi_academy`, `saga_starships`, `uaa`.

Rebuild any corpus with `python research/tools/extract_*.py`; re-OCR with `python research/tools/ocr.py <slug>`.

