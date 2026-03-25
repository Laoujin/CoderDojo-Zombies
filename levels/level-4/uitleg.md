# Level 4: Functies

??? code "Bekijk de volledige code"

    ```python
    --8<-- "level-4/zombie.py"
    ```

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

### Bestanden lezen en schrijven (File I/O)

Je kan gegevens opslaan in een bestand zodat ze bewaard blijven.

**Schrijven naar een bestand:**

```python
with open("highscores.txt", "a") as f:
    f.write(f"{naam},{score}\n")
```

- `open()` opent een bestand
- `"a"` betekent "append" - toevoegen aan het einde
- `"w"` zou "write" zijn - alles overschrijven
- `with` zorgt dat het bestand netjes wordt gesloten
- `f.write()` schrijft tekst naar het bestand
- `\n` is een nieuwe regel

**Lezen uit een bestand:**

```python
with open("highscores.txt", "r") as f:
    for line in f:
        print(line)
```

- `"r"` betekent "read" - lezen
- `for line in f` leest regel voor regel

**Bestand bestaat niet?**

```python
try:
    with open("highscores.txt", "r") as f:
        # lees bestand
except FileNotFoundError:
    print("Bestand bestaat nog niet!")
```

`try/except` vangt fouten op zodat je programma niet crasht.

## BEKIJK

1. Run `zombie.py`
2. Type `help` om de help functie te zien
3. Let op hoe het spel hetzelfde werkt, maar de code is anders georganiseerd

## PROBEER

Voeg een extra print statement toe in de `toon_help()` functie met een nieuwe tip en maak die actie ook mogelijk.
