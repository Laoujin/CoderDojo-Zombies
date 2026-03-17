### Zombie Winkans

Elk zombie type heeft een andere winkans

**Hint:** Maak een dictionary met kansen per type

??? note "Spieken"
    ```python
    # Kans om te winnen per zombie type (hoe hoger, hoe makkelijker)
    zombie_moeilijkheid = {
        "langzame zombie": 2,    # 2 op 3 kans
        "snelle zombie": 2,      # 2 op 3 kans
        "sterke zombie": 3,      # 1 op 3 kans
        "baby zombie": 1         # 1 op 2 kans (makkelijk)
    }

    moeilijkheid = zombie_moeilijkheid[zombie]
    kans = random.randint(1, moeilijkheid)
    ```



### Random Events

Voeg willekeurige events toe tussen rondes

**Hint:** Maak een `events` lijst en aan het begin van de ronde heb je een kans dat er zich een van de events voordoet.

??? note "Spieken"
    ```python
    events = [
        ("Je struikelt over een steen!", -1, None),       # verlies leven
        ("Je vindt een verborgen kist!", 0, "medkit"),    # vind item
        ("Een kat schrikt je!", 0, None),                 # niks
        ("Je hoort andere overlevenden!", 0, None),       # niks
    ]

    # Aan het begin van elke ronde:
    if random.randint(1, 4) == 1:  # 25% kans op event
        event = random.choice(events)
        print(f"! {event[0]}")
        if event[1] != 0:
            levens += event[1]
        if event[2]:
            inventory.append(event[2])
    ```



### Locaties

Voeg locaties toe: straat -> ziekenhuis -> supermarkt

**Hint:** Maak een `locaties` lijst en een `huidige_locatie` variabele

??? note "Spieken"
    ```python
    locaties = ["straat", "ziekenhuis", "supermarkt", "politiebureau"]
    locatie_index = 0

    while levens > 0 and locatie_index < len(locaties):
        huidige_locatie = locaties[locatie_index]
        print(f"Je bent bij: {huidige_locatie}")

        # ... zombie encounter ...

        # Na overleven, ga naar volgende locatie
        if levens > 0:
            locatie_index += 1
            if locatie_index < len(locaties):
                print(f"Je gaat verder naar {locaties[locatie_index]}...")

    if locatie_index >= len(locaties):
        print("Je hebt alle locaties overleefd!")
    ```


### Crafting

Combineer 2 items tot iets beters

**Hint:** Check of beide items in inventory zitten, verwijder ze, voeg het nieuwe item toe

??? note "Spieken"
    ```python
    elif actie == "craft":
        if "zaklamp" in inventory and "honkbalknuppel" in inventory:
            print("Je combineert de zaklamp en knuppel...")
            inventory.remove("zaklamp")
            inventory.remove("honkbalknuppel")
            inventory.append("lichtgevende knuppel")
            print("Je hebt nu een LICHTGEVENDE KNUPPEL!")
        else:
            print("Je hebt niet de juiste items om te craften.")
            print("(Nodig: zaklamp + honkbalknuppel)")
    ```

---

### Shop

Ruil items met een NPC handelaar

**Hint:** Toon wat de handelaar heeft, vraag wat de speler wil ruilen

??? note "Spieken"
    ```python
    # Random kans op handelaar
    if random.randint(1, 5) == 1:
        print("Je ontmoet een handelaar!")
        print("   Hij biedt aan: medkit")
        print("   Hij wil: 2 energie bars")

        if inventory.count("energie bar") >= 2:
            ruil = input("Wil je ruilen? (ja/nee) ")
            if ruil == "ja":
                inventory.remove("energie bar")
                inventory.remove("energie bar")
                inventory.append("medkit")
                print("Geruild!")
        else:
            print("Je hebt niet genoeg energie bars...")
    ```
