# Crawler Core — the engine

*Version 0.2.0-draft. The rules every game on this engine shares. A game copies this
file verbatim and records anything it does differently in its `DIVERGENCES.md`.*

*"The referee" below means whoever runs the game, by whatever name that game gives them.*

---

## 1. Resolution

**Four rolls, and which one depends on what is being resolved.**

| To resolve | Roll | Against |
|---|---|---|
| An attack | d20 + Attack Bonus + attribute modifier | Armour Class |
| A saving throw | d20 + save bonus + attribute modifier | a target — **OPEN**, see Modules: Mutant fixes it at 15; S&S sets it by threat; the author is deciding |
| A check with no trait covering it | 2d6 + attribute modifier | **easy 7 / ordinary 9 / hard 11.** The referee names the row. Help, time and tools make a check easy |
| A trait that states its own chance | what the trait says | usually **x-in-6** |

**Most of the time there is no roll.** A trait that lets a character do something says
so and states its own chance. The 2d6 check is the fallback for the moment nothing on
the sheet covers what was just tried. The referee names the attribute; there is no
skill list.

**Help makes a check easy.** A second pair of hands is the same thing as time and tools.

**Where each thing lives.** What a character *is* is a number on the sheet. What the
*world* is, is the target. What the character *did*, or the state they are in, is
which row of the table they are on. Nothing is ever two of those at once.

**Opposed rolls:** both roll 2d6 + the attribute; higher wins; the defender wins ties.

**On a natural 1 a save fails and an attack misses, whatever the modifiers. On a natural
20 a save succeeds and an attack hits.**

## 2. Attributes

Six, 3d6 each: STR, DEX, CON, INT, WIS, CHA. **The modifier table is B/X's own bands:**

| Score | Modifier |
|---:|:--:|
| 3 | −3 |
| 4–5 | −2 |
| 6–8 | −1 |
| 9–12 | 0 |
| 13–15 | +1 |
| 16–17 | +2 |
| 18 | +3 |

STR adds to melee attack and damage. DEX adds to missile attack, initiative and AC.
CON adds to hit points at every level. **A game may add a rule that moves scores off
the 3d6 range; the table extends the same curve in both directions.**

## 3. Hit points and hit dice

**One Hit Die per level. At Level 1, the die's highest value rather than a roll.** Every
later level is rolled. CON applies every level, and a level never gives fewer than 1.

**A monster's Hit Die is a d8.** Its Attack Bonus is HD − 1, minimum 0. Half a Hit Die
is 1d4 hit points at +0. Monsters have no attribute scores and add nothing.

**At 0 hit points a character is Helpless** — unconscious or dying, as the game rules.
Attacks against a Helpless creature hit automatically.

## 4. Armour Class

**AC = 10 + DEX modifier + natural armour + worn armour + shield.** One suit of worn
armour at a time. A shield stacks with everything. **Natural armour sources never stack
with each other:** take the single best. Natural and worn armour stack, because hide
under a coat is two layers.

## 5. The round

**A round is about ten seconds.** Everyone acts once, in initiative order.

**Initiative is d20 + DEX modifier, high first, rolled once at the start of an
encounter and kept for the whole of it.** Ties go to the player.

**On your turn: move up to your Speed, and do one thing** — either order, or split the
movement around the action. The one thing is usually an attack, but it is equally using
an item, dragging somebody, opening a stuck door, or anything a trait says costs an
action. **Instead of moving and acting, run flat out:** double Speed, nothing else.

**A hit never does less than 1 damage.**

**A target that does not know you are there is attacked at +2.** That is the only
positional advantage in Core.

**Carrying somebody** of your size or larger halves your Speed; somebody smaller costs
nothing.

**Leaving a melee.** Walk away from an enemy you are in melee with and it attacks you
once, free, as you go. Move at half speed instead and it does not.

## 6. Grappling

**Opposed 2d6 + STR, as your action. Higher wins; the defender wins ties.**

* **±2 for every size step of difference.**
* **+2 for a creature whose block or traits give it a grab, a crushing bite or a
  constriction** — a tagged trait, or *grab* on an attack line. Nothing else qualifies,
  and the referee does not decide it mid-fight.
* **On a win the target is held:** it cannot move or attack. (Each game names the
  condition — *Entangled*, *Restrained* — and it means this.)
* **Holding on costs nothing.** While you hold it you may squeeze instead of attacking,
  for your STR modifier or your natural weapon damage, whichever is higher.
* **Escaping is their action:** opposed 2d6 + STR or DEX, their choice, against your
  2d6 + STR.

## 7. Combat manoeuvres

**Anyone can try any of these. No training, no prerequisite.** Each is your action and
each is an opposed 2d6 roll on the attribute named; higher wins, defender wins ties.

| Manoeuvre | Roll | On a win |
|---|---|---|
| **Charge** | no roll — move 10' or more straight at them, then attack | +1 to hit and +1 damage on that strike; you can be Set against |
| **Trip** | STR or DEX, your choice | they are Prone |
| **Shove** | STR | they move 5' where you choose |
| **Disarm** | STR or DEX, your choice | their weapon lands 5' away, direction the referee's |
| **Set against a charge** | no roll — ready a spear or polearm | anything that charges into your reach is hit first, for double damage |
| **Aim** | no roll — spend your action steadying | +2 to hit with your next missile attack |
| **Grapple** | STR, and §6 | they are held |

There is no coup de grâce: attacks against a Helpless creature already hit
automatically.

## 8. Morale

**A creature's willingness to keep fighting, 5–12.** Roll 2d6 against it; higher than
the score and it breaks — flees, surrenders or stops, as makes sense.

**Check Morale when** a group takes its first casualty, and when it is reduced to half
its number. **A creature on its own** has no number to halve: it checks at half its hit
points instead. Never more than twice in an encounter; a creature that has held twice
fights to the end. **Player characters never check.**

An NPC built with a game's character generation has Morale 8 unless the game or the
referee says otherwise.

## 9. Reaction

**When something is met and it is not immediately hostile, roll 2d6 and add the CHA
modifier** and any trait that names reaction rolls.

| 2d6 | Reaction |
|---:|---|
| 2 or less | **Hostile.** It attacks, or does the worst thing available to it |
| 3–5 | **Unfriendly.** It refuses, threatens, or moves against you shortly |
| 6–8 | **Uncertain.** It waits. Talk, offer, threaten — something has to happen |
| 9–11 | **Indifferent to friendly.** It will trade, pass by, or hear you out |
| 12 or more | **Friendly.** It helps, within reason, and keeps helping |

A reaction roll is for what it does now, not what it thinks of you forever.

## 10. Surprise

**Roll 1d6 for each side that might be caught out. On a 1–2 that side is surprised**
and loses its first round. Roll only when neither side knew the other was there. Being
surprised is not being helpless: you are behind, not down.

## 11. Conditions

**A condition earns a name only if two or more different rules grant it and it means the
same thing each time.** Anything granted by one rule is stated in that rule. Each game
keeps its own list under that rule; Core requires only these two meanings:

* **Prone** — −2 to hit, attackers at +2 in melee. Standing up costs half your movement.
* **Helpless** — unconscious, bound, or at 0 hit points. Attacks against you hit
  automatically.

## 12. Time

* **Round** — about ten seconds. One action each. Used in a fight.
* **Turn** — ten minutes. The unit of careful work. A trait that costs a turn cannot be
  used in a fight.
* **Watch** — four hours. The unit of travel and of who is awake.

## 13. The encounter, in order

1. **Surprise.** 1d6 each side that might be caught out.
2. **Distance.** 2d6 × 10' indoors; 4d6 × 10' outdoors. Surprise halves it.
3. **Reaction**, if it is not obviously already hostile.
4. **Initiative**, and then rounds.
5. **Morale**, at the first casualty and at half the group.

Most encounters should end at step 2 or 3.

**Leaving.** If the fleeing side is faster, it gets away, no roll. If it is slower or
equal, 2d6: on 8 or more it escapes, with anything obvious as a modifier — dropping
something worth stopping for is +2. When a party splits, this is per character.

---

## Modules

*Defined once here. Each game declares each one on or off in its `DIVERGENCES.md`.*

| Module | What it is | Status |
|---|---|---|
| **Leaving a melee** | **Core, ruled 2026-09-13.** Walk away from an enemy you are in melee with and it attacks you once, free, as you go. Move at half speed instead and it does not. Measured against OSE's alternative (+2 to be hit, no shield) over 500 retreats: the same cost within a quarter of a character. Kept because it is one sentence every player already knows. Stone & Spear switches back. | settled |
| **Passive Perception** | A static number a stealth roll must beat. On this engine's 2d6 stealth, it is **7 + WIS**. Stone & Spear on; Project Mutant off (its surprise roll does the job). | settled as a Module |
| **Advantage / Disadvantage** | Roll 3d6 and keep the best or worst two. Worth about ±1.5 on 2d6. **Never printed on a sheet** in any game: sheets carry flat modifiers. Optional in both. | settled as a Module |
| **Treasure as XP** | B/X's reward loop. Optional in Project Mutant; declared off in Stone & Spear, which pays for hexes mapped instead. | settled as a Module |
| **Bonus actions** | An extra action slot. Neither game has one; the round is "move and do one thing". Held as data — Stone & Spear tags every feature with what it costs in the round, and if the count asks for the slot, this row changes. | off |
| **Save target** | **OPEN — the author is deciding, and has asked for research first.** Project Mutant: a fixed 15, difficulty as a ± modifier on the source — chosen so that 127 save-bonus traits, and the sim's shell and venom prices, are priced against one number. Stone & Spear: the TN set by the threat — 10 weak, 12 standard, 15 strong, 18 extreme — and every one of 188 bestiary behaviours names its own; S&S has no priced save bonuses yet. Crypt Crawler v3 (unaudited): 10 / 13 / 15. **Votes:** Mutant, Star Crawler and X-Gen for 15, because they share priced content; S&S expects a ruling, not a divergence, and says switching costs it a re-pointing pass. **At the table the two are one roll with the same odds** ("save vs 18" is "save at −3 vs 15"); the difference is what the books print, and whether a save bonus means the same thing in every book. A middle position exists: 15 is the standard, a source may name 10 / 12 / 15 / 18, all bonuses priced against 15 — under which no game changes anything. **The author leans by-threat with a standard anchor** and wants it thought through. Research pointer: in B/X and OSE the save number lives on the character's table and a source only ever *adjusts* it ("save vs poison at −2") — the fixed-plus-modifier idiom; a per-source TN is the 5e idiom. (mail #2, #6, #7, #8, #9) | open |
| **The check ladder** | **Core, ruled 2026-09-13: 7 easy / 9 ordinary / 11 hard, 9 standard.** The games had differed on what the check *is* — Mutant's is a fallback for what no trait covers, Stone & Spear's was the skill game itself on a 7-standard ladder — not on the arithmetic. The author ruled it for S&S after `skillsim.py` ran 3,000 days of survival checks: at 7 an ordinary person succeeds 60% and a level-1 band eats 99 days in 100; at 9, 31% and 82 in 100, which is the game S&S's own Chapter 1 describes. S&S 18.20.0 adopted 9; Star Crawler and X-Gen declared for it; Mutant had it. Four games, one ladder. A game may still say what the check is *for*; the numbers are Core. (mail #6, #7, #8, #9) | settled |
| **Flanking** | For tables using a grid: two enemies in melee with the same target on opposite sides each attack at +1, no stacking. Both games optional. | settled as a Module |

---

*Nothing in this file names a setting, a class, a race, a Family, or a person. If it
does, that line belongs in a game and not here.*
