# Level 3 Challenges

## Opwarmer

### Zombie Geluiden

Laat de zombie een geluid maken wanneer hij verschijnt

**Hint:** Maak een lijst `zombie_geluiden = ["GRAAH!", "BRAINS!", ...]` en gebruik `random.choice()`

---

### Items Verbeteren

Pas de medkit en energie bar aan: medkit geeft 3 levens, energie bar geeft 1 leven

**Hint:** Check welk item je gebruikt met `if ... in inventory` en pas `levens +=` aan

---

## Pittig

### Zombie Drops

Laat de zombie soms een item droppen als je wint

**Hint:** Na het verslaan, gebruik `random.randint(1, 3) == 1` om te checken of er iets valt, en `random.choice()` om een item te kiezen


---

## Boss

### Sterke Zombie

Voeg een "sterke zombie" toe die moeilijker te verslaan is

**Hint:** Voeg "sterke zombie" toe aan de lijst en check `if zombie == "sterke zombie":` bij vechten

---

### Wapen Bonus

De honkbalknuppel maakt vechten makkelijker (vooral tegen sterke zombies!)

**Hint:** Check `if "honkbalknuppel" in inventory:` en geef een betere kans

