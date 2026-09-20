# RESEARCH

*How other games do the three things Star Crawler has to decide — races, classes,
the Force — before Star Crawler decides them. Draft stage: this folder produces
evidence, not rulings. A file here is the provenance a later decision points at.*

*Method is Project Mutant's `research/`: the same questions asked of every system,
a comparison table, then a synthesis that says what the evidence supports. Where a
source is a corpus (WEG's 435 species, 133 Force powers), it is extracted to data
and counted, not summarised from memory.*

## The three axes and the questions asked of every system

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

## Canon

**Dan's working position: Star Crawler is Legends.** Every corpus record carries
`canon:` — `legends`, `disney`, `both`, or `n/a` for a rule rather than a thing.
WEG (1987–99) and WotC (2000–10) are Legends by definition. SW5e and anything
post-2014 is tagged per record, in one lookup table per extractor so the judgement
can be argued with. Nothing enters `content/` without the tag.

## Systems

| System | Kind | Where | Status |
|---|---|---|---|
| WEG Star Wars d6 (REUP, 2e R&E) | licensed, 1987–99 | `H:\RPG\Game Systems\Star Wars d6\` — REUP.pdf, rancorpit `Aliens_Stats.pdf` (435 species), `Force_Powers.pdf` (133 powers), Galaxy Guides, `WEG40065` (Tales of the Jedi Companion — Force) | on disk |
| WotC Star Wars RCR (d20, 2002) + Ultimate Alien Anthology | licensed | web | to find |
| WotC Saga Edition (2007) | licensed | web | to find |
| FFG Edge / Age / Force & Destiny (2013–) | licensed | web | to find |
| SW5e (fan, 5e) | fan | `H:\RPG\Game Systems\Star Wars 5e\` — PHB, Scum & Villainy | on disk |
| White Star (S&W-based) | OSR knockoff | web | to find |
| Stars Without Number (rev.) | OSR sci-fi, psionics | web | to find |
| Star Adventurer / Star Crawl / X-plorers / Hulks & Horrors | OSR sci-fi | web | to find |
| Mothership | OSR-adjacent sci-fi, no powers | web | for classes only |
| Scum and Villainy (FitD) | SW knockoff | web; a d6 conversion is in rancorpit | to find |
| Star Frontiers / Traveller (Cepheus) | pre-OSR sci-fi, race and career models | web | to find |
| OSE (via Mutant's `OSE_Race_Abilities_Analysis.md`) | the vocabulary's source | `H:\Project Mutant\research\` | done, reuse |
| Project Mutant | the sibling: Family pool + Strains | `H:\Project Mutant\` | done, reuse |

## Outputs

| File | What it establishes |
|---|---|
| `corpora/weg/species.yaml` | **done** — 449 WEG species, 831 special abilities, Legends |
| `corpora/weg/force_powers.yaml` | **done** — 122 WEG Force powers by C/S/A axis and side, with provenance tiers (published / converted / fan) |
| `corpora/sw5e/species.yaml` | **done** — 30 SW5e species incl. droid classes I–V, 360 traits, canon-tagged |
| `corpora/sw5e/force_powers.yaml` | **done** — 200 SW5e Force powers by level and side |
| `corpora/weg/droids.yaml` | **done** — 319 WEG droids with the Degree → category taxonomy (5 Degrees, 26 categories) |
| `corpora/uaa/species.yaml` | **done** — 161 UAA species (d20 RCR format), 1,033 traits, from OCR; Legends |
| `Race_Models_Compared.md` | **first draft** — WEG measured; Star Adventurer, White Star, SWN read; Saga/RCR/FFG pending |
| `Class_Models_Compared.md` | Every system's class model against the class questions. |
| `Force_Models_Compared.md` | **first draft** — WEG measured (60/76 fixed-difficulty, 13 opposed), RCR, SW5e, Star Adventurer, White Star; Saga/FFG pending |
| `Species_Shape_Fit.md` | WEG's 435 species' abilities mapped to the 55 shapes. Which do not fit, and why. |
| `Droid_Models_Compared.md` | **first draft** — WEG corpus, SW5e, Saga Scavenger's (chassis-as-species), White Star, SWN |
| `Generators_Compared.md` | **first draft** — planets (Traveller, SWN, GG8, Saga UR), ships (Traveller, SWN, GG6, White Star), droids cross-ref |
| `Synthesis.md` | What the evidence supports for Star Crawler. Draft positions, not decisions. |
