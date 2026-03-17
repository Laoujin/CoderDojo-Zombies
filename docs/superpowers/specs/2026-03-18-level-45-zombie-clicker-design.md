# Level 4.5: Zombie Clicker — Design Document

## Overview

**Purpose:** Bridge the gap between Level 4 (console-based with functions) and Level 5 (full Pygame Zero with state machines, timers, animations). Level 4.5 introduces Pygame Zero fundamentals in isolation.

**Target audience:** 10-16 year olds who completed Level 4.

**Game concept:** Click zombies to defeat them. Endless gameplay with score counter. Sound plays on hit.

## Game Mechanics

- A single zombie appears at a random position on screen
- Player clicks the zombie to defeat it
- On hit: play sound, increment score, zombie respawns at new random position
- No win/lose condition — endless play
- Score displayed on screen

## Pygame Zero Concepts Introduced

| Concept | Usage |
|---------|-------|
| `Actor` | The zombie sprite |
| `draw()` | Render zombie and score each frame |
| `on_mouse_down(pos)` | Detect mouse clicks |
| `actor.collidepoint(pos)` | Check if click hit the zombie |
| `sounds.xxx.play()` | Play sound effect on hit |
| `screen.draw.text()` | Display score |

## Concepts NOT Introduced (Saved for Level 5)

- `update(dt)` — no movement or animation
- `clock.schedule()` — no timers
- `Rect` — Actor handles its own collision
- State machines — no game states (playing/game over)
- `images` object — using Actor instead

## Code Structure

```
levels/level-4.5/
├── zombie.py          # Main game (~40 lines)
├── uitleg.md          # Explanation document
├── images/
│   └── zombie.png     # Zombie sprite
└── sounds/
    └── hit.wav        # Hit sound effect
```

### zombie.py outline

```python
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Zombie Clicker"

# Game variables
zombie = Actor("zombie")
score = 0

def plaats_zombie():
    """Place zombie at random position."""
    zombie.x = random.randint(50, WIDTH - 50)
    zombie.y = random.randint(50, HEIGHT - 50)

# Initial placement
plaats_zombie()

def draw():
    screen.fill("darkgreen")
    zombie.draw()
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30)

def on_mouse_down(pos):
    global score
    if zombie.collidepoint(pos):
        sounds.hit.play()
        score += 1
        plaats_zombie()
```

## Assets Required

**Images:**
- `zombie.png` — zombie sprite (can reuse from level-5 or create simpler version)

**Sounds:**
- `hit.wav` — satisfying hit/defeat sound

## Documentation (uitleg.md)

Should cover:
1. How to run (`pgzrun zombie.py`)
2. What `Actor` is and how to use it
3. The `draw()` function — called every frame
4. The `on_mouse_down(pos)` function — called on click
5. How `collidepoint()` works
6. How sounds work (file in `sounds/` folder, `sounds.name.play()`)

## Challenge Ideas

| Difficulty | Challenge |
|------------|-----------|
| Opwarmer | Change the background color |
| Opwarmer | Make the zombie bigger/smaller |
| Pittig | Add a miss counter (clicks that don't hit) |
| Pittig | Play a different sound on miss |
| Boss | Add a second zombie |
| Boss | Make zombies shrink over time (needs `update()`) |

## Success Criteria

- Kid can run the game with `pgzrun zombie.py`
- Kid understands `Actor` represents a sprite
- Kid understands `draw()` is called repeatedly
- Kid understands `on_mouse_down()` responds to clicks
- Code is ~40 lines, easy to read and modify
