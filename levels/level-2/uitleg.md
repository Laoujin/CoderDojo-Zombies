# Level 2: Levens en Loops

## Wat leer je?

In dit level leer je hoe je code herhaalt met `while` loops en hoe je variabelen gebruikt om de status van het spel bij te houden.

## De code

### Variabelen

```python
levens = 3
```

Je kan variabelen aanpassen, vb om een leven te verliezen: `levens = levens - 1`.

### While loop

```python
while levens > 0:
    # deze code herhaalt zolang levens groter is dan 0
```

De code binnen de `while` blijft herhalen totdat de voorwaarde (`levens > 0`) niet meer waar is.


## BEKIJK

1. Run `zombie.py`
2. Let op: het spel stopt niet na één beurt!


## LEES

Lees de code en beantwoord:
- Wanneer stopt de while loop?
- Wat gebeurt er met `levens` als je geraakt wordt?
- Waarom staat `levens = 0` bij de `else`?

## PROBEER

Verander `levens = 3` naar `levens = 5`. Run het spel - je hebt nu 5 levens!
