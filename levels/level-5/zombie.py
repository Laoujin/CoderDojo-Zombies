# Zombie Apocalypse - Level 5
# Run met: pgzrun zombie.py

import random

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Apocalypse"

# === GAME STATE ===
toestand = "spel"  # "spel", "resultaat", "game_over"
levens = 3
resultaat_tekst = ""
resultaat_goed = False
laatste_actie = ""  # "vechten" of "rennen"

# Button positions (x, y, width, height)
KNOP_VECHTEN = Rect(100, 480, 150, 80)
KNOP_RENNEN = Rect(550, 480, 150, 80)


def teken_tekst(tekst, center, fontsize, kleur="white"):
    """Teken tekst met een schaduw voor betere leesbaarheid."""
    x, y = center
    screen.draw.text(tekst, center=(x+2, y+2), fontsize=fontsize, color="black")
    screen.draw.text(tekst, center=(x, y), fontsize=fontsize, color=kleur)


def draw():
    if toestand == "spel":
        # Background with zombie
        screen.blit("achtergrond", (0, 0))

        # Hearts (lives)
        for i in range(levens):
            screen.blit("hart", (20 + i * 50, 20))

        # Buttons
        screen.blit("knop_vechten", KNOP_VECHTEN.topleft)
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
        teken_tekst(resultaat_tekst, center=(400, 300), fontsize=36)

    elif toestand == "game_over":
        screen.blit("game_over", (0, 0))
        teken_tekst("GAME OVER", center=(400, 250), fontsize=60, kleur="red")
        teken_tekst("Klik om opnieuw te spelen", center=(400, 350), fontsize=24, kleur="gray")


def on_mouse_down(pos):
    global toestand, levens, resultaat_tekst, resultaat_goed, laatste_actie

    if toestand == "spel":
        if KNOP_VECHTEN.collidepoint(pos):
            laatste_actie = "vechten"
            # Fight: 50/50 chance
            if random.randint(1, 2) == 1:
                resultaat_tekst = "Je verslaat de zombie!"
                resultaat_goed = True
            else:
                resultaat_tekst = "De zombie bijt je..."
                resultaat_goed = False
                levens -= 1
            toestand = "resultaat"
            clock.schedule(ga_naar_volgende, 2.0)

        elif KNOP_RENNEN.collidepoint(pos):
            laatste_actie = "rennen"
            # Run: 50/50 chance
            if random.randint(1, 2) == 1:
                resultaat_tekst = "Je bent ontsnapt!"
                resultaat_goed = True
            else:
                resultaat_tekst = "De zombie was sneller..."
                resultaat_goed = False
                levens -= 1
            toestand = "resultaat"
            clock.schedule(ga_naar_volgende, 2.0)

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
