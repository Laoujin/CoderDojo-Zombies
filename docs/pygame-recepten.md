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

## Coole effecten

Maak je spel leuker met deze effecten! Allemaal gebruiken ze `tijd` voor animatie:

```python
import math
tijd = 0

def update(dt):
    global tijd
    tijd += dt
```

### Bounce (springen)

```python
def draw():
    bounce = abs(math.sin(tijd * 8)) * 15
    screen.blit("knop", (KNOP.x, KNOP.y - bounce))
```

### Shake (schudden)

```python
import random

def draw():
    offset_x = random.randint(-4, 4)
    offset_y = random.randint(-4, 4)
    screen.blit("knop", (KNOP.x + offset_x, KNOP.y + offset_y))
```

Voor scherm-schudden bij een hit:

```python
schud_tijd = 0

def start_schudden():
    global schud_tijd
    schud_tijd = 0.3  # 0.3 seconden

def update(dt):
    global schud_tijd
    if schud_tijd > 0:
        schud_tijd -= dt

def draw():
    if schud_tijd > 0:
        offset = random.randint(-5, 5)
    else:
        offset = 0
    screen.blit("achtergrond", (offset, 0))
```

### Spin (draaien)

```python
def draw():
    # Simuleer rotatie door breedte te veranderen
    spin = math.cos(tijd * 5)
    nieuwe_breedte = abs(spin) * KNOP.width
    x = KNOP.x + (KNOP.width - nieuwe_breedte) / 2
    nieuwe_rect = Rect(x, KNOP.y, nieuwe_breedte, KNOP.height)
    screen.draw.filled_rect(nieuwe_rect, "green")
```

### Rainbow (regenboog)

```python
def draw():
    r = int((math.sin(tijd * 3) + 1) * 127)
    g = int((math.sin(tijd * 3 + 2) + 1) * 127)
    b = int((math.sin(tijd * 3 + 4) + 1) * 127)
    screen.draw.filled_rect(KNOP, (r, g, b))
```

### Fade (vervagen)

```python
def draw():
    fade = (math.sin(tijd * 4) + 1) / 2  # 0 tot 1
    grijs = int(50 + fade * 200)
    screen.draw.filled_rect(KNOP, (grijs, grijs, grijs))
```

### Squash (pletten)

```python
def draw():
    squash = math.sin(tijd * 8)
    nieuwe_hoogte = KNOP.height + squash * 15
    nieuwe_breedte = KNOP.width - squash * 10
    x = KNOP.x + (KNOP.width - nieuwe_breedte) / 2
    y = KNOP.y + (KNOP.height - nieuwe_hoogte) / 2
    screen.draw.filled_rect(Rect(x, y, nieuwe_breedte, nieuwe_hoogte), "purple")
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
