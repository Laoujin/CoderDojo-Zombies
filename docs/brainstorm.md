# Brainstorm

!!! warning "Level 6: Bouw Je Eigen Spel!"
    Dit is **Level 6** - de ultieme uitdaging!

    Gebruik alles wat je geleerd hebt in Level 1-5 om een slimmer zombie spel te maken waar de stats van elke zombie ertoe doen!

    - Begin met een [Starter Kit](levels/level-6/uitleg.md)
    - Bekijk de [Zombiepedia](zombiepedia.md) voor alle zombies en hun stats

## De Uitdaging

Maak een spel waar je **tactisch** moet nadenken:

- **Snelle zombie?** → Rennen werkt niet!
- **Slimme zombie?** → Verstoppen werkt niet!
- **Sterke zombie?** → Vechten zonder wapen werkt niet!

Kies het juiste wapen, de juiste actie, en overleef!

<div class="grid cards" markdown>

-   :material-sword:{ .lg .middle } **Wapens Systeem**

    ---

    Verschillende wapens werken beter tegen bepaalde zombies

-   :material-head-question:{ .lg .middle } **Slimme AI**

    ---

    Gebruik de stats om kansen te berekenen

-   :material-treasure-chest:{ .lg .middle } **Inventory**

    ---

    Verzamel items en kies wanneer je ze gebruikt

-   :material-map-marker-path:{ .lg .middle } **Meerdere Locaties**

    ---

    Elke locatie heeft andere zombie types

</div>

---

## Hoe Bouw Je Level 6?

!!! tip "Start Simpel"
    Begin met een **basis versie** en voeg stap voor stap features toe:

    1. **Stap 1:** Maak een dictionary met zombie stats
    2. **Stap 2:** Laat de actie-kans afhangen van de stats
    3. **Stap 3:** Voeg wapens toe die de kansen veranderen
    4. **Stap 4:** Maak het visueel met Pygame Zero

!!! example "Voorbeeld: Zombie Stats"
    ```python
    zombies = {
        "Baby Zombie": {"snelheid": 2, "slimheid": 1, "kracht": 1},
        "Ninja Zombie": {"snelheid": 5, "slimheid": 4, "kracht": 3},
        "Tank Zombie": {"snelheid": 1, "slimheid": 1, "kracht": 5},
    }
    ```

!!! example "Voorbeeld: Slimme Kansen"
    ```python
    def bereken_kans(zombie, actie, wapen):
        stats = zombies[zombie]

        if actie == "rennen":
            # Snelle zombies zijn moeilijk te ontlopen
            kans = 5 - stats["snelheid"]
        elif actie == "verstoppen":
            # Slimme zombies vinden je
            kans = 5 - stats["slimheid"]
        elif actie == "vechten":
            # Sterke zombies zijn moeilijk te verslaan
            kans = 5 - stats["kracht"]
            if wapen:
                kans += 2  # Wapen geeft bonus!

        return random.randint(1, 5) <= kans
    ```

!!! warning "De Regels"
    - **Hoge Snelheid?** → Rennen werkt NIET
    - **Hoge Slimheid?** → Verstoppen werkt NIET
    - **Hoge Kracht?** → Vechten werkt NIET (zonder wapen)

    Combineer je wapen met de zwakte van de zombie voor de beste kans!

---

## Inspiratie: Extra Game Mechanics

Kies de features die jij cool vindt en bouw ze in jouw spel!

### Stamina Systeem

Je kunt niet eeuwig blijven rennen!

- `stamina = 3` aan het begin
- Rennen kost 1 stamina
- Bij 0 stamina: "Je bent te moe om te rennen!"
- Rusten = stamina terug (maar kost een beurt)
- Visueel: `⚡⚡⚡` of `⚡⚡○`

### Geluidsmeter

Maak te veel lawaai en verstoppen werkt niet meer!

- `geluid = 0` (stil) tot `5` (LUID)
- Rennen: +2 geluid
- Vechten: +3 geluid
- Verstoppen: -1 geluid
- Hoog geluid = zombie vindt je makkelijker
- Visueel: `🔊🔊🔊○○`

### Vallen Plaatsen

Plaats vallen om zombies te vertragen of te vangen!

- Touw Val — zombie zit vast (skip beurt)
- Bananen Schil — zombie valt (bonus aanval)
- Spijker Plank — zombie neemt schade
- Val plaatsen kost een beurt
- Val werkt maar één keer

### Random Events

Onverwachte gebeurtenissen maken het spel spannender!

- "Je vindt een verborgen wapen!"
- "Je struikelt over een steen!" (-1 stamina)
- "Je telefoon gaat af!" (+3 geluid)
- "Je vindt een blikje eten!" (+1 HP)
- "Het begint te regenen..." (zombies trager)
- "Je zaklamp batterij is leeg!"
- "Een extra zombie verschijnt!"
- "De zombie valt even in slaap..." (gratis beurt)
- 30% kans per beurt op een event

### Weer Effecten

Het weer beïnvloedt het spel!

- **Regen** — rennen trager, geluid gedempt
- **Mist** — verstoppen makkelijker
- **Nacht** — zombies sterker, zaklamp nodig
- **Storm** — random events vaker
- Weer verandert elke X beurten

### Dag/Nacht Cyclus

's Nachts wordt het gevaarlijker!

- Dag: normale stats
- Schemering: zombies +1 snelheid
- Nacht: zombies +1 op alles, verstoppen moeilijker
- Zaklamp werkt alleen 's nachts

### Crafting Systeem

Combineer items tot betere items!

- Stok + Spijkers = Spijkerknuppel
- Fles + Doek + Aansteker = Molotov
- Verband + Alcohol = Medkit
- Recepten ontdekken door te experimenteren

### Locaties

Elke plek heeft eigen zombies en items!

- **School** — Leraar, Gamer zombie + boeken, potloden
- **Supermarkt** — Chef zombie + eten, blikken
- **Ziekenhuis** — Tandarts zombie + medkits, verband
- **Pretpark** — Clown zombie + speelgoed, ballonnen
- **Politiebureau** — Tank zombie + wapens, radio
- Kies waar je heen gaat, elke locatie heeft risico's en beloningen

### Hordes

Meerdere zombies tegelijk!

- Normale ronde: 1 zombie
- Horde ronde: 2-4 zombies tegelijk
- Elke actie raakt maar 1 zombie
- Vallen en wapens met "splash" raken meerdere
- Overleef de horde voor bonus items

### Boss Fights

Speciale zombies met fases!

- Boss heeft meerdere HP (bijv. 3 hits nodig)
- Bij 50% HP: "De zombie wordt BOOS!" (stats omhoog)
- Speciale aanval patronen
- Versla de boss = unlock geheime zombie

### Survivors (NPCs)

Red andere mensen!

- Vind survivors in locaties
- Keuze: help ze of negeer ze
- Geredde survivors helpen later:
    - Extra aanval per beurt
    - Delen items met je
    - Waarschuwen voor gevaar

### Achievements

Verdien badges voor speciale acties!

- "Ninja" — Versla 5 zombies zonder gezien te worden
- "Tank" — Overleef 10 gevechten op rij
- "Verzamelaar" — Vind alle wapens
- "Geluidloos" — Win zonder geluid te maken
- "Survivor" — Eindig met 1 HP

### Highscores

Sla je beste scores op!

- Gebruik File I/O uit Level 4
- `highscores.txt` met naam + score
- Toon top 5 bij game over
- Score = zombies verslagen × overgebleven HP

### Critical Hits

Kleine kans op instant win!

- 10% kans op "CRITICAL HIT!"
- Verslaat elke zombie in één klap
- Sommige wapens hebben hogere crit kans
- Visueel: extra vet of kleur

### Armor/Bescherming

Verminder schade!

- Helm: -1 schade van aanvallen
- Vest: 50% kans om schade te negeren
- Schild: blokkeer 1 aanval volledig (breekt daarna)
- Armor vinden in locaties

### Hunger/Dorst

Je moet eten en drinken!

- `honger = 10` aan het begin
- Elke beurt: -1 honger
- Bij 0 honger: -1 HP per beurt
- Eten vinden herstelt honger
- Extra tactiek: wanneer zoek je eten vs wanneer vecht je?

### Munitie

Wapens hebben beperkte kogels!

- Pistool: 6 kogels
- Shotgun: 2 kogels (maar sterker)
- Geen kogels = wapen is nutteloos
- Kogels vinden is zeldzaam

### New Game+

Tweede playthrough is moeilijker!

- Na winnen: "New Game+ unlocked!"
- Alle zombies +1 op stats
- Maar je houdt één item/wapen
- Hoe ver kom je?

### Easter Eggs

Geheime verrassingen!

- Typ "konami" = gratis wapen
- Vind de geheime kamer
- Bepaalde zombie + wapen combo = grappige tekst
- Verborgen achievement voor ontdekken
