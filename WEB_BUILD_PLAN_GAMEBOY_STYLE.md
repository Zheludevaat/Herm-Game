# METAXY Web Build Plan (Simple, Professional, Game Boy-Style)

This plan converts the large narrative brief into a **practical, shippable web game build** with a classic Game Boy-inspired look and Zelda-like top-down gameplay.

## 1) Product Goal (MVP First)

Build a premium-feeling, single-player, browser-playable top-down action-adventure RPG with:
- crisp 2D pixel presentation (Game Boy / GBC inspired palette discipline),
- simple but polished exploration/combat/dialogue loops,
- one complete vertical slice (Prologue + Reception + Moon Plateau + Moon Trial),
- architecture that can scale to all seven acts.

**MVP scope:** 2 to 4 hours of high-quality content.

---

## 2) Core Tech Stack (Keep It Simple)

### Engine and language
- **Phaser 3** (WebGL/canvas, battle-tested for web 2D)
- **TypeScript** (safer iteration, easier refactor than plain JS)
- **Vite** (fast local dev + production bundling)

### Content tools
- **Tiled** for tilemaps and collision layers
- **Aseprite** (or LibreSprite) for sprites/tiles/UI assets
- **Ink** (optional in MVP) or JSON dialogue graphs for branching dialogue

### Audio
- **Howler.js** or Phaser sound API
- OGG/MP3 for music loops, WAV for short SFX

### Save/state
- Browser **LocalStorage** for MVP
- versioned save schema from day one

---

## 3) Visual Direction: “Professional Game Boy”

### Style rules
- Native internal render resolution: **320x180** (or 256x144 for stricter retro)
- Integer scaling only (no blurry interpolation)
- Tile size: **16x16**
- Character sprites: 16x16 base, 24x24 for bosses/NPC variants

### Palette strategy
Two options:
1. strict 4-color per map chunk (DMG-like mood), or
2. curated 12–24 color master palette (GBC-inspired, recommended for readability).

Recommended palette clusters:
- Metaxy: indigo + silver accents
- Moon: pearl/gray/lavender
- UI neutral: dark ink, light parchment, accent gold

### Professional polish checklist
- consistent light direction on all sprites
- 1px outline policy documented
- animation timing bible (idle/walk/interact/hit)
- screen transition style fixed early (fade/wipe)

---

## 4) Gameplay Loop (Web-Friendly)

1. Explore zone (movement, interactables, NPCs)
2. Resolve room-scale puzzle or combat encounter
3. Gain Clarity / story state
4. Unlock new path via verb ability
5. Enter trial space (mini-boss/boss puzzle)
6. Release moment + narrative checkpoint

### Controls (keyboard + gamepad)
- Move: WASD / Left Stick
- Interact: E / A button
- Verb action: Space / X button
- Dodge/step (optional): Shift / B button
- Menu: Esc / Start

Keep input mapping rebindable in settings.

---

## 5) Systems to Implement First (MVP)

### 5.1 Player controller
- 8-direction movement
- acceleration/deceleration tuned for “retro crisp” feel
- collision and pushback
- interaction cone/radius

### 5.2 Dialogue system
- portrait + name + text box
- typewriter effect with skip
- branching responses (3 max per prompt in MVP)
- choices update hidden variables: `clarity`, `moon_weight`, `daimon_bond`

### 5.3 Coherence and clarity
- Coherence = survivability/focus meter
- Clarity = progression currency + dialogue gates
- Obscured state on zero coherence: reset to last threshold (no death screen)

### 5.4 Moon verb: Witness
- toggle overlay to reveal hidden paths, false walls, memory traces
- drains small coherence while active (prevents permanent spam)

### 5.5 One Governor trial (Selenos)
- no brute-force combat
- phase puzzle: identify true witness point among reflections
- success triggers garment release cutscene (in-engine)

---

## 6) Vertical Slice Content Plan (What to Actually Build)

### Slice includes
1. **Mortal Prologue** (10–15 min)
2. **Reception space** with elemental ritual/tutorial
3. **Metaxy connector** (small explorable hub)
4. **Mirror’s Palace** (Moon Plateau hub)
5. 2 side quests
6. 1 memory chain (3 shards)
7. **Selenos Trial**
8. Sophene reunion bridge and Act-end save

### Slice target duration
- 90–150 minutes first playthrough.

---

## 7) Content Budget (Small Team Realism)

For MVP vertical slice:
- Tilesets: 4 (prologue, reception, metaxy, moon)
- Maps: 12–18 rooms/screens
- NPCs: 15–20
- Enemies/hazards: 4–6 archetypes
- Bosses: 1 (Selenos trial form)
- Music tracks: 6–8 loops
- SFX: 60–90
- Dialogue lines: 1,500–2,500

---

## 8) Project Structure

```txt
/src
  /game
    /scenes
    /entities
    /systems
    /ui
    /data
  /content
    /maps
    /dialogue
    /quests
    /audio
    /sprites
  /core
    config.ts
    save.ts
    state.ts
```

### Scene architecture
- BootScene
- PreloadScene
- MainMenuScene
- WorldScene (loads map chunks)
- UIScene (HUD/dialogue/menu)
- TrialScene (for special rule spaces)

---

## 9) Milestone Plan (16 Weeks, Practical)

### Milestone 1 (Weeks 1–2): Foundation
- Phaser + TS + Vite scaffold
- camera, tile collisions, room transitions
- input system (keyboard/gamepad)
- debug overlay

### Milestone 2 (Weeks 3–5): Core Play
- dialogue UI + branching variables
- quest flags
- coherence/clarity HUD and save/load
- base interactables (switches, gates, memory nodes)

### Milestone 3 (Weeks 6–8): Moon Mechanics
- Witness mechanic
- reflection tiles + hidden layer reveal
- Moon hub map complete graybox -> art pass 1

### Milestone 4 (Weeks 9–11): Trial + Narrative
- Selenos trial scripted phases
- release sequence and reunions
- first full narrative pass with placeholder VO barks

### Milestone 5 (Weeks 12–14): Polish
- combat/puzzle feel tuning
- animation polish
- audio pass and mix pass
- accessibility options (font size, contrast, input remap)

### Milestone 6 (Weeks 15–16): Ship Slice
- bug fixing and performance
- web build optimization and loading screen
- QA sweep and balancing
- public demo packaging

---

## 10) Performance + Web Delivery Requirements

- Target 60 FPS on mid-tier laptops
- Texture atlas packing mandatory
- Avoid runtime shader-heavy effects in MVP
- Lazy-load non-critical audio
- First playable load under 10 seconds on broadband
- Progressive asset loading between zones

---

## 11) Minimum Accessibility and UX

Ship in MVP:
- rebindable keys
- gamepad support
- font size slider
- dyslexia-friendly font toggle
- high-contrast UI mode
- reduced screen shake option
- puzzle hint toggle

---

## 12) Risks and Practical Mitigations

1. **Over-scope from full 7-act vision**  
   Mitigation: freeze MVP to Act I only.

2. **Retro look becoming amateur**  
   Mitigation: enforce art bible + palette + animation standards before asset scaling.

3. **Narrative complexity blocking implementation**  
   Mitigation: data-driven dialogue, max 3 branches per node in MVP.

4. **Web performance drops**  
   Mitigation: strict atlas sizes, scene streaming, perf budget checks each milestone.

---

## 13) Definition of Done (Vertical Slice)

The slice is done when:
- a new player can complete the flow without docs,
- one complete emotional arc lands (death -> reception -> temptation -> trial -> release),
- Witness is meaningfully used in exploration + trial,
- save/load survives browser refresh,
- build runs smoothly in Chrome/Firefox/Edge,
- demo feels “small but premium,” not prototype-fragile.

---

## 14) Recommended Next Step

Immediately start with:
1. Phaser TypeScript project scaffold,
2. one-room movement test with final target resolution,
3. dialogue box and state variable plumbing,
4. Witness prototype in a tiny Moon test room.

Once these 4 are stable, scale content production.
