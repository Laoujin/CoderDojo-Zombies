# =============================================================================
# ZOMBIE CLICKER - Level 4.5
# =============================================================================
# Start met: pgzrun zombie.py
# Of met F5 in VSCode
#
# Dit is je eerste GRAFISCHE spel met Pygame Zero!
# Nieuw in dit level:
# - Pygame Zero basics (geen while loop nodig!)
# - Actor: een plaatje dat je kunt bewegen
# - draw(): wordt 60x per seconde aangeroepen om te tekenen
# - on_mouse_down(): wordt aangeroepen als je klikt
# - global: om variabelen buiten een functie te veranderen
# =============================================================================

import random

# =============================================================================
# PYGAME ZERO IMPORTS
# =============================================================================
# Pygame Zero heeft speciale objecten die we importeren:
# - Actor: een sprite (plaatje) dat je kunt bewegen en tekenen
# - sounds: om geluidseffecten af te spelen
# - Screen: het scherm waar we op tekenen
# =============================================================================

from pgzero.builtins import Actor, sounds
from pgzero.screen import Screen
screen: Screen  # Dit helpt VSCode met code-suggesties

# =============================================================================
# VENSTER INSTELLINGEN
# =============================================================================
# WIDTH en HEIGHT bepalen hoe groot het venster wordt (in pixels)
# TITLE is de tekst in de titelbalk van het venster
# Pygame Zero herkent deze variabelen automatisch!
# =============================================================================

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Clicker"

# =============================================================================
# ACTOR (SPRITE)
# =============================================================================
# Een Actor is een plaatje dat je kunt bewegen en tekenen
# Actor("zombie") laadt het plaatje "zombie.png" uit de images/ map
# Je kunt de positie veranderen met zombie.x en zombie.y
# =============================================================================
zombie = Actor("zombie")
score = 0


def plaats_zombie():
    """Zet de zombie op een willekeurige plek op het scherm."""

    # We houden 50 pixels afstand van de randen
    zombie.x = random.randint(50, WIDTH - 50)
    zombie.y = random.randint(50, HEIGHT - 50)


# Zet zombie op willekeurige startpositie
plaats_zombie()


# =============================================================================
# DE DRAW FUNCTIE
# =============================================================================
# Pygame Zero roept draw() automatisch 60x per seconde aan
# Hier teken je alles wat je op het scherm wilt zien
#
# BELANGRIJK: draw() tekent het HELE scherm opnieuw elke keer
# Daarom beginnen we met screen.fill() om alles te wissen
# =============================================================================
def draw():
    """Teken het scherm"""

    # Vul het hele scherm met een kleur (wist het vorige frame)
    screen.fill("darkgreen")

    # Teken de zombie Actor
    zombie.draw()

    # Teken de score in de linkerbovenhoek
    # topleft=(10, 10) betekent 10 pixels van links en 10 van boven
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30, color="white")


# =============================================================================
# MUISKLIK EVENT
# =============================================================================
# on_mouse_down() wordt aangeroepen als de speler klikt
# De parameter "pos" is een tuple (x, y) met de muispositie
#
# .collidepoint(pos) checkt of de klik BINNEN de Actor valt
# =============================================================================
def on_mouse_down(pos):
    """Wordt aangeroepen als je klikt."""

    # =================================================================
    # GLOBAL
    # =================================================================
    # Normaal kan een functie variabelen van buiten alleen LEZEN
    # Met "global score" zeggen we: ik wil score ook kunnen VERANDEREN
    # Zonder global zou Python denken dat je een nieuwe lokale variabele maakt
    # =================================================================
    global score

    # Check of de klik op de zombie was
    if zombie.collidepoint(pos):
        # Speel een geluid af (whack.wav uit de sounds/ map)
        sounds.whack.play()

        # Verhoog de score
        score += 1

        # Zet zombie op nieuwe plek
        plaats_zombie()
