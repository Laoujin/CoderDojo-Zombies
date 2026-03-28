# =============================================================================
# ZOMBIE APOCALYPSE - Level 6 - Starter B: Locaties
# =============================================================================
# Start met: pgzrun zombie.py
#
# Deze starter laat zien hoe je met pijltjestoetsen tussen
# locaties kan navigeren. Elke locatie heeft een eigen achtergrond.
#
# Nieuw in deze starter:
# - Keyboard input met on_key_down()
# - Navigatie tussen verschillende schermen
# =============================================================================

from pgzero.screen import Screen
screen: Screen

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Apocalypse"


# =============================================================================
# LOCATIES
# =============================================================================
# Een lijst van tuples: (naam, afbeelding)
#
# Een tuple lijkt op een lijst maar kan niet veranderd worden.
# Perfect voor vaste data!
#   locaties[0]    -> ("Kelder", "loc_basement")
#   locaties[0][0] -> "Kelder"
#   locaties[0][1] -> "loc_basement"
# =============================================================================
locaties = [
    ("Kelder", "loc_basement"),
    ("Supermarkt", "loc_supermarket"),
    ("Park", "loc_park"),
    ("Dak", "loc_rooftop"),
]

huidige_locatie = 0


def draw():
    naam, afbeelding = locaties[huidige_locatie]

    screen.blit(afbeelding, (0, 0))
    screen.draw.text(naam.upper(), center=(400, 50), fontsize=48, color="white",
                     shadow=(2, 2), scolor="black")

    teken_navigatie()







# =============================================================================
# KEYBOARD INPUT
# =============================================================================
# on_key_down(key) wordt aangeroepen als je een toets indrukt.
# key is een constante zoals keys.LEFT, keys.SPACE, etc.
# =============================================================================
def on_key_down(key):
    if key == keys.UP:
        ga_naar(-1)
    elif key == keys.DOWN:
        ga_naar(1)


def on_mouse_down(pos):
    x, y = pos
    # Klik op de pijltjes onderaan
    if 350 < x < 450:
        if y > 545:
            ga_naar(1)
        elif y > 510:
            ga_naar(-1)


def update(dt):
    """Wordt elk frame aangeroepen. Handig voor animaties!"""
    pass


# =============================================================================
# HELPER FUNCTIES
# =============================================================================
def ga_naar(richting):
    """Verander van locatie. richting is 1 (vooruit) of -1 (terug)."""
    global huidige_locatie
    nieuwe_locatie = huidige_locatie + richting
    if 0 <= nieuwe_locatie < len(locaties):
        huidige_locatie = nieuwe_locatie


def teken_navigatie():
    """Teken pijltjes onderaan om te navigeren (klikbaar!)."""
    if huidige_locatie > 0:
        screen.draw.text("^", center=(400, 530), fontsize=60, color="white",
                         shadow=(2, 2), scolor="black")
    if huidige_locatie < len(locaties) - 1:
        screen.draw.text("v", center=(400, 560), fontsize=60, color="white",
                         shadow=(2, 2), scolor="black")
