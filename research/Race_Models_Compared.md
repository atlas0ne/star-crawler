---
title: "Race Models Compared"
status: SCAFFOLD
---

# Race Models Compared

*How eleven games build a playable species, asked the same questions. Draft stage:
this file produces evidence, not rulings. Numbers come from `corpora/`; a claim with
no number behind it is a reading. Written 2026-09-20; FFG, Saga and UAA sections are
placeholders until their text is in.*

## The questions

1. How many races, and are they *species* (Wookiee) or *archetypes* (Brute)?
2. Fixed package or built? If built, with what currency?
3. What does a race give — attribute shifts · size · speed · senses · special
   abilities · a drawback · a story hook · languages?
4. Is there a **race builder** for new species, and what does it look like?
5. How is one race priced against another?
6. Do the abilities fit Core's 55 shapes? Which do not?
7. Where does the robot / droid go?

## The systems

### WEG Star Wars d6 (1987–99) — *corpus: 449 species, 421 statted*

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

### SW5e (fan, 5e) — *corpus: 30 species, 360 traits*

| | |
|---|---|
| How many | 30 in the PHB incl. **five droid classes as species** |
| Fixed or built | fixed, 5e-style |
| What it gives | 12 traits each, always: Ability Score Increase · Age · Alignment · Size · Speed · Languages, plus 4–8 specials (Wookiee: Claws, Darkvision, Hide, Menacing, Powerful Build, Treeclimber) |
| Race builder | none in the PHB |
| Pricing | 5e's implicit budget (+2/+1, one or two "ribbons", one real ability) |
| Shape fit | all 5e shapes: proficiency, advantage, natural weapon, darkvision, climb speed. Advantage does not exist in Core (Module, off); proficiency does not exist in Core. |
| Droids | **species**, one per Degree, with shared Droid traits (resistances, no eat/breathe, ion vulnerability, Force-insensitive) + per-class differences |

### Star Adventurer (RPGPundit, OSR) — *read in full*

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

### White Star Galaxy Edition (S&W WhiteBox) — *read: classes, mysticism*

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

### Stars Without Number Revised — *read: pp. 199, 209*

| | |
|---|---|
| How many | none by default; humans |
| Fixed or built | **built by the GM, from a menu** |
| What it gives | an alien race is an **Origin Focus**: GM picks **two** from — Aptitude for Violence (+1 attack) · Environmental Native · Innate Ability (2–3 items' worth, or one psionic technique) · Natural Defenses (AC 15 + ½ level) · Origin Skill · Psychic Aptitude · Shapeshifting · Strong Attribute (+1 mod) · Tough (first HD maxed) — "or three if a couple are minor" |
| Race builder | **yes, this is one**, a page long |
| Pricing | the race **costs the player's free focus pick** — one price, paid once, same for every race. Flaws explicitly *not* a balance tool ("players pick classes unhindered by the flaw") |
| Shape fit | every menu item is a Core shape |
| Droids | VI PCs are the **same mechanism**: an origin focus, with the VI special rules (no sleep/eat, vacuum-immune, poison-immune, no Psychic class) |

### Hulks & Horrors — *read: contents*

Races are classes (Hovering Squid, Omega Reticulan, Bearman) beside the human
classes (Pilot, Scientist, Soldier, Psyker). Race-as-class, White Star's model.

### X-Plorers — *read: p. 28*

Humans only as PCs. "Alien Races" is a creature-building section: standard stat
blocks plus a special-abilities list (Swallow, Swarm, Web…). The race builder is
for monsters. Nothing for us on the PC side; the monster builder is the same shape
as Saga's *Creating New Beasts*.

### Star Frontiers (TSR 1982) — *to read; from memory, to verify*

Four races, fixed: Human, Dralasite, Vrusk, Yazirian. Each: ability-score
adjustments, one or two special abilities (Dralasite lie detection + elasticity,
Vrusk comprehension + ambidexterity, Yazirian battle rage + gliding + night vision).
The earliest "race as a small fixed package" in the genre.

### OSE — *via Mutant's `OSE_Race_Abilities_Analysis.md`*

21 races. The two-free-traits parity rule, the Light Sensitivity drawback template,
the Gargantua size finding. Race-as-class in B/X; Advanced splits them. Reuse as-is.

### Project Mutant — *the sibling*

Family (8+ priced pool) → Breed (3+) → Named Variant; bought with Biogen; every
trait has a shape and a price; every Family a behaviour note; free traits at 3 or
under; Signatures may exceed if pre-paid. **The most built model on this list**,
and the one whose tooling this game inherits.

### Saga Edition core (2007) — *read from OCR*

| | |
|---|---|
| How many | **14** in the core (Human, Bothan, Cerean, Duros, Ewok, Gamorrean, Gungan, Ithorian, Kel Dor, Mon Calamari, Quarren, Rodian, Sullustan, Trandoshan, Twi'lek, Wookiee, Zabrak); campaign guides add ~10 each; *Threats* and *Unknown Regions* more |
| Fixed or built | fixed |
| What it gives | Ability Modifiers (Wookiee +4 STR +2 CON −2 DEX −2 WIS −2 CHA) · Size · Speed · 2–4 specials (Extraordinary Recuperation; Rage — once/day, +2 melee, then −1 persistent condition step; Weapon Familiarity) · **Skills** (take 10 on Climb; reroll Persuasion to intimidate) · Automatic Languages. Human: bonus feat + bonus trained skill — **the baseline every species is priced against** |
| Race builder | *Unknown Regions* **Near-Humans**: "substantially the same as Humans … one or more differences" — swap the human bonus feat or bonus skill for one near-human trait from a table (extra arms, darkvision, quick healing …), plus a physical-variation table. A one-trait builder on a human chassis. Also *Creating New Beasts* for monsters |
| Pricing | against the human's feat + skill; a species' package is "worth" about those two |
| Shape fit | ability shifts, natural healing rate, a once-a-day surge with a hangover, take-10 and reroll (which are 3.5 skill mechanics Core lacks) |
| Droids | ch. 12: droid heroes with a standard score package; the five Degrees named in prose; Scavenger's Guide makes the chassis a species |

### UAA (d20 RCR format) — *corpus: 161 species, 1,033 traits*

Every entry: Ability Modifiers (152 of 161) · size (Medium 109, Small 23, Large 12)
· Speed (147) · Free Language Skills (140) · then 1–5 specials. Modal specials:
Bonus Feat 54 · Natural Armor 32 · Skill Bonus(es) 52 · Natural Weapon(s) 23 ·
Low-Light Vision 14 · Darkvision 10 · Extra Limbs 10 · Breathe Underwater 8 ·
Damage Reduction 6 · **Primitive** 15 (a drawback: no proficiency with modern gear)
· Xenophobic 4. Median 5–6 traits, of which three are the boilerplate (mods, size,
speed, languages) — so **2–3 real abilities per species**, one more than WEG's
1–2, with d20's bonus feat doing the work WEG's skill bonus did.

### FFG — *OCR done; section to write*

Species as characteristic spreads (1–4 across six) + wound/strain thresholds +
starting XP + one special ability. Section next.

## Side by side

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
| Saga / RCR / FFG | — | species | fixed | Near-Human | vs human baseline | Saga: species+systems |

## What the evidence points at (readings, not rulings)

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

## Still to do in this file

- Saga, RCR/UAA, FFG sections from OCR text; UAA extracted as a corpus.
- ~~GG4~~ done: GG4 has only the format; the builder is Alien Encounters ch. 1 / GG8 ch. 7.
- Star Frontiers verified from the book.
- `Species_Shape_Fit.md`: the 831 WEG abilities mapped to the 55 shapes, properly,
  by a script with a reviewed mapping table — the crude families above are a
  first cut only.
