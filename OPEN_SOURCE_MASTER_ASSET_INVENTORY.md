# METAXY — Unabridged Open-Source Asset & Systems Inventory (2D Retro GBC)

Purpose: comprehensive prediction list of everything we might need for production, with explicit notes on what can come from open/free sources.

Use this as the master procurement + replacement tracker.

---

## 0) Usage Rules

- `OS-Ship`: can ship from open-source/free source if license is valid and quality bar is met.
- `OS-Temp`: can use for prototyping but expected bespoke replacement.
- `Custom`: should be custom-built for final product identity.

Every imported item must track:

- source URL
- author/publisher
- license
- attribution requirement
- modification status
- usage scope (prototype/shipping)

---

## 1) Core Visual Asset Inventory (Sprites, Tiles, FX)

## 1.1 Player & Character Sprites

- [ ] Player idle animations (all directions) — `OS-Temp`
- [ ] Player walk/run cycles — `OS-Temp`
- [ ] Player interaction animations (inspect, push, pull, kneel, release) — `OS-Temp`
- [ ] Player emotional states (hurt, relieved, obscured) — `OS-Temp`
- [ ] Player outfit variants by act progression — `Custom`
- [ ] Daimon (Sophene) base sprite set — `Custom`
- [ ] Sophene “impossible signature” VFX overlays — `Custom`
- [ ] Elemental Guardians sprite sets (Zephyros, Pyralis, Undine, Chthonia) — `Custom`
- [ ] Sphere Governors sprite/portrait forms (7 total) — `Custom`
- [ ] Major named NPC sprite sets per act — `OS-Temp -> Custom`
- [ ] Minor resident NPC archetypes (crowd variants) — `OS-Ship` (restyled)

## 1.2 Enemy/Encounter Sprites (non-traditional combat entities)

- [ ] Dissonance swarm entities (abstract thought forms) — `OS-Temp`
- [ ] Resonance duel opponents (act-specific) — `Custom`
- [ ] Hazard sprites (light cones, rhetorical storms, mirrored ripples) — `OS-Temp -> Custom`
- [ ] Encounter telegraph sprites/icons — `OS-Ship`

## 1.3 Tilesets & Environment Modules (Act by Act)

- [ ] Metaxy hub base tileset (paths, thresholds, void edges) — `OS-Temp -> Custom`
- [ ] Moon tileset pack (mirror halls, silver gardens, water floors) — `OS-Temp -> Custom`
- [ ] Mercury tileset pack (diagram halls, notes, clockwork motifs) — `OS-Temp -> Custom`
- [ ] Venus tileset pack (galleries, arches, floral courtyards) — `OS-Temp -> Custom`
- [ ] Sun tileset pack (radiant courts, testimony halls) — `OS-Temp -> Custom`
- [ ] Mars tileset pack (barricades, arenas, ironworks) — `OS-Temp -> Custom`
- [ ] Jupiter tileset pack (tribunal architecture, civic plazas) — `OS-Temp -> Custom`
- [ ] Saturn tileset pack (bare stone, winter groves, threshold ruins) — `OS-Temp -> Custom`
- [ ] Generic interiors (rooms, corridors, service spaces) — `OS-Ship`
- [ ] Utility tiles (stairs, doors, ladders, railings) — `OS-Ship`
- [ ] Collision-only helper tiles — `OS-Ship`

## 1.4 Props & Interactive Objects

- [ ] Memory shard pickups (21 visual variants) — `Custom`
- [ ] Relic objects (notebook, ring, badge, medical tag, seal, review frame, family object) — `Custom`
- [ ] Puzzle devices (mirrors, scales, inscriptions, braziers, registers) — `OS-Temp -> Custom`
- [ ] Signage, banners, codex terminals, witness altars — `OS-Temp -> Custom`
- [ ] Ambient props (books, crates, lamps, benches, planters, vases) — `OS-Ship`

## 1.5 VFX / Pixel Effects

- [ ] Coherence hit/depletion FX — `Custom`
- [ ] Clarity gain FX — `Custom`
- [ ] Garment weight aura overlays (7 channels) — `Custom`
- [ ] Witness overlay and layer reveal shaders — `Custom`
- [ ] Name glyph reveal/truth-line VFX — `Custom`
- [ ] Attune pulse/radius FX — `Custom`
- [ ] Expose glare strip effect — `Custom`
- [ ] Stand impact/parry and refusal FX — `OS-Temp -> Custom`
- [ ] Weigh consequence branch visualization FX — `Custom`
- [ ] Release dissolve/quieting FX — `Custom`
- [ ] Environmental ambient FX (dust, motes, rain, leaves, fog) — `OS-Ship`

## 1.6 UI Sprites & Icons

- [ ] Coherence meter frames/fills — `Custom`
- [ ] Clarity pips/icons — `Custom`
- [ ] Inquiry wheel icons (Observe/Ask/Name/Challenge/Confess/Release/Silence) — `Custom`
- [ ] Verb prompt icons (7 sphere verbs) — `Custom`
- [ ] Menu tab icons — `OS-Ship` (restyled)
- [ ] Accessibility icons — `OS-Ship`
- [ ] Input glyph packs (keyboard/controller/mobile touch) — `OS-Ship`

## 1.7 Portraits, Cut-ins, and Narrative Panels

- [ ] Key story portrait set (Pilgrim, Sophene, Governors) — `Custom`
- [ ] Act NPC portrait library — `OS-Temp -> Custom`
- [ ] Memory flashback panel assets — `Custom`
- [ ] Ending panel art — `Custom`

---

## 2) Animation Inventory

## 2.1 Character Animation Data

- [ ] 4/8-direction locomotion for player
- [ ] interaction loops
- [ ] stumble/obscuration loops
- [ ] stillness meditation loops
- [ ] each verb-specific animation states
- [ ] NPC ambient loops (sit, converse, gesture, pray, archive, patrol)

Sourcing: sprite templates and placeholder cycles can be `OS-Temp`; final animation timing/style should be `Custom`.

## 2.2 VFX Animation Sheets

- [ ] hit spark sheets
- [ ] aura loops
- [ ] dissolve/reveal loops
- [ ] screen-space overlays

Sourcing: generic effect sheets `OS-Ship` where style-compatible.

---

## 3) Audio Inventory

## 3.1 Music

- [ ] Main theme
- [ ] Metaxy exploration loop
- [ ] 7 act ambient suites
- [ ] 7 Plateau social themes
- [ ] 7 Governor trial themes
- [ ] memory scene motifs
- [ ] ending suites (true, reincarnation, vow-return, soft, false)

Sourcing recommendation: temp music can be `OS-Temp`; final score is `Custom`.

## 3.2 Sound Effects

- [ ] UI navigation sounds
- [ ] dialogue select/confirm sounds
- [ ] movement/footstep sets by surface
- [ ] interaction sounds by prop category
- [ ] spell/verb ability sounds
- [ ] encounter telegraph/warning sounds
- [ ] trial event sounds
- [ ] ambient location loops (wind, room tone, crowd murmur)

Sourcing recommendation: many can be `OS-Ship` if license/provenance is clean.

## 3.3 Voice Assets

- [ ] placeholder VO for timing/prototype
- [ ] final VO recordings (player, Sophene, Governors, key NPCs)
- [ ] effort sounds/breaths/reactions

Sourcing recommendation: placeholder TTS can be open tools; final VO is `Custom`.

---

## 4) Narrative/Data Content Inventory

## 4.1 Dialogue & Script Data

- [ ] mainline dialogue scripts
- [ ] side quest dialogue scripts
- [ ] branching conditional responses
- [ ] silence nodes
- [ ] hint lines for obscuration assists

Sourcing: tools/frameworks open-source; final authored text `Custom`.

## 4.2 Quest Data

- [ ] critical path quest nodes
- [ ] side quest node graphs
- [ ] failure/recovery branch states
- [ ] reward and state mutation tables

Sourcing: schema/tooling open-source; content definitions mostly `Custom`.

## 4.3 Codex & Lore Data

- [ ] sphere entries
- [ ] governor entries
- [ ] plateau entries
- [ ] relic entries
- [ ] question entries

Sourcing: `Custom` text, open-source tooling for pipelines.

---

## 5) Code & Systems Inventory (Open-source Reuse Candidates)

## 5.1 Engine/Runtime Layer

- [ ] 2D renderer pipeline
- [ ] tilemap loading and collision
- [ ] animation state machine
- [ ] camera control + shake + deadzone
- [ ] save/load serialization
- [ ] input abstraction

Sourcing: mostly from engine + open addons (`OS-Ship` with review).

## 5.2 Gameplay Systems

- [ ] dialogue runtime
- [ ] quest state machine
- [ ] Coherence/Clarity managers
- [ ] garment weight modifiers
- [ ] resonance profile calculator
- [ ] memory lattice tracker
- [ ] daimon bond tracker
- [ ] encounter scripting framework

Sourcing: scaffolding `OS-Temp`; final system logic `Custom`.

## 5.3 Tooling and Authoring

- [ ] dialogue validators
- [ ] quest graph validators
- [ ] localization extractor/importer
- [ ] save migration tools
- [ ] sprite atlas builders
- [ ] batch importers

Sourcing: high `OS-Ship` confidence.

## 5.4 Build/QA Infrastructure

- [ ] CI runners
- [ ] artifact packaging
- [ ] regression scripts
- [ ] screenshot diff checks
- [ ] perf telemetry collectors
- [ ] crash reporting integrations

Sourcing: high `OS-Ship` confidence.

---

## 6) UI/UX Inventory

- [ ] HUD components (coherence, clarity, prompts)
- [ ] inventory/relic panels
- [ ] codex screens
- [ ] accessibility menu
- [ ] save/load screens
- [ ] settings pages
- [ ] dialogue wheel interface
- [ ] controller/touch overlays

Sourcing:

- base widgets and iconography can be `OS-Temp`/`OS-Ship`
- final branded skin/layout motion should be `Custom`

---

## 7) Localization & Accessibility Inventory

- [ ] localization string database
- [ ] font families for extended language sets
- [ ] subtitle rendering styles
- [ ] colorblind palette options
- [ ] dyslexia-friendly font option
- [ ] audio captions and silence cues
- [ ] remapping presets

Sourcing: tooling/fonts can be `OS-Ship`; tuning and authored metadata are `Custom`.

---

## 8) Marketing/Store/Community Asset Inventory

- [ ] key art
- [ ] capsule images (Steam/mobile)
- [ ] animated GIF snippets
- [ ] trailer B-roll capture scenes
- [ ] logo lockups
- [ ] press kit page templates

Sourcing: template kits can be `OS-Temp`; shipping brand assets should be `Custom`.

---

## 9) Open-Source Source Pools to Mine

## Art/Sprites

- Kenney (CC0 packs)
- OpenGameArt (license-filtered)
- Liberated Pixel Cup assets
- Itch free packs with explicit license

## Audio

- Freesound (license-filtered)
- OpenGameArt audio
- Sonniss GDC free bundles (check terms)

## Code/Frameworks

- Godot open-source addons (dialogue, FSM, save/load, camera)
- Ink runtime/tooling
- MonoGame/FNA examples for sprite control patterns

## Toolchain

- Blender, Krita, Aseprite-compatible exporters, TexturePacker alternatives
- ffmpeg, ImageMagick, Python ecosystem tools
- OpenTelemetry/Grafana/Prometheus/Loki stacks

---

## 10) Predicted Missing Items Teams Forget (Include Early)

- [ ] placeholder fail-state art/UX assets
- [ ] loading transition sprites
- [ ] debug visualization icons
- [ ] QA map markers and test room tiles
- [ ] controller rumble tuning tables
- [ ] fallback fonts for unsupported glyphs
- [ ] legal attribution scene or credits block
- [ ] end-card assets for each ending branch
- [ ] save slot thumbnails and corruption recovery UI
- [ ] platform-specific safe-area UI variants

---

## 11) Recommended Procurement Sequence

1. Acquire open-source pipeline/tooling first.
2. Acquire prototype sprite/tile/audio packs for vertical slice.
3. Build license manifest and replacement tracker.
4. Replace all identity-critical assets with bespoke versions by beta.
5. Freeze only provenance-clean assets at release candidate.

---

## 12) Bottom Line

Yes — we can source a very large amount of sprites, code scaffolding, audio placeholders, tools, and infrastructure from open/free ecosystems.

To preserve premium quality:

- use open-source for speed and production leverage,
- reserve identity-defining content (hero art, Sophene, Governors, endings, signature motifs) for custom production.
