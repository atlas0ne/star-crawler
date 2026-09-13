# -*- coding: utf-8 -*-
"""Run a fight a few hundred times and say what happened.

The book has a round (6.8), attack maths (6.1), a morale rule (7.9) and a
bestiary (9.11), and none of them has ever been run against another. This
takes a party from generate.py and puts it against monsters from the bestiary
or a warband of other anthros, and runs the fight to the end, N times.

It answers questions the rules cannot answer by being read:

    Does a first-level party of four beat four wild dogs, and how often does
    somebody go down doing it? At what level does a party stop losing people
    to 2 HD things? Does morale end fights before the last hit point does?

WHAT IT MODELS, and only this:
    Initiative d20 + DEX once (6.8). Everyone attacks something living each
    round, melee, d20 + AB + STR vs AC (6.1); a natural 20 hits. Damage is
    the weapon die plus STR. At 0 hp you are down and out of the fight. The
    monster side checks Morale (7.9) at its first casualty and at half, and a
    break ends the fight. Thirty rounds is a draw.

WHAT IT DOES NOT MODEL, deliberately - each is a rule the sim would have to
invent a policy for, and a policy is a design decision:
    Traits in play. Manoeuvres. Missile fire. Healing. Who attacks whom beyond
    "something living". Retreat before the end. Comes Back (6.4).

So the numbers are a FLOOR: a party that does nothing clever. A real table
does better than this, and the gap is what traits and Picks are for.

Usage:
    python tools/skirmish.py --party 4 --vs "Wild Dog" --count 4
    python tools/skirmish.py --party 4 --level 3 --vs "Grizzly Bear"
    python tools/skirmish.py --party 4 --warband 4 --level 2
    python tools/skirmish.py --party 4 --vs "Bandit" --count 6 --runs 1000
    python tools/skirmish.py --party 4 --vs "Wild Dog" --count 4 --show
"""
import argparse
import io
import os
import random
import re
import statistics as st
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
os.chdir(ROOT)
import generate as G  # noqa: E402


# ------------------------------------------------------------------ dice
def roll(rng, expr):
    """'1d6', '2d6', '1d8+1', '1d4'. Returns an int."""
    m = re.match(r"\s*(\d+)d(\d+)\s*([+-]\s*\d+)?", str(expr))
    if not m:
        flat = re.match(r"\s*(\d+)", str(expr))
        return int(flat.group(1)) if flat else 1
    n, d = int(m.group(1)), int(m.group(2))
    mod = int(m.group(3).replace(" ", "")) if m.group(3) else 0
    return sum(rng.randint(1, d) for _ in range(n)) + mod


# ----------------------------------------------------------- combatants
class Fighter(object):
    def __init__(self, name, side, hp, ac, ab, dmg, dex_mod=0, str_mod=0,
                 attacks=1, morale=None):
        self.name, self.side = name, side
        self.hp, self.max_hp, self.ac, self.ab = hp, hp, ac, ab
        self.dmg, self.dex_mod, self.str_mod = dmg, dex_mod, str_mod
        self.attacks, self.morale = attacks, morale
        self.init = 0

    @property
    def up(self):
        return self.hp > 0


def from_character(ch, i):
    """A generate.py Character, as a Fighter."""
    return Fighter(
        "%s (%s %s)" % (ch.breed["name"], ch.size, ch.cls["formal_name"]),
        "party", ch.hp, ch.ac, ch.ab, ch.damage,
        dex_mod=ch._mod(ch.attrs["DEX"]), str_mod=ch._mod(ch.attrs["STR"]))


def parse_attacks(att):
    """Every attack line, as [(count, die), ...]. A bear with two claw lines
    and a bite makes three attacks. 'A or B' on one line takes A."""
    out = []
    for line in (att if isinstance(att, list) else [att]):
        first = str(line).split(" or ")[0]
        m = re.match(r"\s*(\d+)\s*x\s*[^(]*\((\d+d\d+(?:[+-]\d+)?|\d+)", first)
        if m:
            out.append((int(m.group(1)), m.group(2)))
            continue
        m = re.search(r"\((\d+d\d+(?:[+-]\d+)?|\d+)", first)
        out.append((1, m.group(1) if m else "1d4"))
    return out or [(1, "1d4")]


def from_monster(mon, rng, n):
    """A bestiary block, per 9.11: HD sets hp (d8 each) and attack bonus."""
    hd_txt = str(mon["hd"])
    m = re.match(r"(\d+)(?:\+(\d+))?", hd_txt.replace("1/2", "0"))
    hd = int(m.group(1)) if m else 1
    plus = int(m.group(2)) if m and m.group(2) else 0
    hp = max(1, sum(rng.randint(1, 8) for _ in range(max(hd, 1))) + plus) if hd else rng.randint(1, 4)
    ab = max(0, hd - 1)
    routine = parse_attacks(mon.get("attacks") or ["1 x bite (1d4)"])
    f = Fighter("%s #%d" % (mon["name"], n), "foe", hp, int(mon["ac"]), ab,
                routine[0][1], morale=int(mon.get("morale") or 7))
    f.routine = routine
    return f


# --------------------------------------------------------------- the fight
def fight(party, foes, rng, show=False):
    """Returns (winner, rounds, party_down, fled)."""
    everyone = party + foes
    for f in everyone:
        f.init = rng.randint(1, 20) + f.dex_mod
    order = sorted(everyone, key=lambda f: (-f.init, f.side != "party"))
    first_loss_checked = half_checked = False
    fled = False
    for rnd in range(1, 31):
        for f in order:
            if not f.up:
                continue
            targets = [t for t in everyone if t.side != f.side and t.up]
            if not targets:
                break
            routine = getattr(f, "routine", None) or [(f.attacks, f.dmg)]
            for count, die in routine:
              if not targets:
                  break       # a bear whose third attack has nobody left
              for _ in range(count):
                if not targets:
                    break
                t = rng.choice(targets)
                d20 = rng.randint(1, 20)
                hit = d20 == 20 or (d20 != 1 and d20 + f.ab + f.str_mod >= t.ac)
                if hit:
                    dmg = max(1, roll(rng, die) + f.str_mod)
                    t.hp -= dmg
                    if show:
                        print("   r%d  %-28s hits %-24s for %2d%s"
                              % (rnd, f.name, t.name, dmg, "  DOWN" if not t.up else ""))
                targets = [x for x in targets if x.up]
                if not targets:
                    break
        p_up = [f for f in party if f.up]
        f_up = [f for f in foes if f.up]
        if not f_up:
            return "party", rnd, len(party) - len(p_up), False
        if not p_up:
            return "foes", rnd, len(party), False
        # 7.9: the monster side checks at first casualty and at half strength.
        # A creature on its own has no number to halve: half its hit points.
        down = len(foes) - len(f_up)
        check = None
        if len(foes) == 1:
            if f_up[0].hp * 2 <= f_up[0].max_hp and not half_checked:
                half_checked, check = True, "half hit points"
        elif down >= 1 and not first_loss_checked:
            first_loss_checked, check = True, "first casualty"
        elif down * 2 >= len(foes) and not half_checked:
            half_checked, check = True, "half down"
        if check and foes[0].morale is not None:
            ml = foes[0].morale
            if sum(rng.randint(1, 6) for _ in range(2)) > ml:
                if show:
                    print("   r%d  foes break morale (%s, ML %d)" % (rnd, check, ml))
                return "party", rnd, len(party) - len(p_up), True
    return "draw", 30, len(party) - len([f for f in party if f.up]), False


# --------------------------------------------------------------- reporting
def main():
    ap = argparse.ArgumentParser(description="Project Mutant skirmish simulator")
    ap.add_argument("--party", type=int, default=4)
    ap.add_argument("--level", type=int, default=1)
    ap.add_argument("--vs", help="a bestiary creature by name")
    ap.add_argument("--count", type=int, default=4, help="how many of --vs")
    ap.add_argument("--warband", type=int, help="fight N generated anthros instead")
    ap.add_argument("--warband-level", type=int)
    ap.add_argument("--runs", type=int, default=300)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--family", help="every party member from this Family")
    ap.add_argument("--cls", help="every party member this Class")
    ap.add_argument("--size", help="every party member this Size Tier (Tiny/Small/Medium/Large)")
    ap.add_argument("--habitat", help="party drawn from Families found here: urban / farm / wild / water / exotic")
    ap.add_argument("--warband-habitat", help="the warband drawn from here")
    ap.add_argument("--show", action="store_true", help="narrate one fight, then stop")
    ap.add_argument("--roll-hp1", action="store_true",
                    help="6.1 optional rule: roll the first Hit Die (default is its top value)")
    a = ap.parse_args()

    rng = random.Random(a.seed)
    C = G.Corpus()
    best = yaml.safe_load(io.open("content/bestiary.yaml", encoding="utf-8"))
    mon = None
    if a.vs:
        mon = next((c for c in best["creatures"] if c["name"].lower() == a.vs.lower()), None)
        if not mon:
            sys.exit("no creature called %r in the bestiary" % a.vs)
    elif not a.warband:
        sys.exit("give --vs NAME or --warband N")

    results = []
    down_by = {}
    for _ in range(1 if a.show else a.runs):
        chars = []
        while len(chars) < a.party:
            ch = G.Character(C, rng, family=a.family, cls=a.cls, level=a.level,
                             max_hp1=not a.roll_hp1, habitat=a.habitat)
            if a.size and ch.size != a.size:
                continue          # a filter, not a rule: reroll until it fits
            chars.append(ch)
        party = [from_character(c, i) for i, c in enumerate(chars)]
        if mon:
            foes = [from_monster(mon, rng, i + 1) for i in range(a.count)]
        else:
            wl = a.warband_level or a.level
            # the same rules on both sides, or a mirror match is not one
            wchars = [G.Character(C, rng, level=wl, max_hp1=not a.roll_hp1,
                                  habitat=a.warband_habitat)
                      for _ in range(a.warband)]
            foes = [from_character(c, i) for i, c in enumerate(wchars)]
            for f in foes:
                f.side, f.morale = "foe", 8       # 7.15/7.9: NPCs check, at 8
        if a.show:
            print("PARTY")
            for f in party:
                print("   %-34s HP %2d  AC %2d  AB +%d  %s%+d"
                      % (f.name, f.hp, f.ac, f.ab, f.dmg, f.str_mod))
            print("FOES")
            for f in foes:
                rt = " + ".join("%dx%s" % cd for cd in getattr(f, "routine", [(f.attacks, f.dmg)]))
                print("   %-34s HP %2d  AC %2d  AB +%d  %s  ML %s"
                      % (f.name, f.hp, f.ac, f.ab, rt, f.morale))
            print()
        w, r, d, fled = fight(party, foes, rng, show=a.show)
        results.append((w, r, d, fled))
        for c, f in zip(chars, party):
            if not f.up:
                k = c.cls["formal_name"]
                down_by[k] = down_by.get(k, 0) + 1
        if a.show:
            print("\n   %s after %d rounds; %d of the party down%s"
                  % (w.upper(), r, d, ", foes fled" if fled else ""))
            return

    n = len(results)
    wins = sum(1 for w, _, _, _ in results if w == "party")
    tpk = sum(1 for w, _, _, _ in results if w == "foes")
    fled = sum(1 for _, _, _, f in results if f)
    downs = [d for _, _, d, _ in results]
    rounds = [r for _, r, _, _ in results]
    foe = ("%d x %s" % (a.count, mon["name"]) if mon else
           "a warband of %d%s" % (a.warband, (" (%s)" % a.warband_habitat) if a.warband_habitat else ""))
    who = "%d-strong %sparty" % (a.party, (a.habitat + " ") if a.habitat else "")
    print("=" * 66)
    print("  %s at level %d  vs  %s   (%d fights)" % (who, a.level, foe, n))
    print("=" * 66)
    print("  party wins      %5.1f%%   (of which foes broke morale: %.1f%%)"
          % (100.0 * wins / n, 100.0 * fled / n))
    print("  party wiped     %5.1f%%" % (100.0 * tpk / n))
    print("  draws           %5.1f%%" % (100.0 * (n - wins - tpk) / n))
    print("  rounds          mean %.1f, median %d" % (st.mean(rounds), st.median(rounds)))
    print("  party down/fight mean %.2f   nobody down %.1f%%   everybody %.1f%%"
          % (st.mean(downs), 100.0 * sum(1 for d in downs if d == 0) / n,
             100.0 * sum(1 for d in downs if d == a.party) / n))
    if down_by:
        tot = sum(down_by.values())
        print("  who goes down   " + ", ".join("%s %.0f%%" % (k, 100.0 * v / tot)
                                              for k, v in sorted(down_by.items(), key=lambda kv: -kv[1])))
    print()
    print("  This is a floor. Nobody used a trait, a manoeuvre, a missile or a")
    print("  potion, and nobody ran. A real table does better than this.")


if __name__ == "__main__":
    main()
