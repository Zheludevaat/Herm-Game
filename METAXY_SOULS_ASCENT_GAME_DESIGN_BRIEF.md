# METAXY: The Soul's Ascent

## Full Game Design Brief

Prepared as a build-ready framework for a premium single-player narrative adventure RPG.

---

## Project-wide Direction Update (Mandatory)

- The project is a **2D retro Game Boy Color-style level-based game** (not a 3D third-person title).
- Visual constraints: limited palette discipline, pixel-art readability, low-resolution silhouettes, tile-based level composition.
- Camera/gamefeel constraints: tight 2D controls, readable hitboxes, fast restart loops, room/level chunking.
- All future design, production, and sourcing decisions must favor this 2D retro format.

---

## 1. Executive Summary

**Game concept:** A premium 2D retro narrative adventure RPG (Game Boy Color-inspired presentation) in which the player guides a newly dead soul through the Metaxy, the seven planetary spheres, and a chain of seductive Plateaus that embody half-truths. The game is built on internal Hermetic metaphysics: the cosmos is a school, not a prison; souls descend through the spheres to acquire garments needed for embodied life; after death, the ascent requires recognizing and releasing those garments; daimons guide but do not solve; and Plateaus are voluntary stopping places where a soul mistakes a partial truth for the whole.

**Core promise:** The player does not level up by collecting stronger gear or larger numbers. The player advances by seeing more clearly, surrendering false identifications, and choosing continuation over comfort.

**Genre blend:** Narrative adventure, environmental exploration, inquiry-driven dialogue RPG, symbolic action, puzzle-trial boss encounters, light systemic immersion.

**Target scope:** 28 to 35 hours for main path, 40 to 50 hours for completionist path, one premium boxed product with future expansion potential.

**Recommended platform and engine:** PC, iPhone, Android; recommended engine: Godot 4 (2D pipeline) or Unity 2D URP.

**Commercial position:** Prestige single-player game for players who enjoy rich worlds, philosophical narrative, emotional companions, and atmospheric traversal. Comparable audience tastes include narrative-first action-adventure, dialogue-rich RPGs, and art-forward contemplative games, but the structure here is uniquely Hermetic and progression is built on release rather than accumulation.

**One-line pitch:**

> A soul dies, meets the being that has always walked beside it, and must pass through beauty, reason, heroism, struggle, mercy, and death itself without mistaking any of them for the destination.

## 2. Canon and Non-Negotiable World Rules

The game must treat the framework as canon. The following rules are not optional.

### 2.1 Cosmology

- The metaphysical hierarchy is: **The One -> Nous -> World Soul -> Seven Spheres -> Sublunary embodied life**.
- The soul descends through the spheres and acquires garments that make embodied life possible.
- The ascent is not an escape from a bad creation. It is a graduation through understanding and release.
- The cosmos is alive, meaningful, and fundamentally educational.

### 2.2 Anti-Gnostic orientation

- The game must not treat matter as evil.
- The body must never be framed as a prison in the game's truth-state.
- A Gnostic reading can appear as a late-game error state or false doctrine within a Plateau, but the game's ontological truth is Hermetic, not Gnostic.

### 2.3 Daimon rules

- Every soul has a daimon.
- The daimon can guide during life through dreams, intuitions, questions, arranged encounters, and discomfort.
- After death, the daimon can accompany the soul in the Metaxy and to thresholds.
- The daimon cannot enter the interior of a Plateau.
- The daimon cannot enter the Governor's testing domain inside a sphere.
- The daimon waits at the boundary and reappears when the soul emerges.

### 2.4 Plateau rules

- Plateaus are not punishments. They are voluntary settlements created by resonance.
- Each Plateau contains a genuine insight mixed with a distortion.
- Souls stay because the Plateau flatters a wound or identity.
- A Plateau can only be exited by recognition and choice, not by force.
- Soft failure in the game is the player choosing to remain. This must be reversible from the meta menu after seeing the consequence.

### 2.5 Sphere rules

- Each sphere is governed by a living intelligence, not a standard boss monster.
- Tests reveal what remains in the soul. They are examinations, not punitive trials.
- Each sphere asks for release of one garment.
- Governors:
  - Moon: **Selenos**
  - Mercury: **Hermaia**
  - Venus: **Kypria**
  - Sun: **Helion**
  - Mars: **Areon**
  - Jupiter: **Jovian**
  - Saturn: **Kronikos**

### 2.6 Reception after death

- The soul is received by the Four Elemental Guardians:
  - **Zephyros**: clarity, orientation
  - **Pyralis**: purification, shock release
  - **Undine**: grief held and soothed
  - **Chthonia**: grounding, ontological stability
- They circle three times. This is a fixed ritual language in the world.

### 2.7 Thematic law

The player must repeatedly feel that:

- partial truths are real but insufficient,
- identity can harden into a trap,
- release is harder than conquest,
- love and participation reveal more than contempt and escape,
- the path upward is a movement into reality, not away from it.

## 3. Product Definition

### 3.1 Working title

**The Hermetic Journey**

### 3.2 Format

- Premium single-player game
- 2D top-down / side-view exploration with cinematic dialogue framing
- No live service
- No multiplayer
- No randomized loot dependency
- No open world sprawl

### 3.3 Business model

- Full premium purchase
- Deluxe edition may include soundtrack, art book, and commentary
- Post-launch content can add additional incarnations or late-game return-by-vow episodes
- No season pass at launch
- No microtransactions

### 3.4 Target audience

**Primary:**

- Players aged 18+
- Narrative-first players
- Art-driven exploration players
- Players interested in metaphysics, philosophy, and spiritual drama

**Secondary:**

- Fans of dialogue-rich RPGs
- Fans of contemplative traversal games
- Players drawn to mythic and symbolic worldbuilding

### 3.5 Rating target

Mature Teen or PEGI 16 equivalent due to:

- death and afterlife themes
- grief, self-deception, despair, guilt
- mild symbolic violence
- existential intensity

## 4. High Concept Experience

The player begins in embodied life, inside a short interactive prologue that establishes three things: what the soul loved, what the soul feared, and what identity the soul mistook for itself. Death occurs early, within the first 20 minutes. The player is received by the Elemental Guardians, meets their daimon, enters the Metaxy, and is introduced to the first choice: move toward the Moon, or drift into a Plateau that already resonates with the soul's unfinished patterns.

Core progression pattern:

1. Threshold arrival
2. Exploration and orientation
3. Plateau temptation or direct continuation
4. Investigation through dialogue, memory, and symbolic encounters
5. Recognition of the garment currently dominating the soul
6. Sphere test
7. Release scene
8. Boundary reunion with the daimon
9. Advance, return, or remain

Major area components:

- a social hub
- one central metaphysical distortion
- 2 to 4 side quests that dramatize that distortion
- one major recognition scene
- one threshold choice
- one climactic test

## 5. Game Pillars

1. **Walk the metaphysics**
2. **Partial truth is the enemy, not evil**
3. **Progress is release**
4. **The daimon is the emotional spine**
5. **The game is challenging without cynicism**
6. **Symbolic gameplay, not abstract essay**
7. **Humor remains alive**

## 6. Player Character Framework

### 6.1 Protagonist model

The protagonist is one soul, but the player authors its mortal surface through a guided prologue.

- Working in-game title: **The Pilgrim**
- Player choices: mortal name, pronouns, one of three callings

### 6.2 Mortal callings

- **Scholar**
  - strength: inquiry
  - shadow: abstraction, over-explanation
- **Caregiver**
  - strength: compassion
  - shadow: savior identity, usefulness addiction
- **Reformer**
  - strength: will and justice
  - shadow: heroism, control, righteousness

### 6.3 Core wound

The soul mistook a garment for its essence and tried to become worthy through that mistake.

### 6.4 Why this structure works

- preserves one authored ascent arc
- makes Plateau resonance personal
- avoids blank-slate protagonist drift
- keeps production manageable with macro reconvergence

### 6.5 The daimon

Working name: **Sophene**

Presentation:

- appears ordinary at first glance
- impossible signature appears in timing/shadow/light behavior
- speaks with patience, warmth, and exactness
- never forces a choice
- knows the soul intimately but not future choices

Functions:

- emotional truth anchor
- boundary companion
- memory prompt
- subtle mirror of what the soul could become without distortion

## 7. Core Story Arc

### Prologue: The Last Day

Length: 15 to 20 minutes.

Goals:

- establish mortal identity
- introduce unresolved relationship
- show dominant garment
- stage ordinary but meaningful death

### Act 0: Reception

- separation from body
- Elemental Guardians circle three times
- silver threshold space
- first Sophene conversation
- tutorials: movement, dialogue, stillness, observation
- first Metaxy glimpse

### Acts I to VII (Questions by sphere)

- **Moon:** What in you is image, and what in you sees the image?
- **Mercury:** Are you using language to reveal, or to evade?
- **Venus:** Do you love what is, or do you want to possess what moves you?
- **Sun:** Who are you when no one is watching?
- **Mars:** What does your strength serve?
- **Jupiter:** What are your systems for?
- **Saturn:** What remains when all structures fail?

### Epilogue options

- ascent toward Nous
- reincarnation
- vow-return service
- soft Plateau ending
- Gnostic false ending (later rejectable)

## 8. Macro Structure and Content Scope

Shipping structure:

- 1 mortal prologue
- 1 reception/tutorial space
- 1 Metaxy connective world
- 7 sphere test spaces
- 7 paired Plateau acts
- 28 to 35 side quests
- 21 major memory scenes
- 7 boundary reunions with Sophene
- 4 full endings plus soft Plateau endings

Runtime goals:

- Mainline: 28 to 35 hours
- Completionist: 40 to 50 hours

## 9. Acts, Zones, and Plateau Pairings

- **Act I: Moon**
  - Major Plateau: The Mirror's Palace
  - Attached district: Material Campus
  - Exit insight: images serve; they do not rule.
- **Act II: Mercury**
  - Major Plateau: The Tower of Reasons
  - Attached district: The House of Inevitable Tea
  - Exit insight: explanation is not being; acceptance can become avoidance.
- **Act III: Venus**
  - Major Plateau: The Eternal Biennale
  - Attached district: The Ladder of Lovers
  - Exit insight: beauty is a window, not a trophy; love is seeing, not owning.
- **Act IV: Sun**
  - Major Plateau: Hall of Illuminated Testimony
  - Attached district: Sanctuary of Radiance
  - Exit insight: truth does not need a protagonist; goodness does not need an audience.
- **Act V: Mars**
  - Major Plateau: Arena of the Strong
  - Attached district: Archive of Perpetual Struggle
  - Exit insight: will is real; it must serve more than motion.
- **Act VI: Jupiter**
  - Major Plateau: Grand Tribunal of Perfect Justice
  - Attached district: The Messianic Camp
  - Exit insight: order must serve persons; mercy and consequence belong together; service is not identity.
- **Act VII: Saturn**
  - Major Plateau: The Avenue of Accepted Fate
  - Attached district: Gnostic Threshold
  - Exit insight: finitude is not proof of imprisonment; letting go is not negation; gratitude opens where contempt seals shut.

## 10. Act-by-Act Detailed Design

Each act includes:

- visual language
- core verbs
- major NPCs
- quest chain
- sphere test setup

(Refer to source framework for full beat-level details if implementing mission scripts.)

## 11. Core Gameplay Loop

### 11.1 Moment-to-moment

1. Traverse symbolic space
2. Notice dissonance
3. Talk and gather memory echoes
4. Use verbs to reveal hidden truth
5. Resolve local quest
6. Increase Clarity and reduce Garment Weight
7. Reach act cracking question
8. Choose release or rationalization
9. Enter Governor trial

### 11.2 Plateau loop

- arrive in profoundly right-feeling place
- participate in routines
- receive rewards
- notice unresolved ache
- create crack in logic
- act on crack
- walk to edge

### 11.3 Sphere loop

- enter alone
- confront symbolic scenario
- use learned verbs in purified form
- answer via play and dialogue
- release garment
- exit to Sophene

## 12. Player Verbs and Mechanical Language

Base verbs:

- Walk
- Observe
- Converse
- Remember
- Still

Sphere verbs:

- **Witness (Moon)**
- **Name (Mercury)**
- **Attune (Venus)**
- **Expose (Sun)**
- **Stand (Mars)**
- **Weigh (Jupiter)**
- **Release (Saturn)**

Each verb must work across traversal, dialogue, questing, puzzles, and Governor trials.

## 13. Core Systems

- **Coherence:** survivability/presence resource (replaces health)
- **Clarity:** central growth currency (truth-based progression)
- **Garment Weight:** seven identity loads influencing systems and narrative
- **Resonance Profile:** hidden matrix shaping invitations/reactions/endings
- **Memory Lattice:** 21 memory shards, 3 per act
- **Daimon Bond:** trust/honesty relationship with Sophene

## 14. Encounters, Failure, and Difficulty

Encounter categories:

- Dissonance encounters
- Resonance duels
- Governor trials

Difficulty modes:

- Story
- Standard
- Contemplative Challenge

Accessibility principle: difficulty should never mean opacity.

## 15. Dialogue System

Inquiry wheel actions:

- Observe
- Ask
- Name
- Challenge
- Confess
- Release
- Remain silent

Silence is a real and sometimes required option.

## 16. Quest Design Framework

Quest categories:

- Cracking Question Quests (mandatory)
- Soul Case Quests (optional/substantial)
- Memory Quests
- Metaxy Interludes

Quest rule: each quest must reveal garment dynamics, expose distortion, deepen relationship, or alter readiness for next act.

## 17. Progression, Economy, and Rewards

No loot treadmill, no crafting bloat, no store-based systems.

Includes:

- Clarity currency
- Memory Shards
- Relics with temptation tradeoffs
- perception/refinement-style upgrades
- soul-state cosmetics

## 18. Endings and State Logic

- **True ending:** Ascent toward Nous
- **Reincarnation ending**
- **Vow-return ending**
- **Soft Plateau ending**
- **False Gnostic ending** (revealed as another stopping place)

## 19. UI and UX

Core principles:

- minimal and legible
- calm-state HUD suppression
- emotional-scene meter restraint

Primary HUD elements:

- Coherence arc
- Clarity pips
- contextual verbs
- subtle garment ring

Includes full accessibility suite.

## 20. Art Direction

Style: painterly metaphysical realism.

Each domain should have unique shape language, palette, and symbolic architecture.

## 21. Audio Direction

Music should feel liturgical, intimate, and psychologically exact.

Silence is a gameplay tool, especially in late Saturn trials.

## 22. Technical Design and Implementation

Recommended engine: **Godot 4** (primary) or **Unity 2D URP** (fallback).

Narrative scripting: **Ink or equivalent** integrated solution.

Prototype first:

- 2D traversal, tilemap collision, and room streaming
- inquiry-wheel dialogue
- Coherence and Clarity systems
- Witness + Name verbs
- one Plateau hub
- one Governor trial
- one Sophene reunion

## 23. Production Plan

- Team size: 65 to 90
- Pre-production: 8 to 10 months
- Production: 20 to 24 months
- Alpha: 4 months
- Beta/certification: 3 to 4 months
- Total: ~35 to 42 months

Vertical slice target: full Act I loop.

## 24. Narrative Bible Rules

Tone: humane, exact, spiritually serious, with warmth and irony.

Avoid: nihilism, generic prophecy language, reducing systems to exposition, or sinner-trial framing.

## 25. Risks and Mitigations

Core risks addressed:

1. Too abstract to play
2. Too literary to be game-like
3. Plateau repetition
4. Overwritten dialogue
5. Gnostic misread
6. Didactic ending
7. Scope creep

## 26. Shipping Content Checklist

Critical path, side content, and polish items are defined as production gates.

## 27. Final Creative Recommendation

Build it as a **release fantasy**, not a combat power fantasy.

Player fantasy:

- I am seen all the way through.
- I learn what I have been carrying.
- I stop mistaking the garment for myself.
- I continue.

## 28. Appendix A: Canon Extraction Summary

Immutable truths:

- The One emanates Nous.
- Nous contains the Forms.
- World Soul mediates into living cosmos.
- Descent order: Saturn, Jupiter, Mars, Sun, Venus, Mercury, Moon.
- Souls descend to learn and acquire garments.
- Ascent requires release.
- Cosmos is school, not prison.
- Daimons guide but do not compel.
- Plateaus are partial-truth identity settlements.
- Governors test readiness, not punish worth.
- Gratitude and participation open ascent.

## 29. Appendix B: Recommended Build Priorities

If constrained, cut in this order:

1. attached district complexity (not core Plateau)
2. side quest count (not act count)
3. cinematic count (not boundary reunions)
4. cosmetic systems (not inquiry systems)
5. optional endings (after protecting ascent + reincarnation)

Do not cut:

- Sophene scenes
- Governor trials
- Elemental reception
- Memory lattice
- garment system
- Hermetic truth-state
