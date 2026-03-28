# =============================================================================
# ZOMBIE APOCALYPSE - Level 6 - Starter A: Game States
# =============================================================================
# Start met: pgzrun zombie.py
#
# Deze starter laat zien hoe je een Enum gebruikt voor game states.
# In Level 5 gebruikten we strings zoals "spel" en "game_over".
# Met een Enum kan dat niet meer fout gaan!
#
# Nieuw in deze starter:
# - Enum: een vaste lijst van mogelijke waarden
# - Duidelijkere code door Toestand.SPEL i.p.v. "spel"
# =============================================================================

import random
from enum import Enum

from pgzero.builtins import clock
from pgzero.screen import Screen
screen: Screen

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Apocalypse"


# =============================================================================
# ENUM VOOR GAME STATES
# =============================================================================
# Een Enum (enumeration) is een klasse met vaste waarden.
# Voordeel t.o.v. strings:
# - Je kan geen typfout maken (Toestand.SPEL vs "speel")
# - Je editor helpt je met automatisch aanvullen
# - Je ziet meteen welke toestanden er zijn
#
# class Seizoen(Enum):
#     LENTE = "lente"
#     ZOMER = "zomer"
#     HERFST = "herfst"
#     WINTER = "winter"
# =============================================================================
class Toestand(Enum):
    SPEL = "spel"
    RESULTAAT = "resultaat"
    GAME_OVER = "game_over"


toestand = Toestand.SPEL
levens = 3
resultaat_tekst = ""


def draw():
    if toestand == Toestand.SPEL:
        screen.blit("achtergrond", (0, 0))

        for i in range(levens):
            screen.blit("hart", (20 + i * 50, 20))

        screen.draw.text("Klik om te vechten!", center=(400, 300), fontsize=48, color="white")

    elif toestand == Toestand.RESULTAAT:
        screen.blit("achtergrond", (0, 0))
        screen.draw.text(resultaat_tekst, center=(400, 300), fontsize=48, color="white")

    elif toestand == Toestand.GAME_OVER:
        screen.blit("game_over", (0, 0))
        screen.draw.text("GAME OVER", center=(400, 250), fontsize=60, color="red")
        screen.draw.text("Klik om opnieuw te spelen", center=(400, 350), fontsize=24, color="gray")


def update(dt):
    """Wordt elk frame aangeroepen. Handig voor animaties!"""
    pass


def on_mouse_down(pos):
    global toestand, levens, resultaat_tekst

    if toestand == Toestand.SPEL:
        if random.randint(1, 2) == 1:
            resultaat_tekst = "Je verslaat de zombie!"
        else:
            resultaat_tekst = "De zombie bijt je..."
            levens -= 1

        toestand = Toestand.RESULTAAT
        clock.schedule(ga_naar_volgende, 2.0)

    elif toestand == Toestand.GAME_OVER:
        toestand = Toestand.SPEL
        levens = 3


def ga_naar_volgende():
    global toestand
    if levens <= 0:
        toestand = Toestand.GAME_OVER
    else:
        toestand = Toestand.SPEL
