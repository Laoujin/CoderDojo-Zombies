# CoderDojo Zombie Game Curriculum — Design Document

## 1. Project Overview

**Project naam:** CoderDojo Zombie Game Curriculum

**Doel:** Leer kinderen (8-16 jaar) programmeren in Python via een zombie-thema spel. Start met tekst-gebaseerd, eindig met grafisch (Pygame Zero).

**Doelgroep:**
- Kinderen die Scratch ontgroeid zijn
- Werken zelfstandig op eigen tempo
- Nederlandse interface, Engelse keywords worden aangeleerd

**Kernprincipes:**
- Fun first, concepts second
- Elk level introduceert één nieuw concept
- Uitbreidingen via challenge cards (makkelijk/medium/moeilijk)
- Materialen in het Nederlands

**Deliverables:**
1. 4 text-based Python levels (`.py` bestanden)
2. 2+ Pygame Zero levels (na text-based)
3. MkDocs website (instructies + showcase)
4. Printbare challenge cards (gegenereerd uit dezelfde Markdown)

---

## 2. Level Progression (Text-based)

| Level | Nieuw concept | Game feature | Voorbeeld |
|-------|---------------|--------------|-----------|
| **1** | `if`/`elif`/`else`, `input()`, `print()` | Keuze maken: rennen of vechten | Bestaande Zombie1.py |
| **2** | `while`, variabelen, state | Levens systeem, game loop | Bestaande Zombie2.py |
| **3** | `import random`, lijsten | Willekeurige events, zombie types, inventory | Wapens verzamelen, verschillende zombies |
| **4** | `def` functies | Code organiseren, herbruikbare acties | `def vecht():`, `def toon_inventaris():` |

### Per level structuur

```
BEKIJK  → Run de code, zie wat het doet (30 sec)
LEES    → Loop door code, begrijp elk deel (5 min)
PROBEER → Kleine guided change (5-10 min)
UITDAGING → Kies een challenge card (15+ min)
```

### Voorbeeld challenges Level 1

| Moeilijkheid | Challenge |
|--------------|-----------|
| Makkelijk | Voeg een derde optie toe: "verstoppen" |
| Makkelijk | Verander de teksten (maak je eigen verhaal) |
| Medium | De zombie heeft een naam (random uit lijst) |
| Moeilijk | Voeg een "praten" optie toe met eigen logica |

### Voorbeeld challenges Level 2

| Moeilijkheid | Challenge |
|--------------|-----------|
| Makkelijk | Verander het aantal levens naar 5 |
| Makkelijk | Voeg een "game over" bericht toe als je dood bent |
| Medium | Voeg een "zoeken" actie toe om een wapen te vinden |
| Medium | Het wapen verhoogt je winkans bij vechten |
| Moeilijk | Voeg een score toe die omhoog gaat per overwonnen zombie |

---

## 3. Level Progression (Pygame Zero)

Na de 4 text-based levels, transitie naar grafisch:

| Level | Nieuw concept | Game feature |
|-------|---------------|--------------|
| **5** | `draw()`, `screen`, basale graphics | Dezelfde game maar met knoppen en kleuren |
| **6** | `Actor`, images, `on_mouse_down()` | Zombie sprites, klikbare acties |
| **7+** | Animatie, meerdere schermen, sounds | Volledig clicker/adventure game |

### Waarom deze volgorde werkt

- Level 4 introduceert functies → Level 5 gebruikt `def draw():` (bekend patroon)
- Kids begrijpen al state/variabelen → Pygame Zero state management voelt logisch
- Beloning: "Je code doet nu hetzelfde, maar met graphics!"

### Pygame Zero voordelen

- Minimale boilerplate (geen `pygame.init()`, geen event loop)
- Images in `images/` folder, klaar
- `pgzrun zombie.py` en het werkt

### Assets

- Images gegenereerd via Midjourney
- Simpele sprites: zombie, achtergrond, knoppen
- Kids kunnen eigen images toevoegen als challenge

---

## 4. Project Structure

```
CoderDojo-Zombies/
├── levels/
│   ├── level-1/
│   │   ├── zombie.py
│   │   ├── uitleg.md              # Explanation for website
│   │   └── challenges.md          # Challenge cards content
│   ├── level-2/
│   │   ├── zombie.py
│   │   ├── uitleg.md
│   │   └── challenges.md
│   ├── level-3/
│   │   └── ...
│   ├── level-4/
│   │   └── ...
│   └── level-5-pgzero/
│       ├── zombie.py
│       ├── uitleg.md
│       ├── challenges.md
│       └── images/
│           └── zombie.png
│
├── docs/                           # MkDocs root (non-level pages)
│   ├── index.md                    # Landing page
│   └── aan-de-slag.md              # Getting started
│
├── print/                          # Generated printable cards
├── mkdocs.yml                      # MkDocs config
└── README.md
```

---

## 5. Website (MkDocs)

### Tech

- MkDocs met Material theme
- Hosting: GitHub Pages via `mkdocs gh-deploy`

### Navigatie

```
Zombie Apocalypse
├── Home                    # Wat is dit? Voor wie?
├── Aan de Slag             # Python installeren, VS Code setup
├── Levels
│   ├── Level 1 - Keuzes
│   ├── Level 2 - Levens
│   ├── Level 3 - Inventory
│   ├── Level 4 - Functies
│   └── Level 5 - Graphics
└── Printbare Kaarten       # Link naar print-friendly versie
```

### Per level pagina bevat

1. **Wat leer je?** — nieuw concept in 2-3 zinnen
2. **De code** — syntax highlighted, copy button
3. **BEKIJK → LEES → PROBEER** — korte instructies
4. **Challenges** — tabel met moeilijkheid + beschrijving

### Taal

Volledig Nederlands

### mkdocs.yml

```yaml
site_name: Zombie Apocalypse
theme:
  name: material
  language: nl
  palette:
    scheme: slate
    primary: red
nav:
  - Home: index.md
  - Aan de Slag: aan-de-slag.md
  - Levels:
    - Level 1: levels/level-1/uitleg.md
    - Level 2: levels/level-2/uitleg.md
    # ...
```

---

## 6. Printable Challenge Cards

### Bron

Dezelfde `challenges.md` per level

### Format in Markdown

```markdown
# Level 1 Challenges

## Makkelijk

### Verstoppen
Voeg een derde optie toe: "verstoppen"
**Hint:** Gebruik `elif actie == "verstoppen":`

---

### Eigen Verhaal
Verander alle teksten naar je eigen zombie verhaal
**Hint:** Pas de strings aan in de `print()` statements

---

## Medium

### Zombie Naam
De zombie heeft een naam (kies random uit een lijst)
**Hint:** Maak een lijst: `namen = ["Gerrit", "Zombie-Jan", "Ransen"]`

---

# Level 2 Challenges

## Medium

### Wapen Zoeken
Voeg een "zoeken" actie toe om een wapen te vinden
**Hint:** Maak een variabele `heeft_wapen = False` aan het begin
```

### Print oplossing

CSS print stylesheet die:
- Elke `###` heading = nieuwe kaart
- Moeilijkheid als kleur/badge (groen/oranje/rood)
- Hints op achterkant (of inklapbaar)
- 4 kaarten per A4

### Workflow

1. Schrijf challenges in `challenges.md`
2. Website toont ze als lijst
3. Print pagina (`/cards/level-1/`) rendert als kaarten
4. Mentor print, knipt, lamineer, klaar

---

## 7. Developer Experience (DX)

### Error handling

- VS Code + Pylance extension (verplicht in setup)
- `friendly-traceback` package met Nederlandse errors
- Elke level file begint met `import friendly; friendly.install()`

### Running scripts

- VS Code Run button (▶️) — standaard methode
- Documenteer met screenshots in "Aan de Slag"
- Kids openen altijd folder (niet los bestand)

### VS Code aanbevolen extensions

- Python (Microsoft)
- Pylance
- Code Runner (optioneel)

### Aan de Slag checklist

1. Installeer Python
2. Installeer VS Code
3. Installeer Python + Pylance extensions
4. `pip install friendly-traceback pgzero`
5. Open folder in VS Code
6. Klik ▶️ om te runnen

---

## 8. Scope

### In scope (dit project)

- 4 text-based levels met werkende code
- 2 Pygame Zero levels (basis)
- MkDocs website met alle content
- Printbare challenge cards (CSS print stylesheet)
- Nederlandse content
- Midjourney-gegenereerde images voor Pygame Zero levels

### Out of scope (mogelijk later)

- Progress tracking / login systeem
- Community features (delen van creaties)
- Meer dan 6 levels
- OOP / classes (bewust weggelaten)
- Andere talen dan Nederlands
- PDF generator script (CSS print is voldoende voor v1)

---

## 9. Risks & Mitigations

| Risico | Mitigatie |
|--------|-----------|
| Pygame Zero te moeilijke sprong | Level 4 functies goed oefenen, level 5 simpel houden |
| Kids raken vast | Hints op challenge cards, mentoren beschikbaar |
| Engelse keywords verwarrend | Cheat sheet kaart met NL→Python vertalingen |
| Syntax errors frustrerend | Pylance + friendly-traceback installeren |

---

## 10. Python Keywords Cheat Sheet

| Nederlands | Python |
|------------|--------|
| als | `if` |
| anders als | `elif` |
| anders | `else` |
| zolang | `while` |
| voor | `for` |
| in | `in` |
| en | `and` |
| of | `or` |
| niet | `not` |
| waar | `True` |
| onwaar | `False` |
| functie | `def` |
| teruggeven | `return` |
| importeren | `import` |
