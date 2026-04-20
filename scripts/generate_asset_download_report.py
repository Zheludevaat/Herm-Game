#!/usr/bin/env python3
"""Generate a tracked report proving which OSS libraries were downloaded."""

from __future__ import annotations

import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "preproduction" / "library_sources.csv"
INDEX = ROOT / "preproduction" / "asset_library_index.csv"
ARCHIVES = ROOT / "preproduction" / "archives"
OUT = ROOT / "preproduction" / "asset_download_report.csv"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    sources = list(csv.DictReader(SOURCES.open(encoding="utf-8")))
    index_rows = {r["name"]: r for r in csv.DictReader(INDEX.open(encoding="utf-8"))}
    now = datetime.now(timezone.utc).isoformat()

    rows = []
    for src in sources:
        name = src["name"]
        category = src["category"]
        archive = ARCHIVES / category / f"{name}.archive"
        exists = archive.exists()
        size = archive.stat().st_size if exists else 0
        digest = sha256_file(archive) if exists else ""
        extracted = index_rows.get(name, {}).get("file_count", "0")
        rows.append(
            {
                "name": name,
                "category": category,
                "source_url": src["source_url"],
                "license": src["license"],
                "downloaded": "yes" if exists else "no",
                "archive_bytes": str(size),
                "archive_sha256": digest,
                "extracted_file_count": extracted,
                "verified_utc": now,
            }
        )

    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "name",
                "category",
                "source_url",
                "license",
                "downloaded",
                "archive_bytes",
                "archive_sha256",
                "extracted_file_count",
                "verified_utc",
            ],
        )
        w.writeheader()
        w.writerows(rows)

    downloaded = sum(1 for r in rows if r["downloaded"] == "yes")
    print(f"downloaded_packs={downloaded}/{len(rows)}")
    print(f"report={OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
