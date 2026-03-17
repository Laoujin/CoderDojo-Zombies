#!/usr/bin/env python3
"""
Generate challenge card background images using Google Gemini API.

Usage:
    python docs/cards/generate_images.py --level 1

Requires:
    pip install google-genai
    Set GEMINI_API_KEY environment variable (or GOOGLE_API_KEY)
"""

import argparse
import os
import re
from pathlib import Path


def slugify(text: str) -> str:
    """Convert text to filename-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text


def parse_prompts_from_markdown(filepath: Path) -> list[dict]:
    """Parse images.md file and extract prompts."""
    content = filepath.read_text(encoding="utf-8")
    prompts = []

    # Find sections with ## filename.png
    sections = re.split(r"\n## ", content)

    for section in sections[1:]:  # Skip header
        lines = section.strip().split("\n")
        if not lines:
            continue

        # First line is filename
        filename_match = re.match(r"(\S+\.png)", lines[0])
        if not filename_match:
            continue

        filename = filename_match.group(1)

        # Find code block with prompt
        code_match = re.search(r"```\n(.+?)\n```", section, re.DOTALL)
        if not code_match:
            continue

        prompt = code_match.group(1).strip()

        # Convert Midjourney prompt to Gemini format
        # Remove --ar and --style flags
        prompt = re.sub(r"\s*--ar\s+\S+", "", prompt)
        prompt = re.sub(r"\s*--style\s+\S+", "", prompt)

        # Add aspect ratio instruction naturally
        prompt = f"{prompt}. The image should be in landscape format with 3:2 aspect ratio (wider than tall)."

        prompts.append({"filename": filename, "prompt": prompt})

    return prompts


def generate_image(prompt: str, output_path: Path):
    """Generate an image using Gemini API."""
    from google import genai

    # Initialize client (uses GOOGLE_API_KEY or GEMINI_API_KEY env var)
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Set GEMINI_API_KEY or GOOGLE_API_KEY environment variable")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-exp-image-generation",
        contents=prompt,
        config=genai.types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
        ),
    )

    # Extract and save image
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            image_data = part.inline_data.data
            import base64

            # Decode base64 and save
            with open(output_path, "wb") as f:
                f.write(base64.b64decode(image_data))
            return True

    return False


def main():
    parser = argparse.ArgumentParser(description="Generate card images with Gemini")
    parser.add_argument("--level", type=int, required=True, help="Level number")
    args = parser.parse_args()

    cards_dir = Path(__file__).parent
    images_md = cards_dir / f"level-{args.level}" / "images.md"

    if not images_md.exists():
        print(f"Error: {images_md} not found")
        return

    prompts = parse_prompts_from_markdown(images_md)
    print(f"Found {len(prompts)} prompts in {images_md}")

    output_dir = cards_dir / f"level-{args.level}"
    output_dir.mkdir(exist_ok=True)

    for i, item in enumerate(prompts, 1):
        output_path = output_dir / item["filename"]
        print(f"\n[{i}/{len(prompts)}] Generating {item['filename']}...")
        print(f"  Prompt: {item['prompt'][:80]}...")

        try:
            if generate_image(item["prompt"], output_path):
                print(f"  Saved: {output_path}")
            else:
                print(f"  Warning: No image in response")
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    main()
