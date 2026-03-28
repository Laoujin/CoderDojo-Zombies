# Level 4 Uitdagingen

## Opwarmer

### Status Verbeteren

Pas `toon_status()` aan om ook het aantal items te tonen

**Hint:** Gebruik `len(inventory)` om het aantal items te tellen

---

### Gebruik Item

Maak een nieuwe functie `gebruik_item(item, levens, inventory)` die een item uit je inventory gebruikt.

- Medkit: +2 levens
- Energie bar: +1 leven
- De functie returned het nieuwe aantal levens
- Roep de functie aan in `main()` in plaats van de bestaande medkit code

**Hint:** Maak een `def gebruik_item(item, levens, inventory):` met `if item == "medkit":` en `return levens`

---

## Pittig

### Meerdere Wapens

Pas `vecht()` aan en voeg andere wapens toe als mogelijke inventory.

**Hint:** Verander `heeft_wapen` naar `wapen_type` (None, "honkbalknuppel", "zwaard", etc.)

---

### Crafting

Maak een `craft(inventory)` functie die twee items combineert tot iets beters. Gebruik een `recepten` dictionary.

- Honkbalknuppel + spijkers = spijkerknuppel
- Zaklamp + batterij = super zaklamp
- Voeg "craft" toe als actie in het spel

**Hint:** Maak een dictionary `recepten = {"spijkerknuppel": ["honkbalknuppel", "spijkers"]}` en check of beide items in de inventory zitten

---

## Boss

### Zombie HP

Geef zombies meerdere levens zodat je ze vaker moet raken

**Hint:** Voeg `"hp": 2` toe aan de zombie dictionary in `maak_zombie()`. Bij vechten: `zombie["hp"] -= 1` en check of hp 0 is.

    ```python
    types = [
        ("baby zombie", 1),
        ("langzame zombie", 2),
        ("snelle zombie", 2),
        ("sterke zombie", 3),
    ]

    zombie_type, hp = random.choice(types)
    ```
