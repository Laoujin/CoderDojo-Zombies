#!/usr/bin/env python3
"""
Generate syntax reference cards (error zombies + level recaps).

Usage:
    python docs/cards/syntax/generate.py [--errors] [--recaps] [--html]

Modes:
    Default: Uses Playwright to render PNG + PDF (needs: pip install playwright && playwright install chromium)
    --html:  Generates a single HTML file you can open in a browser and print/screenshot

Background images:
    Place images in docs/cards/syntax/ with matching filenames.
    Example: docs/cards/syntax/syntax-error.png

Output:
    Cards are saved to docs/cards/syntax/output/
"""

import asyncio
import base64
from pathlib import Path
from dataclasses import dataclass


# ─── Error Cards Data ────────────────────────────────────────────────

@dataclass
class ErrorCard:
    slug: str
    error_type: str      # Python error class name
    title: str           # Zombie name
    danger: str          # Danger level label
    description: str     # What causes this error
    fix: str             # How to fix it

ERROR_CARDS = [
    ErrorCard(
        slug="syntax-error",
        error_type="SyntaxError",
        title="De Verminkte Zombie",
        danger="Gevaarlijk",
        description="Python snapt je code niet! Er mist iets: een <code>:</code> na if/while/def, aanhalingstekens <code>\"\"</code> niet gesloten, of haakjes <code>()</code> vergeten.",
        fix="Kijk naar het <b>einde van de regel</b> die Python aanwijst. Mis je een <code>:</code> of <code>\"</code>? Check ook de regel <b>erboven</b>!",
    ),
    ErrorCard(
        slug="name-error",
        error_type="NameError",
        title="De Onzichtbare Zombie",
        danger="Verraderlijk",
        description="Python kent deze naam niet! Een variabele die niet bestaat, een typfout in de naam, of je bent vergeten hem aan te maken.",
        fix="Check de <b>spelling</b> — <code>levens</code> is niet <code>Levens</code>. Is de variabele al aangemaakt <b>boven</b> deze regel?",
    ),
    ErrorCard(
        slug="indentation-error",
        error_type="IndentationError",
        title="De Dronken Zombie",
        danger="Sluipend",
        description="Je code staat niet recht! Na <code>if</code>, <code>while</code>, of <code>def</code> moet de volgende regel inspringen met spaties.",
        fix="Gebruik <b>4 spaties</b> (of Tab) na elke <code>:</code>. Meng nooit tabs en spaties! Kijk of alles <b>netjes onder elkaar</b> staat.",
    ),
    ErrorCard(
        slug="type-error",
        error_type="TypeError",
        title="De Verwarde Zombie",
        danger="Verwarrend",
        description="Je mixt dingen die niet samen kunnen! Tekst en getallen optellen, of een functie verkeerd aanroepen.",
        fix="Gebruik <code>str()</code> om een getal naar tekst om te zetten, of <code>int()</code> voor tekst naar getal. Check: <code>\"Score: \" + str(score)</code>",
    ),
    ErrorCard(
        slug="index-error",
        error_type="IndexError",
        title="De Gulzige Zombie",
        danger="Hebberig",
        description="Je grijpt naar iets dat er niet is! De lijst heeft minder items dan je denkt. Lijsten beginnen bij <code>0</code>, niet bij <code>1</code>!",
        fix="Een lijst met 3 items heeft index <code>0</code>, <code>1</code>, <code>2</code>. Gebruik <code>len(lijst)</code> om te checken hoeveel items er zijn.",
    ),
    ErrorCard(
        slug="file-not-found-error",
        error_type="FileNotFoundError",
        title="De Verdwaalde Zombie",
        danger="Misleidend",
        description="Python kan het bestand niet vinden! Verkeerd pad, verkeerde naam, of het bestand bestaat nog niet.",
        fix="Check de <b>bestandsnaam</b> en het <b>pad</b>. Staat het bestand in dezelfde map als je script? Tip: <code>open(\"scores.txt\", \"w\")</code> maakt een nieuw bestand.",
    ),
]


# ─── Level Recap Cards Data ──────────────────────────────────────────

@dataclass
class RecapCard:
    slug: str
    level: int
    title: str
    theme: str
    powers: list  # list of (icon, code, label) tuples

RECAP_CARDS = [
    RecapCard(
        slug="level-1-recap",
        level=1,
        title="Eerste Hulp Kit",
        theme="Overlevingskaart",
        powers=[
            ("🖨️", "print()", "Tekst tonen"),
            ("🎤", "input()", "Speler laten typen"),
            ("🔀", "if / elif / else", "Keuzes maken"),
            ("🎲", "random.randint()", "Willekeurig getal"),
            ("⏳", "time.sleep()", "Even wachten"),
            ("⚠️", "= opslaan, == vergelijken", "Pas op!"),
        ],
    ),
    RecapCard(
        slug="level-2-recap",
        level=2,
        title="Overlevingsgids",
        theme="Overlevingskaart",
        powers=[
            ("🔄", "while levens > 0:", "Herhalen tot klaar"),
            ("💔", "levens = levens - 1", "Variabele aanpassen"),
            ("⚖️", "> < == != >= <=", "Vergelijken"),
            ("🛑", "levens = 0", "Loop stoppen"),
        ],
    ),
    RecapCard(
        slug="level-3-recap",
        level=3,
        title="Wapenarsenaal",
        theme="Overlevingskaart",
        powers=[
            ("📋", "lijst = [a, b, c]", "Lijst maken"),
            ("➕", "lijst.append(x)", "Item toevoegen"),
            ("➖", "lijst.remove(x)", "Item verwijderen"),
            ("🔍", "if x in lijst:", "Zoeken in lijst"),
            ("🎯", "random.choice(lijst)", "Willekeurig kiezen"),
            ("✨", 'f"Score: {score}"', "f-strings"),
        ],
    ),
    RecapCard(
        slug="level-4-recap",
        level=4,
        title="Commandocentrum",
        theme="Overlevingskaart",
        powers=[
            ("⚙️", "def functie(x):", "Functies maken"),
            ("🔢", "return waarde", "Waarde teruggeven"),
            ("📖", '{\"naam\": \"waarde\"}', "Dictionaries"),
            ("🔑", 'zombie[\"naam\"]', "Waarde opvragen"),
            ("🧹", ".lower() .strip()", "Tekst opschonen"),
            ("🚫", "None", "Niks / geen waarde"),
        ],
    ),
]


# ─── Card Rendering ──────────────────────────────────────────────────

def load_background(image_path: Path | None) -> str:
    """Load background image as CSS value."""
    if image_path and image_path.exists():
        with open(image_path, "rb") as f:
            img_data = base64.b64encode(f.read()).decode("utf-8")
        ext = image_path.suffix.lower()
        mime = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"
        return f'url("data:{mime};base64,{img_data}") center/cover'

    return "linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)"


def render_error_card(card: ErrorCard, template: str, images_dir: Path) -> str:
    """Render an error card to HTML."""
    bg_path = images_dir / f"{card.slug}.png"
    if not bg_path.exists():
        bg_path = images_dir / f"{card.slug}.jpg"

    bg = load_background(bg_path if bg_path.exists() else None)

    html = template.replace("{{BACKGROUND}}", bg)
    html = html.replace("{{DANGER}}", card.danger)
    html = html.replace("{{ERROR_TYPE}}", card.error_type)
    html = html.replace("{{TITLE}}", card.title)
    html = html.replace("{{DESCRIPTION}}", card.description)
    html = html.replace("{{FIX}}", card.fix)
    return html


def render_recap_card(card: RecapCard, template: str, images_dir: Path) -> str:
    """Render a recap card to HTML."""
    bg_path = images_dir / f"{card.slug}.png"
    if not bg_path.exists():
        bg_path = images_dir / f"{card.slug}.jpg"

    bg = load_background(bg_path if bg_path.exists() else None)

    powers_html = ""
    for icon, code, label in card.powers:
        powers_html += f"""
        <div class="power-item">
          <span class="power-icon">{icon}</span>
          <span class="power-text">
            <span class="power-code">{code}</span>
            <span class="power-label">{label}</span>
          </span>
        </div>"""

    html = template.replace("{{BACKGROUND}}", bg)
    html = html.replace("{{LEVEL}}", str(card.level))
    html = html.replace("{{THEME}}", card.theme)
    html = html.replace("{{TITLE}}", card.title)
    html = html.replace("{{POWERS}}", powers_html)
    return html


async def generate_card_image(html: str, output_path: Path, browser):
    """Generate PNG image from HTML using Playwright."""
    page = await browser.new_page(
        viewport={"width": 600, "height": 400},
        device_scale_factor=3,
    )
    await page.set_content(html)
    await page.screenshot(path=str(output_path), type="png")
    await page.close()


def generate_pdfs(output_dir: Path, prefix: str, label: str):
    """Generate a PDF from all PNGs with a given prefix."""
    from PIL import Image

    pngs = sorted(output_dir.glob(f"{prefix}*.png"))
    if not pngs:
        return

    images = []
    for png_path in pngs:
        img = Image.open(png_path)
        if img.mode == "RGBA":
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            images.append(bg)
        else:
            images.append(img.convert("RGB"))

    if not images:
        return

    pdf_path = output_dir / f"{prefix.rstrip('-')}s.pdf"
    # Set resolution so cards print at 600x400 "points" (~21x14cm)
    dpi = images[0].width / 600 * 72  # scale factor * 72
    images[0].save(
        pdf_path, "PDF",
        save_all=True,
        append_images=images[1:],
        resolution=dpi,
    )
    print(f"  Generated PDF: {pdf_path.name} ({len(images)} cards, {dpi:.0f} DPI)")


def generate_combined_html(syntax_dir: Path, output_dir: Path, do_errors: bool, do_recaps: bool):
    """Generate a single HTML file with all cards for browser viewing/printing."""
    cards_html = []

    if do_errors:
        template = (syntax_dir / "template-error.html").read_text(encoding="utf-8")
        for card in ERROR_CARDS:
            card_html = render_error_card(card, template, syntax_dir)
            # Extract just the <body> inner content and styles
            cards_html.append(card_html)

    if do_recaps:
        template = (syntax_dir / "template-recap.html").read_text(encoding="utf-8")
        for card in RECAP_CARDS:
            card_html = render_recap_card(card, template, syntax_dir)
            cards_html.append(card_html)

    # Wrap each card in an iframe-like container
    card_frames = ""
    for i, html in enumerate(cards_html):
        # Encode the full HTML as a data URL for each iframe
        encoded = base64.b64encode(html.encode("utf-8")).decode("utf-8")
        card_frames += f'    <iframe src="data:text/html;base64,{encoded}" width="600" height="400" style="border: 2px solid #333; border-radius: 12px; margin: 10px;"></iframe>\n'

    page = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Zombie Syntax Cards</title>
  <style>
    body {{
      background: #0f0f1a;
      color: white;
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 40px;
      text-align: center;
    }}
    h1 {{
      font-size: 36px;
      margin-bottom: 8px;
    }}
    h2 {{
      font-size: 24px;
      margin: 30px 0 10px;
      color: #fca5a5;
    }}
    .subtitle {{
      color: #888;
      margin-bottom: 30px;
    }}
    .cards {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0;
    }}
    iframe {{
      flex-shrink: 0;
    }}
    @media print {{
      body {{ background: white; padding: 0; }}
      iframe {{
        page-break-inside: avoid;
        margin: 5px;
      }}
    }}
  </style>
</head>
<body>
  <h1>☣ Zombie Syntax Cards ☣</h1>
  <p class="subtitle">Print deze pagina of maak screenshots van de kaarten</p>
  <div class="cards">
{card_frames}
  </div>
</body>
</html>"""

    output_path = output_dir / "all-cards.html"
    output_path.write_text(page, encoding="utf-8")
    print(f"  Generated: {output_path.name}")

    # Also write individual card HTML files
    if do_errors:
        template = (syntax_dir / "template-error.html").read_text(encoding="utf-8")
        for card in ERROR_CARDS:
            card_html = render_error_card(card, template, syntax_dir)
            card_path = output_dir / f"error-{card.slug}.html"
            card_path.write_text(card_html, encoding="utf-8")
            print(f"  Generated: {card_path.name}")

    if do_recaps:
        template = (syntax_dir / "template-recap.html").read_text(encoding="utf-8")
        for card in RECAP_CARDS:
            card_html = render_recap_card(card, template, syntax_dir)
            card_path = output_dir / f"recap-level-{card.level}.html"
            card_path.write_text(card_html, encoding="utf-8")
            print(f"  Generated: {card_path.name}")

    return output_path


async def generate_pngs(syntax_dir: Path, output_dir: Path, do_errors: bool, do_recaps: bool):
    """Generate PNG + PDF cards using Playwright."""
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        if do_errors:
            print("Generating error zombie cards...")
            template = (syntax_dir / "template-error.html").read_text(encoding="utf-8")

            for card in ERROR_CARDS:
                html = render_error_card(card, template, syntax_dir)
                output_file = output_dir / f"error-{card.slug}.png"
                await generate_card_image(html, output_file, browser)
                print(f"  Generated: {output_file.name}")

        if do_recaps:
            print("Generating level recap cards...")
            template = (syntax_dir / "template-recap.html").read_text(encoding="utf-8")

            for card in RECAP_CARDS:
                html = render_recap_card(card, template, syntax_dir)
                output_file = output_dir / f"recap-level-{card.level}.png"
                await generate_card_image(html, output_file, browser)
                print(f"  Generated: {output_file.name}")

        await browser.close()

    # Generate PDFs
    if do_errors:
        generate_pdfs(output_dir, "error-", "Error Zombies")
    if do_recaps:
        generate_pdfs(output_dir, "recap-", "Level Recaps")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate syntax reference cards")
    parser.add_argument("--errors", action="store_true", help="Generate only error cards")
    parser.add_argument("--recaps", action="store_true", help="Generate only recap cards")
    parser.add_argument("--html", action="store_true", help="Generate HTML file instead of PNGs (no Playwright needed)")
    args = parser.parse_args()

    # Default to all
    if not args.errors and not args.recaps:
        args.errors = True
        args.recaps = True

    syntax_dir = Path(__file__).parent
    output_dir = syntax_dir / "output"
    output_dir.mkdir(exist_ok=True)

    if args.html:
        print("Generating combined HTML file...")
        output_path = generate_combined_html(syntax_dir, output_dir, args.errors, args.recaps)
        print(f"\nDone! Open in browser: {output_path}")
    else:
        asyncio.run(generate_pngs(syntax_dir, output_dir, args.errors, args.recaps))
        print(f"\nDone! Cards saved to {output_dir}/")


if __name__ == "__main__":
    main()
