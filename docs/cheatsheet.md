# Python Cheatsheet

Python gebruikt Engelse woorden. Hier is een vertaling:

## Keywords

| Nederlands | Python   | Voorbeeld                           |
|------------|----------|-------------------------------------|
| als        | `if`     | `if actie == "rennen":`             |
| anders als | `elif`   | `elif actie == "vechten":`          |
| anders     | `else`   | `else:`                             |
| zolang     | `while`  | `while levens > 0:`                 |
| voor       | `for`    | `for item in lijst:`                |
| in         | `in`     | `if "mes" in inventory:`            |
| en         | `and`    | `if levens > 0 and heeft_wapen:`    |
| of         | `or`     | `if actie == "ja" or actie == "j":` |
| niet       | `not`    | `if not heeft_wapen:`               |
| waar       | `True`   | `gevonden = True`                   |
| onwaar     | `False`  | `heeft_wapen = False`               |
| functie    | `def`    | `def vecht():`                      |
| teruggeven | `return` | `return True`                       |
| importeren | `import` | `import random`                     |

## Symbolen

| Wat               | Symbool | Voorbeeld               |
|-------------------|---------|-------------------------|
| is gelijk aan     | `==`    | `if actie == "rennen":` |
| toewijzen         | `=`     | `levens = 3`            |
| niet gelijk aan   | `!=`    | `if naam != "":`        |
| groter dan        | `>`     | `if levens > 0:`        |
| kleiner dan       | `<`     | `if kans < 3:`          |
| groter of gelijk  | `>=`    | `if score >= 100:`      |
| kleiner of gelijk | `<=`    | `if levens <= 0:`       |
| plus              | `+`     | `score = score + 10`    |
| min               | `-`     | `levens = levens - 1`   |
| plus-is           | `+=`    | `score += 10`           |
| min-is            | `-=`    | `levens -= 1`           |

## Veelgebruikte functies

| Functie            | Wat het doet          | Voorbeeld                   |
|--------------------|-----------------------|-----------------------------|
| `print()`          | Tekst tonen           | `print("Hallo!")`           |
| `input()`          | Vraag om input        | `naam = input("Naam? ")`    |
| `len()`            | Tel items             | `len(inventory)`            |
| `random.choice()`  | Kies willekeurig      | `random.choice(["a", "b"])` |
| `random.randint()` | Random getal          | `random.randint(1, 6)`      |
| `.append()`        | Toevoegen aan lijst   | `inventory.append("mes")`   |
| `.remove()`        | Verwijderen uit lijst | `inventory.remove("mes")`   |
| `time.sleep()`     | Pauzeren              | `time.sleep(1)`             |

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
