# Pygame Zero Recepten

Handige code patronen voor je spel!

---

## Meerdere plaatjes tonen (Inventory)

Toon een lijst van items op het scherm:

```python
inventory = ["medkit", "sword", "key"]

def draw():
    # Toon elk item naast elkaar
    for i, item in enumerate(inventory):
        x = 50 + (i * 60)  # 60 pixels tussen elk item
        screen.blit(f"inv_{item}", (x, 500))
```

---

## Gewogen random keuze (Zombie Types)

Sommige dingen vaker laten gebeuren dan andere:

```python
import random

# Zombie types met hun kans (hoe hoger, hoe vaker)
zombie_types = [
    ("baby", 40),      # 40% kans - makkelijk
    ("normal", 35),    # 35% kans
    ("fast", 15),      # 15% kans
    ("strong", 10),    # 10% kans - zeldzaam!
]

def kies_zombie():
    types = [z[0] for z in zombie_types]    # ["baby", "normal", ...]
    kansen = [z[1] for z in zombie_types]   # [40, 35, ...]
    return random.choices(types, weights=kansen)[0]

# Gebruik:
huidige_zombie = kies_zombie()  # Meestal "baby" of "normal"
```

---

## Vertraagde actie (Timer)

Wacht even voordat iets gebeurt:

```python
def zoek_item():
    screen.draw.text("Zoeken...", center=(400, 300))
    clock.schedule(toon_resultaat, 1.5)  # Wacht 1.5 seconden

def toon_resultaat():
    global gevonden_item
    if random.randint(1, 100) <= 50:
        gevonden_item = "medkit"
    else:
        gevonden_item = None
```

---

## Smooth beweging (Animate)

Laat iets vloeiend bewegen in plaats van direct:

```python
zombie = Actor("zombie", (100, 300))

def beweeg_zombie():
    # Beweeg naar x=600 in 2 seconden
    animate(zombie, x=600, duration=2)

def beweeg_met_effect():
    # Met "bounce" effect aan het einde
    animate(zombie, y=100, duration=1, tween='bounce_end')
```

**Tween effecten:** `'linear'`, `'accelerate'`, `'decelerate'`, `'bounce_end'`, `'elastic_end'`

---

## Fade effect (scherm overgang)

Maak een fade tussen schermen:

```python
fade_alpha = 0
fade_richting = 0  # 0=geen, 1=fade out, -1=fade in

def start_fade_out():
    global fade_alpha, fade_richting
    fade_alpha = 0
    fade_richting = 1

def update():
    global fade_alpha, fade_richting
    if fade_richting == 1:  # Fade out
        fade_alpha += 5
        if fade_alpha >= 255:
            fade_alpha = 255
            wissel_scherm()
            fade_richting = -1  # Start fade in
    elif fade_richting == -1:  # Fade in
        fade_alpha -= 5
        if fade_alpha <= 0:
            fade_alpha = 0
            fade_richting = 0

def draw():
    # Teken je spel hier...

    # Teken fade overlay
    if fade_alpha > 0:
        screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (0, 0, 0, fade_alpha))
```

---

## Hover effect (muis over knop)

Verander kleur als de muis over een knop gaat:

```python
KNOP = Rect(300, 400, 200, 60)

def draw():
    # Check of muis over knop is
    muis_pos = pygame.mouse.get_pos()
    if KNOP.collidepoint(muis_pos):
        kleur = "lightgreen"  # Hover kleur
    else:
        kleur = "green"       # Normale kleur

    screen.draw.filled_rect(KNOP, kleur)
    screen.draw.text("Klik mij!", center=KNOP.center)
```

---

## Scherm schudden (Hit effect)

Schud het scherm als je geraakt wordt:

```python
schud_offset = 0
schud_tijd = 0

def start_schudden():
    global schud_tijd
    schud_tijd = 10  # 10 frames schudden

def update():
    global schud_offset, schud_tijd
    if schud_tijd > 0:
        schud_offset = random.randint(-5, 5)
        schud_tijd -= 1
    else:
        schud_offset = 0

def draw():
    # Gebruik schud_offset voor alle tekeningen
    screen.blit("achtergrond", (schud_offset, 0))
    screen.blit("zombie", (400 + schud_offset, 300))
```

---

## Levens als hartjes

Toon levens als plaatjes in plaats van tekst:

```python
levens = 3
max_levens = 5

def draw():
    for i in range(max_levens):
        x = 20 + (i * 35)
        if i < levens:
            screen.blit("hart", (x, 20))       # Vol hartje
        else:
            screen.blit("hart_leeg", (x, 20))  # Leeg hartje
```

---

## Knipperende tekst

Laat tekst knipperen voor aandacht:

```python
knipper_timer = 0

def update():
    global knipper_timer
    knipper_timer += 1

def draw():
    # Toon tekst alleen als timer even is (elke 30 frames wisselen)
    if (knipper_timer // 30) % 2 == 0:
        screen.draw.text("DRUK OP SPATIE!", center=(400, 500), fontsize=28)
```

---

## Simpele animatie (sprite wissel)

Wissel tussen plaatjes voor animatie:

```python
zombie_frames = ["zombie_1", "zombie_2", "zombie_3", "zombie_2"]
frame_index = 0
frame_timer = 0

def update():
    global frame_index, frame_timer
    frame_timer += 1
    if frame_timer >= 10:  # Wissel elke 10 frames
        frame_timer = 0
        frame_index = (frame_index + 1) % len(zombie_frames)

def draw():
    screen.blit(zombie_frames[frame_index], (400, 300))
```

---

## Geluid met volume

Speel geluid af met aangepast volume:

```python
# Zacht geluid
sounds.hit.play()
sounds.hit.set_volume(0.3)  # 30% volume

# Achtergrond muziek (herhaalt automatisch)
music.play("spooky_music")
music.set_volume(0.5)
```

---

## Willekeurige positie op scherm

Spawn iets op een random plek:

```python
def random_positie():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    return (x, y)

# Gebruik:
zombie.pos = random_positie()
```

---

## Cooldown (wachttijd tussen acties)

Voorkom spam-klikken:

```python
cooldown = 0

def update():
    global cooldown
    if cooldown > 0:
        cooldown -= 1

def on_mouse_down(pos):
    global cooldown
    if cooldown == 0:
        # Doe de actie
        schiet()
        cooldown = 30  # Wacht 30 frames (0.5 seconde)
```
