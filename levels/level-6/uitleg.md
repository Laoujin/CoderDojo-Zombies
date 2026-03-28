# Level 6: Bouw Je Eigen Spel!

!!! tip "Kies een starter"
    Dit level heeft **3 starter kits**. Elke starter leert je iets nieuws.
    Kies er een, of combineer ideeën uit meerdere starters!

## Het doel

Bouw je eigen tactisch zombie spel! Gebruik alles wat je geleerd hebt
in de vorige levels en voeg nieuwe dingen toe.

## De starters

### Starter A: Game States

```bash
cd levels/level-6/starter-a-states
pgzrun zombie.py
```

??? code "Bekijk de code"

    ```python
    --8<-- "level-6/starter-a-states/zombie.py"
    ```

Een **Enum** is een klasse met vaste waarden. In Level 5 gebruikten we
strings zoals `"spel"` en `"game_over"`. Met een Enum kan je geen typfouten
meer maken!

```python
from enum import Enum

class Toestand(Enum):
    SPEL = "spel"
    RESULTAAT = "resultaat"
    GAME_OVER = "game_over"
```

In plaats van:
```python
if toestand == "spel":     # typfout? "speel"? 😱
```

Gebruik je nu:
```python
if toestand == Toestand.SPEL:  # geen typfout mogelijk! ✅
```

Je editor helpt je zelfs met automatisch aanvullen.

---

### Starter B: Locaties

```bash
cd levels/level-6/starter-b-world-map
pgzrun zombie.py
```

??? code "Bekijk de code"

    ```python
    --8<-- "level-6/starter-b-world-map/zombie.py"
    ```

Navigeer met de **pijltjestoetsen** (of klik) tussen verschillende locaties.
Elke locatie heeft een eigen achtergrond.

**Nieuw: Keyboard input!**

```python
def on_key_down(key):
    if key == keys.UP:
        ga_naar(-1)
    elif key == keys.DOWN:
        ga_naar(1)
```

Dit is anders dan `on_mouse_down(pos)` uit Level 5. Andere toetsen
die je kan gebruiken: `keys.LEFT`, `keys.RIGHT`, `keys.SPACE`, `keys.ESCAPE`.

**Nieuw: Tuples!**

```python
locaties = [
    ("Kelder", "loc_basement"),
    ("Supermarkt", "loc_supermarket"),
    ("Park", "loc_park"),
    ("Dak", "loc_rooftop"),
]
```

Een **tuple** lijkt op een lijst maar kan niet veranderd worden.
Perfect voor vaste data! Je kan de waarden uitpakken:

```python
naam, afbeelding = locaties[0]
# naam = "Kelder", afbeelding = "loc_basement"
```

---

### Starter C: JSON Data

```bash
cd levels/level-6/starter-c-json-data
pgzrun zombie.py
```

??? code "Bekijk de code"

    ```python
    --8<-- "level-6/starter-c-json-data/zombie.py"
    ```

Laad zombie data uit een **JSON bestand**. Zo staat je speldata los van de code!

**Nieuw: JSON laden!**

```python
import json

with open("data.json") as bestand:
    data = json.load(bestand)

zombies = data["zombies"]
```

JSON lijkt heel erg op Python dictionaries. Open `data.json` om te zien
hoe de data eruitziet. Je kan makkelijk zombies toevoegen of aanpassen
zonder de Python code te veranderen.

## En nu?

Kies een starter en bouw je eigen spel! Hier zijn wat ideeën:

- **Combineer starters**: Enum + locaties + JSON data
- **Voeg knoppen toe**: vechten, rennen, zoeken
- **Zombie stats**: laat de stats bepalen hoe moeilijk een zombie is
- **Inventory**: verzamel items die je helpen
- **Meer locaties**: er zijn veel meer locatie plaatjes beschikbaar!
- **Geluiden**: voeg geluidseffecten toe
- **Score en highscores**: houd bij hoe goed je het doet

Kijk in de `images/` map in de hoofdmap van het project voor alle
beschikbare plaatjes van zombies, locaties, items en wapens.
