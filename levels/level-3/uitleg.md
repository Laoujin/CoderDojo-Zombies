# Level 3: Lijsten en Inventory

## Wat leer je?

In dit level leer je over **lijsten** - een manier om meerdere dingen te bewaren in één variabele. Je leert ook `random.choice()` om iets willekeurigs uit een lijst te kiezen.

## De code

### Een lijst maken

```python
inventory = []  # lege lijst
zombie_types = ["langzame zombie", "snelle zombie", "sterke zombie"]
```

Lijsten gebruiken vierkante haken `[]`. Items worden gescheiden door komma's.

### Iets uit een lijst kiezen

```python
zombie = random.choice(zombie_types)
```

`random.choice()` pakt een willekeurig item uit de lijst.

### Iets toevoegen aan een lijst

```python
inventory.append("honkbalknuppel")
```


### Checken of iets in een lijst zit

```python
if "honkbalknuppel" in inventory:
    print("Je hebt een wapen!")
```

`in` checkt of iets in de lijst zit.

### Iets verwijderen uit een lijst

```python
inventory.remove("medkit")
```


## BEKIJK

1. Run `zombie.py`
2. Probeer te zoeken naar items
3. Let op hoe je inventory groeit

## LEES

- Welke lijsten zijn er in de code?
- Wat gebeurt er als je een zombie verslaat?
- Hoe werkt de medkit?

## PROBEER

Voeg een nieuw zombie type toe aan de `zombie_types` lijst. Misschien een "baby zombie" die makkelijk te verslaan is?
