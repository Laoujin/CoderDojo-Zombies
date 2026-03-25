# =============================================================================
# ZOMBIE APOCALYPSE - Level 2
# =============================================================================
# Nieuw in dit level:
# - while loops (herhalen zolang iets waar is)
# - Variabelen veranderen (levens = levens - 1)
# =============================================================================

import os
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')

# We maken een variabele "levens" en geven die de waarde 3
# Dit is een getal, geen tekst - dus geen aanhalingstekens
levens = 3

print("🧟‍♂️💀 WELKOM BIJ ZOMBIE APOCALYPSE 💀🧟‍♂️")
print("Je hebt drie levens")
print()

# =============================================================================
# WHILE LOOP
# =============================================================================
# Een while loop herhaalt code ZOLANG de voorwaarde waar is
# "while levens > 0" betekent: zolang levens groter is dan 0, blijf herhalen
#
# Vergelijkingen die je kunt gebruiken:
#   >   groter dan
#   <   kleiner dan
#   >=  groter dan of gelijk aan
#   <=  kleiner dan of gelijk aan
#   ==  gelijk aan
#   !=  niet gelijk aan
# =============================================================================

while levens > 0:
    # Alles wat INGESPRONGEN staat (met 4 spaties) hoort bij de while loop
    # Dit wordt steeds herhaald totdat levens 0 of minder is

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

            # We halen 1 af van levens
            levens = levens - 1

    elif actie == "vechten":
        print("⚔️ Je maakt je klaar om te vechten...")
        time.sleep(1)

        kans = random.randint(1, 2)
        if kans == 1:
            print("💥🧟‍♂️ BOEM! Je verslaat de zombie als een held!")
        else:
            print("🧟‍♂️💢 De zombie bijt je...")
            levens = levens - 1

    else:
        print("🤦 Zombies twijfelen niet...")
        print("☠️ Je bent dood.")
        # We zetten levens op 0 zodat de while loop stopt
        levens = 0

# Dit staat NIET ingesprongen, dus het hoort niet meer bij de while loop
# Dit wordt pas uitgevoerd als de loop stopt (levens is 0 of minder)
print()
print("🎬 THE END 🎬")
