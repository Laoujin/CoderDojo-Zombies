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
