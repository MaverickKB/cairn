#!/usr/bin/env python3
"""Check that the kit docs match cairn.json and stay generic."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "cairn.json"
README = ROOT / "README.md"
LICENSE = ROOT / "LICENSE"

BANNED = (
    "/Users/",
    "/home/",
    "192.168.",
    "@gmail",
    "MIT License",
)


def fail(message):
    print(message)
    return 1


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    readme = README.read_text(encoding="utf-8")
    license_text = LICENSE.read_text(encoding="utf-8")
    errors = []

    if "Noncommercial" not in license_text:
        errors.append("LICENSE is not the noncommercial grant")
    if "MIT License" in license_text:
        errors.append("LICENSE is still MIT")

    start_id = manifest["start"]
    start = None
    seen = set()
    for item in manifest["components"]:
        item_id = item["id"]
        if item_id in seen:
            errors.append(f"duplicate component id {item_id}")
        seen.add(item_id)
        if item_id == start_id:
            start = item
        if item["required"] and not item["in_start_path"]:
            errors.append(f"{item_id} is required but not in the start path")
        if item["in_start_path"] and item["url"] not in readme:
            errors.append(f"start component {item_id} is missing from README")

    if start is None:
        errors.append(f"start id {start_id} is not a component")
    elif not start["required"]:
        errors.append("start component is not required")

    for path in (MANIFEST, README, LICENSE):
        text = path.read_text(encoding="utf-8").lower()
        for word in BANNED:
            if word.lower() in text:
                errors.append(f"{path.name} contains {word}")

    if errors:
        for item in errors:
            print(item)
        return 1
    print(f"ok {len(manifest['components'])} components, start={start_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
