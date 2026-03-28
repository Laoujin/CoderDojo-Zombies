# =============================================================================
# ZOMBIE APOCALYPSE - Level 6 - Starter C: JSON Data
# =============================================================================
# Start met: pgzrun zombie.py
#
# Deze starter laat zien hoe je game data uit een JSON bestand laadt.
# Zo kan je zombies, items en locaties aanpassen zonder code te wijzigen!
#
# Nieuw in deze starter:
# - JSON bestanden laden met json.load()
# - Data-driven design: speldata staat los van de code
# - Afbeeldingen laden op basis van namen uit data
# =============================================================================

import json
import random

import pygame
from pgzero.builtins import Rect, images
from pgzero.screen import Screen
screen: Screen

WIDTH = 800
HEIGHT = 600
TITLE = "Brainstorm"


# =============================================================================
# JSON LADEN
# =============================================================================
# JSON (JavaScript Object Notation) is een standaard formaat
# om data op te slaan. Het lijkt heel erg op Python dictionaries!
#
# json.load(bestand) leest een JSON bestand en geeft een
# Python dictionary of lijst terug.
#
# Voordeel: je kan de data aanpassen in data.json zonder
# de Python code te veranderen!
# =============================================================================
with open("data.json") as bestand:
    data = json.load(bestand)

zombies = data["zombies"]

# Willekeurige zombie uit de JSON data
huidige_zombie = random.choice(zombies)


def draw():
    screen.fill((30, 30, 40))

    teken_tekst("Zombie Dex", center=(400, 40), fontsize=44)
    teken_zombie(huidige_zombie)

    teken_tekst("Klik voor een andere zombie",
                center=(400, HEIGHT - 40), fontsize=20, kleur="gray")


def teken_zombie(zombie):
    """Teken een zombie met afbeelding en stats."""
    # ==========================================================================
    # AFBEELDING OP BASIS VAN DATA
    # ==========================================================================
    # In data.json staat: "afbeelding": "zombie_chef"
    # Dit is dezelfde naam als het bestand in images/: zombie_chef.png
    #
    # getattr(images, naam) laadt het plaatje met die naam
    # transform.scale past de grootte van het plaatje aan
    # ==========================================================================
    img = getattr(images, zombie["afbeelding"])
    geschaald = pygame.transform.scale(img, (210, 140))
    screen.surface.blit(geschaald, (295, 100))

    # Zombie naam
    teken_tekst(zombie["naam"], center=(400, 310), fontsize=36)

    # ==========================================================================
    # STATS TEKENEN
    # ==========================================================================
    # We tekenen een simpele balk voor elke stat
    # De breedte van de balk is gebaseerd op de waarde (1-5)
    # ==========================================================================
    stats = zombie["stats"]
    stat_namen = {
        "snelheid": "Snelheid",
        "kracht": "Kracht",
        "slimheid": "Slimheid",
    }

    y_start = 400
    for i, (sleutel, label) in enumerate(stat_namen.items()):
        y = y_start + i * 50
        waarde = stats[sleutel]

        # Label
        teken_tekst(label, center=(250, y), fontsize=24)

        # Achtergrond balk
        balk_x = 340
        balk_breedte = 200
        screen.draw.filled_rect(Rect(balk_x, y - 10, balk_breedte, 20), (60, 60, 80))

        # Gekleurde balk op basis van waarde (1-5)
        gevuld = int(balk_breedte * waarde / 5)
        kleur = (50 + waarde * 40, 200 - waarde * 30, 50)
        screen.draw.filled_rect(Rect(balk_x, y - 10, gevuld, 20), kleur)

        # Waarde als tekst
        teken_tekst(str(waarde), center=(balk_x + balk_breedte + 30, y), fontsize=24)


def on_mouse_down(pos):
    """Klik voor een nieuwe willekeurige zombie."""
    global huidige_zombie
    huidige_zombie = random.choice(zombies)


def teken_tekst(tekst, center, fontsize, kleur="white"):
    x, y = center
    screen.draw.text(tekst, center=(x+2, y+2), fontsize=fontsize, color="black")
    screen.draw.text(tekst, center=(x, y), fontsize=fontsize, color=kleur)
