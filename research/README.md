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
| `weg_species.yaml` | Every WEG species, extracted: attribute dice, move, size, special abilities as text. The corpus. |
| `weg_force.yaml` | Every WEG Force power: the CSA axis, difficulty, effect text. The corpus. |
| `Race_Models_Compared.md` | Every system's race model against the race questions. Includes the builders. |
| `Class_Models_Compared.md` | Every system's class model against the class questions. |
| `Force_Models_Compared.md` | Every system's Force model. Counts of never-list violations per system. |
| `Species_Shape_Fit.md` | WEG's 435 species' abilities mapped to the 55 shapes. Which do not fit, and why. |
| `Synthesis.md` | What the evidence supports for Star Crawler. Draft positions, not decisions. |
