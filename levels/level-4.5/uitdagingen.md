# Level 4.5 Uitdagingen

## Opwarmer

### Mis-klik

Voeg een straf toe als je naast de zombie klikt: -1 score en een geluid.

**Hint:** Voeg een `else:` toe aan de `if zombie.collidepoint(pos):` check

---

## Pittig

### Timer

Voeg een countdown timer toe van 30 seconden. Als de tijd op is, is het game over!

**Hint:** Maak een `tijd = 30` variabele en gebruik `update(dt)` om af te tellen. Teken de tijd met `screen.draw.text()`.

---

## Boss

### Meerdere Zombies

Laat 3 zombies tegelijk op het scherm verschijnen. Elke zombie die je klikt geeft een punt!

**Hint:** Maak een lijst `zombies = [Actor("zombie"), Actor("zombie"), Actor("zombie")]` en gebruik een `for` loop in `draw()` en `on_mouse_down()`
