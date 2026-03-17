# Level 5: Pygame Zero Clicker Game — Design Document

## Overview

**Goal**: Translate the Level 2 text-based game into a graphical Pygame Zero game. Introduces core Pygame Zero concepts while keeping gameplay simple (lives system, game loop until death).

**Target audience**: Kids 8-16 who completed Levels 1-4 (text-based Python).

**Why this approach**: Level 5 focuses on learning Pygame Zero, not adding gameplay complexity. By recreating Level 2's mechanics graphically, kids see their familiar game come to life visually.

---

## Pygame Zero Concepts Taught

| Concept | How it's used |
|---------|---------------|
| `draw()` | Main render function, called every frame |
| `screen.blit()` | Drawing images (background, buttons, hearts, result screens) |
| `screen.draw.text()` | Dynamic text overlay on result screens |
| `Rect` | Button hit detection |
| `on_mouse_down(pos)` | Handling mouse clicks |
| `clock.schedule()` | Timed transitions between states |
| Game state variables | Managing `toestand`, `levens`, tracking game flow |

---

## Game Flow

```
┌─────────────────────────────────────────────────────────┐
│  MAIN SCREEN                                            │
│  - Background with zombie                               │
│  - Fight button, Run button                             │
│  - 3 heart icons (lives)                                │
│                                                         │
│  Player clicks a button...                              │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│  RESULT SCREEN                                          │
│  - Success OR failure background image                  │
│  - Text overlay ("Je bent ontsnapt!" / "De zombie       │
│    bijt je...")                                         │
│  - clock.schedule() waits ~2 seconds                    │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│  STATE UPDATE                                           │
│  - If failure: levens -= 1                              │
│  - If levens > 0: back to MAIN SCREEN                   │
│  - If levens == 0: go to GAME OVER                      │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼ (when levens == 0)
┌─────────────────────────────────────────────────────────┐
│  GAME OVER SCREEN                                       │
│  - Themed game over background (graveyard/zombie win)   │
│  - "GAME OVER" text                                     │
│  - Click anywhere to restart                            │
└─────────────────────────────────────────────────────────┘
```

---

## Game States

```python
toestand = "spel"  # "spel", "resultaat", "game_over"
```

| State | Description |
|-------|-------------|
| `"spel"` | Main game screen, waiting for player input |
| `"resultaat"` | Showing result (success/failure), auto-advances after delay |
| `"game_over"` | Game ended, click to restart |

---

## Gameplay Mechanics

- **Lives**: Player starts with 3 lives (heart icons)
- **Actions**: Fight or Run (click styled buttons)
- **Outcomes**: 50/50 random chance for each action
  - Fight win: zombie defeated, continue
  - Fight lose: bitten, lose 1 life
  - Run success: escaped, continue
  - Run fail: caught, lose 1 life
- **Game over**: When lives reach 0
- **Restart**: Click anywhere on game over screen

---

## Images Required

All images go in `levels/level-5/images/` folder.

| Filename | Dimensions | Description |
|----------|------------|-------------|
| `achtergrond.png` | 800x600 | Main scene with zombie visible |
| `knop_vechten.png` | ~150x80 | Fight button (weapon icon, themed) |
| `knop_rennen.png` | ~150x80 | Run button (escape icon, themed) |
| `hart.png` | ~40x40 | Heart icon for lives display |
| `resultaat_goed.png` | 800x600 | Success background |
| `resultaat_slecht.png` | 800x600 | Failure background |
| `game_over.png` | 800x600 | Death/game over background |

**Note**: Button dimensions are approximate. Exact hit detection will use `Rect` based on actual image size and position.

---

## Screen Layout

```
┌────────────────────────────────────────────────────────────┐
│  ♥ ♥ ♥                                        (top-left)  │
│                                                            │
│                                                            │
│                    [ZOMBIE IN BACKGROUND]                  │
│                                                            │
│                                                            │
│                                                            │
│         [VECHTEN]                    [RENNEN]              │
│         (bottom-left area)           (bottom-right area)   │
└────────────────────────────────────────────────────────────┘
```

- Hearts: top-left corner, spaced horizontally
- Buttons: bottom area, left and right sides
- Zombie: part of background image, centered

---

## Code Structure

```python
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Apocalypse"

# Game state
toestand = "spel"
levens = 3
resultaat_tekst = ""
resultaat_goed = False

# Button positions (Rect for hit detection)
knop_vechten = Rect(100, 480, 150, 80)
knop_rennen = Rect(550, 480, 150, 80)

def draw():
    if toestand == "spel":
        # Draw background, buttons, hearts
        ...
    elif toestand == "resultaat":
        # Draw result image + text
        ...
    elif toestand == "game_over":
        # Draw game over screen
        ...

def on_mouse_down(pos):
    # Handle button clicks based on current state
    ...

def ga_naar_spel():
    # Called by clock.schedule() to return to main screen
    ...

def reset_game():
    # Reset all state for new game
    ...
```

---

## File Location

```
levels/level-5/
├── zombie.py
├── uitleg.md
├── challenges.md
└── images/
    ├── achtergrond.png
    ├── knop_vechten.png
    ├── knop_rennen.png
    ├── hart.png
    ├── resultaat_goed.png
    ├── resultaat_slecht.png
    └── game_over.png
```

---

## Out of Scope (Level 5)

These are intentionally deferred to keep Level 5 focused on Pygame Zero basics:

- Score tracking
- Zombie types / variations
- Inventory system
- Sound effects
- Animations
- `Actor` class (zombie is baked into background)

These can become Level 5 challenges or Level 6+ features.

---

## Success Criteria

1. Game runs with `pgzrun zombie.py`
2. Player can click fight/run buttons
3. Random outcomes display with themed result screens
4. Lives decrease on failure (hearts disappear)
5. Game over screen shows when lives = 0
6. Click to restart works
7. Code is readable and follows patterns from Levels 1-4
