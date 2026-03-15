# Level 3 Challenges

## Opwarmer

### Zombie Geluiden

Laat de zombie een geluid maken als hij verschijnt

**Hint:** Maak een lijst `zombie_geluiden = ["GRAAH!", "BRAINS!", ...]` en gebruik `random.choice()`

??? note "Spieken"
    ```python
    zombie_geluiden = ["GRAAAAAH!", "BRAAAAINS!", "UGHHHH...", "GRRRR!"]

    # Bij zombie encounter:
    geluid = random.choice(zombie_geluiden)
    print(f"De zombie gromt: {geluid}")
    ```

---

### Items Verbeteren

Pas de medkit en energie bar aan: medkit geeft 3 levens, energie bar geeft 1 leven

**Hint:** Check welk item je gebruikt met `if ... in inventory` en pas `levens +=` aan

??? note "Spieken"
    ```python
    if "medkit" in inventory:
        gebruik = input("Medkit gebruiken? (+3 levens) (ja/nee) ")
        if gebruik == "ja":
            inventory.remove("medkit")
            levens += 3
            print("+3 levens!")

    if "energie bar" in inventory:
        gebruik = input("Energie bar gebruiken? (+1 leven) (ja/nee) ")
        if gebruik == "ja":
            inventory.remove("energie bar")
            levens += 1
            print("+1 leven!")
    ```

---

## Pittig

### Zombie Drops

Laat de zombie soms een item droppen als je wint

**Hint:** Na het verslaan, gebruik `random.randint(1, 3) == 1` om te checken of er iets valt, en `random.choice()` om een item te kiezen

??? note "Spieken"
    ```python
    if kans >= 2 or (kans == 1 and heeft_wapen):
        print("Je verslaat de zombie!")
        # Zombie laat soms iets vallen
        if random.randint(1, 3) == 1:
            item = random.choice(["medkit", "zaklamp", "energie bar"])
            print(f"De zombie liet een {item} vallen!")
            inventory.append(item)
    ```

---

## Boss

