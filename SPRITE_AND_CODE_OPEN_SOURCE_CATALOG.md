# 2D Retro Open-Source Sprite & Code Catalog

Purpose: shortlist free/open sources we can use to accelerate a 2D Game Boy Color-style production pipeline.

---

## 1) Sprite / Tileset Libraries

## Recommended first-pass sources

- **Kenney (CC0)**
  - Great for rapid prototypes and UI/icon placeholders.
  - Safe licensing for commercial use.
- **OpenGameArt**
  - Large variety of sprite sheets, tilesets, and VFX.
  - Must filter by permissive license and capture attribution requirements.
- **itch.io free pixel packs (license varies)**
  - Useful for temp biome studies and style exploration.
  - Only ingest packs with explicit commercial terms.
- **Liberated Pixel Cup collections**
  - Helpful for animation and equipment pipeline references.

## Ingestion rule

Every imported asset must include:

- source URL,
- author,
- exact license,
- attribution requirement,
- replacement status (`TEMP_OPEN` / `FINAL_CUSTOM`).

---

## 2) Code Libraries / Frameworks for Sprite Control and 2D Gameplay

## Preferred engine track (Godot 4)

- **Godot built-in TileMap/TileSet/AnimationPlayer/StateTree support**.
- **Open-source Godot addons** for:
  - dialogue systems,
  - finite state machines,
  - save/load helpers,
  - pixel camera and screen shake,
  - 2D pathfinding.

## Alternate C# track

- **MonoGame** / **FNA**
  - Strong if you want explicit low-level control over sprite rendering, animation timing, and input.
- **Aseprite JSON pipelines + import tooling**
  - Common for deterministic sprite animation export workflows.

---

## 3) Audio and SFX Libraries (Open/Free)

- **Freesound** (license-filtered only).
- **OpenGameArt audio packs**.
- **Audacity + ffmpeg** for pipeline processing.

Use for prototype and non-signature effects; keep key leitmotifs custom.

---

## 4) Immediate Pull Plan

## Week 1

- Build `third_party_assets.csv` and `third_party_code.csv` inventories.
- Import 2 provisional tilesets + 1 character set + 1 UI set.
- Integrate one open-source controller/state-machine addon.

## Week 2

- Stand up replacement tracker for all temp assets.
- Validate license compatibility for release targets.
- Lock one canonical sprite scale/palette spec for GBC-style output.

---

## 5) Guardrails

- No unknown-license content in main branch.
- No copyleft runtime dependency without explicit approval.
- Replace generic visual packs in player-facing hero zones before content lock.

---

## 6) Bottom Line

Yes — we can pull a lot of open/free sprite libraries and control-code scaffolding to save time, tokens, and effort.

Best approach:

- open-source for prototype speed and pipeline acceleration,
- bespoke replacement for signature art, final identity, and narrative-critical scenes.
