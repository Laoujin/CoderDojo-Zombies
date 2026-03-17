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


def draw():
    if toestand == "spel":
        # Background
        screen.fill("darkgreen")

        # Title
        screen.draw.text("ZOMBIE APOCALYPSE", center=(400, 50), fontsize=48, color="red")
        screen.draw.text("Een zombie komt op je af!", center=(400, 150), fontsize=28, color="white")

        # Hearts (lives)
        for i in range(levens):
            screen.draw.text("♥", topleft=(20 + i * 50, 20), fontsize=40, color="red")

        # Buttons (placeholder rectangles)
        screen.draw.filled_rect(KNOP_VECHTEN, "darkred")
        screen.draw.text("VECHTEN", center=KNOP_VECHTEN.center, fontsize=24, color="white")

        screen.draw.filled_rect(KNOP_RENNEN, "darkblue")
        screen.draw.text("RENNEN", center=KNOP_RENNEN.center, fontsize=24, color="white")

    elif toestand == "resultaat":
        if resultaat_goed:
            screen.fill("darkgreen")
        else:
            screen.fill("darkred")
        screen.draw.text(resultaat_tekst, center=(400, 300), fontsize=36, color="white")

    elif toestand == "game_over":
        screen.fill("darkred")
        screen.draw.text("GAME OVER", center=(400, 300), fontsize=60, color="white")
        screen.draw.text("Klik om opnieuw te spelen", center=(400, 380), fontsize=24, color="gray")


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
