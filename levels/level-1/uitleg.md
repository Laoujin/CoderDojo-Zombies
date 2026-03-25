# Level 1: Keuzes Maken

??? code "Bekijk de volledige code"

    ```python
    --8<-- "level-1/zombie.py"
    ```

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
