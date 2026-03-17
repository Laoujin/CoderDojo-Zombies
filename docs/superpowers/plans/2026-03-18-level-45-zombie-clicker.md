# Level 4.5: Zombie Clicker Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a simple Pygame Zero clicker game that introduces `Actor`, `draw()`, `on_mouse_down()`, and sounds — bridging Level 4 (console) and Level 5 (full Pygame Zero).

**Architecture:** Single-file game (~40 lines) with one Actor (zombie), click detection, score counter, and sound effect. No state machine, no timers, no movement.

**Tech Stack:** Python, Pygame Zero

**Spec:** `docs/superpowers/specs/2026-03-18-level-45-zombie-clicker-design.md`

---

## File Structure

```
levels/level-4.5/
├── zombie.py          # Main game code
├── uitleg.md          # Documentation for kids
├── images/
│   └── zombie.png     # Zombie sprite (create simple one)
└── sounds/
    └── hit.wav        # Hit sound effect (source from freesound or similar)
```

---

## Chunk 1: Assets and Directory Setup

### Task 1: Create directory structure

**Files:**
- Create: `levels/level-4.5/images/` (directory)
- Create: `levels/level-4.5/sounds/` (directory)

- [ ] **Step 1: Create level-4.5 directory with subdirectories**

```bash
mkdir -p levels/level-4.5/images levels/level-4.5/sounds
```

- [ ] **Step 2: Verify structure**

```bash
ls -la levels/level-4.5/
```

Expected: `images/` and `sounds/` directories exist.

---

### Task 2: Add zombie sprite

**Files:**
- Create: `levels/level-4.5/images/zombie.png`

The zombie sprite needs to be a simple, clickable image. Options:
1. Create a simple colored circle/square as placeholder
2. Use an online free asset
3. Generate with an image tool

- [ ] **Step 1: Create a simple placeholder zombie image**

Use Python to generate a simple 100x100 green circle as a placeholder zombie:

```python
# Run once to generate placeholder
from PIL import Image, ImageDraw

img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.ellipse([5, 5, 95, 95], fill=(100, 150, 100), outline=(50, 100, 50))
draw.ellipse([25, 30, 40, 45], fill=(200, 50, 50))  # left eye
draw.ellipse([60, 30, 75, 45], fill=(200, 50, 50))  # right eye
draw.arc([30, 55, 70, 75], 0, 180, fill=(50, 80, 50), width=3)  # mouth
img.save('levels/level-4.5/images/zombie.png')
print("Created zombie.png")
```

Run: `python -c "<above code>"` or save as temp script and run.

Alternative: Download a free zombie icon from a site like game-icons.net or opengameart.org.

- [ ] **Step 2: Verify image exists**

```bash
ls -la levels/level-4.5/images/
```

Expected: `zombie.png` exists.

---

### Task 3: Add hit sound

**Files:**
- Create: `levels/level-4.5/sounds/hit.wav`

- [ ] **Step 1: Source or create a hit sound**

Options:
1. Download from freesound.org (search "hit" or "punch", pick a short one)
2. Use `ffmpeg` to generate a simple beep:

```bash
ffmpeg -f lavfi -i "sine=frequency=800:duration=0.1" -ar 44100 levels/level-4.5/sounds/hit.wav
```

Or download a free sound effect.

- [ ] **Step 2: Verify sound exists**

```bash
ls -la levels/level-4.5/sounds/
```

Expected: `hit.wav` exists.

- [ ] **Step 3: Commit assets**

```bash
git add levels/level-4.5/images levels/level-4.5/sounds
git commit -m "Add level 4.5 assets (zombie sprite, hit sound)"
```

---

## Chunk 2: Game Code

### Task 4: Write zombie.py

**Files:**
- Create: `levels/level-4.5/zombie.py`

- [ ] **Step 1: Create the game file**

Write `levels/level-4.5/zombie.py`:

```python
# Zombie Clicker - Level 4.5
# Start met: pgzrun zombie.py

import random

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
        sounds.hit.play()
        score += 1
        plaats_zombie()
```

- [ ] **Step 2: Test the game runs**

```bash
cd levels/level-4.5 && pgzrun zombie.py
```

Expected: Window opens, zombie visible, clicking zombie increases score and plays sound.

- [ ] **Step 3: Commit game code**

```bash
git add levels/level-4.5/zombie.py
git commit -m "Add level 4.5 zombie clicker game"
```

---

## Chunk 3: Documentation

### Task 5: Write uitleg.md

**Files:**
- Create: `levels/level-4.5/uitleg.md`

- [ ] **Step 1: Create the documentation file**

Write `levels/level-4.5/uitleg.md`:

```markdown
# Level 4.5: Pygame Zero Intro

## Wat leer je?

In dit level leer je over **Pygame Zero** - een library om grafische spelletjes te maken. Je leert hoe je een plaatje op het scherm zet en hoe je muisklikken afhandelt.

## Opstarten

```bash
cd levels/level-4.5
pgzrun zombie.py
```

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
        sounds.hit.play()
        score += 1
        plaats_zombie()
```

- `on_mouse_down(pos)` wordt aangeroepen als je klikt
- `pos` is de (x, y) positie van je muisklik
- `zombie.collidepoint(pos)` checkt of je op de zombie klikte
- `global score` is nodig om de score variabele aan te passen

### Geluiden afspelen

```python
sounds.hit.play()
```

- Geluidsbestanden staan in de `sounds/` map
- `sounds.hit` verwijst naar `sounds/hit.wav`
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
```

- [ ] **Step 2: Verify documentation renders correctly**

Check the markdown renders properly (preview in VS Code or similar).

- [ ] **Step 3: Commit documentation**

```bash
git add levels/level-4.5/uitleg.md
git commit -m "Add level 4.5 documentation"
```

---

## Chunk 4: Integration

### Task 6: Update VS Code launch config (optional)

**Files:**
- Modify: `.vscode/launch.json`

The existing launch config should work since it runs `pgzrun ${file}`. No changes needed unless we want a specific config.

- [ ] **Step 1: Test launch config works**

Open `levels/level-4.5/zombie.py` in VS Code and press F5.

Expected: Game runs.

---

### Task 7: Final verification

- [ ] **Step 1: Run the complete game**

```bash
cd levels/level-4.5 && pgzrun zombie.py
```

Verify:
- Window opens with green background
- Zombie sprite visible
- Clicking zombie plays sound
- Score increments
- Zombie moves to new position

- [ ] **Step 2: Review code is ~40 lines and readable**

```bash
wc -l levels/level-4.5/zombie.py
```

Expected: ~35-45 lines.

- [ ] **Step 3: Final commit if any changes**

```bash
git status
# If changes exist:
git add -A && git commit -m "Level 4.5 zombie clicker complete"
```

---

## Summary

After completing this plan:
- `levels/level-4.5/` contains a working Pygame Zero clicker game
- Kids learn: `Actor`, `draw()`, `on_mouse_down()`, `collidepoint()`, `sounds`
- Documentation explains each concept in Dutch
- Ready to progress to Level 5 (state machines, timers, animations)
