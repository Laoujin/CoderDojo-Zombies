import friendly
friendly.install()

import random
import time


# === FUNCTIES ===

def toon_status(levens, score, inventory):
    """Toon de huidige status van de speler."""
    print()
    print(f"❤️ Levens: {levens} | 🏆 Score: {score}")
    if inventory:
        print(f"🎒 Inventory: {inventory}")
    print()


def maak_zombie():
    """Maak een nieuwe zombie met random eigenschappen."""
    types = ["langzame zombie", "snelle zombie", "sterke zombie"]
    namen = ["Gerrit", "Jan", "Pansen", "Ransen", "Kansen"]
    geluiden = ["GRAAAAAH!", "BRAAAAINS!", "UGHHHH..."]

    return {
        "type": random.choice(types),
        "naam": random.choice(namen),
        "geluid": random.choice(geluiden)
    }


def toon_zombie(zombie):
    """Toon de zombie met spanning."""
    print("🌫️ Het is donker... je hoort gegrom...")
    time.sleep(1)
    print(f"🧟‍♂️ {zombie['naam']} de {zombie['type']} komt op je af!")
    print(f"   '{zombie['geluid']}'")


def bereken_winkans(zombie, heeft_wapen):
    """Bereken de kans om te winnen tegen deze zombie."""
    basis_kans = 2  # 1 op 2

    if zombie["type"] == "sterke zombie":
        basis_kans = 3  # moeilijker
    elif zombie["type"] == "langzame zombie":
        basis_kans = 2  # normaal

    if heeft_wapen:
        basis_kans = max(1, basis_kans - 1)  # makkelijker met wapen

    return basis_kans


def vecht(zombie, heeft_wapen):
    """
    Vecht tegen een zombie.
    Returns: True als je wint, False als je verliest.
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
    Returns: True als je ontsnapt, False als je gepakt wordt.
    """
    print("🏃‍♂️ Je probeert weg te sprinten...")
    time.sleep(1)

    if zombie["type"] == "snelle zombie":
        kans = random.randint(1, 3)  # moeilijker
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
    Returns: het gevonden item of None.
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


# === MAIN GAME ===

def main():
    levens = 3
    score = 0
    inventory = []

    print("🧟‍♂️💀 WELKOM BIJ ZOMBIE APOCALYPSE 💀🧟‍♂️")
    print("Type 'help' voor alle opties")

    while levens > 0:
        toon_status(levens, score, inventory)

        zombie = maak_zombie()
        toon_zombie(zombie)
        print()

        actie = input("⚡ Wat doe je? ➜ ").lower().strip()

        if actie == "help":
            toon_help()
            continue  # Sla de rest over, begin opnieuw

        elif actie == "rennen":
            if not ren_weg(zombie):
                levens -= 1

        elif actie == "vechten":
            heeft_wapen = "honkbalknuppel" in inventory
            if vecht(zombie, heeft_wapen):
                score += 10
                # Kans op drop
                if random.randint(1, 3) == 1:
                    item = random.choice(["medkit", "energie bar"])
                    print(f"   {zombie['naam']} liet een {item} vallen!")
                    inventory.append(item)
            else:
                levens -= 1

        elif actie == "zoeken":
            item = zoek_item(inventory)
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


# Start het spel
if __name__ == "__main__":
    main()
