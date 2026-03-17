# Level 5 Uitdagingen

## Opwarmer

### Score Teller

Voeg een score teller toe die omhoog gaat bij elke succesvolle actie.

- +10 punten voor een gewonnen gevecht
- +5 punten voor een succesvolle ontsnapping
- Score reset bij game over

**Hint:** Maak een `score` variabele en teken het met `screen.draw.text()`

---

### Verstoppen

Voeg een derde knop "Verstoppen" toe als extra actie.

- Nieuwe knop in het midden van het scherm
- 50/50 kans op succes/faal
- Succes: "De zombie ziet je niet!"
- Faal: "De zombie vindt je!"

**Hint:** Kopieer de rennen logica en pas de tekst aan. Benodigde plaatjes: `knop_verstoppen.png`, `verstoppen_succes.png`, `verstoppen_faal.png`

---

## Pittig

### Inventory Systeem

Voeg een inventory toe die items opslaat en het spel beinvloedt.

- Wapens (honkbalknuppel, mes): verhoog winkans van 50% naar 66%
- Healing (medkit, energie bar): medkit +2 levens, energie bar +1 leven
- Toon inventory op het scherm

**Hint:** Gebruik een lijst voor items en check met `if item in inventory:`

---

### Zombie Types

Verschillende zombies verschijnen met verschillende winkansen.

- Baby zombie: 66% winkans (makkelijk)
- Langzame zombie: 50% winkans
- Snelle zombie: 40% winkans
- Sterke zombie: 33% winkans (moeilijk)

**Hint:** Gebruik een dictionary met kansen per zombie type

---

## Boss

### Meerdere Locaties

Ga door 5 locaties heen om het spel te winnen.

- Locaties: Suburb → Library → School → Hospital → Mall
- Elke succesvolle actie brengt je naar de volgende locatie
- Falen kost een leven maar je gaat ook door
- Overleef alle 5 locaties = gewonnen!

**Hint:** Gebruik een lijst met locaties en een `locatie_index` variabele. Benodigde plaatjes: `achtergrond_suburb.png`, `achtergrond_library.png`, `achtergrond_school.png`, `achtergrond_hospital.png`, `achtergrond_mall.png`, `gewonnen.png`

---

### Zoeken na Gevecht

Win een gevecht om het gebied te doorzoeken voor items.

- Na een gewonnen gevecht verschijnt een "Zoeken" knop
- 50% kans om een item te vinden (medkit, wapen, etc.)
- Rennen of verliezen = geen zoeken, direct door naar volgende locatie
- Combineert met Inventory Systeem en Meerdere Locaties

**Hint:** Voeg een nieuwe toestand `"zoeken"` toe. Benodigde plaatjes: `knop_zoeken.png`, `knop_doorgaan.png`
