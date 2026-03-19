# Level 5 Uitdagingen

## Opwarmer

### Score Teller

Voeg een score teller toe die omhoog gaat bij elke succesvolle actie.

- +10 punten voor een gewonnen gevecht
- +5 punten voor een succesvolle ontsnapping
- Score reset bij game over
- Toon de score in `score.png`

**Hint:** Maak een `score` variabele en teken het met `screen.draw.text()`

??? note "Spieken"
    ```python
    score = 0

    # Bij succes:
    if resultaat_goed:
        if laatste_actie == "vechten":
            score += 10
        else:
            score += 5

    # In draw():
    screen.draw.text(f"Score: {score}", topright=(780, 20), fontsize=24, color="white")
    ```

---

### Verstoppen

Voeg een derde knop "Verstoppen" toe als extra actie.

- Nieuwe knop in het midden van het scherm
- 50/50 kans op succes/faal
- Succes: "De zombie ziet je niet!"
- Faal: "De zombie vindt je!"

**Hint:** Kopieer de rennen logica en pas de tekst aan

??? note "Spieken"
    ```python
    KNOP_VERSTOPPEN = Rect(325, 400, 150, 150)

    # In draw():
    teken_knop_met_pulse("knop_verstoppen", KNOP_VERSTOPPEN)

    # In on_mouse_down():
    elif KNOP_VERSTOPPEN.collidepoint(pos):
        laatste_actie = "verstoppen"
        if random.randint(1, 2) == 1:
            resultaat_tekst = "De zombie ziet je niet!"
            resultaat_goed = True
        else:
            resultaat_tekst = "De zombie vindt je!"
            resultaat_goed = False
            levens -= 1
        toestand = "resultaat"
        clock.schedule(ga_naar_volgende, 2.5)
    ```

**Benodigde plaatjes:** `knop_verstoppen.png`, `verstoppen_succes.png`, `verstoppen_faal.png`

---

## Pittig

### Inventory Systeem

Voeg een inventory toe die items opslaat en het spel beinvloedt.

- Wapens (honkbalknuppel, mes): verhoog winkans van 50% naar 66%
- Healing (medkit, energie bar): medkit +2 levens, energie bar +1 leven
- Toon inventory op het scherm
- Er zijn verschillende plaatjes beschikbaar, ze beginnen met `inv_`

**Hint:** Gebruik een lijst voor items en check met `in`

??? note "Spieken"
    ```python
    inventory = []

    # Toon inventory in draw():
    for i, item in enumerate(inventory):
        screen.draw.text(item, topleft=(20, 80 + i * 25), fontsize=18, color="white")

    # Aangepaste vecht logica:
    if "honkbalknuppel" in inventory or "mes" in inventory:
        win = random.randint(1, 3) <= 2  # 66% kans
    else:
        win = random.randint(1, 2) == 1  # 50% kans

    # Gebruik medkit:
    if "medkit" in inventory and levens < 3:
        inventory.remove("medkit")
        levens = min(levens + 2, 5)
    ```

---

### Zombie Types

Verschillende zombies verschijnen met verschillende winkansen.

- Baby zombie: 66% winkans (makkelijk)
- Langzame zombie: 50% winkans
- Snelle zombie: 40% winkans
- Sterke zombie: 33% winkans (moeilijk)
- Er zijn verschillende plaatjes beschikbaar, ze beginnen met `zombie_`

**Hint:** Gebruik een dictionary met kansen per zombie type

??? note "Spieken"
    ```python
    zombie_kansen = {
        "Baby zombie": (2, 3),      # win op 1-2 van 3
        "Langzame zombie": (1, 2),  # win op 1 van 2
        "Snelle zombie": (2, 5),    # win op 1-2 van 5
        "Sterke zombie": (1, 3),    # win op 1 van 3
    }

    huidige_zombie = random.choice(list(zombie_kansen.keys()))

    # Bij vechten:
    kans = zombie_kansen[huidige_zombie]
    win = random.randint(1, kans[1]) <= kans[0]

    # Toon zombie type in draw():
    screen.draw.text(huidige_zombie, center=(400, 550), fontsize=24, color="yellow")
    ```

---

## Boss

### Meerdere Locaties

Ga door 5 locaties heen om het spel te winnen.

- Locaties: Suburb → Library → School → Hospital → Mall
- Elke succesvolle actie brengt je naar de volgende locatie
- Falen kost een leven maar je gaat ook door
- Overleef alle 5 locaties = gewonnen!
- Er zijn verschillende locaties beschikbaar, de plaatjes beginnen met `loc_`

**Hint:** Gebruik een lijst met locaties en een index

??? note "Spieken"
    ```python
    locaties = ["Suburb", "Library", "School", "Hospital", "Mall"]
    locatie_index = 0

    def ga_naar_volgende():
        global toestand, locatie_index
        if levens <= 0:
            toestand = "game_over"
        elif locatie_index >= len(locaties) - 1:
            toestand = "gewonnen"
        else:
            locatie_index += 1
            toestand = "spel"

    # In draw() bij "spel":
    achtergrond = f"achtergrond_{locaties[locatie_index].lower()}"
    screen.blit(achtergrond, (0, 0))
    screen.draw.text(locaties[locatie_index], center=(400, 30), fontsize=28, color="white")

    # In draw() bij "gewonnen":
    elif toestand == "gewonnen":
        screen.blit("gewonnen", (0, 0))
        screen.draw.text("JE HEBT GEWONNEN!", center=(400, 300), fontsize=48, color="gold")
    ```

**Benodigde plaatjes:** `achtergrond_suburb.png`, `achtergrond_library.png`, `achtergrond_school.png`, `achtergrond_hospital.png`, `achtergrond_mall.png`, `gewonnen.png`

---

### Zoeken na Gevecht

Win een gevecht om het gebied te doorzoeken voor items.

- Na een gewonnen gevecht verschijnt een "Zoeken" knop
- 50% kans om een item te vinden (medkit, wapen, etc.)
- Rennen of verliezen = geen zoeken, direct door naar volgende locatie
- Combineert met Inventory Systeem en Meerdere Locaties

**Hint:** Voeg een nieuwe toestand "zoeken" toe

??? note "Spieken"
    ```python
    KNOP_ZOEKEN = Rect(250, 400, 150, 150)
    KNOP_DOORGAAN = Rect(400, 400, 150, 150)

    # Na gewonnen gevecht in on_mouse_down():
    if laatste_actie == "vechten" and resultaat_goed:
        toestand = "zoeken"
    else:
        toestand = "resultaat"
        clock.schedule(ga_naar_volgende, 2.5)

    # Nieuwe elif in on_mouse_down():
    elif toestand == "zoeken":
        if KNOP_ZOEKEN.collidepoint(pos):
            if random.randint(1, 2) == 1:
                item = random.choice(["medkit", "honkbalknuppel", "energie bar", "mes"])
                inventory.append(item)
                resultaat_tekst = f"Je vindt een {item}!"
            else:
                resultaat_tekst = "Je vindt niks..."
            toestand = "resultaat"
            clock.schedule(ga_naar_volgende, 2.0)
        elif KNOP_DOORGAAN.collidepoint(pos):
            ga_naar_volgende()

    # In draw() bij "zoeken":
    elif toestand == "zoeken":
        screen.blit("vechten_succes", (0, 0))
        screen.draw.text("Wil je het gebied doorzoeken?", center=(400, 80), fontsize=28, color="white")
        teken_knop_met_pulse("knop_zoeken", KNOP_ZOEKEN)
        teken_knop_met_pulse("knop_doorgaan", KNOP_DOORGAAN)
    ```

**Benodigde plaatjes:** `knop_zoeken.png`, `knop_doorgaan.png`
