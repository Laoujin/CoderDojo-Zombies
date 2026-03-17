# Level 5: Pygame Zero Clicker Game — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a graphical Pygame Zero version of the Level 2 zombie game with lives system, styled buttons, and themed result screens.

**Architecture:** Single-file Pygame Zero game using state machine pattern (`toestand` variable). All rendering in `draw()`, all input in `on_mouse_down()`. Timed transitions via `clock.schedule()`.

**Tech Stack:** Python 3, Pygame Zero (`pgzrun`)

**Spec:** `docs/superpowers/specs/2026-03-17-level-5-pygame-zero-design.md`

---

## File Structure

```
levels/level-5/
├── zombie.py           # Main game code
└── images/
    ├── achtergrond.png
    ├── knop_vechten.png
    ├── knop_rennen.png
    ├── hart.png
    ├── resultaat_goed.png
    ├── resultaat_slecht.png
    └── game_over.png
```

**Note:** Images are created by the user. Documentation files (`uitleg.md`, `challenges.md`) will be added later when requested.

---

## Chunk 1: Project Setup and Main Game Screen

### Task 1: Create folder structure and placeholder images

**Files:**
- Create: `levels/level-5/zombie.py`
- Create: `levels/level-5/images/` (folder)

- [ ] **Step 1: Create the level-5 folder and images subfolder**

```bash
mkdir levels\level-5\images
```

(On Unix/Mac: `mkdir -p levels/level-5/images`)

- [ ] **Step 2: Create minimal zombie.py that runs**

```python
# Zombie Apocalypse - Level 5
# Run met: pgzrun zombie.py

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Apocalypse"


def draw():
    screen.fill("darkgreen")
    screen.draw.text("Level 5 - Coming Soon!", center=(400, 300), fontsize=48, color="white")
```

- [ ] **Step 3: Verify it runs**

Run: `pgzrun levels/level-5/zombie.py`
Expected: Window opens with green background and "Coming Soon!" text

- [ ] **Step 4: Commit**

```bash
git add levels/level-5/
git commit -m "Level 5: initial setup with placeholder"
```

---

### Task 2: Add game state variables and draw main screen

**Files:**
- Modify: `levels/level-5/zombie.py`

- [ ] **Step 1: Add game state variables**

Add after the WIDTH/HEIGHT/TITLE constants:

```python
import random

# === GAME STATE ===
toestand = "spel"  # "spel", "resultaat", "game_over"
levens = 3
resultaat_tekst = ""
resultaat_goed = False

# Button positions (x, y, width, height)
KNOP_VECHTEN = Rect(100, 480, 150, 80)
KNOP_RENNEN = Rect(550, 480, 150, 80)
```

- [ ] **Step 2: Update draw() for "spel" state with rectangles as placeholders**

Replace the `draw()` function:

```python
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
        screen.fill("black")
        screen.draw.text("Resultaat...", center=(400, 300), fontsize=36, color="white")

    elif toestand == "game_over":
        screen.fill("darkred")
        screen.draw.text("GAME OVER", center=(400, 300), fontsize=60, color="white")
```

- [ ] **Step 3: Verify it runs**

Run: `pgzrun levels/level-5/zombie.py`
Expected: Green screen with title, 3 hearts, and two colored button rectangles

- [ ] **Step 4: Commit**

```bash
git add levels/level-5/zombie.py
git commit -m "Level 5: add game state and main screen layout"
```

---

### Task 3: Add button click handling

**Files:**
- Modify: `levels/level-5/zombie.py`

- [ ] **Step 1: Add on_mouse_down function**

Add after the `draw()` function:

```python
def on_mouse_down(pos):
    global toestand, levens, resultaat_tekst, resultaat_goed

    if toestand == "spel":
        if KNOP_VECHTEN.collidepoint(pos):
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
```

- [ ] **Step 2: Add helper functions**

Add after `on_mouse_down`:

```python
def ga_naar_volgende():
    global toestand
    if levens <= 0:
        toestand = "game_over"
    else:
        toestand = "spel"


def reset_game():
    global toestand, levens, resultaat_tekst, resultaat_goed
    toestand = "spel"
    levens = 3
    resultaat_tekst = ""
    resultaat_goed = False
```

- [ ] **Step 3: Update draw() resultaat state to show result text**

Replace the `elif toestand == "resultaat":` block in `draw()`:

```python
    elif toestand == "resultaat":
        if resultaat_goed:
            screen.fill("darkgreen")
        else:
            screen.fill("darkred")
        screen.draw.text(resultaat_tekst, center=(400, 300), fontsize=36, color="white")
```

- [ ] **Step 4: Verify it runs**

Run: `pgzrun levels/level-5/zombie.py`
Expected:
- Click VECHTEN or RENNEN → shows result screen for 2 seconds
- Returns to main screen (or game over if lives = 0)
- Click on game over screen → restarts

- [ ] **Step 5: Commit**

```bash
git add levels/level-5/zombie.py
git commit -m "Level 5: add button clicks and game flow"
```

---

## Chunk 2: Add Images

### Task 4: Replace placeholders with images

**Files:**
- Modify: `levels/level-5/zombie.py`

**Prerequisite:** User has created the 7 required images in `levels/level-5/images/`

- [ ] **Step 1: Update draw() to use background image in "spel" state**

Replace the `if toestand == "spel":` block:

```python
    if toestand == "spel":
        # Background with zombie
        screen.blit("achtergrond", (0, 0))

        # Hearts (lives)
        for i in range(levens):
            screen.blit("hart", (20 + i * 50, 20))

        # Buttons
        screen.blit("knop_vechten", KNOP_VECHTEN.topleft)
        screen.blit("knop_rennen", KNOP_RENNEN.topleft)
```

- [ ] **Step 2: Update draw() to use result images**

Replace the `elif toestand == "resultaat":` block:

```python
    elif toestand == "resultaat":
        if resultaat_goed:
            screen.blit("resultaat_goed", (0, 0))
        else:
            screen.blit("resultaat_slecht", (0, 0))
        screen.draw.text(resultaat_tekst, center=(400, 300), fontsize=36, color="white")
```

- [ ] **Step 3: Update draw() to use game over image**

Replace the `elif toestand == "game_over":` block:

```python
    elif toestand == "game_over":
        screen.blit("game_over", (0, 0))
        screen.draw.text("GAME OVER", center=(400, 250), fontsize=60, color="white")
        screen.draw.text("Klik om opnieuw te spelen", center=(400, 350), fontsize=24, color="gray")
```

- [ ] **Step 4: Verify it runs with images**

Run: `pgzrun levels/level-5/zombie.py`
Expected: All screens show images instead of solid colors

- [ ] **Step 5: Commit**

```bash
git add levels/level-5/zombie.py
git commit -m "Level 5: add image rendering"
```

---

## Chunk 3: Polish

### Task 5: Final polish

**Files:**
- Modify: `levels/level-5/zombie.py`

- [ ] **Step 1: Add text shadow/outline for readability**

Create a helper function at the top of the file (after imports):

```python
def teken_tekst(tekst, center, fontsize, kleur="white"):
    """Teken tekst met een schaduw voor betere leesbaarheid."""
    x, y = center
    # Shadow
    screen.draw.text(tekst, center=(x+2, y+2), fontsize=fontsize, color="black")
    # Text
    screen.draw.text(tekst, center=(x, y), fontsize=fontsize, color=kleur)
```

- [ ] **Step 2: Use teken_tekst() for result and game over text**

Update the resultaat and game_over blocks to use the helper:

```python
    elif toestand == "resultaat":
        if resultaat_goed:
            screen.blit("resultaat_goed", (0, 0))
        else:
            screen.blit("resultaat_slecht", (0, 0))
        teken_tekst(resultaat_tekst, center=(400, 300), fontsize=36)

    elif toestand == "game_over":
        screen.blit("game_over", (0, 0))
        teken_tekst("GAME OVER", center=(400, 250), fontsize=60, kleur="red")
        teken_tekst("Klik om opnieuw te spelen", center=(400, 350), fontsize=24, kleur="gray")
```

- [ ] **Step 3: Verify final game**

Run: `pgzrun levels/level-5/zombie.py`
Expected: Complete game loop with images, readable text, smooth transitions

- [ ] **Step 4: Commit**

```bash
git add levels/level-5/zombie.py
git commit -m "Level 5: add text shadow for readability"
```

---

## Complete Code Reference

For reference, here is the complete `zombie.py` after all tasks:

```python
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

# Button positions (x, y, width, height) - adjust to match your images
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
        if resultaat_goed:
            screen.blit("resultaat_goed", (0, 0))
        else:
            screen.blit("resultaat_slecht", (0, 0))
        teken_tekst(resultaat_tekst, center=(400, 300), fontsize=36)

    elif toestand == "game_over":
        screen.blit("game_over", (0, 0))
        teken_tekst("GAME OVER", center=(400, 250), fontsize=60, kleur="red")
        teken_tekst("Klik om opnieuw te spelen", center=(400, 350), fontsize=24, kleur="gray")


def on_mouse_down(pos):
    global toestand, levens, resultaat_tekst, resultaat_goed

    if toestand == "spel":
        if KNOP_VECHTEN.collidepoint(pos):
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
    global toestand, levens, resultaat_tekst, resultaat_goed
    toestand = "spel"
    levens = 3
    resultaat_tekst = ""
    resultaat_goed = False
```
