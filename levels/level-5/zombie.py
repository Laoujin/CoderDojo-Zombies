# Zombie Apocalypse - Level 5
# Run met: pgzrun zombie.py

import random
import math
import pygame

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Apocalypse"

# === GAME STATE ===
toestand = "spel"  # "spel", "resultaat", "game_over"
levens = 3
resultaat_tekst = ""
resultaat_goed = False
laatste_actie = ""  # "vechten" of "rennen"
tijd = 0  # Voor animaties

# Knop posities (x, y, breedte, hoogte)
KNOP_VECHTEN = Rect(100, 400, 150, 150)
KNOP_RENNEN = Rect(550, 400, 150, 150)


def teken_tekst(tekst, center, fontsize, kleur="white"):
    """Teken tekst met een schaduw voor betere leesbaarheid."""
    x, y = center
    screen.draw.text(tekst, center=(x+2, y+2), fontsize=fontsize, color="black")
    screen.draw.text(tekst, center=(x, y), fontsize=fontsize, color=kleur)


def draw():
    if toestand == "spel":
        # Achtergrond met zombie
        screen.blit("achtergrond", (0, 0))

        # Hartjes (levens)
        for i in range(levens):
            screen.blit("hart", (20 + i * 50, 20))

        # Haal muispositie op voor hover effecten
        muis_pos = pygame.mouse.get_pos()
        hover_vechten = KNOP_VECHTEN.collidepoint(muis_pos)
        hover_rennen = KNOP_RENNEN.collidepoint(muis_pos)

        # Knop VECHTEN - Pulse effect bij hover
        if hover_vechten:
            pulse = 1.0 + 0.08 * math.sin(tijd * 5)
            new_size = int(150 * pulse)
            offset = (new_size - 150) // 2
            img = images.knop_vechten
            scaled = pygame.transform.scale(img, (new_size, new_size))
            screen.surface.blit(scaled, (KNOP_VECHTEN.x - offset, KNOP_VECHTEN.y - offset))
        else:
            screen.blit("knop_vechten", KNOP_VECHTEN.topleft)

        # Knop RENNEN - Pulse effect bij hover
        if hover_rennen:
            pulse = 1.0 + 0.08 * math.sin(tijd * 5)
            new_size = int(150 * pulse)
            offset = (new_size - 150) // 2
            img = images.knop_rennen
            scaled = pygame.transform.scale(img, (new_size, new_size))
            screen.surface.blit(scaled, (KNOP_RENNEN.x - offset, KNOP_RENNEN.y - offset))
        else:
            screen.blit("knop_rennen", KNOP_RENNEN.topleft)

    elif toestand == "resultaat":
        # Kies de juiste afbeelding op basis van actie en resultaat
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


def update(dt):
    """Update tijd en cursor."""
    global tijd
    tijd += dt

    # Cursor op basis van hover status
    if toestand == "spel":
        muis_pos = pygame.mouse.get_pos()
        if KNOP_VECHTEN.collidepoint(muis_pos) or KNOP_RENNEN.collidepoint(muis_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    elif toestand == "game_over":
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def on_mouse_down(pos):
    global toestand, levens, resultaat_tekst, resultaat_goed, laatste_actie

    if toestand == "spel":
        if KNOP_VECHTEN.collidepoint(pos):
            laatste_actie = "vechten"
            # Vechten: 50/50 kans
            if random.randint(1, 2) == 1:
                resultaat_tekst = "Je verslaat de zombie!"
                resultaat_goed = True
            else:
                resultaat_tekst = "De zombie bijt je..."
                resultaat_goed = False
                levens -= 1
            toestand = "resultaat"
            clock.schedule(ga_naar_volgende, 3.0)

        elif KNOP_RENNEN.collidepoint(pos):
            laatste_actie = "rennen"
            # Rennen: 50/50 kans
            if random.randint(1, 2) == 1:
                resultaat_tekst = "Je bent ontsnapt!"
                resultaat_goed = True
            else:
                resultaat_tekst = "De zombie was sneller..."
                resultaat_goed = False
                levens -= 1
            toestand = "resultaat"
            clock.schedule(ga_naar_volgende, 3.0)

    elif toestand == "game_over":
        reset_game()


def ga_naar_volgende():
    global toestand
    if levens <= 0:
        toestand = "game_over"
    else:
        toestand = "spel"


def reset_game():
    global toestand, levens, resultaat_tekst, resultaat_goed, laatste_actie
    toestand = "spel"
    levens = 3
    resultaat_tekst = ""
    resultaat_goed = False
    laatste_actie = ""
