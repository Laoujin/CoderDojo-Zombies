# CoderDojo Zombie Apocalypse

Leer Python programmeren met een zombie spel!

**Website:** https://laoujin.github.io/CoderDojo-Zombies/

## Voor Coaches

Dit is een curriculum voor CoderDojo om kinderen (8-16 jaar) Python te leren. Het project bevat:

- **4 tekst-based levels** met oplopende moeilijkheid
- **1 Pygame Zero level** voor "clicker-game"
- **Printbare uitdaging kaarten** voor in de sessie (Opwarmer / Pittig / Boss)
- **MkDocs website** met alle instructies
- **Coaches handleiding** met sessie-voorbereiding tips

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

**Let op:** Python 3.12 is vereist (pygame werkt nog niet met 3.13+). Check met `python --version`.

```bash
# Installeer dependencies
pip install -r requirements.txt
pip install mkdocs mkdocs-material

# Sync level docs naar docs/ (nodig voor MkDocs)
cp levels/level-*/*.md docs/levels/level-*/  # Linux/Mac
# Of maak docs/levels/ folders aan en kopieer handmatig op Windows

# Start de website lokaal
mkdocs serve

# Deploy naar GitHub Pages (automatisch via GitHub Actions)
mkdocs gh-deploy
```

## Levels

| Level | Concept           | Files             |
|-------|-------------------|-------------------|
| 1     | if/elif/else      | `levels/level-1/` |
| 2     | while, variabelen | `levels/level-2/` |
| 3     | lijsten, random   | `levels/level-3/` |
| 4     | functies          | `levels/level-4/` |

## Printbare Uitdagingen Kaarten

Genereer uitdaging kaarten met custom achtergrondafbeeldingen.

### Setup

```bash
pip install playwright
playwright install chromium
```

### Achtergrondafbeeldingen toevoegen

Plaats afbeeldingen in `docs/cards/level-{n}/` met de slugified uitdaging naam:

```
docs/cards/
├── level-1/
│   ├── eigen-verhaal.png
│   ├── verstoppen.png
│   └── praten.png
├── level-2/
│   └── ...
└── output/          # Gegenereerde kaarten
```

Gebruik `--list` om te zien welke afbeeldingen verwacht worden:

```bash
python docs/cards/generate.py --list
```

### Kaarten genereren

```bash
# Alle kaarten genereren
python docs/cards/generate.py

# Alleen level 1
python docs/cards/generate.py --level 1
```

Kaarten worden opgeslagen in `docs/cards/output/` als PNG (600x400px, 3:2 ratio).

**Tip:** Afbeeldingen van ~600x400px (of 3:2 ratio) werken het beste. De afbeelding wordt gecentreerd en bedekt de hele kaart.
