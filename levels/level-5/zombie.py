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
