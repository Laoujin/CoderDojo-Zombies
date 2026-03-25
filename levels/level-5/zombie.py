# =============================================================================
# ZOMBIE APOCALYPSE - Level 5
# =============================================================================
# Start met: pgzrun zombie.py
# Of met F5 in VSCode
#
# Nieuw in dit level:
# - Game states (toestanden): menu, spel, game over
# - Rect: een rechthoek voor knoppen en collision detection
# - clock.schedule(): code uitvoeren na X seconden
# =============================================================================

import random
import math

# =============================================================================
# PYGAME IMPORTS
# =============================================================================
# pygame is de "echte" library onder Pygame Zero
# We gebruiken het voor:
# - pygame.mouse: muiscursor veranderen
# - pygame.transform.scale: plaatjes groter/kleiner maken
# =============================================================================

import pygame

from pgzero.builtins import Rect, images, clock
from pgzero.screen import Screen
screen: Screen

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Apocalypse"

# =============================================================================
# GAME STATES (TOESTANDEN)
# =============================================================================
# Een game heeft vaak verschillende "schermen" of toestanden:
# - "spel": het echte spel
# - "resultaat": laat zien of je actie gelukt is
# - "game_over": het einde
#
# We gebruiken een variabele om bij te houden in welke toestand we zijn
# =============================================================================
toestand = "spel"  # Kan zijn: "spel", "resultaat" of "game_over"

levens = 3
resultaat_tekst = ""
resultaat_goed = False
laatste_actie = ""  # "vechten" of "rennen"
tijd = 0  # Voor animaties (telt op elke frame)

# =============================================================================
# RECT (RECHTHOEK)
# =============================================================================
# Een Rect definieert een rechthoekig gebied op het scherm
# Rect(x, y, breedte, hoogte)
#   x, y = linkerbovenhoek
#   breedte, hoogte = grootte
#
# Handig voor knoppen! Met .collidepoint(pos) check je of een punt erin valt
# =============================================================================
KNOP_VECHTEN = Rect(100, 400, 150, 150)
KNOP_RENNEN = Rect(550, 400, 150, 150)


def draw():
    """Teken het scherm op basis van de huidige toestand."""

    # We tekenen anders afhankelijk van de game state
    if toestand == "spel":
        # Teken achtergrond (achtergrond.png uit images/ map)
        screen.blit("achtergrond", (0, 0))

        # Teken hartjes voor levens
        # range(levens) geeft 0, 1, 2 als levens=3
        for i in range(levens):
            # Elk hartje 50 pixels verder naar rechts
            screen.blit("hart", (20 + i * 50, 20))

        # Teken knoppen met pulse effect
        teken_knop_met_pulse("knop_vechten", KNOP_VECHTEN)
        teken_knop_met_pulse("knop_rennen", KNOP_RENNEN)

    elif toestand == "resultaat":
        # Toon het resultaat van je actie
        if laatste_actie == "vechten":
            if resultaat_goed:
                screen.blit("vechten_succes", (0, 0))
            else:
                screen.blit("vechten_faal", (0, 0))
        else:  # rennen
            if resultaat_goed:
                screen.blit("rennen_succes", (0, 0))
            else:
                screen.blit("rennen_faal", (0, 0))

        teken_tekst(resultaat_tekst, center=(400, 80), fontsize=36)

    elif toestand == "game_over":
        screen.blit("game_over", (0, 0))
        teken_tekst("GAME OVER", center=(400, 250), fontsize=60, kleur="red")
        teken_tekst("Klik om opnieuw te spelen", center=(400, 350), fontsize=24, kleur="gray")


# =============================================================================
# UPDATE FUNCTIE
# =============================================================================
# update(dt) wordt elke frame aangeroepen, net als draw()
# dt = "delta time" = hoeveel seconden sinds vorige frame (meestal ~0.016)
# We gebruiken dit voor animaties en de muiscursor
# =============================================================================
def update(dt):
    """Update tijd en cursor - wordt elk frame aangeroepen."""
    global tijd

    # Tel tijd op voor pulse animaties
    tijd += dt

    # Verander muiscursor op basis van waar de muis is
    if toestand == "spel":
        # pygame.mouse.get_pos() geeft de huidige muispositie
        muis_pos = pygame.mouse.get_pos()

        # Als muis op een knop staat, toon handje
        if KNOP_VECHTEN.collidepoint(muis_pos) or KNOP_RENNEN.collidepoint(muis_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    elif toestand == "game_over":
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def on_mouse_down(pos):
    """Wordt aangeroepen als je klikt."""
    global toestand, levens, resultaat_tekst, resultaat_goed, laatste_actie

    if toestand == "spel":
        # Check welke knop is geklikt
        if KNOP_VECHTEN.collidepoint(pos):
            # We houden de laatste actie bij zodat we daarna
            # de juiste foto kunnen tonen (vechten / rennen)
            laatste_actie = "vechten"

            # 50/50 kans
            if random.randint(1, 2) == 1:
                resultaat_tekst = "Je verslaat de zombie!"
                resultaat_goed = True
            else:
                resultaat_tekst = "De zombie bijt je..."
                resultaat_goed = False
                levens -= 1

            toestand = "resultaat"

            # ================================================================
            # CLOCK.SCHEDULE
            # ================================================================
            # clock.schedule(functie, seconden) roept een functie aan
            # na het opgegeven aantal seconden
            # Hier wachten we 2.5 seconden voordat we verder gaan
            # ================================================================
            clock.schedule(ga_naar_volgende, 2.5)

        elif KNOP_RENNEN.collidepoint(pos):
            laatste_actie = "rennen"
            if random.randint(1, 2) == 1:
                resultaat_tekst = "Je bent ontsnapt!"
                resultaat_goed = True
            else:
                resultaat_tekst = "De zombie was sneller..."
                resultaat_goed = False
                levens -= 1

            toestand = "resultaat"
            clock.schedule(ga_naar_volgende, 2.5)

    elif toestand == "game_over":
        # Klik om opnieuw te starten
        reset_game()


def ga_naar_volgende():
    """Ga naar het volgende scherm na het resultaat."""
    global toestand
    if levens <= 0:
        toestand = "game_over"
    else:
        toestand = "spel"


def reset_game():
    """Reset alle variabelen om opnieuw te beginnen."""
    global toestand, levens, resultaat_tekst, resultaat_goed, laatste_actie
    toestand = "spel"
    levens = 3
    resultaat_tekst = ""
    resultaat_goed = False
    laatste_actie = ""



# =============================================================================
# =                                DANGER ZONE                                =
# =============================================================================
# LET OP: De code hieronder is wat geavanceerder!!
#
# Voor de animatie hebben we wat wiskunde nodig! (wie had gedacht dat
# je dat ooit zou kunnen gebruiken...)
#
# Zie ook "Pygame Recepten" op de website voor andere voorbeelden van animaties
# die je kan gebruiken in je games!
# =============================================================================


# =============================================================================
# ANIMATIES MET MATH.SIN
# =============================================================================
# math.sin() geeft een getal tussen -1 en 1 dat "golft"
# Als je de tijd erin stopt, krijg je een vloeiende op-en-neer beweging
# Perfect voor "pulse" effecten!
#
# sin(tijd * 5) golft 5x zo snel
# 1.0 + 0.08 * sin(...) geeft een waarde tussen 0.92 en 1.08
# =============================================================================
def teken_knop_met_pulse(image_name, rect):
    """Teken een knop, met pulse animatie als de muis erop staat."""
    muis_pos = pygame.mouse.get_pos()

    if rect.collidepoint(muis_pos):
        # Muis staat op de knop - teken groter/kleiner (pulse)
        pulse = 1.0 + 0.08 * math.sin(tijd * 5)
        new_size = int(150 * pulse)
        offset = (new_size - 150) // 2  # Centreer de grotere knop

        # ================================================================
        # GETATTR EN PYGAME.TRANSFORM.SCALE
        # ================================================================
        # getattr(images, "naam") is hetzelfde als images.naam
        # Handig als de naam in een variabele staat!
        #
        # pygame.transform.scale(plaatje, (breedte, hoogte))
        # maakt het plaatje groter of kleiner
        # ================================================================
        img = getattr(images, image_name)
        scaled = pygame.transform.scale(img, (new_size, new_size))

        # screen.surface is het echte pygame oppervlak
        # .blit() tekent een plaatje op een positie
        screen.surface.blit(scaled, (rect.x - offset, rect.y - offset))
    else:
        # Muis staat niet op knop - teken normaal
        screen.blit(image_name, rect.topleft)


# kleur="white": kleur is hier een optionele parameter
# Als je bij het aanroepen van teken_tekst zelf geen
# kleur meegeeft, dan zal "white" gebruikt worden
def teken_tekst(tekst, center, fontsize, kleur="white"):
    """Teken tekst met een schaduw voor betere leesbaarheid."""
    x, y = center

    # Eerst zwarte schaduw, iets verschoven
    screen.draw.text(tekst, center=(x+2, y+2), fontsize=fontsize, color="black")

    # Dan de echte tekst erboven
    screen.draw.text(tekst, center=(x, y), fontsize=fontsize, color=kleur)
