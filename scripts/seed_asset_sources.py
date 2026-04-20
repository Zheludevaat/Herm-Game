#!/usr/bin/env python3
"""Apply curated source metadata seeds into preproduction/assets_manifest.csv."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "preproduction" / "assets_manifest.csv"
SEED = ROOT / "preproduction" / "source_seed.csv"


def main() -> int:
    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8")))
    seeds = {r["id"]: r for r in csv.DictReader(SEED.open(encoding="utf-8"))}

    updated = 0
    for row in rows:
        sid = row["id"]
        if sid not in seeds:
            continue
        seed = seeds[sid]
        row["source_name"] = seed["source_name"]
        row["source_url"] = seed["source_url"]
        row["license"] = seed["license"]
        row["attribution"] = seed["attribution"]
        row["status"] = "seeded"
        updated += 1

    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"Updated {updated} manifest entries from {SEED.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
