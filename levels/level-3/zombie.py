import os
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')

# === VARIABELEN ===
levens = 3
inventory = []
zombie_types = ["langzame zombie", "snelle zombie", "sterke zombie"]
zombie_geluiden = ["GRAAAAAH!", "BRAAAAINS!", "UGHHHH...", "GRRRR!"]

print("🧟‍♂️💀 WELKOM BIJ ZOMBIE APOCALYPSE 💀🧟‍♂️")
print("Je hebt drie levens")
print()

# === GAME LOOP ===
while levens > 0:
    # Toon status
    print(f"❤️ Levens: {levens}")
    if inventory:
        print(f"🎒 Inventory: {inventory}")
    print()

    # Random zombie verschijnt
    zombie = random.choice(zombie_types)
    geluid = random.choice(zombie_geluiden)

    print("🌫️ Het is donker... je hoort gegrom...")
    time.sleep(1)
    print(f"🧟‍♂️ Een {zombie} komt op je af!")
    print(f"   '{geluid}'")
    print()

    actie = input("⚡ Wat doe je? (rennen / vechten / zoeken) ➜ ")

    if actie == "rennen":
        print("🏃‍♂️ Je probeert weg te sprinten...")
        time.sleep(1)

        # Snelle zombie is moeilijker te ontsnappen
        if zombie == "snelle zombie":
            kans = random.randint(1, 3)  # 1 op 3 kans
        else:
            kans = random.randint(1, 2)  # 1 op 2 kans

        if kans == 1:
            print("💨 Je bent ontsnapt!")
        else:
            print("😱 De zombie was sneller!")
            levens -= 1

    elif actie == "vechten":
        print("⚔️ Je maakt je klaar om te vechten...")
        time.sleep(1)

        # Check voor wapen in inventory
        heeft_wapen = "honkbalknuppel" in inventory

        # Sterke zombie is moeilijker te verslaan
        if zombie == "sterke zombie":
            if heeft_wapen:
                kans = random.randint(1, 2)  # 1 op 2 met wapen
            else:
                kans = random.randint(1, 4)  # 1 op 4 zonder
        else:
            if heeft_wapen:
                kans = random.randint(1, 3)  # 2 op 3 met wapen
            else:
                kans = random.randint(1, 2)  # 1 op 2 zonder

        if kans >= 2 or (kans == 1 and heeft_wapen):
            print("💥 Je verslaat de zombie!")
            # Zombie laat soms iets vallen
            if random.randint(1, 3) == 1:
                item = random.choice(["medkit", "zaklamp", "energie bar"])
                print(f"   De zombie liet een {item} vallen!")
                inventory.append(item)
        else:
            print("🧟‍♂️ De zombie bijt je...")
            levens -= 1

    elif actie == "zoeken":
        print("🔍 Je zoekt rond...")
        time.sleep(1)

        if "honkbalknuppel" not in inventory:
            if random.randint(1, 2) == 1:
                print("⚔️ Je vindt een honkbalknuppel!")
                inventory.append("honkbalknuppel")
            else:
                print("Je vindt niks bruikbaars...")
        else:
            # Zoek naar andere items
            if random.randint(1, 2) == 1:
                item = random.choice(["medkit", "zaklamp", "energie bar"])
                print(f"Je vindt een {item}!")
                inventory.append(item)
            else:
                print("Je vindt niks bruikbaars...")

    else:
        print("🤦 Zombies twijfelen niet...")
        levens = 0

    # Check voor medkit gebruik
    if levens < 3 and "medkit" in inventory:
        gebruik = input("💊 Je hebt een medkit. Gebruiken? (ja/nee) ➜ ")
        if gebruik == "ja":
            inventory.remove("medkit")
            levens += 1
            print("❤️ +1 leven!")

    print()

print("🎬 THE END 🎬")
if levens > 0:
    print("🏆 Je hebt overleefd!")
else:
    print("💀 Game over...")
