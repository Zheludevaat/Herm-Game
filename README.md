# Herm-Game

## Core Documents
- `METAXY_THE_SOULS_ASCENT_GAME_DESIGN_BRIEF.md` — full narrative and systems design brief.
- `WEB_BUILD_PLAN_GAMEBOY_STYLE.md` — practical web implementation plan for a simple, professional Game Boy-style Zelda-like build.

## Web Prototype (Started)
A minimal Phaser + TypeScript web prototype is now scaffolded.

### Run locally
1. `npm install`
2. `npm run dev`
3. open the local Vite URL (usually `http://localhost:5173`)
4. use the Main Menu to start/continue/clear save

### Current implemented slice
- 320x180 pixel-art game canvas with integer-friendly scaling
- generated high-quality retro pixel textures (hero, floor, walls, chasm, gate, node, bridge)
- top-down 8-direction movement (WASD / Arrow Keys)
- interact key (`E`) with a Memory Node
- Witness toggle (`Q`) with Coherence drain + hidden bridge reveal
- obstacle/chasm collision checks
- objective-driven mini quest tracker loaded from content data (`src/content/quests/moonObjectives.ts`)
- map data extracted to `src/content/maps/*` with shared renderer/collision helpers in `src/game/systems/mapRenderer.ts`
- interactable Sophene NPC hint dialogue
- unlockable exit gate that transitions to a Threshold scene and into a new Metaxy corridor map
- fade-in/fade-out scene transition helper
- playtest-ready Main Menu (start/continue from saved checkpoint/clear-save)
- continue now restores last saved player position within the checkpoint scene
- configurable SFX volume ([ and ]) persisted to save data with retro UI feedback tones
- pause menu overlay (`ESC`) with resume/reset/main-menu options
- data-driven dialogue content loaded from `src/content/dialogue.ts`
- local save/load for Clarity, Coherence, node discovery, and quest completion
- save reset hotkey (`R`) for quick iteration/testing
