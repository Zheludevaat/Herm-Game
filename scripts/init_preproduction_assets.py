#!/usr/bin/env python3
"""Initialize preproduction asset retrieval workspace from master inventory.

- Parses OPEN_SOURCE_MASTER_ASSET_INVENTORY.md checklist items.
- Generates preproduction/assets_manifest.csv.
- Creates directory scaffolding and request JSON stubs per item.
- Optional --fetch downloads assets for entries with source_url values.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "OPEN_SOURCE_MASTER_ASSET_INVENTORY.md"
MANIFEST = ROOT / "preproduction" / "assets_manifest.csv"
ASSET_ROOT = ROOT / "preproduction" / "assets"

CHECK_RE = re.compile(r"^- \[ \] (.+?)(?:\s+—\s+`([^`]+)`)?\s*$")


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")




def load_existing_manifest() -> dict[str, dict[str, str]]:
    if not MANIFEST.exists():
        return {}
    with MANIFEST.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return {row["id"]: row for row in rows}


def parse_inventory() -> list[dict[str, str]]:
    lines = INVENTORY.read_text(encoding="utf-8").splitlines()
    section = "general"
    subsection = "general"
    out = []
    idx = 1

    for line in lines:
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if line.startswith("### "):
            subsection = line[4:].strip()
            continue
        m = CHECK_RE.match(line)
        if not m:
            continue

        item = m.group(1).strip()
        sourcing = m.group(2) or "UNCLASSIFIED"

        # Handle lines where sourcing marker was embedded in item text, e.g.
        # "Minor resident... — `OS-Ship` (restyled)".
        if sourcing == "UNCLASSIFIED":
            embedded = re.search(r"—\s*`(OS-(?:Ship|Temp)|Custom)`", item)
            if embedded:
                sourcing = embedded.group(1)
                item = re.sub(r"\s*—\s*`(?:OS-(?:Ship|Temp)|Custom)`.*$", "", item).strip()
        category = slugify(section)
        subcategory = slugify(subsection)
        asset_id = f"A{idx:04d}"
        filename = slugify(item)[:80] or asset_id.lower()
        target_dir = ASSET_ROOT / category / subcategory
        target_path = target_dir / f"{filename}.asset-request.json"

        out.append(
            {
                "id": asset_id,
                "section": section,
                "subsection": subsection,
                "item": item,
                "sourcing": sourcing,
                "status": "pending",
                "source_name": "",
                "source_url": "",
                "license": "",
                "attribution": "",
                "target_stub": str(target_path.relative_to(ROOT)),
            }
        )
        idx += 1

    return out


def write_manifest(rows: list[dict[str, str]]) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "id",
        "section",
        "subsection",
        "item",
        "sourcing",
        "status",
        "source_name",
        "source_url",
        "license",
        "attribution",
        "target_stub",
    ]
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def write_stubs(rows: list[dict[str, str]]) -> None:
    for row in rows:
        stub = ROOT / row["target_stub"]
        stub.parent.mkdir(parents=True, exist_ok=True)
        if stub.exists():
            continue
        payload = {
            "id": row["id"],
            "item": row["item"],
            "section": row["section"],
            "subsection": row["subsection"],
            "sourcing": row["sourcing"],
            "status": row["status"],
            "source": {
                "name": row["source_name"],
                "url": row["source_url"],
                "license": row["license"],
                "attribution": row["attribution"],
            },
            "notes": "Fill source details before retrieval.",
        }
        stub.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def fetch_assets(rows: list[dict[str, str]]) -> int:
    downloaded = 0
    for row in rows:
        url = row.get("source_url", "").strip()
        if not url:
            continue
        dst = ROOT / "preproduction" / "downloads" / row["id"]
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            urllib.request.urlretrieve(url, dst)
            downloaded += 1
        except Exception as exc:  # pragma: no cover
            print(f"WARN {row['id']} failed: {exc}")
    return downloaded


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", action="store_true", help="Download entries with source_url set")
    args = parser.parse_args()

    if not INVENTORY.exists():
        raise SystemExit("Missing OPEN_SOURCE_MASTER_ASSET_INVENTORY.md")

    rows = parse_inventory()
    existing = load_existing_manifest()
    for row in rows:
        prev = existing.get(row["id"])
        if not prev:
            continue
        for key in ("status", "source_name", "source_url", "license", "attribution"):
            if prev.get(key):
                row[key] = prev[key]

    write_manifest(rows)
    write_stubs(rows)

    downloaded = 0
    if args.fetch:
        downloaded = fetch_assets(rows)

    print(f"Initialized {len(rows)} asset requests.")
    print(f"Manifest: {MANIFEST.relative_to(ROOT)}")
    print(f"Downloads: {downloaded}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
