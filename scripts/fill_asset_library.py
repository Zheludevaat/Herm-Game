#!/usr/bin/env python3
"""Download and unpack curated open-source asset library packs for preproduction."""

from __future__ import annotations

import csv
import io
import tarfile
import zipfile
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "preproduction" / "library_sources.csv"
LIB_ROOT = ROOT / "preproduction" / "asset_library"
ARCHIVE_ROOT = ROOT / "preproduction" / "archives"


def fetch_bytes(url: str) -> bytes:
    with urlopen(url) as r:
        return r.read()


def unpack_archive(blob: bytes, destination: Path, source_url: str) -> None:
    destination.mkdir(parents=True, exist_ok=True)

    # Detect zip by signature (GitHub codeload URLs often omit .zip suffix).
    if blob[:4] == b"PK\x03\x04":
        with zipfile.ZipFile(io.BytesIO(blob)) as z:
            z.extractall(destination)
        return

    # Detect gzip/tar by signature.
    if blob[:2] == b"\x1f\x8b":
        with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as t:
            t.extractall(destination)
        return

    # fallback: save raw file if non-archive
    (destination / "download.bin").write_bytes(blob)


def main() -> int:
    rows = list(csv.DictReader(SOURCES.open(encoding="utf-8")))
    retrieved = 0

    for row in rows:
        name = row["name"].strip()
        category = row["category"].strip()
        url = row["source_url"].strip()
        subdir = row["extract_subdir"].strip() or name.lower()

        archive_dir = ARCHIVE_ROOT / category
        archive_dir.mkdir(parents=True, exist_ok=True)
        archive_path = archive_dir / f"{name}.archive"

        print(f"Fetching {name} from {url}")
        try:
            blob = fetch_bytes(url)
        except Exception as exc:
            print(f"WARN failed to fetch {name}: {exc}")
            continue

        archive_path.write_bytes(blob)

        target = LIB_ROOT / category / subdir
        unpack_archive(blob, target, url)

        meta = target / "SOURCE_METADATA.txt"
        meta.write_text(
            "\n".join(
                [
                    f"name: {name}",
                    f"category: {category}",
                    f"license: {row['license']}",
                    f"source_url: {url}",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        retrieved += 1

    print(f"Retrieved packs: {retrieved}")
    print(f"Library root: {LIB_ROOT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
