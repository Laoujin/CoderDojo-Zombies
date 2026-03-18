# Zombie Clicker - Level 4.5
# Start met: pgzrun zombie.py
# Of met F5

import random
from pgzero.builtins import Actor, sounds
from pgzero.screen import Screen
screen: Screen

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Clicker"

# Maak de zombie
zombie = Actor("zombie")
score = 0


def plaats_zombie():
    """Zet de zombie op een willekeurige plek."""
    zombie.x = random.randint(50, WIDTH - 50)
    zombie.y = random.randint(50, HEIGHT - 50)


# Zet zombie op startpositie
plaats_zombie()


def draw():
    """Teken het scherm (wordt 60x per seconde aangeroepen)."""
    screen.fill("darkgreen")
    zombie.draw()
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30, color="white")


def on_mouse_down(pos):
    """Wordt aangeroepen als je klikt."""
    global score
    if zombie.collidepoint(pos):
        sounds.whack.play()
        score += 1
        plaats_zombie()
