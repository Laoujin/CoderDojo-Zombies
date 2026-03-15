import friendly_traceback
friendly_traceback.install()

import os
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')

print("🧟‍♂️💀 WELKOM BIJ ZOMBIE APOCALYPSE 💀🧟‍♂️")
print()

print("🌫️ Het is donker... je hoort gegrom...")
time.sleep(1)
print("🧟‍♂️ Er komt een zombie op je af!")
print()

actie = input("⚡ Wat doe je? (rennen / vechten) ➜ ")

if actie == "rennen"
    print("🏃‍♂️ Je probeert weg te sprinten...")
    time.sleep(1)

    kans = random.randint(1, 2)
    if kans == 1:
        print("💨🔥 Je bent ontsnapt! Je hart bonkt in je keel...")
    else:
        print("😱 De zombie was sneller!")
        print("🩸 Hij grijpt je arm...")

elif actie == "vechten":
    print("⚔️ Je maakt je klaar om te vechten...")
    time.sleep(1)

    kans = random.randint(1, 2)
    if kans == 1:
        print("💥🧟‍♂️ BOEM! Je verslaat de zombie als een held!")
    else:
        print("🧟‍♂️💢 De zombie bijt je...")

else:
    print("🤦 Zombies twijfelen niet...")
    print("☠️ Je bent dood.")

print()
print("🎬 THE END 🎬")
