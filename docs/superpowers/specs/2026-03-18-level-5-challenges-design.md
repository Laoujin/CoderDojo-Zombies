# Level 5 Challenges Design

## Overview

Six challenges for Level 5 (Pygame Zero) following the 3-tier difficulty structure. Challenges mix visual/graphical concepts with gameplay mechanics, building progressively in complexity.

## Target Audience

Kids 8-16 who have completed levels 1-4. They understand Python basics (variables, functions, lists, dictionaries) and have just learned Pygame Zero fundamentals from `uitleg.md`.

## Challenge Structure

| Tier | Count | Focus |
|------|-------|-------|
| Opwarmer | 2 | Features that were "pittig" in earlier levels |
| Pittig | 2 | Inventory and zombie variety systems |
| Boss | 2 | Multi-location progression with search mechanic |

---

## Opwarmer Challenges

### Opwarmer 1: Score Teller

Add a score counter that increases with each successful action.

**Requirements:**
- Global `score` variable starting at 0
- +10 points for successful fight
- +5 points for successful escape
- Display score in top-right corner using `screen.draw.text()`
- Score persists across rounds
- Score resets on game over

**Hint:**
```python
screen.draw.text(f"Score: {score}", topright=(780, 20), fontsize=24, color="white")
```

**Concepts practiced:** Global variables, string formatting, `screen.draw.text()`

---

### Opwarmer 2: Verstoppen

Add a third button "Verstoppen" (hide) as an alternative action.

**Requirements:**
- New `KNOP_VERSTOPPEN = Rect(...)` in center position
- Draw button in `draw()` with pulse effect (reuse `teken_knop_met_pulse`)
- Handle click in `on_mouse_down()` with 50/50 win/lose odds
- Success text: "De zombie ziet je niet!"
- Fail text: "De zombie vindt je!"
- New `laatste_actie = "verstoppen"` case

**New images required:**
- `knop_verstoppen.png`
- `verstoppen_succes.png`
- `verstoppen_faal.png`

**Hint:**
```python
KNOP_VERSTOPPEN = Rect(325, 400, 150, 150)

# In draw():
teken_knop_met_pulse("knop_verstoppen", KNOP_VERSTOPPEN)

# In on_mouse_down():
elif KNOP_VERSTOPPEN.collidepoint(pos):
    laatste_actie = "verstoppen"
    if random.randint(1, 2) == 1:
        resultaat_tekst = "De zombie ziet je niet!"
        resultaat_goed = True
    else:
        resultaat_tekst = "De zombie vindt je!"
        resultaat_goed = False
        levens -= 1
    toestand = "resultaat"
    clock.schedule(ga_naar_volgende, 2.5)
```

**Concepts practiced:** Rect, click detection, extending existing patterns

---

## Pittig Challenges

### Pittig 1: Inventory Systeem

Add an inventory that stores items and affects gameplay.

**Requirements:**
- Global `inventory = []` list
- Display inventory on screen (text list or icons)
- Item types:
  - **Weapons** (honkbalknuppel, mes): improve fight odds from 50% to 66%
  - **Healing** (medkit, energie bar): medkit restores 2 lives, energie bar restores 1 life
- Use healing items via button or automatically when found
- For standalone testing, items can be found randomly (1 in 4 chance per round)

**Hint:**
```python
inventory = []

# In draw(), show inventory:
for i, item in enumerate(inventory):
    screen.draw.text(item, topleft=(20, 80 + i * 25), fontsize=18, color="white")

# Modified fight logic:
if "honkbalknuppel" in inventory or "mes" in inventory:
    win = random.randint(1, 3) <= 2  # 66% kans
else:
    win = random.randint(1, 2) == 1  # 50% kans

# Use medkit:
if "medkit" in inventory and levens < 3:
    inventory.remove("medkit")
    levens = min(levens + 2, 5)
```

**Concepts practiced:** Lists, `in` operator, game balance

---

### Pittig 2: Zombie Types

Different zombies appear with different win/lose chances.

**Requirements:**
- Global `huidige_zombie` variable
- Zombie types with win chances:
  - Baby zombie: 66% (easy)
  - Langzame zombie: 50% (medium)
  - Snelle zombie: 40% (hard)
  - Sterke zombie: 33% (very hard)
- Random zombie selection at start of each round
- Display zombie type name on screen
- Optional: different zombie images per type

**Hint:**
```python
zombie_kansen = {
    "Baby zombie": (2, 3),      # win op 1-2 van 3
    "Langzame zombie": (1, 2),  # win op 1 van 2
    "Snelle zombie": (2, 5),    # win op 1-2 van 5
    "Sterke zombie": (1, 3),    # win op 1 van 3
}

huidige_zombie = random.choice(list(zombie_kansen.keys()))

# In fight logic:
kans = zombie_kansen[huidige_zombie]
win = random.randint(1, kans[1]) <= kans[0]

# In draw():
screen.draw.text(huidige_zombie, center=(400, 550), fontsize=24, color="yellow")
```

**Concepts practiced:** Dictionaries, tuples, random selection

---

## Boss Challenges

### Boss 1: Meerdere Locaties

Progress through 5 locations to win the game.

**Requirements:**
- Location list: `["Suburb", "Library", "School", "Hospital", "Mall"]`
- Global `locatie_index = 0` tracking progress
- Display current location name prominently
- Different background image per location
- Progression rules:
  - Any success (fight win OR run success) → advance
  - Any fail → lose life AND advance (can't stay forever)
- Win condition: survive past Mall → victory screen
- New state: `toestand = "gewonnen"`

**New images required:**
- `achtergrond_suburb.png`
- `achtergrond_library.png`
- `achtergrond_school.png`
- `achtergrond_hospital.png`
- `achtergrond_mall.png`
- `gewonnen.png`

**Hint:**
```python
locaties = ["Suburb", "Library", "School", "Hospital", "Mall"]
locatie_index = 0

def ga_naar_volgende():
    global toestand, locatie_index
    if levens <= 0:
        toestand = "game_over"
    elif locatie_index >= len(locaties) - 1:
        toestand = "gewonnen"
    else:
        locatie_index += 1
        toestand = "spel"

# In draw() for "spel" state:
achtergrond = f"achtergrond_{locaties[locatie_index].lower()}"
screen.blit(achtergrond, (0, 0))
screen.draw.text(locaties[locatie_index], center=(400, 30), fontsize=28, color="white")

# In draw() for "gewonnen" state:
elif toestand == "gewonnen":
    screen.blit("gewonnen", (0, 0))
    screen.draw.text("JE HEBT GEWONNEN!", center=(400, 300), fontsize=48, color="gold")
```

**Concepts practiced:** Lists, indexing, string formatting, state machine extension

---

### Boss 2: Zoeken na Gevecht

Win a fight to unlock the option to search the area for items.

**Requirements:**
- Prerequisite: Boss 1 (locations) + Pittig 1 (inventory)
- New state: `toestand = "zoeken"` after successful fight only
- "Zoeken" button appears on fight victory screen
- Click to search: 50% chance to find item
- Possible items: medkit, honkbalknuppel, energie bar, mes
- "Je vindt een [item]!" or "Je vindt niks..."
- After search → advance to next location
- Run success or any fail → skip search, advance directly

**New images required:**
- `knop_zoeken.png`

**Hint:**
```python
# After successful fight in on_mouse_down():
if laatste_actie == "vechten" and resultaat_goed:
    toestand = "zoeken"
else:
    toestand = "resultaat"
    clock.schedule(ga_naar_volgende, 2.5)

# New state handling in on_mouse_down():
elif toestand == "zoeken":
    if KNOP_ZOEKEN.collidepoint(pos):
        if random.randint(1, 2) == 1:
            item = random.choice(["medkit", "honkbalknuppel", "energie bar", "mes"])
            inventory.append(item)
            resultaat_tekst = f"Je vindt een {item}!"
        else:
            resultaat_tekst = "Je vindt niks..."
        toestand = "resultaat"
        clock.schedule(ga_naar_volgende, 2.0)
    elif KNOP_DOORGAAN.collidepoint(pos):
        # Skip search
        clock.schedule(ga_naar_volgende, 0.1)

# In draw() for "zoeken" state:
elif toestand == "zoeken":
    screen.blit("vechten_succes", (0, 0))
    screen.draw.text("Wil je het gebied doorzoeken?", center=(400, 80), fontsize=28)
    teken_knop_met_pulse("knop_zoeken", KNOP_ZOEKEN)
```

**Concepts practiced:** Complex state machine, conditional logic, combining systems

---

## Image Assets Summary

| Challenge | New Images |
|-----------|------------|
| Opwarmer 2 | `knop_verstoppen.png`, `verstoppen_succes.png`, `verstoppen_faal.png` |
| Boss 1 | `achtergrond_suburb.png`, `achtergrond_library.png`, `achtergrond_school.png`, `achtergrond_hospital.png`, `achtergrond_mall.png`, `gewonnen.png` |
| Boss 2 | `knop_zoeken.png` |

Total: 10 new images

---

## Challenge Dependencies

```
Opwarmer 1: Score Teller ─────────────────────────────────┐
Opwarmer 2: Verstoppen ───────────────────────────────────┤
                                                          ├─► Can be done
Pittig 1: Inventory Systeem ──────────────────────────────┤   independently
Pittig 2: Zombie Types ───────────────────────────────────┤
                                                          │
Boss 1: Meerdere Locaties ────────────────────────────────┘
            │
            ▼
Boss 2: Zoeken na Gevecht (requires Boss 1 + Pittig 1)
```

---

## Output File

Create `levels/level-5/uitdagingen.md` following the format of levels 1-4:
- Markdown headers for each tier
- Challenge name as H3
- Brief description
- **Hint:** section with code example
