# Zombie Curriculum Implementation Plan

> **STATUS: COMPLETED** - All text-based levels (1-4) have been implemented and deployed. See "Implementation Notes" at the end for changes made during implementation.

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a complete Python learning curriculum for CoderDojo using a zombie game theme, with 4 text-based levels, documentation website, and printable challenge cards.

**Architecture:** Each level is self-contained in its own folder with code, explanation, and challenges. MkDocs aggregates everything into a website. Challenge cards are generated from the same Markdown source using a CSS print stylesheet.

**Tech Stack:** Python 3, MkDocs with Material theme, friendly-traceback, Pygame Zero (later levels)

**Spec:** `docs/superpowers/specs/2026-03-15-zombie-curriculum-design.md`

---

## File Structure

```
CoderDojo-Zombies/
├── levels/
│   ├── level-1/
│   │   ├── zombie.py           # Move from Zombie1.py
│   │   ├── uitleg.md           # Level explanation
│   │   └── uitdagingen.md      # Challenge cards source
│   ├── level-2/
│   │   ├── zombie.py           # Move from Zombie2.py
│   │   ├── uitleg.md
│   │   └── uitdagingen.md
│   ├── level-3/
│   │   ├── zombie.py           # New: inventory + zombie types
│   │   ├── uitleg.md
│   │   └── uitdagingen.md
│   └── level-4/
│       ├── zombie.py           # New: functions + I/O
│       ├── uitleg.md
│       └── uitdagingen.md
├── docs/
│   ├── index.md                # Landing page
│   ├── aan-de-slag.md          # Getting started guide
│   ├── stylesheets/
│   │   └── print-cards.css     # Print stylesheet for cards
│   └── cheatsheet.md           # Python keywords NL→EN
├── mkdocs.yml                  # MkDocs configuration
└── README.md                   # Project overview
```

---

## Chunk 1: Project Setup & Level 1-2 Migration

### Task 1: Create folder structure

**Files:**
- Create: `levels/level-1/` (directory)
- Create: `levels/level-2/` (directory)
- Create: `levels/level-3/` (directory)
- Create: `levels/level-4/` (directory)
- Create: `docs/stylesheets/` (directory)

- [x] **Step 1: Create level directories**

```bash
mkdir -p levels/level-1 levels/level-2 levels/level-3 levels/level-4
mkdir -p docs/stylesheets
```

- [x] **Step 2: Verify structure**

```bash
ls -la levels/
```

Expected: 4 directories (level-1 through level-4)

- [x] **Step 3: Commit**

```bash
git add levels/ docs/
git commit -m "Create level folder structure"
```

---

### Task 2: Migrate Level 1

**Files:**
- Move: `Zombie1.py` → `levels/level-1/zombie.py`
- Modify: Add friendly-traceback import

- [ ] **Step 1: Copy Zombie1.py to new location**

```bash
cp Zombie1.py levels/level-1/zombie.py
```

- [ ] **Step 2: Add friendly-traceback to the file**

Edit `levels/level-1/zombie.py` — add at the very top (before other imports):

```python
import friendly
friendly.install()

```

- [ ] **Step 3: Verify file runs**

```bash
cd levels/level-1 && python zombie.py
```

Expected: Game runs, prompts for input

- [ ] **Step 4: Commit**

```bash
git add levels/level-1/zombie.py
git commit -m "Add Level 1: if/elif/else basics"
```

---

### Task 3: Migrate Level 2

**Files:**
- Move: `Zombie2.py` → `levels/level-2/zombie.py`
- Modify: Add friendly-traceback import

- [ ] **Step 1: Copy Zombie2.py to new location**

```bash
cp Zombie2.py levels/level-2/zombie.py
```

- [ ] **Step 2: Add friendly-traceback to the file**

Edit `levels/level-2/zombie.py` — add at the very top:

```python
import friendly
friendly.install()

```

- [ ] **Step 3: Verify file runs**

```bash
cd levels/level-2 && python zombie.py
```

Expected: Game runs with lives system

- [ ] **Step 4: Commit**

```bash
git add levels/level-2/zombie.py
git commit -m "Add Level 2: while loops and state"
```

---

### Task 4: Create Level 1 documentation

**Files:**
- Create: `levels/level-1/uitleg.md`
- Create: `levels/level-1/uitdagingen.md`

- [ ] **Step 1: Create uitleg.md**

Create `levels/level-1/uitleg.md`:

```markdown
# Level 1: Keuzes Maken

## Wat leer je?

In dit level leer je hoe je de computer keuzes laat maken met `if`, `elif` en `else`. Je leert ook hoe je input van de speler vraagt met `input()`.

## De code

Bekijk de code in `zombie.py`. Dit is wat elk deel doet:

### Imports

```python
import random
import time
```

`import` haalt extra functies binnen. `random` is voor willekeurige getallen, `time` is voor pauzes.

### Input vragen

```python
actie = input("Wat doe je? (rennen / vechten) ➜ ")
```

Dit vraagt de speler om te typen. Wat ze typen komt in de variabele `actie`.

### Keuzes maken

```python
if actie == "rennen":
    # dit gebeurt als je "rennen" typt
elif actie == "vechten":
    # dit gebeurt als je "vechten" typt
else:
    # dit gebeurt bij alles anders
```

Let op de dubbele `==` ! Eén `=` is voor toewijzen, twee `==` is voor vergelijken.

## BEKIJK

1. Open `zombie.py` in VS Code
2. Klik op ▶️ om te runnen
3. Speel het spel een paar keer

## LEES

Lees de code en beantwoord:
- Wat gebeurt er als je "rennen" typt?
- Wat doet `random.randint(1, 2)`?
- Wanneer ben je "dood"?

## PROBEER

Verander de tekst "Er komt een zombie op je af!" naar iets anders. Run het spel om je verandering te zien.
```

- [ ] **Step 2: Create uitdagingen.md**

Create `levels/level-1/uitdagingen.md`:

```markdown
# Level 1 Uitdagingen

## Opwarmer

### Verstoppen

Voeg een derde optie toe: "verstoppen"

**Hint:** Gebruik `elif actie == "verstoppen":`

??? note "Spieken"
    ```python
    elif actie == "verstoppen":
        print("🙈 Je verstopt je achter een auto...")
        kans = random.randint(1, 3)
        if kans == 1:
            print("De zombie ziet je niet! Je bent veilig.")
        else:
            print("De zombie ruikt je...")
    ```

---

### Eigen Verhaal

Verander alle teksten naar je eigen zombie verhaal

**Hint:** Pas de strings aan in de `print()` statements

??? note "Spieken"
    Geen code nodig - verander gewoon de tekst tussen aanhalingstekens!
    Bijvoorbeeld: `print("👻 Een geest verschijnt...")`

---

## Pittig

### Zombie Naam

De zombie heeft een naam (kies random uit een lijst)

**Hint:** Maak een lijst: `namen = ["Zombert", "Kreunald", "Stumpertje"]` en gebruik `random.choice()`

??? note "Spieken"
    ```python
    import random

    namen = ["Zombert", "Kreunald", "Stumpertje"]
    zombie_naam = random.choice(namen)

    print(f"🧟 {zombie_naam} de zombie komt op je af!")
    ```

---

## Moeilijk

### Praten

Voeg een "praten" optie toe met je eigen logica

**Hint:** Maak een `elif actie == "praten":` en bedenk zelf wat er gebeurt. Misschien kan je de zombie overtuigen?

??? note "Spieken"
    ```python
    elif actie == "praten":
        print("🗣️ Je probeert met de zombie te praten...")
        wat_zeg_je = input("Wat zeg je? (hallo / ga weg / ik ben ook een zombie) ➜ ")

        if wat_zeg_je == "hallo":
            print("De zombie gromt en valt aan!")
        elif wat_zeg_je == "ga weg":
            print("De zombie snapt je niet...")
        elif wat_zeg_je == "ik ben ook een zombie":
            print("🧟 De zombie gelooft je! Hij loopt door.")
        else:
            print("De zombie kijkt je raar aan...")
    ```
```

- [ ] **Step 3: Commit**

```bash
git add levels/level-1/uitleg.md levels/level-1/uitdagingen.md
git commit -m "Add Level 1 documentation and challenges"
```

---

### Task 5: Create Level 2 documentation

**Files:**
- Create: `levels/level-2/uitleg.md`
- Create: `levels/level-2/uitdagingen.md`

- [ ] **Step 1: Create uitleg.md**

Create `levels/level-2/uitleg.md`:

```markdown
# Level 2: Levens en Loops

## Wat leer je?

In dit level leer je hoe je code herhaalt met `while` loops. Je leert ook hoe je variabelen gebruikt om de staat van het spel bij te houden (zoals hoeveel levens je hebt).

## De code

### Variabelen voor staat

```python
levens = 3
```

Dit is een variabele die bijhoudt hoeveel levens je hebt. We kunnen dit getal veranderen tijdens het spel.

### While loop

```python
while levens > 0:
    # deze code herhaalt zolang levens groter is dan 0
```

De code binnen de `while` blijft herhalen totdat de voorwaarde (`levens > 0`) niet meer waar is.

### Variabele aanpassen

```python
levens -= 1
```

Dit is hetzelfde als `levens = levens - 1`. Het haalt 1 af van levens.

## BEKIJK

1. Run `zombie.py`
2. Let op: het spel stopt niet na één beurt!
3. Probeer te winnen (alle zombies verslaan)

## LEES

Lees de code en beantwoord:
- Wanneer stopt de while loop?
- Wat gebeurt er met `levens` als je geraakt wordt?
- Waarom staat `levens = 0` bij de `else`?

## PROBEER

Verander `levens = 3` naar `levens = 5`. Run het spel - je hebt nu 5 levens!
```

- [ ] **Step 2: Create uitdagingen.md**

Create `levels/level-2/uitdagingen.md`:

```markdown
# Level 2 Uitdagingen

## Makkelijk

### Meer Levens

Verander het aantal levens naar 5

**Hint:** Zoek de regel `levens = 3` en pas het aan

??? note "Spieken"
    ```python
    levens = 5
    ```

---

### Game Over Bericht

Voeg een speciaal bericht toe als je dood gaat

**Hint:** Voeg code toe NA de while loop maar VOOR "THE END"

??? note "Spieken"
    ```python
    while levens > 0:
        # ... bestaande code ...

    if levens == 0:
        print("💀 GAME OVER 💀")
        print("De zombies hebben gewonnen...")

    print("🎬 THE END 🎬")
    ```

---

## Medium

### Wapen Zoeken

Voeg een "zoeken" actie toe om een wapen te vinden

**Hint:** Maak een variabele `heeft_wapen = False` aan het begin

??? note "Spieken"
    ```python
    heeft_wapen = False

    while levens > 0:
        # ... bestaande intro code ...

        actie = input("⚡ Wat doe je? (rennen / vechten / zoeken) ➜ ")

        if actie == "zoeken":
            if not heeft_wapen:
                print("🔍 Je zoekt rond...")
                print("⚔️ Je vindt een honkbalknuppel!")
                heeft_wapen = True
            else:
                print("Je hebt al een wapen!")

        elif actie == "rennen":
            # ... bestaande code ...
    ```

---

### Wapen Bonus

Het wapen verhoogt je winkans bij vechten

**Hint:** Check `if heeft_wapen:` en pas de `random.randint()` aan

??? note "Spieken"
    ```python
    elif actie == "vechten":
        print("⚔️ Je maakt je klaar om te vechten...")
        time.sleep(1)

        if heeft_wapen:
            print("Je zwaait met je honkbalknuppel!")
            kans = random.randint(1, 3)  # 2 van 3 kans om te winnen
        else:
            kans = random.randint(1, 2)  # 1 van 2 kans om te winnen

        if kans >= 2:
            print("💥 Je verslaat de zombie!")
        else:
            print("🧟 De zombie bijt je...")
            levens -= 1
    ```

---

## Moeilijk

### Score Systeem

Voeg een score toe die omhoog gaat per overwonnen zombie

**Hint:** Maak `score = 0` aan het begin, en `score += 10` als je wint

??? note "Spieken"
    ```python
    levens = 3
    score = 0

    while levens > 0:
        print(f"Levens: {levens} | Score: {score}")

        # ... bestaande code ...

        # Bij winnen:
        if kans >= 2:
            print("💥 Je verslaat de zombie!")
            score += 10

    print(f"🏆 Eindscore: {score}")
    ```
```

- [ ] **Step 3: Commit**

```bash
git add levels/level-2/uitleg.md levels/level-2/uitdagingen.md
git commit -m "Add Level 2 documentation and challenges"
```

---

## Chunk 2: Level 3 & 4 Code and Documentation

### Task 6: Create Level 3 code

**Files:**
- Create: `levels/level-3/zombie.py`

- [ ] **Step 1: Create zombie.py with inventory and zombie types**

Create `levels/level-3/zombie.py`:

```python
import friendly
friendly.install()

import random
import time

# === VARIABELEN ===
levens = 3
inventory = []
zombie_types = ["langzame zombie", "snelle zombie", "sterke zombie"]
zombie_geluiden = ["GRAAAAAH!", "BRAAAAINS!", "UGHHHH...", "GRRRR!"]

print("🧟‍♂️💀 WELKOM BIJ ZOMBIE APOCALYPSE 💀🧟‍♂️")
print("Je hebt drie levens")
print()

# === GAME LOOP ===
while levens > 0:
    # Toon status
    print(f"❤️ Levens: {levens}")
    if inventory:
        print(f"🎒 Inventory: {inventory}")
    print()

    # Random zombie verschijnt
    zombie = random.choice(zombie_types)
    geluid = random.choice(zombie_geluiden)

    print("🌫️ Het is donker... je hoort gegrom...")
    time.sleep(1)
    print(f"🧟‍♂️ Een {zombie} komt op je af!")
    print(f"   '{geluid}'")
    print()

    actie = input("⚡ Wat doe je? (rennen / vechten / zoeken) ➜ ")

    if actie == "rennen":
        print("🏃‍♂️ Je probeert weg te sprinten...")
        time.sleep(1)

        # Snelle zombie is moeilijker te ontsnappen
        if zombie == "snelle zombie":
            kans = random.randint(1, 3)  # 1 op 3 kans
        else:
            kans = random.randint(1, 2)  # 1 op 2 kans

        if kans == 1:
            print("💨 Je bent ontsnapt!")
        else:
            print("😱 De zombie was sneller!")
            levens -= 1

    elif actie == "vechten":
        print("⚔️ Je maakt je klaar om te vechten...")
        time.sleep(1)

        # Check voor wapen in inventory
        heeft_wapen = "honkbalknuppel" in inventory

        # Sterke zombie is moeilijker te verslaan
        if zombie == "sterke zombie":
            if heeft_wapen:
                kans = random.randint(1, 2)  # 1 op 2 met wapen
            else:
                kans = random.randint(1, 4)  # 1 op 4 zonder
        else:
            if heeft_wapen:
                kans = random.randint(1, 3)  # 2 op 3 met wapen
            else:
                kans = random.randint(1, 2)  # 1 op 2 zonder

        if kans >= 2 or (kans == 1 and heeft_wapen):
            print("💥 Je verslaat de zombie!")
            # Zombie laat soms iets vallen
            if random.randint(1, 3) == 1:
                item = random.choice(["medkit", "zaklamp", "energie bar"])
                print(f"   De zombie liet een {item} vallen!")
                inventory.append(item)
        else:
            print("🧟‍♂️ De zombie bijt je...")
            levens -= 1

    elif actie == "zoeken":
        print("🔍 Je zoekt rond...")
        time.sleep(1)

        if "honkbalknuppel" not in inventory:
            if random.randint(1, 2) == 1:
                print("⚔️ Je vindt een honkbalknuppel!")
                inventory.append("honkbalknuppel")
            else:
                print("Je vindt niks bruikbaars...")
        else:
            # Zoek naar andere items
            if random.randint(1, 2) == 1:
                item = random.choice(["medkit", "zaklamp", "energie bar"])
                print(f"Je vindt een {item}!")
                inventory.append(item)
            else:
                print("Je vindt niks bruikbaars...")

    else:
        print("🤦 Zombies twijfelen niet...")
        levens = 0

    # Check voor medkit gebruik
    if levens < 3 and "medkit" in inventory:
        gebruik = input("💊 Je hebt een medkit. Gebruiken? (ja/nee) ➜ ")
        if gebruik == "ja":
            inventory.remove("medkit")
            levens += 1
            print("❤️ +1 leven!")

    print()

print("🎬 THE END 🎬")
if levens > 0:
    print("🏆 Je hebt overleefd!")
else:
    print("💀 Game over...")
```

- [ ] **Step 2: Verify file runs**

```bash
cd levels/level-3 && python zombie.py
```

Expected: Game runs with inventory system and zombie types

- [ ] **Step 3: Commit**

```bash
git add levels/level-3/zombie.py
git commit -m "Add Level 3: lists and inventory system"
```

---

### Task 7: Create Level 3 documentation

**Files:**
- Create: `levels/level-3/uitleg.md`
- Create: `levels/level-3/uitdagingen.md`

- [ ] **Step 1: Create uitleg.md**

Create `levels/level-3/uitleg.md`:

```markdown
# Level 3: Lijsten en Inventory

## Wat leer je?

In dit level leer je over **lijsten** - een manier om meerdere dingen te bewaren in één variabele. Je leert ook `random.choice()` om iets willekeurigs uit een lijst te kiezen.

## De code

### Een lijst maken

```python
inventory = []  # lege lijst
zombie_types = ["langzame zombie", "snelle zombie", "sterke zombie"]
```

Lijsten gebruiken vierkante haken `[]`. Items worden gescheiden door komma's.

### Iets uit een lijst kiezen

```python
zombie = random.choice(zombie_types)
```

`random.choice()` pakt een willekeurig item uit de lijst.

### Iets toevoegen aan een lijst

```python
inventory.append("honkbalknuppel")
```

`.append()` voegt iets toe aan het einde van de lijst.

### Checken of iets in een lijst zit

```python
if "honkbalknuppel" in inventory:
    print("Je hebt een wapen!")
```

`in` checkt of iets in de lijst zit.

### Iets verwijderen uit een lijst

```python
inventory.remove("medkit")
```

`.remove()` haalt het eerste gevonden item weg.

## BEKIJK

1. Run `zombie.py`
2. Probeer te zoeken naar items
3. Let op hoe je inventory groeit

## LEES

- Welke lijsten zijn er in de code?
- Wat gebeurt er als je een zombie verslaat?
- Hoe werkt de medkit?

## PROBEER

Voeg een nieuw zombie type toe aan de `zombie_types` lijst. Misschien een "baby zombie" die makkelijk te verslaan is?
```

- [ ] **Step 2: Create uitdagingen.md**

Create `levels/level-3/uitdagingen.md`:

```markdown
# Level 3 Uitdagingen

## Makkelijk

### Meer Geluiden

Voeg meer zombie geluiden toe aan de lijst

**Hint:** Pas de `zombie_geluiden` lijst aan

??? note "Spieken"
    ```python
    zombie_geluiden = [
        "GRAAAAAH!",
        "BRAAAAINS!",
        "UGHHHH...",
        "GRRRR!",
        "MMMMMM...",
        "HUNGRYYYY!",
        "*kwijlt*"
    ]
    ```

---

### Zombie Drops

Laat de zombie altijd iets vallen als je wint

**Hint:** Verwijder de `if random.randint(1, 3) == 1:` check

??? note "Spieken"
    ```python
    if kans >= 2 or (kans == 1 and heeft_wapen):
        print("💥 Je verslaat de zombie!")
        # Altijd een drop:
        item = random.choice(["medkit", "zaklamp", "energie bar"])
        print(f"   De zombie liet een {item} vallen!")
        inventory.append(item)
    ```

---

## Medium

### Locaties

Voeg locaties toe: straat → ziekenhuis → supermarkt

**Hint:** Maak een `locaties` lijst en een `huidige_locatie` variabele

??? note "Spieken"
    ```python
    locaties = ["straat", "ziekenhuis", "supermarkt", "politiebureau"]
    locatie_index = 0

    while levens > 0 and locatie_index < len(locaties):
        huidige_locatie = locaties[locatie_index]
        print(f"📍 Je bent bij: {huidige_locatie}")

        # ... zombie encounter ...

        # Na overleven, ga naar volgende locatie
        if levens > 0:
            locatie_index += 1
            if locatie_index < len(locaties):
                print(f"Je gaat verder naar {locaties[locatie_index]}...")

    if locatie_index >= len(locaties):
        print("🏆 Je hebt alle locaties overleefd!")
    ```

---

### Zombie Winkans

Elk zombie type heeft een andere winkans

**Hint:** Maak een dictionary met kansen per type

??? note "Spieken"
    ```python
    # Kans om te winnen per zombie type (hoe hoger, hoe makkelijker)
    zombie_moeilijkheid = {
        "langzame zombie": 2,    # 2 op 3 kans
        "snelle zombie": 2,      # 2 op 3 kans
        "sterke zombie": 3,      # 1 op 3 kans
        "baby zombie": 1         # 1 op 2 kans (makkelijk)
    }

    moeilijkheid = zombie_moeilijkheid[zombie]
    kans = random.randint(1, moeilijkheid)
    ```

---

### Random Events

Voeg willekeurige events toe tussen rondes

**Hint:** Maak een `events` lijst en kies er random een

??? note "Spieken"
    ```python
    events = [
        ("Je struikelt over een steen!", -1, None),       # verlies leven
        ("Je vindt een verborgen kist!", 0, "medkit"),    # vind item
        ("Een kat schrikt je!", 0, None),                  # niks
        ("Je hoort andere overlevenden!", 0, None),       # niks
    ]

    # Aan het begin van elke ronde:
    if random.randint(1, 4) == 1:  # 25% kans op event
        event = random.choice(events)
        print(f"❗ {event[0]}")
        if event[1] != 0:
            levens += event[1]
        if event[2]:
            inventory.append(event[2])
    ```

---

## Moeilijk

### Crafting

Combineer 2 items tot iets beters

**Hint:** Check of beide items in inventory zitten, verwijder ze, voeg het nieuwe item toe

??? note "Spieken"
    ```python
    elif actie == "craft":
        if "zaklamp" in inventory and "honkbalknuppel" in inventory:
            print("🔧 Je combineert de zaklamp en knuppel...")
            inventory.remove("zaklamp")
            inventory.remove("honkbalknuppel")
            inventory.append("lichtgevende knuppel")
            print("⚡ Je hebt nu een LICHTGEVENDE KNUPPEL!")
        else:
            print("Je hebt niet de juiste items om te craften.")
            print("(Nodig: zaklamp + honkbalknuppel)")
    ```

---

### Shop

Ruil items met een NPC handelaar

**Hint:** Toon wat de handelaar heeft, vraag wat de speler wil ruilen

??? note "Spieken"
    ```python
    # Random kans op handelaar
    if random.randint(1, 5) == 1:
        print("👤 Je ontmoet een handelaar!")
        print("   Hij biedt aan: medkit")
        print("   Hij wil: 2 energie bars")

        if inventory.count("energie bar") >= 2:
            ruil = input("Wil je ruilen? (ja/nee) ➜ ")
            if ruil == "ja":
                inventory.remove("energie bar")
                inventory.remove("energie bar")
                inventory.append("medkit")
                print("✅ Geruild!")
        else:
            print("Je hebt niet genoeg energie bars...")
    ```
```

- [ ] **Step 3: Commit**

```bash
git add levels/level-3/uitleg.md levels/level-3/challenges.md
git commit -m "Add Level 3 documentation and challenges"
```

---

### Task 8: Create Level 4 code

**Files:**
- Create: `levels/level-4/zombie.py`

- [ ] **Step 1: Create zombie.py with functions**

Create `levels/level-4/zombie.py`:

```python
import friendly
friendly.install()

import random
import time


# === FUNCTIES ===

def toon_status(levens, score, inventory):
    """Toon de huidige status van de speler."""
    print()
    print(f"❤️ Levens: {levens} | 🏆 Score: {score}")
    if inventory:
        print(f"🎒 Inventory: {inventory}")
    print()


def maak_zombie():
    """Maak een nieuwe zombie met random eigenschappen."""
    types = ["langzame zombie", "snelle zombie", "sterke zombie"]
    namen = ["Zombert", "Kreunald", "Rottie", "Stumpertje"]
    geluiden = ["GRAAAAAH!", "BRAAAAINS!", "UGHHHH..."]

    return {
        "type": random.choice(types),
        "naam": random.choice(namen),
        "geluid": random.choice(geluiden)
    }


def toon_zombie(zombie):
    """Toon de zombie met spanning."""
    print("🌫️ Het is donker... je hoort gegrom...")
    time.sleep(1)
    print(f"🧟‍♂️ {zombie['naam']} de {zombie['type']} komt op je af!")
    print(f"   '{zombie['geluid']}'")


def bereken_winkans(zombie, heeft_wapen):
    """Bereken de kans om te winnen tegen deze zombie."""
    basis_kans = 2  # 1 op 2

    if zombie["type"] == "sterke zombie":
        basis_kans = 3  # moeilijker
    elif zombie["type"] == "langzame zombie":
        basis_kans = 2  # normaal

    if heeft_wapen:
        basis_kans = max(1, basis_kans - 1)  # makkelijker met wapen

    return basis_kans


def vecht(zombie, heeft_wapen):
    """
    Vecht tegen een zombie.
    Returns: True als je wint, False als je verliest.
    """
    print("⚔️ Je maakt je klaar om te vechten...")
    if heeft_wapen:
        print("   Je zwaait met je wapen!")
    time.sleep(1)

    moeilijkheid = bereken_winkans(zombie, heeft_wapen)
    kans = random.randint(1, moeilijkheid)

    if kans == 1:
        print(f"💥 Je verslaat {zombie['naam']}!")
        return True
    else:
        print(f"🧟‍♂️ {zombie['naam']} bijt je...")
        return False


def ren_weg(zombie):
    """
    Probeer weg te rennen.
    Returns: True als je ontsnapt, False als je gepakt wordt.
    """
    print("🏃‍♂️ Je probeert weg te sprinten...")
    time.sleep(1)

    if zombie["type"] == "snelle zombie":
        kans = random.randint(1, 3)  # moeilijker
    else:
        kans = random.randint(1, 2)

    if kans == 1:
        print("💨 Je bent ontsnapt!")
        return True
    else:
        print("😱 De zombie was sneller!")
        return False


def zoek_item(inventory):
    """
    Zoek naar items.
    Returns: het gevonden item of None.
    """
    print("🔍 Je zoekt rond...")
    time.sleep(1)

    mogelijke_items = ["honkbalknuppel", "medkit", "zaklamp", "energie bar"]

    if random.randint(1, 2) == 1:
        item = random.choice(mogelijke_items)
        print(f"✨ Je vindt een {item}!")
        return item
    else:
        print("Je vindt niks bruikbaars...")
        return None


def toon_help():
    """Toon alle beschikbare acties."""
    print()
    print("=== HELP ===")
    print("rennen  - Probeer te ontsnappen (makkelijker bij langzame zombies)")
    print("vechten - Vecht tegen de zombie (beter met wapen)")
    print("zoeken  - Zoek naar items")
    print("help    - Toon dit menu")
    print("=============")
    print()


# === MAIN GAME ===

def main():
    levens = 3
    score = 0
    inventory = []

    print("🧟‍♂️💀 WELKOM BIJ ZOMBIE APOCALYPSE 💀🧟‍♂️")
    print("Type 'help' voor alle opties")

    while levens > 0:
        toon_status(levens, score, inventory)

        zombie = maak_zombie()
        toon_zombie(zombie)
        print()

        actie = input("⚡ Wat doe je? ➜ ").lower().strip()

        if actie == "help":
            toon_help()
            continue  # Sla de rest over, begin opnieuw

        elif actie == "rennen":
            if not ren_weg(zombie):
                levens -= 1

        elif actie == "vechten":
            heeft_wapen = "honkbalknuppel" in inventory
            if vecht(zombie, heeft_wapen):
                score += 10
                # Kans op drop
                if random.randint(1, 3) == 1:
                    item = random.choice(["medkit", "energie bar"])
                    print(f"   {zombie['naam']} liet een {item} vallen!")
                    inventory.append(item)
            else:
                levens -= 1

        elif actie == "zoeken":
            item = zoek_item(inventory)
            if item:
                inventory.append(item)

        else:
            print("🤷 Dat snap ik niet. Type 'help' voor opties.")

        # Medkit gebruiken?
        if levens < 3 and "medkit" in inventory:
            gebruik = input("💊 Medkit gebruiken? (ja/nee) ➜ ").lower()
            if gebruik == "ja":
                inventory.remove("medkit")
                levens += 1
                print("❤️ +1 leven!")

    # Game over
    print()
    print("🎬 THE END 🎬")
    print(f"🏆 Eindscore: {score}")
    if score >= 50:
        print("🌟 GEWELDIG! Je bent een echte zombie-jager!")
    elif score >= 20:
        print("👍 Goed gedaan!")
    else:
        print("💀 Probeer het nog eens...")


# Start het spel
if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Verify file runs**

```bash
cd levels/level-4 && python zombie.py
```

Expected: Game runs with function-based structure

- [ ] **Step 3: Commit**

```bash
git add levels/level-4/zombie.py
git commit -m "Add Level 4: functions and code organization"
```

---

### Task 9: Create Level 4 documentation

**Files:**
- Create: `levels/level-4/uitleg.md`
- Create: `levels/level-4/challenges.md`

- [ ] **Step 1: Create uitleg.md**

Create `levels/level-4/uitleg.md`:

```markdown
# Level 4: Functies

## Wat leer je?

In dit level leer je over **functies** - een manier om code te organiseren in herbruikbare blokken. Functies maken je code overzichtelijker en makkelijker aan te passen.

## De code

### Een functie maken

```python
def toon_status(levens, score, inventory):
    """Toon de huidige status van de speler."""
    print(f"❤️ Levens: {levens} | 🏆 Score: {score}")
```

- `def` betekent "define" - je definieert een functie
- `toon_status` is de naam van de functie
- `(levens, score, inventory)` zijn **parameters** - informatie die de functie nodig heeft
- De tekst tussen `"""` is een **docstring** - uitleg wat de functie doet

### Een functie aanroepen

```python
toon_status(3, 50, ["honkbalknuppel"])
```

Je roept de functie aan met waarden voor elke parameter.

### Een waarde teruggeven

```python
def bereken_winkans(zombie, heeft_wapen):
    basis_kans = 2
    if heeft_wapen:
        basis_kans = 1
    return basis_kans  # Geef het resultaat terug
```

`return` geeft een waarde terug die je kan gebruiken:

```python
kans = bereken_winkans(zombie, True)
print(kans)  # print 1
```

### De main() functie

```python
def main():
    # Hier begint het spel
    levens = 3
    # ...

if __name__ == "__main__":
    main()
```

Dit is een patroon dat je vaak ziet. `main()` is waar je programma start.

## BEKIJK

1. Run `zombie.py`
2. Type `help` om de help functie te zien
3. Let op hoe het spel hetzelfde werkt, maar de code is anders georganiseerd

## LEES

- Hoeveel functies zijn er?
- Welke functie maakt een nieuwe zombie?
- Welke functie geeft True of False terug?

## PROBEER

Voeg een extra print statement toe in de `toon_help()` functie met een nieuwe tip.
```

- [ ] **Step 2: Create challenges.md**

Create `levels/level-4/challenges.md`:

```markdown
# Level 4 Challenges

## Makkelijk

### Status Verbeteren

Pas `toon_status()` aan om ook het aantal items te tonen

**Hint:** Gebruik `len(inventory)` om het aantal items te tellen

??? note "Spieken"
    ```python
    def toon_status(levens, score, inventory):
        print()
        print(f"❤️ Levens: {levens} | 🏆 Score: {score} | 🎒 Items: {len(inventory)}")
        if inventory:
            print(f"   Inventory: {inventory}")
        print()
    ```

---

### Eigen Functie

Verplaats de medkit-logica naar een eigen functie

**Hint:** Maak `def gebruik_medkit(levens, inventory):` die het nieuwe aantal levens teruggeeft

??? note "Spieken"
    ```python
    def gebruik_medkit(levens, inventory):
        """Vraag of speler medkit wil gebruiken. Return nieuw aantal levens."""
        if levens < 3 and "medkit" in inventory:
            gebruik = input("💊 Medkit gebruiken? (ja/nee) ➜ ").lower()
            if gebruik == "ja":
                inventory.remove("medkit")
                print("❤️ +1 leven!")
                return levens + 1
        return levens

    # In main():
    levens = gebruik_medkit(levens, inventory)
    ```

---

## Medium

### Functie met Parameter

Pas `vecht()` aan zodat je kan kiezen welk wapen je gebruikt

**Hint:** Verander `heeft_wapen` naar `wapen_type` (None, "honkbalknuppel", "zwaard", etc.)

??? note "Spieken"
    ```python
    def vecht(zombie, wapen_type):
        print("⚔️ Je maakt je klaar om te vechten...")

        if wapen_type == "zwaard":
            print("   Je zwaait met je zwaard!")
            bonus = 2
        elif wapen_type == "honkbalknuppel":
            print("   Je zwaait met je knuppel!")
            bonus = 1
        else:
            print("   Je balt je vuisten...")
            bonus = 0

        moeilijkheid = bereken_winkans(zombie, wapen_type is not None)
        kans = random.randint(1, max(1, moeilijkheid - bonus))

        return kans == 1
    ```

---

### Waarde Teruggeven

Maak een `bereken_score()` functie die bonuspunten geeft voor moeilijke zombies

**Hint:** Return 10 voor normale zombies, 20 voor sterke zombies

??? note "Spieken"
    ```python
    def bereken_score(zombie):
        """Bereken hoeveel punten een zombie waard is."""
        if zombie["type"] == "sterke zombie":
            return 20
        elif zombie["type"] == "snelle zombie":
            return 15
        else:
            return 10

    # In main(), bij winst:
    punten = bereken_score(zombie)
    score += punten
    print(f"   +{punten} punten!")
    ```

---

## Moeilijk

### Help Functie

Maak een interactieve help die uitlegt hoe elk zombie type werkt

**Hint:** Vraag eerst "Waarover wil je meer weten?"

??? note "Spieken"
    ```python
    def toon_help():
        print()
        print("=== HELP ===")
        print("1. Acties")
        print("2. Zombie types")
        print("3. Items")
        print()
        keuze = input("Kies een nummer (of Enter om terug te gaan): ")

        if keuze == "1":
            print("rennen  - Ontsnappen (makkelijker bij langzame zombies)")
            print("vechten - Vechten (beter met wapen)")
            print("zoeken  - Zoek items")
        elif keuze == "2":
            print("langzame zombie - Normaal, makkelijk te ontsnappen")
            print("snelle zombie   - Moeilijk te ontsnappen!")
            print("sterke zombie   - Moeilijk te verslaan!")
        elif keuze == "3":
            print("honkbalknuppel - Verhoogt je winkans bij vechten")
            print("medkit         - Herstelt 1 leven")
            print("energie bar    - Voor later...")
        print()
    ```

---

### Zombie Generator

Maak een `nieuwe_zombie()` functie die steeds moeilijkere zombies maakt

**Hint:** Geef een `ronde` parameter mee, en maak sterkere zombies in latere rondes

??? note "Spieken"
    ```python
    def maak_zombie(ronde):
        """Maak een zombie. Hogere rondes = moeilijkere zombies."""

        if ronde <= 2:
            types = ["langzame zombie"]
        elif ronde <= 5:
            types = ["langzame zombie", "snelle zombie"]
        else:
            types = ["langzame zombie", "snelle zombie", "sterke zombie"]

        namen = ["Zombert", "Kreunald", "Rottie", "Stumpertje"]

        return {
            "type": random.choice(types),
            "naam": f"{random.choice(namen)} #{ronde}",
            "geluid": "GRAAAH!"
        }

    # In main():
    ronde = 0
    while levens > 0:
        ronde += 1
        zombie = maak_zombie(ronde)
    ```
```

- [ ] **Step 3: Commit**

```bash
git add levels/level-4/uitleg.md levels/level-4/challenges.md
git commit -m "Add Level 4 documentation and challenges"
```

---

## Chunk 3: MkDocs Website Setup

### Task 10: Create MkDocs configuration

**Files:**
- Create: `mkdocs.yml`

- [ ] **Step 1: Create mkdocs.yml**

Create `mkdocs.yml`:

```yaml
site_name: Zombie Apocalypse
site_description: Leer Python programmeren met een zombie spel!
site_url: https://yourusername.github.io/CoderDojo-Zombies/

theme:
  name: material
  language: nl
  palette:
    scheme: slate
    primary: red
    accent: orange
  features:
    - content.code.copy
    - content.code.annotate
    - navigation.sections
    - navigation.expand

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - attr_list
  - md_in_html

nav:
  - Home: index.md
  - Aan de Slag: aan-de-slag.md
  - Levels:
    - Level 1 - Keuzes: levels/level-1/uitleg.md
    - Level 2 - Loops: levels/level-2/uitleg.md
    - Level 3 - Lijsten: levels/level-3/uitleg.md
    - Level 4 - Functies: levels/level-4/uitleg.md
  - Challenges:
    - Level 1: levels/level-1/challenges.md
    - Level 2: levels/level-2/challenges.md
    - Level 3: levels/level-3/challenges.md
    - Level 4: levels/level-4/challenges.md
  - Cheatsheet: cheatsheet.md

extra_css:
  - stylesheets/print-cards.css
```

- [ ] **Step 2: Commit**

```bash
git add mkdocs.yml
git commit -m "Add MkDocs configuration"
```

---

### Task 11: Create landing page

**Files:**
- Create: `docs/index.md`

- [ ] **Step 1: Create index.md**

Create `docs/index.md`:

```markdown
# Zombie Apocalypse

**Leer Python programmeren door een zombie spel te bouwen!**

Dit project is gemaakt voor CoderDojo. Je leert stap voor stap programmeren, van simpele keuzes tot complete functies.

## Voor wie is dit?

- Kinderen van 8-16 jaar
- Je hebt Scratch gedaan en wilt "echte" code leren
- Je houdt van games en zombies 🧟

## Wat ga je leren?

| Level | Concept | Wat je bouwt |
|-------|---------|--------------|
| 1 | `if`/`else` | Keuzes maken: rennen of vechten |
| 2 | `while` loops | Levens systeem, game loop |
| 3 | Lijsten | Inventory, zombie types |
| 4 | Functies | Georganiseerde code |

## Hoe werkt het?

1. **BEKIJK** - Run de code, speel het spel
2. **LEES** - Begrijp wat de code doet
3. **PROBEER** - Maak een kleine aanpassing
4. **UITDAGING** - Kies een challenge kaart

## Begin hier

👉 [Aan de Slag](aan-de-slag.md) - Installeer Python en VS Code

👉 [Level 1](levels/level-1/uitleg.md) - Start met programmeren!
```

- [ ] **Step 2: Commit**

```bash
git add docs/index.md
git commit -m "Add landing page"
```

---

### Task 12: Create getting started guide

**Files:**
- Create: `docs/aan-de-slag.md`

- [ ] **Step 1: Create aan-de-slag.md**

Create `docs/aan-de-slag.md`:

```markdown
# Aan de Slag

Volg deze stappen om te beginnen met programmeren.

## 1. Installeer Python

1. Ga naar [python.org](https://www.python.org/downloads/)
2. Download Python (kies de nieuwste versie)
3. **Belangrijk:** Vink aan "Add Python to PATH" tijdens installatie!
4. Klik op "Install Now"

## 2. Installeer VS Code

1. Ga naar [code.visualstudio.com](https://code.visualstudio.com/)
2. Download en installeer VS Code
3. Open VS Code

## 3. Installeer Extensions

In VS Code:

1. Klik op het blokjes-icoon links (Extensions)
2. Zoek "Python" en installeer de extension van Microsoft
3. Zoek "Pylance" en installeer deze ook

## 4. Installeer Extra Packages

Open een terminal (in VS Code: Terminal → New Terminal) en typ:

```bash
pip install friendly-traceback pgzero
```

## 5. Download de Code

1. Download dit project als ZIP, of clone met git
2. Open de folder in VS Code: File → Open Folder

## 6. Run je eerste programma

1. Open `levels/level-1/zombie.py`
2. Klik op de ▶️ knop rechtsboven
3. Het spel start in de terminal!

## Problemen?

### "python" wordt niet herkend

Python staat niet in je PATH. Installeer Python opnieuw en vink "Add to PATH" aan.

### Foutmelding in rood

Lees de foutmelding! `friendly-traceback` legt uit wat er mis is in begrijpelijke taal.

### Het spel start niet

Controleer of je in de juiste folder bent. Je moet `zombie.py` zien in de file explorer links.

## Klaar?

👉 Ga naar [Level 1](levels/level-1/uitleg.md) om te beginnen!
```

- [ ] **Step 2: Commit**

```bash
git add docs/aan-de-slag.md
git commit -m "Add getting started guide"
```

---

### Task 13: Create cheatsheet

**Files:**
- Create: `docs/cheatsheet.md`

- [ ] **Step 1: Create cheatsheet.md**

Create `docs/cheatsheet.md`:

```markdown
# Python Cheatsheet

Python gebruikt Engelse woorden. Hier is een vertaling:

## Keywords

| Nederlands | Python | Voorbeeld |
|------------|--------|-----------|
| als | `if` | `if actie == "rennen":` |
| anders als | `elif` | `elif actie == "vechten":` |
| anders | `else` | `else:` |
| zolang | `while` | `while levens > 0:` |
| voor | `for` | `for item in lijst:` |
| in | `in` | `if "mes" in inventory:` |
| en | `and` | `if levens > 0 and heeft_wapen:` |
| of | `or` | `if actie == "ja" or actie == "j":` |
| niet | `not` | `if not heeft_wapen:` |
| waar | `True` | `gevonden = True` |
| onwaar | `False` | `heeft_wapen = False` |
| functie | `def` | `def vecht():` |
| teruggeven | `return` | `return True` |
| importeren | `import` | `import random` |

## Symbolen

| Wat | Symbool | Voorbeeld |
|-----|---------|-----------|
| is gelijk aan | `==` | `if actie == "rennen":` |
| toewijzen | `=` | `levens = 3` |
| niet gelijk aan | `!=` | `if naam != "":` |
| groter dan | `>` | `if levens > 0:` |
| kleiner dan | `<` | `if kans < 3:` |
| groter of gelijk | `>=` | `if score >= 100:` |
| kleiner of gelijk | `<=` | `if levens <= 0:` |
| plus | `+` | `score = score + 10` |
| min | `-` | `levens = levens - 1` |
| plus-is | `+=` | `score += 10` |
| min-is | `-=` | `levens -= 1` |

## Veelgebruikte functies

| Functie | Wat het doet | Voorbeeld |
|---------|--------------|-----------|
| `print()` | Tekst tonen | `print("Hallo!")` |
| `input()` | Vraag om input | `naam = input("Naam? ")` |
| `len()` | Tel items | `len(inventory)` |
| `random.choice()` | Kies willekeurig | `random.choice(["a", "b"])` |
| `random.randint()` | Random getal | `random.randint(1, 6)` |
| `.append()` | Toevoegen aan lijst | `inventory.append("mes")` |
| `.remove()` | Verwijderen uit lijst | `inventory.remove("mes")` |
| `time.sleep()` | Pauzeren | `time.sleep(1)` |

## Print tips

```python
# Normaal
print("Hallo wereld!")

# Met variabele (f-string)
naam = "Zombie-Jan"
print(f"Daar is {naam}!")

# Meerdere regels
print("Regel 1")
print("Regel 2")
```
```

- [ ] **Step 2: Commit**

```bash
git add docs/cheatsheet.md
git commit -m "Add Python cheatsheet"
```

---

### Task 14: Create print stylesheet for cards

**Files:**
- Create: `docs/stylesheets/print-cards.css`

- [ ] **Step 1: Create print-cards.css**

Create `docs/stylesheets/print-cards.css`:

```css
/* Print stylesheet for challenge cards */

@media print {
  /* Hide navigation and other UI elements */
  .md-header,
  .md-sidebar,
  .md-footer,
  .md-source,
  nav,
  .md-nav {
    display: none !important;
  }

  /* Card styling */
  article h3 {
    page-break-before: auto;
    border: 2px solid #333;
    border-radius: 8px;
    padding: 1rem;
    margin: 0.5rem;
    background: #fff;
    box-shadow: none;
  }

  /* Difficulty badges */
  article h2:has(+ * + h3) {
    font-size: 0.8rem;
    color: #666;
  }

  h2:contains("Makkelijk"),
  h2:contains("Easy") {
    color: #28a745;
  }

  h2:contains("Medium") {
    color: #fd7e14;
  }

  h2:contains("Moeilijk"),
  h2:contains("Hard") {
    color: #dc3545;
  }

  /* Hide code solutions when printing cards */
  details.note {
    display: none !important;
  }

  /* Card layout - 4 per page */
  article {
    column-count: 2;
    column-gap: 1rem;
  }

  article h3 {
    break-inside: avoid;
    display: inline-block;
    width: 100%;
    min-height: 200px;
  }

  /* QR code placeholder */
  article h3::after {
    content: "📱 Scan voor oplossing";
    display: block;
    font-size: 0.7rem;
    color: #999;
    margin-top: 1rem;
    text-align: right;
  }
}

/* Screen styling for card preview */
@media screen {
  .challenges-page h3 {
    border: 2px solid #444;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    background: #2d2d2d;
  }

  .challenges-page h2 {
    margin-top: 2rem;
    padding: 0.5rem 1rem;
    border-radius: 4px;
  }

  /* Difficulty colors on screen */
  .challenges-page h2:first-of-type,
  .challenges-page h2:contains("Makkelijk") {
    background: rgba(40, 167, 69, 0.2);
    border-left: 4px solid #28a745;
  }
}
```

- [ ] **Step 2: Commit**

```bash
git add docs/stylesheets/print-cards.css
git commit -m "Add print stylesheet for challenge cards"
```

---

### Task 15: Test MkDocs locally

- [ ] **Step 1: Install MkDocs and theme**

```bash
pip install mkdocs mkdocs-material
```

- [ ] **Step 2: Serve locally**

```bash
mkdocs serve
```

Expected: Site runs at http://127.0.0.1:8000

- [ ] **Step 3: Verify navigation works**

Open browser, check:
- Home page loads
- All levels accessible
- Challenges show with collapsible "Spieken" sections
- Cheatsheet displays correctly

- [ ] **Step 4: Stop server and commit any fixes**

Press Ctrl+C to stop. If any fixes were needed, commit them.

---

## Chunk 4: Final Setup

### Task 16: Update README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Create/update README.md**

Create `README.md`:

```markdown
# CoderDojo Zombie Apocalypse

Leer Python programmeren met een zombie spel!

## Voor Coaches

Dit is een curriculum voor CoderDojo om kinderen (8-16 jaar) Python te leren. Het project bevat:

- **4 text-based levels** met oplopende moeilijkheid
- **Challenge cards** voor extra oefeningen
- **MkDocs website** met alle instructies
- **Printbare kaarten** voor in de sessie

## Structuur

```
levels/           # Python code per level
├── level-1/      # if/elif/else
├── level-2/      # while loops
├── level-3/      # lijsten
└── level-4/      # functies

docs/             # Website content
```

## Setup

```bash
# Installeer dependencies
pip install friendly-traceback pgzero mkdocs mkdocs-material

# Start de website lokaal
mkdocs serve

# Deploy naar GitHub Pages
mkdocs gh-deploy
```

## Levels

| Level | Concept | Files |
|-------|---------|-------|
| 1 | if/elif/else | `levels/level-1/` |
| 2 | while, variabelen | `levels/level-2/` |
| 3 | lijsten, random | `levels/level-3/` |
| 4 | functies | `levels/level-4/` |

## Licentie

MIT - Vrij te gebruiken voor CoderDojo's en andere educatieve doeleinden.
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "Add project README"
```

---

### Task 17: Clean up old files

**Files:**
- Remove: `Zombie1.py` (moved to levels/level-1/)
- Remove: `Zombie2.py` (moved to levels/level-2/)

- [ ] **Step 1: Remove old files**

```bash
git rm Zombie1.py Zombie2.py
```

- [ ] **Step 2: Commit**

```bash
git commit -m "Remove old files (moved to levels/)"
```

---

### Task 18: Deploy to GitHub Pages

- [ ] **Step 1: Ensure MkDocs builds without errors**

```bash
mkdocs build
```

Expected: No errors, `site/` folder created

- [ ] **Step 2: Deploy**

```bash
mkdocs gh-deploy
```

Expected: Site deployed to GitHub Pages

- [ ] **Step 3: Verify live site**

Open the GitHub Pages URL and verify everything works.

---

## Summary

**STATUS: COMPLETED** (March 2026)

All text-based levels implemented:

- ✅ 4 text-based Python levels with code
- ✅ Documentation for each level (uitleg.md)
- ✅ Challenge cards for each level (challenges.md)
- ✅ MkDocs website with Material theme
- ✅ Print stylesheet for cards
- ✅ Python cheatsheet (NL→EN)
- ✅ Getting started guide
- ✅ Deployed to GitHub Pages

**Out of scope for this plan (future work):**
- Pygame Zero levels (5+)
- QR code generation for cards
- Midjourney image assets

---

## Implementation Notes (Post-Completion)

The following changes were made during implementation that differ from the original plan:

### Challenge Tier Naming
Changed from "Makkelijk / Medium / Moeilijk" to **"Opwarmer / Pittig / Boss"**:
- Opwarmer (green) = Easy warmup challenges
- Pittig (orange) = Medium difficulty
- Boss (red) = Hard challenges

### Level 4: Added File I/O
Level 4 now includes a section on reading and writing files:
- `open()` with "r", "w", "a" modes
- `with` statement for file handling
- `try/except` for error handling
- Practical example: saving highscores

### Challenge Structure Simplified
Original plan had full "Spieken" (peek) code solutions in collapsible sections. Implementation uses simpler format:
- Challenge title
- Brief hint
- No full solution code (encourages kids to try first)

### Additional Challenges Brainstormed
See `OtherChallenges.md` for ideas not yet integrated into base levels:
- Zombie winkans (difficulty-based win rates)
- Random events system
- Location progression
- Crafting system
- NPC trading/shop
