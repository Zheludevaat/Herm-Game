# Preproduction Asset Retrieval Workspace

This folder is the starting point for preproduction asset retrieval.

## What was generated

- `assets_manifest.csv`: normalized list of asset requests parsed from `OPEN_SOURCE_MASTER_ASSET_INVENTORY.md`.
- `assets/`: one JSON request stub per predicted asset.
- `source_seed.csv`: curated starter sources mapped by asset ID.
- `library_sources.csv`: curated downloadable pack list for bootstrapping the asset library.
- `asset_library_index.csv`: snapshot index of retrieved library packs and extracted file counts.
- `asset_download_report.csv`: proof-of-download report with archive size and SHA256 checksums.

## How to use

1. (Optional) Apply curated seed sources into `assets_manifest.csv`:

```bash
./scripts/seed_asset_sources.py
```

2. Fill remaining `source_name`, `source_url`, `license`, and `attribution` in `assets_manifest.csv`.
3. Retrieve URL-backed manifest items:

```bash
./scripts/init_preproduction_assets.py --fetch
```

4. Pull and unpack full curated OSS libraries:

```bash
./scripts/fill_asset_library.py
```

5. Generate a tracked proof report for downloaded libraries:

```bash
./scripts/generate_asset_download_report.py
```

Assets with `source_url` are downloaded into ignored folders (`preproduction/downloads/`, `preproduction/archives/`, and `preproduction/asset_library/`).

## Policy

Do not retrieve or ship assets with unknown or incompatible licenses.
Use `OS-Temp`, `OS-Ship`, `Custom` classification to guide replacement planning.
