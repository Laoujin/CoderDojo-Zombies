# Level 5: Pygame Zero

## Wat leer je?

In dit level leer je over **Pygame Zero** - een library om grafische spelletjes te maken. Je leert hoe je plaatjes tekent, muisklikken afhandelt en animaties maakt.

## Opstarten

```bash
pgzrun zombie.py
```

Of in VS Code: rechtermuisknop op `zombie.py` → "Run Python File in Terminal" werkt niet voor Pygame Zero. Gebruik altijd `pgzrun`.

## De code

### Het scherm instellen

```python
WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Apocalypse"
```

Dit bepaalt de grootte en titel van je spelvenster.

### De draw() functie

```python
def draw():
    screen.fill("darkgreen")
    screen.blit("achtergrond", (0, 0))
```

- `draw()` wordt **elke frame** aangeroepen (60x per seconde!)
- `screen.fill()` vult het scherm met een kleur
- `screen.blit()` tekent een plaatje op positie (x, y)

**Let op:** Plaatjes moeten in de `images/` folder staan, zonder extensie in de code:
- Bestand: `images/achtergrond.png`
- Code: `screen.blit("achtergrond", (0, 0))`

### Tekst tekenen

```python
screen.draw.text("Hallo!", center=(400, 300), fontsize=36, color="white")
```

- `center=(x, y)` plaatst de tekst gecentreerd op die positie
- `topleft=(x, y)` zou linksboven plaatsen

### Klikken detecteren

```python
def on_mouse_down(pos):
    if KNOP.collidepoint(pos):
        print("Knop geklikt!")
```

- `on_mouse_down(pos)` wordt aangeroepen als je klikt
- `pos` is de (x, y) positie van je muisklik
- `collidepoint()` checkt of een punt binnen een rechthoek valt

### Rechthoeken (Rect)

```python
KNOP = Rect(100, 400, 150, 150)
#          x    y    breedte hoogte
```

Een `Rect` is een onzichtbare rechthoek die je gebruikt voor:
- Positie bepalen waar je iets tekent
- Checken of de muis ergens op klikt

### Iets later laten gebeuren

```python
clock.schedule(mijn_functie, 3.0)
```

Dit roept `mijn_functie` aan na 3 seconden. Handig voor:
- Resultaat even tonen voordat je verder gaat
- Timers en vertragingen

### Game state (toestand)

```python
toestand = "spel"  # "spel", "resultaat", "game_over"

def draw():
    if toestand == "spel":
        # teken het spel
    elif toestand == "resultaat":
        # toon resultaat
    elif toestand == "game_over":
        # game over scherm
```

Met een variabele hou je bij in welke "toestand" je spel is. De `draw()` functie tekent dan het juiste scherm.

### De update() functie

```python
def update(dt):
    global tijd
    tijd += dt
```

- `update(dt)` wordt ook elke frame aangeroepen
- `dt` is de tijd sinds de vorige frame (in seconden)
- Handig voor animaties en timers

## Nieuwe concepten

| Concept | Wat het doet |
|---------|--------------|
| `draw()` | Tekent het scherm (60x per seconde) |
| `screen.blit()` | Plaatje tekenen |
| `screen.draw.text()` | Tekst tekenen |
| `Rect` | Rechthoek voor posities en klikdetectie |
| `on_mouse_down(pos)` | Reageert op muisklikken |
| `clock.schedule()` | Iets later laten gebeuren |
| `update(dt)` | Update logica elke frame |

## BEKIJK

1. Run `pgzrun zombie.py`
2. Klik op de knoppen en kijk wat er gebeurt
3. Let op het pulse effect als je over een knop hovert

## PROBEER

Verander de tekst die verschijnt als je wint of verliest. Zoek naar `resultaat_tekst = "..."` in de code.
