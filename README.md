# Herm-Game

Project format mandate: **2D retro Game Boy Color-style, level-based game**.

## Production bootstrap (now started)

A playable game-production starter now exists in `game/`:

- `game/main.py` — launch entrypoint.
- `game/metaxy_game/` — initial runtime modules (config, level loader, player movement, dialogue wheel, soul state HUD, app loop).
- `game/data/moon_threshold.json` — first Moon threshold prototype map.
- `game/requirements.txt` — runtime dependency list.

Run locally:

```bash
python play.py
```

`play.py` opens a small launcher app with a **Play** button. Pressing it will install missing runtime dependencies (if needed) and start the game in one step.

Run baseline automated checks:

```bash
python scripts/validate_game_data.py
python -m unittest discover -s tests -p "test_*.py"
```

Run M6 gold-candidate regression bundle:

```bash
python scripts/run_m6_regression_suite.py
```

Current prototype features:

- Tilemap movement + collision with themed pixel-art tile rendering, dithering, and gradient backdrops
- Prologue calling selection (Scholar/Caregiver/Reformer)
- Reception ritual sequence with Four Guardians before traversal starts
- Pixel-art player/NPC character sprites with subtle idle animation and richer outlines
- NPC interaction (`E`)
- Inquiry wheel dialogue (`1-7` + `Enter`) with per-act dialogue data in `game/data/dialogue/*.json`
- Seven-verb runtime channeling (TAB cycle, `F` apply): Witness/Name/Attune/Expose/Stand/Weigh/Release
- Coherence/Clarity/Memory HUD updates from dialogue and exploration
- Collectible memory shards (Moon threshold)
- Per-act side quest insight nodes (`Q`) that grant clarity and gate thresholds
- Governor trial nodes (`G`) with a stillness challenge (hold `S`) required for threshold completion
- Per-act relic nodes (`R`) that grant a relic entry and gate threshold crossing
- Save/load hotkeys (`F5` save, `F9` load)
- Dissonance zones reduce Coherence in real time
- Harmony shrines (`H`) restore Coherence when interacted with (`E`)
- Obscuration reset when Coherence reaches zero
- Moon threshold gate (SPACE to cross when requirements met)
- Threshold gates now require **dialogue witness + stats** (talk to resident in each act)
- Moon -> Mercury -> Venus -> Mars level progression driven by `game/data/acts.json`
- Level JSON now includes per-zone spawn/NPC metadata for content-authored staging
- Dynamic ending evaluation (True/Reincarnation/Vow-Return/Soft/False) at final Mars completion
- Simple vertical-slice completion panel with journey reset (`R`)
- Quest tracker line showing current act objective progress
- Codex overlay (`C`) with state-based entry unlocks
- Accessibility quick panel (`F1`): high contrast, reduced flash cadence, UI font size (+/-)

## Core project documents

- `METAXY_SOULS_ASCENT_GAME_DESIGN_BRIEF.md` — full game design brief (updated for 2D retro direction).
- `CODEX_OPTIMIZED_BUILD_PLAN.md` — execution-oriented task list and milestone plan.
- `OPEN_SOURCE_SOURCING_PLAN.md` — what can be sourced from free/open-source tools, frameworks, and content.
- `SPRITE_AND_CODE_OPEN_SOURCE_CATALOG.md` — practical library shortlist for open sprite packs and 2D control-code scaffolding.
- `OPEN_SOURCE_MASTER_ASSET_INVENTORY.md` — unabridged predicted asset/system checklist for open-source procurement and replacement planning.
- `M6_LAUNCH_RUNBOOK.md` — launch-day triage and hotfix workflow for gold-candidate operations.
- `M6_TELEMETRY_PRIVACY_CHECKLIST.md` — release checklist for telemetry/privacy and regression gating.

## Preproduction

- `scripts/seed_asset_sources.py` — applies curated source metadata to manifest rows.
- `scripts/init_preproduction_assets.py` — generates/refreshes preproduction manifests and stubs; supports `--fetch` for URL-backed downloads.
- `scripts/fill_asset_library.py` — downloads and unpacks curated open-source asset libraries.
- `scripts/generate_asset_download_report.py` — generates checksum/size proof for downloaded libraries.
- `preproduction/source_seed.csv` — starter set of open-source source URLs/licenses for immediate retrieval.
- `preproduction/library_sources.csv` — curated downloadable libraries to bootstrap production assets.
- `preproduction/assets_manifest.csv` — normalized checklist of predicted assets for intake tracking.
- `preproduction/asset_library_index.csv` — index of retrieved library packs with extracted file counts.
- `preproduction/asset_download_report.csv` — proof report of downloaded library archives (size + SHA256).
- `preproduction/README.md` — step-by-step retrieval workflow.
