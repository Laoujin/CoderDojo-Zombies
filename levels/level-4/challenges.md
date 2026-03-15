# Level 4 Challenges

## Opwarmer

### Status Verbeteren

Pas `toon_status()` aan om ook het aantal items te tonen

**Hint:** Gebruik `len(inventory)` om het aantal items te tellen

---

## Pittig

### Meerdere Wapens

Pas `vecht()` aan en voeg andere wapens toe als mogelijke inventory.

**Hint:** Verander `heeft_wapen` naar `wapen_type` (None, "honkbalknuppel", "zwaard", etc.)

---

## Boss

### Zombie HP

Geef zombies meerdere levens zodat je ze vaker moet raken

**Hint:** Voeg `"hp": 2` toe aan de zombie dictionary in `maak_zombie()`. Bij vechten: `zombie["hp"] -= 1` en check of hp 0 is.

