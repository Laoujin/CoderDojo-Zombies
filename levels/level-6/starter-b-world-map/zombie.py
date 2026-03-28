# =============================================================================
# ZOMBIE APOCALYPSE - Level 6 - Starter B: World Map
# =============================================================================
# Start met: pgzrun zombie.py
#
# Deze starter laat zien hoe je een wereldkaart maakt waar de speler
# met pijltjestoetsen kan navigeren tussen locaties.
#
# Nieuw in deze starter:
# - Keyboard input met on_key_down()
# - Een grid/kaart van locaties
# - Navigatie tussen schermen
# =============================================================================

from enum import Enum

import pygame
from pgzero.builtins import Rect, images
from pgzero.screen import Screen
screen: Screen

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Apocalypse"


class Toestand(Enum):
    KAART = "kaart"
    LOCATIE = "locatie"


# =============================================================================
# DE WERELDKAART
# =============================================================================
# De kaart is een grid (raster) van locaties.
# Elke locatie heeft een naam en een plaatje.
#
# We gebruiken een 2D lijst (een lijst van lijsten):
#   kaart[rij][kolom]
#
# Voorbeeld:
#   kaart[0][0] = linksboven
#   kaart[0][1] = rechtsboven
#   kaart[1][0] = linksonder
#   kaart[1][1] = rechtsonder
# =============================================================================
kaart = [
    [
        {"naam": "Park", "afbeelding": "loc_park"},
        {"naam": "School", "afbeelding": "loc_school"},
        {"naam": "Ziekenhuis", "afbeelding": "loc_hospital"},
    ],
    [
        {"naam": "Supermarkt", "afbeelding": "loc_supermarket"},
        {"naam": "Politiebureau", "afbeelding": "loc_police"},
        {"naam": "Restaurant", "afbeelding": "loc_restaurant"},
    ],
    [
        {"naam": "Riool", "afbeelding": "loc_sewers"},
        {"naam": "Boomhut", "afbeelding": "loc_treehouse"},
        {"naam": "Bibliotheek", "afbeelding": "loc_library"},
    ],
]

RIJEN = len(kaart)
KOLOMMEN = len(kaart[0])

# Positie van de speler op de kaart
speler_rij = 0
speler_kolom = 0

toestand = Toestand.KAART


def draw():
    screen.fill((30, 30, 40))

    if toestand == Toestand.KAART:
        teken_kaart()
    elif toestand == Toestand.LOCATIE:
        teken_locatie()


def teken_kaart():
    """Teken de wereldkaart als een grid van locaties."""
    teken_tekst("Wereldkaart", center=(400, 40), fontsize=40)
    teken_tekst("Pijltjestoetsen = bewegen, Enter = locatie bezoeken",
                center=(400, 75), fontsize=20, kleur="gray")

    # Grid instellingen
    cel_breedte = 200
    cel_hoogte = 150
    start_x = (WIDTH - KOLOMMEN * cel_breedte) // 2
    start_y = 110

    for rij in range(RIJEN):
        for kolom in range(KOLOMMEN):
            locatie = kaart[rij][kolom]
            x = start_x + kolom * cel_breedte
            y = start_y + rij * cel_hoogte

            # Is dit de geselecteerde cel?
            is_geselecteerd = (rij == speler_rij and kolom == speler_kolom)

            # Teken cel achtergrond
            if is_geselecteerd:
                # Geselecteerd: lichte rand
                screen.draw.filled_rect(Rect(x + 4, y + 4, cel_breedte - 8, cel_hoogte - 8), (60, 60, 80))
                screen.draw.rect(Rect(x + 4, y + 4, cel_breedte - 8, cel_hoogte - 8), "yellow")
            else:
                screen.draw.filled_rect(Rect(x + 4, y + 4, cel_breedte - 8, cel_hoogte - 8), (40, 40, 55))
                screen.draw.rect(Rect(x + 4, y + 4, cel_breedte - 8, cel_hoogte - 8), "gray")

            # Teken locatie thumbnail (geschaald)
            try:
                img = getattr(images, locatie["afbeelding"])
                thumbnail = pygame.transform.scale(img, (cel_breedte - 24, cel_hoogte - 44))
                screen.surface.blit(thumbnail, (x + 12, y + 10))
            except Exception:
                pass

            # Teken locatie naam
            teken_tekst(locatie["naam"],
                        center=(x + cel_breedte // 2, y + cel_hoogte - 18),
                        fontsize=18,
                        kleur="yellow" if is_geselecteerd else "white")


def teken_locatie():
    """Teken de huidige locatie op volledig scherm."""
    locatie = kaart[speler_rij][speler_kolom]

    # Teken de locatie afbeelding als achtergrond
    try:
        img = getattr(images, locatie["afbeelding"])
        geschaald = pygame.transform.scale(img, (WIDTH, HEIGHT))
        screen.surface.blit(geschaald, (0, 0))
    except Exception:
        screen.fill((30, 30, 40))

    # Teken locatie naam
    teken_tekst(locatie["naam"], center=(400, 50), fontsize=48)

    # Instructie
    teken_tekst("Druk op Escape om terug te gaan naar de kaart",
                center=(400, HEIGHT - 40), fontsize=20, kleur="gray")


# =============================================================================
# KEYBOARD INPUT
# =============================================================================
# on_key_down(key) wordt aangeroepen als je een toets indrukt.
# key is een constante zoals keys.UP, keys.LEFT, keys.RETURN, etc.
#
# Dit is anders dan on_mouse_down(pos) die we in Level 5 gebruikten!
# =============================================================================
def on_key_down(key):
    global speler_rij, speler_kolom, toestand

    if toestand == Toestand.KAART:
        # Navigeer met pijltjestoetsen
        if key == keys.UP and speler_rij > 0:
            speler_rij -= 1
        elif key == keys.DOWN and speler_rij < RIJEN - 1:
            speler_rij += 1
        elif key == keys.LEFT and speler_kolom > 0:
            speler_kolom -= 1
        elif key == keys.RIGHT and speler_kolom < KOLOMMEN - 1:
            speler_kolom += 1
        elif key == keys.RETURN:
            # Enter = locatie bezoeken
            toestand = Toestand.LOCATIE

    elif toestand == Toestand.LOCATIE:
        if key == keys.ESCAPE:
            toestand = Toestand.KAART


def teken_tekst(tekst, center, fontsize, kleur="white"):
    x, y = center
    screen.draw.text(tekst, center=(x+2, y+2), fontsize=fontsize, color="black")
    screen.draw.text(tekst, center=(x, y), fontsize=fontsize, color=kleur)
