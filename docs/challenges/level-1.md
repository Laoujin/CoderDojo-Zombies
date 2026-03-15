# Level 1 Challenges

## Opwarmer

### Eigen Verhaal

Verander alle teksten naar je eigen zombie verhaal

**Hint:** Pas de strings aan in de `print()` statements

??? note "Spieken"
    Geen code nodig - verander gewoon de tekst tussen aanhalingstekens!
    Bijvoorbeeld: `print("Een geest verschijnt...")`

---

## Pittig

### Verstoppen

Voeg een derde optie toe: "verstoppen"

**Hint:** Gebruik `elif actie == "verstoppen":`

??? note "Spieken"
    ```python
    elif actie == "verstoppen":
        print("Je verstopt je achter een auto...")
        kans = random.randint(1, 3)
        if kans == 1:
            print("De zombie ziet je niet! Je bent veilig.")
        else:
            print("De zombie ruikt je...")
    ```

---

## Boss

### Praten

Voeg een "praten" optie toe met je eigen logica

**Hint:** Maak een `elif actie == "praten":` en bedenk zelf wat er gebeurt. Misschien kan je de zombie overtuigen?

??? note "Spieken"
    ```python
    elif actie == "praten":
        print("Je probeert met de zombie te praten...")
        wat_zeg_je = input("Wat zeg je? (hallo / ga weg / ik ben ook een zombie) ")

        if wat_zeg_je == "hallo":
            print("De zombie gromt en valt aan!")
        elif wat_zeg_je == "ga weg":
            print("De zombie snapt je niet...")
        elif wat_zeg_je == "ik ben ook een zombie":
            print("De zombie gelooft je! Hij loopt door.")
        else:
            print("De zombie kijkt je raar aan...")
    ```
