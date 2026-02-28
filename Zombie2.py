import random
import time

levens = 3

print("🧟‍♂️💀 WELKOM BIJ ZOMBIE APOCALYPSE 💀🧟‍♂️")
print("Je hebt drie levens")
print()

while levens > 0:
    print("🌫️ Het is donker... je hoort gegrom...")
    time.sleep(1)
    print("🧟‍♂️ Er komt een zombie op je af!")
    print()

    actie = input("⚡ Wat doe je? (rennen / vechten) ➜ ")

    if actie == "rennen":
        print("🏃‍♂️ Je probeert weg te sprinten...")
        time.sleep(1)

        kans = random.randint(1, 2)
        if kans == 1:
            print("💨🔥 Je bent ontsnapt! Je hart bonkt in je keel...")
        else:
            print("😱 De zombie was sneller!")
            print("🩸 Hij grijpt je arm... Je verliest een leven")
            levens -= 1

    elif actie == "vechten":
        print("⚔️ Je maakt je klaar om te vechten...")
        time.sleep(1)

        kans = random.randint(1, 2)
        if kans == 1:
            print("💥🧟‍♂️ BOEM! Je verslaat de zombie als een held!")
        else:
            print("🧟‍♂️💢 De zombie bijt je...")
            levens -= 1

    else:
        print("🤦 Zombies twijfelen niet...")
        print("☠️ Je bent dood.")
        levens = 0

print()
print("🎬 THE END 🎬")