# -*- coding: utf-8 -*-
"""Where the source books are on this machine. One place, so a library
reorganisation is a one-line change here and not a hunt through extractors.

Dan's RPG library moved from H:/RPG/Game Systems/ to H:/RPG_NEW/01_GAME_SYSTEMS/
on 2026-09-20. Override with the STAR_CRAWLER_LIBRARY environment variable.
"""
import os

LIBRARY = os.environ.get("STAR_CRAWLER_LIBRARY", "H:/RPG_NEW/01_GAME_SYSTEMS")

SW = LIBRARY + "/Star Wars"
WEG = SW + "/d6"
WEG_RANCORPIT = WEG + "/The Rancor Pit"
WEG_GG = WEG + "/Galaxy Guides"
WEG_SUPP = WEG + "/supplements"
WEG_SOURCEBOOKS = WEG + "/companions and sourcebooks"
SW5E = SW + "/5e"
WHITE_STAR = LIBRARY + "/White Star"
TRAVELLER = LIBRARY + "/Traveller"
WWN = LIBRARY + "/Worlds Without Number"
PUNDIT = LIBRARY + "/RPGPundit"
OSR_ARCHIVE = "H:/RPG_NEW/07_COLLECTIONS_AND_ARCHIVES/O-S-R archive"

WEG_ALIENS = WEG_RANCORPIT + "/Aliens_Stats.pdf"
WEG_FORCE = WEG_RANCORPIT + "/Force_Powers.pdf"
WEG_DROIDS = WEG_RANCORPIT + "/Droids_Stats.pdf"
WEG_SHIPS = WEG_RANCORPIT + "/Starships_Stats_R&E_censored.pdf"
SW5E_PHB = SW5E + "/SW5e - Player's Handbook.pdf"
SW5E_SHIPS = SW5E + "/SW5e - Starships of the Galaxy - 20210316.pdf"
WHITE_STAR_GALAXY = WHITE_STAR + "/White Star Galaxy Edition.pdf"
WHITE_STAR_WAY = WHITE_STAR + "/Walking The Way, A Mysticism Sourcebook [WhtStar].pdf"
TRAVELLER_BOOK = TRAVELLER + "/Classic_Traveller_CDROM_-_CT_The_Traveller_Book [_ocr_].pdf"
WWN_DELUXE = WWN + "/Worlds Without Number - Deluxe PDF [2021-04-02].pdf"
STAR_ADVENTURER = PUNDIT + "/Star Adventurer/Star Adventurer.pdf"
SWN_DELUXE = OSR_ARCHIVE + "/Stars Without Number/Stars Without Number Revised Deluxe Edition/Stars Without Number Revised Deluxe Edition.pdf"
SWN_FREE = OSR_ARCHIVE + "/Stars Without Number/Stars Without Number Free Edition.pdf"
XPLORERS = OSR_ARCHIVE + "/X-Plorers/X-plorers RPG (illustrated).pdf"
HULKS = OSR_ARCHIVE + "/Hulks & Horrors/Hulks & Horrors Basic Black Edition.pdf"
STAR_FRONTIERS_AD = OSR_ARCHIVE + "/Star Frontiers/Star Frontiers Boxed Set Complete 1980.pdf"
STAR_FRONTIERS_KH = OSR_ARCHIVE + "/Star Frontiers/Star Frontiers Knight Hawks Box/Star Frontiers Knight Hawks Expansion Rules.pdf"
STAR_DOGS = OSR_ARCHIVE + "/Star Dogs/Star Dogs Player's Handbook.pdf"
STARSHIPS_SPACEMEN = OSR_ARCHIVE + "/Starships & Spacemen/Starships & Spacemen 2E.pdf"
SPACE_DUNGEON_1 = OSR_ARCHIVE + "/Space Dungeon/Space Dungeon Book I Starsailors and Psionics.pdf"
MOTSP = OSR_ARCHIVE + "/Machinations of the Space Princess/Machinations of the Space Princess Print.pdf"
BX_SPACE = OSR_ARCHIVE + "/BX-Space/BX-Space [alpha].pdf"

# 99_INBOX arrivals, 2026-09-20. Move these under 01_GAME_SYSTEMS/Star Wars/{d20,FFG}
# when Dan files them and update here. Four are image-only scans (need OCR).
INBOX = "H:/RPG_NEW/99_INBOX"
FFG_FORCE_DESTINY = INBOX + "/Force_and_Destiny.pdf"          # scan, no text
FFG_EDGE = INBOX + "/Edge_of_the_Empire.pdf"                  # scan, no text
D20_RCR = INBOX + "/d20_star_wars-revised_core_rulebook.pdf"  # scan, no text
D20_UAA = INBOX + "/d20_star_wars-ultimate_alien_anthology.pdf"  # scan, no text
SAGA_SCUM = INBOX + "/d20_star_wars-scum_and_villainy.pdf"    # Saga Edition; has text


def check():
    """Print which known sources exist. Run: python research/tools/paths.py"""
    for k, v in sorted(globals().items()):
        if k.isupper() and isinstance(v, str) and v.endswith(".pdf"):
            print("%s %s" % ("ok " if os.path.exists(v) else "MISSING", v))


if __name__ == "__main__":
    check()
