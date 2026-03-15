# Level 4 Challenges

## Makkelijk

### Status Verbeteren

Pas `toon_status()` aan om ook het aantal items te tonen

**Hint:** Gebruik `len(inventory)` om het aantal items te tellen

??? note "Spieken"
    ```python
    def toon_status(levens, score, inventory):
        print()
        print(f"Levens: {levens} | Score: {score} | Items: {len(inventory)}")
        if inventory:
            print(f"   Inventory: {inventory}")
        print()
    ```

---

### Eigen Functie

Verplaats de medkit-logica naar een eigen functie

**Hint:** Maak `def gebruik_medkit(levens, inventory):` die het nieuwe aantal levens teruggeeft

??? note "Spieken"
    ```python
    def gebruik_medkit(levens, inventory):
        """Vraag of speler medkit wil gebruiken. Return nieuw aantal levens."""
        if levens < 3 and "medkit" in inventory:
            gebruik = input("Medkit gebruiken? (ja/nee) ").lower()
            if gebruik == "ja":
                inventory.remove("medkit")
                print("+1 leven!")
                return levens + 1
        return levens

    # In main():
    levens = gebruik_medkit(levens, inventory)
    ```

---

## Medium

### Functie met Parameter

Pas `vecht()` aan zodat je kan kiezen welk wapen je gebruikt

**Hint:** Verander `heeft_wapen` naar `wapen_type` (None, "honkbalknuppel", "zwaard", etc.)

??? note "Spieken"
    ```python
    def vecht(zombie, wapen_type):
        print("Je maakt je klaar om te vechten...")

        if wapen_type == "zwaard":
            print("   Je zwaait met je zwaard!")
            bonus = 2
        elif wapen_type == "honkbalknuppel":
            print("   Je zwaait met je knuppel!")
            bonus = 1
        else:
            print("   Je balt je vuisten...")
            bonus = 0

        moeilijkheid = bereken_winkans(zombie, wapen_type is not None)
        kans = random.randint(1, max(1, moeilijkheid - bonus))

        return kans == 1
    ```

---

### Waarde Teruggeven

Maak een `bereken_score()` functie die bonuspunten geeft voor moeilijke zombies

**Hint:** Return 10 voor normale zombies, 20 voor sterke zombies

??? note "Spieken"
    ```python
    def bereken_score(zombie):
        """Bereken hoeveel punten een zombie waard is."""
        if zombie["type"] == "sterke zombie":
            return 20
        elif zombie["type"] == "snelle zombie":
            return 15
        else:
            return 10

    # In main(), bij winst:
    punten = bereken_score(zombie)
    score += punten
    print(f"   +{punten} punten!")
    ```

---

## Moeilijk

### Help Functie

Maak een interactieve help die uitlegt hoe elk zombie type werkt

**Hint:** Vraag eerst "Waarover wil je meer weten?"

??? note "Spieken"
    ```python
    def toon_help():
        print()
        print("=== HELP ===")
        print("1. Acties")
        print("2. Zombie types")
        print("3. Items")
        print()
        keuze = input("Kies een nummer (of Enter om terug te gaan): ")

        if keuze == "1":
            print("rennen  - Ontsnappen (makkelijker bij langzame zombies)")
            print("vechten - Vechten (beter met wapen)")
            print("zoeken  - Zoek items")
        elif keuze == "2":
            print("langzame zombie - Normaal, makkelijk te ontsnappen")
            print("snelle zombie   - Moeilijk te ontsnappen!")
            print("sterke zombie   - Moeilijk te verslaan!")
        elif keuze == "3":
            print("honkbalknuppel - Verhoogt je winkans bij vechten")
            print("medkit         - Herstelt 1 leven")
            print("energie bar    - Voor later...")
        print()
    ```

---

### Zombie Generator

Maak een `nieuwe_zombie()` functie die steeds moeilijkere zombies maakt

**Hint:** Geef een `ronde` parameter mee, en maak sterkere zombies in latere rondes

??? note "Spieken"
    ```python
    def maak_zombie(ronde):
        """Maak een zombie. Hogere rondes = moeilijkere zombies."""

        if ronde <= 2:
            types = ["langzame zombie"]
        elif ronde <= 5:
            types = ["langzame zombie", "snelle zombie"]
        else:
            types = ["langzame zombie", "snelle zombie", "sterke zombie"]

        namen = ["Gerrit", "Jan", "Pansen"]

        return {
            "type": random.choice(types),
            "naam": f"{random.choice(namen)} #{ronde}",
            "geluid": "GRAAAH!"
        }

    # In main():
    ronde = 0
    while levens > 0:
        ronde += 1
        zombie = maak_zombie(ronde)
    ```
