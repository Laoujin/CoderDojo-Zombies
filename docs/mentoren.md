# Voor Mentoren

Tips en oplossingen voor veelvoorkomende problemen.

## Meerdere Python versies

**Probleem:** `ModuleNotFoundError: No module named 'friendly_traceback'` terwijl je `pip install` al hebt gedaan.

**Oorzaak:** Er zijn meerdere Python versies geinstalleerd. Packages worden per versie geinstalleerd.

**Oplossing:**

1. Check welke Python VS Code gebruikt (rechtsonder in de statusbalk)
2. `Ctrl+Shift+P` → "Python: Select Interpreter" → Kies Python 3.12
3. Of installeer packages voor de actieve Python:
   ```bash
   python -m pip install -r requirements.txt
   ```

**Tip:** Gebruik altijd `python -m pip install` in plaats van `pip install` om zeker te zijn dat je de juiste Python gebruikt.

## Python niet gevonden

**Probleem:** `'python' is not recognized` of `python: command not found`

**Oorzaak:** Python staat niet in PATH.

**Oplossing:** Herinstalleer Python en vink "Add Python to PATH" aan.

## Pygame installatie mislukt

**Probleem:** Foutmelding bij `pip install pgzero` over pygame build.

**Oorzaak:** Pygame heeft nog geen wheel voor Python 3.13+.

**Oplossing:** Gebruik Python 3.12:
```bash
winget uninstall Python.Python.3.13
winget install Python.Python.3.12
```

## VS Code extensies

Zorg dat deze extensies geinstalleerd zijn:

- **Python** (Microsoft) - syntax highlighting, debugging
- **Pylance** (Microsoft) - code completion, type checking

## Kids kunnen niet typen

Sommige kinderen (vooral de jongere) kunnen nog niet goed typen. Tips:

- Laat ze eerst de code bekijken en uitleggen wat er staat
- Typ samen met ze (jij typt, zij dicteren)
- Gebruik de challenge cards - minder typen nodig
- Focus op begrip, niet op typsnelheid
