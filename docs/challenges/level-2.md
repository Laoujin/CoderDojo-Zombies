# Level 2 Challenges

## Makkelijk

### Meer Levens

Verander het aantal levens naar 5

**Hint:** Zoek de regel `levens = 3` en pas het aan

??? note "Spieken"
    ```python
    levens = 5
    ```

---

### Game Over Bericht

Voeg een speciaal bericht toe als je dood gaat

**Hint:** Voeg code toe NA de while loop maar VOOR "THE END"

??? note "Spieken"
    ```python
    while levens > 0:
        # ... bestaande code ...

    if levens == 0:
        print("GAME OVER")
        print("De zombies hebben gewonnen...")

    print("THE END")
    ```

---

## Medium

### Wapen Zoeken

Voeg een "zoeken" actie toe om een wapen te vinden

**Hint:** Maak een variabele `heeft_wapen = False` aan het begin

??? note "Spieken"
    ```python
    heeft_wapen = False

    while levens > 0:
        # ... bestaande intro code ...

        actie = input("Wat doe je? (rennen / vechten / zoeken) ")

        if actie == "zoeken":
            if not heeft_wapen:
                print("Je zoekt rond...")
                print("Je vindt een honkbalknuppel!")
                heeft_wapen = True
            else:
                print("Je hebt al een wapen!")

        elif actie == "rennen":
            # ... bestaande code ...
    ```

---

### Wapen Bonus

Het wapen verhoogt je winkans bij vechten

**Hint:** Check `if heeft_wapen:` en pas de `random.randint()` aan

??? note "Spieken"
    ```python
    elif actie == "vechten":
        print("Je maakt je klaar om te vechten...")
        time.sleep(1)

        if heeft_wapen:
            print("Je zwaait met je honkbalknuppel!")
            kans = random.randint(1, 3)  # 2 van 3 kans om te winnen
        else:
            kans = random.randint(1, 2)  # 1 van 2 kans om te winnen

        if kans >= 2:
            print("Je verslaat de zombie!")
        else:
            print("De zombie bijt je...")
            levens -= 1
    ```

---

## Moeilijk

### Score Systeem

Voeg een score toe die omhoog gaat per overwonnen zombie

**Hint:** Maak `score = 0` aan het begin, en `score += 10` als je wint

??? note "Spieken"
    ```python
    levens = 3
    score = 0

    while levens > 0:
        print(f"Levens: {levens} | Score: {score}")

        # ... bestaande code ...

        # Bij winnen:
        if kans >= 2:
            print("Je verslaat de zombie!")
            score += 10

    print(f"Eindscore: {score}")
    ```
