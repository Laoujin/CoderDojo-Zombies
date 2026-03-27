# ☣ Referentiekaarten

Handige kaarten om naast je laptop te leggen terwijl je programmeert!

**Print ze uit** of bekijk ze op je scherm.

---

## Foutmeldingen — Ken Je Vijand!

Elke foutmelding is een zombie die je moet leren verslaan.
Hoe beter je ze kent, hoe sneller je ze uitschakelt!

<div class="zombie-grid" markdown>

<div class="zombie-card tier-hard" markdown>
<div class="zombie-card-img" markdown>
![De Verminkte Zombie](cards/syntax/output/error-syntax-error.png)
</div>

#### ☣ SyntaxError — De Verminkte Zombie

Python snapt je code niet! Er mist een `:` na if/while/def, aanhalingstekens `""` niet gesloten, of haakjes `()` vergeten.

**Versla hem:** Kijk naar het **einde van de regel** die Python aanwijst. Mis je een `:` of `"`? Check ook de regel **erboven**!
</div>

<div class="zombie-card tier-hard" markdown>
<div class="zombie-card-img" markdown>
![De Onzichtbare Zombie](cards/syntax/output/error-name-error.png)
</div>

#### ☣ NameError — De Onzichtbare Zombie

Python kent deze naam niet! Een variabele die niet bestaat, een typfout in de naam, of je bent vergeten hem aan te maken.

**Versla hem:** Check de **spelling** — `levens` is niet `Levens`. Is de variabele al aangemaakt **boven** deze regel?
</div>

<div class="zombie-card tier-medium" markdown>
<div class="zombie-card-img" markdown>
![De Dronken Zombie](cards/syntax/output/error-indentation-error.png)
</div>

#### ☣ IndentationError — De Dronken Zombie

Je code staat niet recht! Na `if`, `while`, of `def` moet de volgende regel inspringen met spaties.

**Versla hem:** Gebruik **4 spaties** (of Tab) na elke `:`. Meng nooit tabs en spaties! Kijk of alles **netjes onder elkaar** staat.
</div>

<div class="zombie-card tier-medium" markdown>
<div class="zombie-card-img" markdown>
![De Verwarde Zombie](cards/syntax/output/error-type-error.png)
</div>

#### ☣ TypeError — De Verwarde Zombie

Je mixt dingen die niet samen kunnen! Tekst en getallen optellen, of een functie verkeerd aanroepen.

**Versla hem:** Gebruik `str()` om een getal naar tekst om te zetten, of `int()` voor tekst naar getal. Check: `"Score: " + str(score)`
</div>

<div class="zombie-card tier-medium" markdown>
<div class="zombie-card-img" markdown>
![De Gulzige Zombie](cards/syntax/output/error-index-error.png)
</div>

#### ☣ IndexError — De Gulzige Zombie

Je grijpt naar iets dat er niet is! De lijst heeft minder items dan je denkt. Lijsten beginnen bij `0`, niet bij `1`!

**Versla hem:** Een lijst met 3 items heeft index `0`, `1`, `2`. Gebruik `len(lijst)` om te checken hoeveel items er zijn.
</div>

<div class="zombie-card tier-easy" markdown>
<div class="zombie-card-img" markdown>
![De Verdwaalde Zombie](cards/syntax/output/error-file-not-found-error.png)
</div>

#### ☣ FileNotFoundError — De Verdwaalde Zombie

Python kan het bestand niet vinden! Verkeerd pad, verkeerde naam, of het bestand bestaat nog niet.

**Versla hem:** Check de **bestandsnaam** en het **pad**. Staat het bestand in dezelfde map als je script? Tip: `open("scores.txt", "w")` maakt een nieuw bestand.
</div>

</div>

---

## Overlevingskaarten — Wat Heb Je Geleerd?

Elke level geeft je nieuwe krachten. Hier is je arsenaal!

<div class="zombie-grid" markdown>

<div class="zombie-card tier-easy" markdown>
<div class="zombie-card-img" markdown>
![Level 1](cards/syntax/output/recap-level-1.png)
</div>

#### Level 1 — Eerste Hulp Kit

| | Code | Wat doet het? |
|---|---|---|
| 🖨️ | `print()` | Tekst tonen |
| 🎤 | `input()` | Speler laten typen |
| 🔀 | `if / elif / else` | Keuzes maken |
| 🎲 | `random.randint()` | Willekeurig getal |
| ⏳ | `time.sleep()` | Even wachten |
| 📦 | `variabele = waarde` | Iets onthouden |
</div>

<div class="zombie-card tier-easy" markdown>
<div class="zombie-card-img" markdown>
![Level 2](cards/syntax/output/recap-level-2.png)
</div>

#### Level 2 — Overlevingsgids

| | Code | Wat doet het? |
|---|---|---|
| 🔄 | `while levens > 0:` | Herhalen tot klaar |
| 💔 | `levens = levens - 1` | Variabele aanpassen |
| ⚖️ | `> < == != >= <=` | Vergelijken |
| 🏁 | `while True / break` | Oneindige loop |
</div>

<div class="zombie-card tier-medium" markdown>
<div class="zombie-card-img" markdown>
![Level 3](cards/syntax/output/recap-level-3.png)
</div>

#### Level 3 — Wapenarsenaal

| | Code | Wat doet het? |
|---|---|---|
| 📋 | `lijst = [a, b, c]` | Lijst maken |
| ➕ | `lijst.append(x)` | Item toevoegen |
| ➖ | `lijst.remove(x)` | Item verwijderen |
| 🔍 | `if x in lijst:` | Zoeken in lijst |
| 🎯 | `random.choice(lijst)` | Willekeurig kiezen |
| ✨ | `f"Score: {score}"` | f-strings |
</div>

<div class="zombie-card tier-hard" markdown>
<div class="zombie-card-img" markdown>
![Level 4](cards/syntax/output/recap-level-4.png)
</div>

#### Level 4 — Commandocentrum

| | Code | Wat doet het? |
|---|---|---|
| ⚙️ | `def functie(x):` | Functies maken |
| 📖 | `{"naam": "waarde"}` | Dictionaries |
| 💾 | `open("bestand.txt")` | Bestanden lezen |
| 🛡️ | `try: ... except:` | Fouten opvangen |
| 🔢 | `return waarde` | Waarde teruggeven |
| 🏆 | `scores.txt` | Highscores opslaan |
</div>

</div>

---

## Printen

Download de kaarten als PDF:

- [☣ Foutmeldingen (PDF)](cards/syntax/output/errors.pdf)
- [Overlevingskaarten (PDF)](cards/syntax/output/recaps.pdf)
