#!/usr/bin/env python3
"""Create a deterministic reference-image manifest for image generation or editing.

Usage:
  python reference_manifest.py IMAGE [IMAGE ...] --roles ROLE [ROLE ...]
  python reference_manifest.py IMAGE [IMAGE ...] --roles ROLE [ROLE ...] --json

The script never uploads or edits images. It only verifies local paths and emits
an ordered manifest that can be copied into prompt notes and tool arguments.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
from pathlib import Path

VALID_ROLES = {
    "edit-target",
    "product-reference",
    "identity-reference",
    "composition-reference",
    "style-reference",
    "material-reference",
    "result-evidence",
}

ROLE_LABELS = {
    "edit-target": "edit target",
    "product-reference": "product reference",
    "identity-reference": "identity reference",
    "composition-reference": "composition reference",
    "style-reference": "style reference",
    "material-reference": "material reference",
    "result-evidence": "result evidence",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create an ordered, role-aware reference image manifest."
    )
    parser.add_argument("images", nargs="+", help="Local reference image paths in stable order.")
    parser.add_argument(
        "--roles",
        nargs="+",
        required=True,
        help="One role per image: edit-target, product-reference, identity-reference, "
        "composition-reference, style-reference, material-reference, or result-evidence.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of Markdown.",
    )
    return parser.parse_args()


def build_manifest(images: list[str], roles: list[str]) -> list[dict[str, object]]:
    if len(images) != len(roles):
        raise ValueError(f"images={len(images)} but roles={len(roles)}; provide exactly one role per image")

    manifest: list[dict[str, object]] = []
    for index, (raw_path, role) in enumerate(zip(images, roles), start=1):
        if role not in VALID_ROLES:
            valid = ", ".join(sorted(VALID_ROLES))
            raise ValueError(f"invalid role {role!r}; choose one of: {valid}")

        path = Path(raw_path).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"reference file does not exist: {path}")

        mime, _ = mimetypes.guess_type(path.name)
        manifest.append(
            {
                "number": f"Image {index}",
                "role": role,
                "role_label": ROLE_LABELS[role],
                "path": str(path),
                "filename": path.name,
                "size_bytes": path.stat().st_size,
                "mime": mime or "application/octet-stream",
            }
        )
    return manifest


def emit_markdown(manifest: list[dict[str, object]]) -> None:
    print("Reference manifest:")
    for item in manifest:
        print(
            f"- {item['number']} — {item['role_label']} — "
            f"{item['path']} — [record must-preserve evidence]"
        )

    print("\nPrompt mapping:")
    for item in manifest:
        if item["role"] == "edit-target":
            instruction = "preserve its crop, framing, and unaffected regions"
        elif item["role"] == "product-reference":
            instruction = "use only for product geometry, color, material, and construction truth"
        elif item["role"] == "identity-reference":
            instruction = "use only for identity cues and recognizable features"
        elif item["role"] == "composition-reference":
            instruction = "use only for framing, camera, scale, and layout logic"
        elif item["role"] == "style-reference":
            instruction = "use only for palette, medium, texture, or lighting language"
        elif item["role"] == "material-reference":
            instruction = "use only for surface and material behavior"
        else:
            instruction = "use for evaluation only; do not treat it as an automatic reference"
        print(f"- {item['number']} is the {item['role_label']}; {instruction}.")

    print("\nActual reference input order:")
    print("references = [")
    for item in manifest:
        print(f"  {item['path']!r},")
    print("]")


def main() -> int:
    args = parse_args()
    try:
        manifest = build_manifest(args.images, args.roles)
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        json.dump(manifest, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        emit_markdown(manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
