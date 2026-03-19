# Pygame Zero Cheatsheet

Pygame Zero maakt het makkelijk om spelletjes te maken met plaatjes en geluid!

## Opstarten

```bash
pgzrun zombie.py
```

Of in VS Code: druk op `F5`

## Het Scherm

```python
WIDTH = 800   # Breedte in pixels
HEIGHT = 600  # Hoogte in pixels
TITLE = "Mijn Spel"
```

## Tekenen (draw)

De `draw()` functie wordt 60x per seconde aangeroepen!

```python
def draw():
    screen.fill("darkgreen")              # Achtergrond kleur
    screen.blit("plaatje", (100, 200))    # Teken plaatje op x=100, y=200
```

`blit()` zal het plaatje zoeken in de folder `images`.


| Functie | Wat het doet | Voorbeeld |
|---------|--------------|-----------|
| `screen.fill()` | Vul scherm met kleur | `screen.fill("black")` |
| `screen.blit()` | Teken een plaatje | `screen.blit("zombie", (x, y))` |

### Tekst tekenen

```python
# Simpel
screen.draw.text("Hallo!", topleft=(10, 10))

# Met opties
screen.draw.text("Score: 100",
    center=(400, 300),     # Positie (midden)
    fontsize=36,           # Tekstgrootte
    color="white"          # Kleur
)
```

**Posities:** `topleft`, `topright`, `center`, `bottomleft`, `bottomright`

## Actors

Een Actor is een plaatje dat je makkelijk kan bewegen en checken.

```python
zombie = Actor("zombie")      # Maakt actor met images/zombie.png
zombie.x = 400                # Zet x positie
zombie.y = 300                # Zet y positie
zombie.pos = (400, 300)       # Of beide tegelijk
```

```python
def draw():
    zombie.draw()             # Teken de actor

def update():
    zombie.x += 5             # Beweeg naar rechts
```

### Actor collision

```python
if zombie.colliderect(speler):
    print("Geraakt!")
```

## Muis Events

```python
def on_mouse_down(pos):
    # pos = (x, y) waar geklikt is
    if zombie.collidepoint(pos):
        print("Zombie aangeklikt!")
```

### Rect (rechthoek) voor knoppen

```python
KNOP = Rect(100, 400, 150, 50)  # x, y, breedte, hoogte

def draw():
    screen.draw.filled_rect(KNOP, "green")
    screen.draw.text("Klik!", center=KNOP.center)

def on_mouse_down(pos):
    if KNOP.collidepoint(pos):
        print("Knop geklikt!")
```

## Toetsenbord Events

```python
def on_key_down(key):
    if key == keys.SPACE:
        print("Spatie!")
    if key == keys.LEFT:
        speler.x -= 10
```

**Keys:** `keys.LEFT`, `keys.RIGHT`, `keys.UP`, `keys.DOWN`, `keys.SPACE`, `keys.RETURN`

## Update (game loop)

De `update()` functie wordt ook 60x per seconde aangeroepen.

```python
def update():
    # Beweeg zombie naar rechts
    zombie.x += 2

    # Houd binnen scherm
    if zombie.x > WIDTH:
        zombie.x = 0
```

## Geluid

Geluidsbestanden in `sounds/` folder (`.wav` of `.ogg`)

```python
sounds.explosion.play()       # Speelt sounds/explosion.wav
sounds.coin.play()            # Speelt sounds/coin.wav
```

## Plaatjes

Alle plaatjes moeten in de `images/` folder staan!

| Bestand | Code |
|---------|------|
| `images/zombie.png` | `screen.blit("zombie", (0,0))` |
| `images/achtergrond.png` | `screen.blit("achtergrond", (0,0))` |

**Let op:** Geen `.png` in de code!

## Handige Patronen

### Game States (toestanden)

```python
toestand = "start"

def draw():
    if toestand == "start":
        screen.draw.text("Druk SPATIE om te starten", center=(400, 300))
    elif toestand == "spel":
        # Teken het spel
        pass
    elif toestand == "game_over":
        screen.draw.text("GAME OVER", center=(400, 300))

def on_key_down(key):
    global toestand
    if key == keys.SPACE and toestand == "start":
        toestand = "spel"
```

### Random keuze

```python
import random

kans = random.randint(1, 100)
if kans <= 50:
    print("Succes!")  # 50% kans
else:
    print("Gefaald!")
```

### Timer / Vertraging

```python
def start_timer():
    clock.schedule_unique(einde_timer, 2.0)  # 2 seconden

def einde_timer():
    print("Tijd is om!")
```

## Kleuren

Enkele kleuren die je kan gebruiken:

`"white"`, `"black"`, `"red"`, `"green"`, `"blue"`, `"yellow"`, `"orange"`, `"purple"`, `"pink"`, `"gray"`, `"darkgreen"`, `"darkblue"`, `"gold"`

Of met RGB: `(255, 0, 0)` = rood
