# =============================================================================
# ZOMBIE APOCALYPSE - Level 4
# =============================================================================
# Nieuw in dit level:
# - Functies (def) om code te organiseren en herbruiken
# - Dictionaries (woordenboeken) voor zombie eigenschappen
# =============================================================================

import os
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')


# =============================================================================
# FUNCTIES
# =============================================================================
# Een functie is een blok code met een naam die je kunt hergebruiken
# Je maakt een functie met "def naam():"
# Je roept een functie aan met "naam()"
#
# Functies kunnen PARAMETERS hebben (input) en iets RETURNEN (output)
# =============================================================================
def toon_status(levens, score, inventory):
    """
    Toon de huidige status van de speler.

    Dit is een "docstring" - uitleg wat de functie doet.
    Deze functie heeft 3 parameters: levens, score en inventory.
    """
    print()
    print(f"❤️ Levens: {levens} | 🏆 Score: {score}")
    if inventory:
        print(f"🎒 Inventory: {inventory}")
    print()


def maak_zombie():
    """
    Maak een nieuwe zombie met random eigenschappen.

    Returns: een dictionary met zombie info
    """

    types = ["langzame zombie", "snelle zombie", "sterke zombie"]
    namen = ["Zombert", "Kreunald", "Rottie", "Stumpertje"]
    geluiden = ["GRAAAAAH!", "BRAAAAINS!", "UGHHHH..."]

    # =========================================================================
    # DICTIONARIES (WOORDENBOEKEN)
    # =========================================================================
    # Een dictionary slaat data op met "sleutel: waarde" paren
    # Je maakt ze met { } en haalt waardes op met ["sleutel"]
    #
    # Bijvoorbeeld: zombie["naam"] geeft de naam van de zombie
    # =========================================================================
    # "return" geeft een waarde terug aan de code die de functie aanriep
    return {
        "type": random.choice(types),
        "naam": random.choice(namen),
        "geluid": random.choice(geluiden)
    }


def toon_zombie(zombie):
    """Toon de zombie met spanning."""
    print("🌫️ Het is donker... je hoort gegrom...")
    time.sleep(1)

    # zombie['naam'] haalt de waarde op die bij sleutel 'naam' hoort
    print(f"🧟‍♂️ {zombie['naam']} de {zombie['type']} komt op je af!")
    print(f"   '{zombie['geluid']}'")


def bereken_winkans(zombie, heeft_wapen):
    """
    Bereken de kans om te winnen tegen deze zombie.

    Parameters:
        zombie: dictionary met zombie info
        heeft_wapen: True of False

    Returns: een getal (hoe hoger, hoe moeilijker)
    """
    basis_kans = 2  # 1 op 2

    if zombie["type"] == "sterke zombie":
        basis_kans = 3  # moeilijker
    elif zombie["type"] == "langzame zombie":
        basis_kans = 2  # normaal

    if heeft_wapen:
        # max() geeft de hoogste waarde
        # We willen niet lager dan 1 (altijd kans om te verliezen)
        basis_kans = max(1, basis_kans - 1)

    return basis_kans


def vecht(zombie, heeft_wapen):
    """
    Vecht tegen een zombie.

    Returns: True als je wint, False als je verliest
    """
    print("⚔️ Je maakt je klaar om te vechten...")
    if heeft_wapen:
        print("   Je zwaait met je wapen!")
    time.sleep(1)

    moeilijkheid = bereken_winkans(zombie, heeft_wapen)
    kans = random.randint(1, moeilijkheid)

    if kans == 1:
        print(f"💥 Je verslaat {zombie['naam']}!")
        return True
    else:
        print(f"🧟‍♂️ {zombie['naam']} bijt je...")
        return False


def ren_weg(zombie):
    """
    Probeer weg te rennen.

    Returns: True als je ontsnapt, False als je gepakt wordt
    """
    print("🏃‍♂️ Je probeert weg te sprinten...")
    time.sleep(1)

    if zombie["type"] == "snelle zombie":
        kans = random.randint(1, 3)
    else:
        kans = random.randint(1, 2)

    if kans == 1:
        print("💨 Je bent ontsnapt!")
        return True
    else:
        print("😱 De zombie was sneller!")
        return False


def zoek_item(inventory):
    """
    Zoek naar items.

    Returns: het gevonden item of None (niks)
    """
    print("🔍 Je zoekt rond...")
    time.sleep(1)

    mogelijke_items = ["honkbalknuppel", "medkit", "zaklamp", "energie bar"]

    if random.randint(1, 2) == 1:
        item = random.choice(mogelijke_items)
        print(f"✨ Je vindt een {item}!")
        return item
    else:
        print("Je vindt niks bruikbaars...")
        # None betekent "niks" of "geen waarde"
        return None


def toon_help():
    """Toon alle beschikbare acties."""
    print()
    print("=== HELP ===")
    print("rennen  - Probeer te ontsnappen (makkelijker bij langzame zombies)")
    print("vechten - Vecht tegen de zombie (beter met wapen)")
    print("zoeken  - Zoek naar items")
    print("help    - Toon dit menu")
    print("=============")
    print()



# =============================================================================
# MAIN FUNCTIE
# =============================================================================
# Dit is het startpunt van de game
# =============================================================================
def main():
    levens = 3
    score = 0
    inventory = []

    print("🧟‍♂️💀 WELKOM BIJ ZOMBIE APOCALYPSE 💀🧟‍♂️")
    toon_highscores()
    print()

    # .strip() haalt spaties weg, "or" geeft alternatief als leeg
    naam = input("Wat is je naam? ➜ ").strip() or "Anoniem"
    print(f"Welkom {naam}! Type 'help' voor alle opties")

    while levens > 0:
        toon_status(levens, score, inventory)

        zombie = maak_zombie()
        toon_zombie(zombie)
        print()

        # .lower() maakt alles kleine letters, .strip() haalt spaties weg
        actie = input("⚡ Wat doe je? ➜ ").lower().strip()

        if actie == "help":
            toon_help()
            # "continue" slaat de rest van de loop over en begint opnieuw
            continue

        elif actie == "rennen":
            if not ren_weg(zombie):
                levens -= 1

        elif actie == "vechten":
            heeft_wapen = "honkbalknuppel" in inventory
            if vecht(zombie, heeft_wapen):
                score += 10
                if random.randint(1, 3) == 1:
                    item = random.choice(["medkit", "energie bar"])
                    print(f"   {zombie['naam']} liet een {item} vallen!")
                    inventory.append(item)
            else:
                levens -= 1

        elif actie == "zoeken":
            item = zoek_item(inventory)
            # None is "niks", alles anders is een item
            if item:
                inventory.append(item)

        else:
            print("🤷 Dat snap ik niet. Type 'help' voor opties.")

        # Medkit gebruiken?
        if levens < 3 and "medkit" in inventory:
            gebruik = input("💊 Medkit gebruiken? (ja/nee) ➜ ").lower()
            if gebruik == "ja":
                inventory.remove("medkit")
                levens += 1
                print("❤️ +1 leven!")

    # Game over
    print()
    print("🎬 THE END 🎬")
    print(f"🏆 Eindscore: {score}")
    if score >= 50:
        print("🌟 GEWELDIG! Je bent een echte zombie-jager!")
    elif score >= 20:
        print("👍 Goed gedaan!")
    else:
        print("💀 Probeer het nog eens...")

    sla_score_op(naam, score)
    print(f"Score opgeslagen voor {naam}!")
    toon_highscores()



# =============================================================================
# =                                DANGER ZONE                                =
# =============================================================================
# LET OP: De code hieronder is wat geavanceerder!!
#
# We gaan met bestanden werken en foutafhandeling voor de highscores
# Je kan deze code gebruiken als inspiratie voor wanneer je zelf dingen wil
# bewaren en/of die je bij opnieuw spelen wil herstellen
#
# Bijvoorbeeld:
# Je kan een bestand bewaren met "levens = 3" om zo het aantal start levens
# configureerbaar te maken!
# =============================================================================




# =============================================================================
# BESTANDEN LEZEN EN SCHRIJVEN
# =============================================================================
# Met open() kun je bestanden openen om te lezen of schrijven
# "r" = read (lezen), "w" = write (schrijven), "a" = append (toevoegen)
#
# "with open() as f:" zorgt dat het bestand netjes gesloten wordt
# =============================================================================
def laad_highscores():
    """Laad highscores uit bestand."""

    # =========================================================================
    # TRY/EXCEPT
    # =========================================================================
    # Soms kan code fout gaan (bijv. bestand bestaat niet)
    # Met try/except kun je fouten opvangen zonder dat het programma crasht
    #
    # try:
    #     code die fout kan gaan
    # except SoortFout:
    #     wat te doen als die fout gebeurt
    # =========================================================================
    try:
        with open("highscores.txt", "r") as f:
            # Nieuw lijst met de highscores
            scores = []

            # f is het bestand, we lezen elke regel
            # Een regel is bewaard als "naam,score"
            # Bijvoorbeeld: "Jan,150"
            for line in f:
                if "," in line:
                    # .strip() haalt spaties en enters weg
                    # .split(",") splitst tekst op de komma
                    naam, score = line.strip().split(",")

                    # int() maakt van tekst een getal
                    # De scores is een lijst van tuples (naam, score)
                    scores.append((naam, int(score)))

            # Let op het level van inspringen van de return:
            # Je wil de scores NA de "for line in f:" loop returnen
            return scores
    except FileNotFoundError:
        # Bestand bestaat nog niet, geef lege lijst terug
        return []


def sla_score_op(naam, score):
    """Sla een score op in het bestand."""

    # "a" = append, voegt toe aan het einde (maakt bestand aan als nodig)
    with open("highscores.txt", "a") as f:
        # .write() schrijft tekst naar het bestand
        # \n is een nieuwe regel (enter)
        f.write(f"{naam},{score}\n")


def toon_highscores():
    """Toon de top 5 highscores."""

    scores = laad_highscores()
    if not scores:
        print("Nog geen highscores!")
        return

    # =========================================================================
    # SORTEREN MET KEY EN LAMBDA
    # =========================================================================
    # .sort() sorteert een lijst
    # key= zegt HOE te sorteren
    # lambda x: x[1] is een mini-functie die het 2e element pakt (de score)
    # lambda x: x[0] zou sorteren op de naam van de speler
    # reverse=True sorteert van hoog naar laag
    # =========================================================================
    scores.sort(key=lambda x: x[1], reverse=True)

    print()
    print("=== HIGHSCORES ===")
    # enumerate() geeft een teller mee, we beginnen bij 1
    # "i" krijgt daardoor eerst de waarde 1, daarna de waarde 2 etc
    # [:5] pakt alleen de eerste 5 items (slicing)
    # (naam, score) gaat de score tuple unpacken waarbij naam de eerste waarde krijgt en score de tweede waarde
    for i, (naam, score) in enumerate(scores[:5], 1):
        print(f"  {i}. {naam}: {score}")

    # Deze code zou ook op deze manier kunnen geschreven worden:
    # for i, score in enumerate(scores[:5], 1):
    #     print(f"  {i}. {score[0]}: {score[1]}")

    # Of op deze manier
    # teller = 1
    # for score in scores[:5]:
    #     print(f"  {teller}. {score[0]}: {score[1]}")
    #     teller += 1

    # Of op deze manier
    # teller = 1
    # for (naam, score) in scores:
    #     if teller < 6:
    #         print(f"  {teller}. {naam}: {score}")
    #     teller += 1

    print("==================")


# =============================================================================
# IF __NAME__ == "__MAIN__"
# =============================================================================
# Deze check zorgt dat main() alleen draait als je DIT bestand start
# Als iemand dit bestand importeert in een ander programma, draait main() niet
# Dit is een standaard patroon in Python
# Op zich is het hier niet zo belangrijk...
# =============================================================================
if __name__ == "__main__":
    main()
