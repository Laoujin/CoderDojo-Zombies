#!/usr/bin/env python3
"""
Generate printable challenge cards from uitdagingen.md files.

Usage:
    python docs/cards/generate.py [--level N] [--list]

Requires:
    pip install playwright
    playwright install chromium

Background images:
    Place images in docs/cards/level-{n}/ with slugified challenge names.
    Example: docs/cards/level-1/verstoppen.png

Output:
    Cards are saved to docs/cards/output/
"""

import argparse
import re
import asyncio
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Challenge:
    level: str
    tier: str  # Opwarmer, Pittig, Boss
    title: str
    description: str
    hint: str
    slug: str


def slugify(text: str) -> str:
    """Convert text to filename-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text


def parse_uitdagingen(filepath: Path, level: str) -> list[Challenge]:
    """Parse a uitdagingen.md file and extract challenges."""
    content = filepath.read_text(encoding="utf-8")
    challenges = []
    current_tier = None

    # Split by --- separator
    sections = re.split(r"\n---\n", content)

    for section in sections:
        # Find tier (## Opwarmer, ## Pittig, ## Boss)
        tier_match = re.search(r"^##\s+(Opwarmer|Pittig|Boss)\s*$", section, re.MULTILINE)
        if tier_match:
            current_tier = tier_match.group(1)

        # Find challenge title (### Title)
        title_match = re.search(r"^###\s+(.+?)\s*$", section, re.MULTILINE)
        if not title_match:
            continue

        title = title_match.group(1)

        # Get content after title
        after_title = section[title_match.end() :].strip()

        # Extract hint
        hint_match = re.search(r"\*\*Hint:\*\*\s*(.+?)(?:\n\n|\n\?\?\?|\Z)", after_title, re.DOTALL)
        hint = hint_match.group(1).strip() if hint_match else ""

        # Description is everything before the hint
        if hint_match:
            description = after_title[: hint_match.start()].strip()
        else:
            description = after_title.strip()

        # Remove any remaining markdown artifacts
        description = re.sub(r"^##.*$", "", description, flags=re.MULTILINE).strip()

        if current_tier and title:
            challenges.append(
                Challenge(
                    level=level,
                    tier=current_tier,
                    title=title,
                    description=description,
                    hint=hint,
                    slug=slugify(title),
                )
            )

    return challenges


def get_tier_color(tier: str) -> str:
    """Get color for tier badge."""
    return {
        "Opwarmer": "#28a745",
        "Pittig": "#fd7e14",
        "Boss": "#dc3545",
    }.get(tier, "#666")


def markdown_inline_code(text: str) -> str:
    """Convert markdown `code` to <code>code</code>."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", text)


def render_card_html(challenge: Challenge, background_path: Path | None, template: str) -> str:
    """Render a challenge as HTML card."""
    import base64

    # Use background image or fallback gradient
    if background_path and background_path.exists():
        # Embed image as base64 data URL (Playwright can't load file:// URLs)
        with open(background_path, "rb") as f:
            img_data = base64.b64encode(f.read()).decode("utf-8")
        ext = background_path.suffix.lower()
        mime = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"
        bg_style = f'url("data:{mime};base64,{img_data}") center/cover'
    else:
        bg_style = "linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)"

    tier_color = get_tier_color(challenge.tier)

    html = template.replace("{{BACKGROUND}}", bg_style)
    html = html.replace("{{TIER}}", challenge.tier)
    html = html.replace("{{TIER_COLOR}}", tier_color)
    html = html.replace("{{LEVEL}}", challenge.level)
    html = html.replace("{{TITLE}}", challenge.title)
    html = html.replace("{{DESCRIPTION}}", markdown_inline_code(challenge.description))
    html = html.replace("{{HINT}}", markdown_inline_code(challenge.hint))

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


def get_all_challenges(levels_dir: Path, level_filter: str | None = None) -> list[Challenge]:
    """Get all challenges from uitdagingen.md files."""
    if level_filter:
        patterns = [levels_dir / f"level-{level_filter}" / "uitdagingen.md"]
    else:
        patterns = sorted(levels_dir.glob("level-*/uitdagingen.md"))

    all_challenges = []
    for filepath in patterns:
        if not filepath.exists():
            print(f"Warning: {filepath} not found")
            continue

        level_match = re.search(r"level-([\d.]+)", str(filepath))
        if not level_match:
            continue

        level = level_match.group(1)
        challenges = parse_uitdagingen(filepath, level)
        all_challenges.extend(challenges)

    return all_challenges


async def main():
    parser = argparse.ArgumentParser(description="Generate challenge cards")
    parser.add_argument("--level", type=str, help="Generate only for specific level")
    parser.add_argument("--list", action="store_true", help="List expected background image paths")
    args = parser.parse_args()

    # Paths
    cards_dir = Path(__file__).parent  # docs/cards/
    root = cards_dir.parent.parent  # project root
    levels_dir = root / "levels"
    output_dir = cards_dir / "output"

    all_challenges = get_all_challenges(levels_dir, args.level)

    if not all_challenges:
        print("No challenges found!")
        return

    # List mode - just show expected image paths
    if args.list:
        print("Expected background images:\n")
        for challenge in all_challenges:
            img_path = cards_dir / f"level-{challenge.level}" / f"{challenge.slug}.png"
            exists = "ok" if img_path.exists() else "MISSING"
            print(f"  [{exists}] {img_path.relative_to(root)}")
        return

    # Count challenges per level
    levels = {}
    for c in all_challenges:
        levels[c.level] = levels.get(c.level, 0) + 1
    for level, count in sorted(levels.items()):
        print(f"Found {count} challenges in level {level}")

    # Load template
    template_path = cards_dir / "template.html"
    template = template_path.read_text(encoding="utf-8")

    output_dir.mkdir(exist_ok=True)

    # Launch browser
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        for challenge in all_challenges:
            # Look for background image in docs/cards/level-{n}/
            bg_dir = cards_dir / f"level-{challenge.level}"
            bg_path = bg_dir / f"{challenge.slug}.png"

            if not bg_path.exists():
                bg_path = bg_dir / f"{challenge.slug}.jpg"

            if not bg_path.exists():
                print(f"  Warning: No background for '{challenge.title}' (expected: level-{challenge.level}/{challenge.slug}.png)")
                bg_path = None

            html = render_card_html(challenge, bg_path, template)
            output_file = output_dir / f"level-{challenge.level}-{challenge.slug}.png"

            await generate_card_image(html, output_file, browser)
            print(f"  Generated: {output_file.name}")

        await browser.close()

    print(f"\nDone! Cards saved to docs/cards/output/")

    # Generate PDFs per level
    generate_pdfs(output_dir, levels.keys())


def generate_pdfs(output_dir: Path, level_numbers: list[str]):
    """Generate PDF files per level from card PNGs."""
    from PIL import Image

    for level in sorted(level_numbers):
        # Find all PNGs for this level
        pngs = sorted(output_dir.glob(f"level-{level}-*.png"))
        if not pngs:
            continue

        # Convert PNGs to RGB images (PDF doesn't support RGBA)
        images = []
        for png_path in pngs:
            img = Image.open(png_path)
            if img.mode == "RGBA":
                # Create white background
                bg = Image.new("RGB", img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[3])
                images.append(bg)
            else:
                images.append(img.convert("RGB"))

        if not images:
            continue

        # Save as PDF - set resolution so cards print at 600x400 "points" (~21x14cm)
        pdf_path = output_dir / f"level-{level}.pdf"
        dpi = images[0].width / 600 * 72  # scale factor * 72
        images[0].save(
            pdf_path, "PDF",
            save_all=True,
            append_images=images[1:],
            resolution=dpi,
        )
        print(f"  Generated PDF: {pdf_path.name} ({len(images)} cards, {dpi:.0f} DPI)")


if __name__ == "__main__":
    asyncio.run(main())
