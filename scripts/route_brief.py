#!/usr/bin/env python3
"""Deterministically propose a GPT-Image2 direction from a short brief."""

from __future__ import annotations

import argparse


ROUTES = {
    "ui": ("UI & Interfaces", "screen hierarchy, components, interaction state, readable labels"),
    "app": ("UI & Interfaces", "screen hierarchy, components, interaction state, readable labels"),
    "dashboard": ("UI & Interfaces", "data hierarchy, widgets, visual grouping, readable labels"),
    "infographic": ("Charts & Infographics", "reading order, data modules, connectors, label hierarchy"),
    "chart": ("Charts & Infographics", "reading order, data modules, connectors, label hierarchy"),
    "poster": ("Posters & Typography", "headline hierarchy, negative space, exact typography"),
    "cover": ("Posters & Typography", "headline hierarchy, negative space, exact typography"),
    "product": ("Products & E-commerce", "product invariants, materials, commercial lighting, benefit order"),
    "ecommerce": ("Products & E-commerce", "product invariants, materials, commercial lighting, benefit order"),
    "brand": ("Brand & Logos", "mark constraints, palette, touchpoints, avoid-list"),
    "logo": ("Brand & Logos", "mark constraints, palette, touchpoints, avoid-list"),
    "architecture": ("Architecture & Spaces", "perspective, material, spatial logic, factual constraints"),
    "interior": ("Architecture & Spaces", "perspective, material, spatial logic, factual constraints"),
    "photo": ("Photography & Realism", "lens, framing, light direction, real material detail"),
    "portrait": ("Photography & Realism", "lens, framing, light direction, real material detail"),
    "illustration": ("Illustration & Art", "medium, line/shape language, palette, composition"),
    "art": ("Illustration & Art", "medium, line/shape language, palette, composition"),
    "character": ("Characters & People", "silhouette, proportions, pose, costume details"),
    "storyboard": ("Scenes & Storytelling", "moment, camera, foreground/background action"),
    "scene": ("Scenes & Storytelling", "moment, camera, foreground/background action"),
    "history": ("History & Classical Themes", "period research, cultural constraints, material and script"),
    "document": ("Documents & Publishing", "page grid, annotation hierarchy, editorial structure"),
}

FORMATS = {
    "hero": "16:9 landscape",
    "landscape": "16:9 landscape",
    "square": "1:1 square",
    "feed": "4:5 portrait",
    "portrait": "4:5 portrait",
    "story": "9:16 vertical",
    "poster": "2:3 vertical",
    "auto": "choose based on final placement",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Suggest a production prompt direction without calling any image API.")
    parser.add_argument("--use-case", required=True, help="e.g. ui, infographic, poster, product, logo, photo, illustration, character")
    parser.add_argument("--format", default="auto", choices=sorted(FORMATS), help="Intended placement format")
    parser.add_argument("--mode", default="generate", choices=["generate", "reference-led", "edit"], help="Image workflow mode")
    parser.add_argument("--references", default="none", choices=["none", "visual", "factual", "both"], help="Reference need")
    args = parser.parse_args()

    key = args.use_case.lower().replace(" ", "")
    category, emphasis = ROUTES.get(key, ("Other Use Cases", "asset intent, composition, material, constraints"))
    print(f"Category: {category}")
    print(f"Mode: {args.mode}")
    print(f"Suggested format: {FORMATS[args.format]}")
    print(f"Prompt emphasis: {emphasis}")
    if args.mode == "edit":
        print("Edit rule: state 'Change only' and 'Preserve exactly' before other detail.")
    elif args.mode == "reference-led":
        print("Reference rule: label every image as composition, style, identity, product, or factual reference.")
    if args.references in {"factual", "both"}:
        print("Research rule: confirm facts before prompting; do not invent named-product, historical, or geographic details.")
    if args.references in {"visual", "both"}:
        print("Visual rule: use reference images for silhouette, layout, materials, or terrain rather than text alone.")
    print("Next: consult the installed Style Library for the nearest template, tags, and example case IDs.")


if __name__ == "__main__":
    main()
