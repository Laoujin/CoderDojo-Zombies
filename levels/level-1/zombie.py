# =============================================================================
# ZOMBIE APOCALYPSE - Level 1
# =============================================================================
# Dit is je eerste Python programma! We leren:
# - Tekst op het scherm zetten met print()
# - De speler iets laten typen met input()
# - Keuzes maken met if/elif/else
# - Willekeurige getallen met random
# =============================================================================

# "import" laadt extra functies die we nodig hebben
# os        = voor het leegmaken van het scherm
# random    = voor willekeurige getallen (zoals een dobbelsteen)
# time      = voor pauzes (wachten)
import os
import random
import time

# Dit maakt het scherm leeg zodat we fris beginnen
# 'cls' is voor Windows, 'clear' is voor Mac/Linux
os.system('cls' if os.name == 'nt' else 'clear')

# print() zet tekst op het scherm
# Alles tussen de aanhalingstekens "" wordt getoond
print("🧟‍♂️💀 WELKOM BIJ ZOMBIE APOCALYPSE 💀🧟‍♂️")
print()  # Lege regel

print("🌫️ Het is donker... je hoort gegrom...")

# time.sleep(1) wacht 1 seconde - dit maakt het spannender!
time.sleep(1)

print("🧟‍♂️ Er komt een zombie op je af!")
print()

# input() vraagt de speler om iets te typen
# Wat de speler typt wordt opgeslagen in de variabele "actie"
# Een variabele is zoals een doosje met een naam waar je iets in stopt
actie = input("⚡ Wat doe je? (rennen / vechten) ➜ ")

# if/elif/else = ALS/ANDERS ALS/ANDERS
# We checken wat de speler heeft getypt
# Let op: == betekent "is gelijk aan" (vergelijken)
#         =  betekent "maak gelijk aan" (opslaan)
#         De : op het einde is belangrijk!
if actie == "rennen":
    # Als de speler "rennen" typt, wordt alles
    # dat 4 spaties ingesprongen is uitgevoerd
    print("🏃‍♂️ Je probeert weg te sprinten...")
    time.sleep(1)

    # random.randint(1, 2) geeft een willekeurig getal: 1 of 2
    # Net als een muntworp: kop of munt
    kans = random.randint(1, 2)

    if kans == 1:
        # Een nieuwe if, dus we springen opnieuw 4 spaties in
        print("💨🔥 Je bent ontsnapt! Je hart bonkt in je keel...")
    else:
        print("😱 De zombie was sneller!")
        print("🩸 Hij grijpt je arm...")

elif actie == "vechten":
    # Dit gebeurt als de speler "vechten" typt
    print("⚔️ Je maakt je klaar om te vechten...")
    time.sleep(1)

    kans = random.randint(1, 2)

    if kans == 1:
        print("💥🧟‍♂️ BOEM! Je verslaat de zombie als een held!")
    else:
        print("🧟‍♂️💢 De zombie bijt je...")

else:
    # Dit gebeurt bij ALLES anders (niet rennen en niet vechten)
    print("🤦 Zombies twijfelen niet...")
    print("☠️ Je bent dood.")

print()
print("🎬 THE END 🎬")
