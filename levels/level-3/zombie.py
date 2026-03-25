# =============================================================================
# ZOMBIE APOCALYPSE - Level 3
# =============================================================================
# Nieuw in dit level:
# - Lijsten (lists) voor inventory en zombie types
# - f-strings voor tekst met variabelen
# - Kortere schrijfwijze: += en -=
# - random.choice() om iets uit een lijst te kiezen
# - Meerdere voorwaarden met "and"
# =============================================================================

import os
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')

# =============================================================================
# LIJSTEN (LISTS)
# =============================================================================
# Een lijst is een verzameling van dingen, tussen [ en ]
# Je kunt er dingen aan toevoegen en uithalen
# =============================================================================

# Een lege lijst - hier stoppen we later gevonden items in
inventory = []

# Een lijst met teksten - de verschillende soorten zombies
zombie_types = ["normale zombie", "snelle zombie"]

levens = 3
ronde = 0

print("🧟‍♂️💀 WELKOM BIJ ZOMBIE APOCALYPSE 💀🧟‍♂️")
print("Overleef 5 rondes om te winnen!")
print()

# =============================================================================
# MEERDERE VOORWAARDEN MET "and"
# =============================================================================
# Je kunt voorwaarden combineren:
#   "and" = beide moeten waar zijn
#   "or"  = minstens één moet waar zijn
# =============================================================================

while levens > 0 and ronde < 5:
    # += is een kortere manier om te schrijven: ronde = ronde + 1
    ronde += 1

    # =========================================================================
    # F-STRINGS
    # =========================================================================
    # Een f-string begint met f voor de aanhalingstekens
    # Alles tussen { } wordt vervangen door de waarde van die variabele
    # f"Ronde {ronde}" wordt bijvoorbeeld "Ronde 3" als ronde 3 is
    # =========================================================================
    print(f"--- Ronde {ronde}/5 ---")
    print(f"❤️ Levens: {levens}")

    # "if inventory" checkt of de lijst NIET leeg is
    # Een lege lijst [] is "False", een lijst met items is "True"
    if inventory:
        print(f"🎒 Inventory: {inventory}")
    print()

    # random.choice() kiest een willekeurig item uit een lijst
    zombie = random.choice(zombie_types)

    print("🌫️ Het is donker... je hoort gegrom...")
    time.sleep(1)
    print(f"🧟‍♂️ Een {zombie} komt op je af!")
    print()

    actie = input("⚡ Wat doe je? (rennen / vechten / zoeken) ➜ ")

    if actie == "rennen":
        print("🏃‍♂️ Je probeert weg te sprinten...")
        time.sleep(1)

        if zombie == "snelle zombie":
            kans = random.randint(1, 3)  # 1 op 3 kans om te ontsnappen
        else:
            kans = random.randint(1, 2)  # 1 op 2 kans

        if kans == 1:
            print("💨 Je bent ontsnapt!")
        else:
            print("😱 De zombie was sneller!")
            # -= is korter voor: levens = levens - 1
            levens -= 1

    elif actie == "vechten":
        print("⚔️ Je maakt je klaar om te vechten...")
        time.sleep(1)

        kans = random.randint(1, 2)

        if kans == 1:
            print("💥 Je verslaat de zombie!")
        else:
            print("🧟‍♂️ De zombie bijt je...")
            levens -= 1

    elif actie == "zoeken":
        print("🔍 Je zoekt rond...")
        time.sleep(1)

        # =================================================================
        # CHECKEN OF IETS IN EEN LIJST ZIT
        # =================================================================
        # "item in lijst" geeft True als item in de lijst zit
        # "item not in lijst" geeft True als item NIET in de lijst zit
        # =================================================================

        if "honkbalknuppel" not in inventory:
            if random.randint(1, 2) == 1:
                print("⚔️ Je vindt een honkbalknuppel!")
                # .append() voegt iets toe aan het EINDE van een lijst
                inventory.append("honkbalknuppel")
            else:
                print("Je vindt niks bruikbaars...")
        else:
            if random.randint(1, 2) == 1:
                item = random.choice(["medkit", "zaklamp", "energie bar"])
                print(f"Je vindt een {item}!")
                inventory.append(item)
            else:
                print("Je vindt niks bruikbaars...")

    else:
        print("🤦 Zombies twijfelen niet...")
        levens = 0

    # Medkit gebruiken als je gewond bent
    if levens < 3 and "medkit" in inventory:
        gebruik = input("💊 Je hebt een medkit. Gebruiken? (ja/nee) ➜ ")
        if gebruik == "ja":
            # .remove() haalt het eerste item met die waarde uit de lijst
            inventory.remove("medkit")
            levens += 1
            print("❤️ +1 leven!")

    print()

print("🎬 THE END 🎬")

if ronde >= 5 and levens > 0:
    print("🏆 Je hebt alle 5 rondes overleefd! Je wint!")
else:
    print("💀 Game over...")
