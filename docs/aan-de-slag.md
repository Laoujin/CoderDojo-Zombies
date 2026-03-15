# Aan de Slag

Volg deze stappen om te beginnen met programmeren.

## 1. Installeer Python

1. Ga naar [python.org/downloads/release/python-3129](https://www.python.org/downloads/release/python-3129/)
2. Download Python **3.12** (niet nieuwer - pygame werkt nog niet met 3.13+)
3. **Belangrijk:** Vink aan "Add Python to PATH" tijdens installatie!
4. Klik op "Install Now"
5. Check je versie: `python --version` moet `3.12.x` tonen

## 2. Installeer VS Code

1. Ga naar [code.visualstudio.com](https://code.visualstudio.com/)
2. Download en installeer VS Code
3. Open VS Code

## 3. Installeer Extensions

In VS Code:

1. Klik op het blokjes-icoon links (Extensions)
2. Zoek "Python" en installeer de extension van Microsoft
3. Zoek "Pylance" en installeer deze ook

## 4. Installeer Extra Packages

Open een terminal (in VS Code: Terminal → New Terminal) en typ:

```bash
pip install -r requirements.txt
```

## 5. Download de Code

1. [Download het project als ZIP](https://github.com/Laoujin/CoderDojo-Zombies/archive/refs/heads/master.zip)
2. Pak de ZIP uit
3. Open de folder in VS Code: File → Open Folder

## 6. Run je eerste programma

1. Open `levels/level-1/zombie.py`
2. Klik op de ▶️ knop rechtsboven
3. Het spel start in de terminal!

## Problemen?

### "python" wordt niet herkend

Python staat niet in je PATH. Installeer Python opnieuw en vink "Add to PATH" aan.

### Foutmelding in rood

Lees de foutmelding! `friendly-traceback` legt uit wat er mis is in begrijpelijke taal.

### Het spel start niet

Controleer of je in de juiste folder bent. Je moet `zombie.py` zien in de file explorer links.

## Klaar?

👉 Ga naar [Level 1](levels/level-1/uitleg.md) om te beginnen!
