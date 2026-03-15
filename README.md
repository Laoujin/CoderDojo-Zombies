# CoderDojo Zombie Apocalypse

Leer Python programmeren met een zombie spel!

## Voor mentoren

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

| Level | Concept           | Files             |
|-------|-------------------|-------------------|
| 1     | if/elif/else      | `levels/level-1/` |
| 2     | while, variabelen | `levels/level-2/` |
| 3     | lijsten, random   | `levels/level-3/` |
| 4     | functies          | `levels/level-4/` |
