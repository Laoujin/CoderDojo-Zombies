# Level 4.5: Pygame Zero Intro

## Wat leer je?

In dit level leer je over **Pygame Zero** - een library om grafische spelletjes te maken. Je leert hoe je een plaatje op het scherm zet en hoe je muisklikken afhandelt.

## Opstarten

```bash
cd levels/level-4.5
pgzrun zombie.py
```

Of open `zombie.py` in VS Code en druk op `F5`.

## De code

### Het scherm instellen

```python
WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Clicker"
```

Dit bepaalt de grootte en titel van je spelvenster.

### Een Actor maken

```python
zombie = Actor("zombie")
```

- Een `Actor` is een plaatje dat je kan tekenen en verplaatsen
- `"zombie"` verwijst naar `images/zombie.png`
- De Actor heeft een `x` en `y` positie

### De draw() functie

```python
def draw():
    screen.fill("darkgreen")
    zombie.draw()
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30)
```

- `draw()` wordt **elke frame** aangeroepen (60x per seconde!)
- `screen.fill()` vult het scherm met een kleur
- `zombie.draw()` tekent de zombie op zijn huidige positie
- `screen.draw.text()` tekent tekst op het scherm

### Klikken detecteren

```python
def on_mouse_down(pos):
    global score
    if zombie.collidepoint(pos):
        sounds.whack.play()
        score += 1
        plaats_zombie()
```

- `on_mouse_down(pos)` wordt aangeroepen als je klikt
- `pos` is de (x, y) positie van je muisklik
- `zombie.collidepoint(pos)` checkt of je op de zombie klikte
- `global score` is nodig om de score variabele aan te passen

### Geluiden afspelen

```python
sounds.whack.play()
```

- Geluidsbestanden staan in de `sounds/` map
- `sounds.whack` verwijst naar `sounds/whack.wav`
- `.play()` speelt het geluid af

## Nieuwe concepten

| Concept | Wat het doet |
|---------|--------------|
| `Actor("naam")` | Maak een sprite van `images/naam.png` |
| `actor.draw()` | Teken de actor op het scherm |
| `actor.x`, `actor.y` | Positie van de actor |
| `actor.collidepoint(pos)` | Check of een punt de actor raakt |
| `draw()` | Wordt elke frame aangeroepen om te tekenen |
| `on_mouse_down(pos)` | Wordt aangeroepen bij muisklik |
| `sounds.naam.play()` | Speel `sounds/naam.wav` af |

## BEKIJK

1. Run `pgzrun zombie.py`
2. Klik op de zombie
3. Let op hoe de score omhoog gaat

## PROBEER

Verander de achtergrondkleur van `"darkgreen"` naar een andere kleur zoals `"purple"` of `"black"`.
