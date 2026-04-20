# METAXY — Free/Open-Source Sourcing Plan

This document identifies which parts of development and production can be sourced from free/open-source tools, assets, frameworks, and workflows while preserving the premium quality target.

> Scope: practical choices for a 2D retro Game Boy Color-style pipeline (pixel art, tilemaps, sprite animation, level progression).

---

## 1) Guiding Policy

- Prefer open-source for **pipeline/tooling**, **automation**, **infrastructure**, and **internal libraries**.
- Use open/free content sources for **prototyping** and **placeholder production**, then selectively replace with bespoke premium assets where artistic uniqueness is mandatory.
- Treat licenses as production constraints:
  - keep a license manifest,
  - avoid copyleft contamination in shipped game code unless intentionally accepted,
  - track attribution obligations per dependency.

---

## 2) What Can Be Reliably Pulled from Free/Open Source

## 2.1 Project Infrastructure & DevOps (High confidence)

These are strong candidates for immediate adoption.

- Version control: Git + Git LFS.
- CI/CD: GitHub Actions / GitLab CI / Jenkins.
- Artifact/build orchestration: Buildkite alternatives, self-hosted runners.
- Task tracking + docs: OpenProject, Wiki.js, MkDocs.
- Static analysis + linting frameworks for script layers.

Why open-source works here:

- commodity problem space,
- low artistic differentiation,
- high maintainability ROI.

## 2.2 Narrative Authoring & Data Pipeline (High confidence)

- Ink (open-source) for branching narrative authoring.
- Open-source JSON/YAML schema validators for quest/state data.
- Localization pipeline helpers (open-source CLI tooling, PO/XLIFF tools).
- Diff/merge helpers for dialogue files.

Use case in METAXY:

- branching dialogue with heavy state tags,
- deterministic content validation in CI.

## 2.3 QA Automation & Test Harnesses (High confidence)

- Test reporting dashboards (Allure, ReportPortal OSS options).
- Fuzz/property-based testing libs for state-machine validation.
- Save-game regression harness scripts in Python.
- Screenshot diff tools for UI regression.

## 2.4 Build Toolchain & Developer Utilities (High confidence)

- Python ecosystem for content transforms and validators.
- ffmpeg for media conversion.
- ImageMagick for batch image processing.
- Blender CLI for automated asset processing tasks.

## 2.5 Telemetry/Observability Backends (Medium–high confidence)

- OpenTelemetry collectors.
- Grafana + Prometheus + Loki stack.
- Metabase/Superset for analytics visualization.

Caveat: compliance, privacy, and hosting complexity must be owned internally.

---

## 2.6 Open-source sprite/code libraries for 2D retro production (Direct answer)

Yes — there are solid open-source options you can pull from to save time:

- **Kenney assets (CC0)**: large free sprite/tile/UI sets for prototyping and some shippable elements with restyling.
- **OpenGameArt (mixed licenses)**: sprite sheets, tilesets, VFX, and SFX; requires strict license filtering and attribution tracking.
- **Liberated Pixel Cup assets (CC-BY-SA/GPL variants)**: useful for character animation references and placeholders.
- **Godot open-source addons**:
  - dialogue managers,
  - state machine helpers,
  - platformer/top-down controller templates,
  - tilemap workflow extensions.
- **MonoGame/FNA ecosystem examples**: robust 2D sprite control code patterns if building custom C# runtime logic.

Recommended usage pattern:

1. Pull open assets for prototype velocity.
2. Tag assets by license and replacement priority.
3. Keep hero/brand-defining art bespoke before beta/content lock.

## 3) What Can Be Partially Sourced from Free/Open Source

## 3.1 Art Production Tools (Very strong for pipeline, mixed for final content)

- **Can source freely/openly:**
  - Blender (modeling, rigging, animation support tasks),
  - Krita / GIMP / Inkscape for concept and paint-over workflows,
  - Material authoring helpers and texture utilities.
- **Should remain bespoke for final quality:**
  - hero characters,
  - Governors,
  - signature environments,
  - key cinematic shots,
  - unique iconography tied to metaphysical themes.

Rationale: toolchain can be open; final visual identity must stay distinct.

## 3.2 Audio & Music (Mixed confidence)

- **Can source freely/openly:**
  - DAWs/utilities (e.g., Ardour, Audacity),
  - synthesis/sound design plugins with permissive licenses,
  - open-source middleware helpers for processing.
- **Use with caution:**
  - stock/open music packs for final score (risk of generic feel),
  - open SFX libraries without strict provenance.

Recommendation:

- use open libraries for prototyping and temp tracks,
- commission/custom-produce final leitmotifs and Governor signatures.

## 3.3 Animation/Mocap Supporting Stack (Medium confidence)

- Open-source retargeting and cleanup scripts.
- Blender-based retarget/cleanup workflows.
- Free motion datasets for prototype blocking.

Keep final performance capture and principal character animation curated/bespoke.

## 3.4 UI & Font Resources (Medium confidence)

- Open-source UI icon sets for prototypes.
- Open-licensed fonts with readability and language coverage.

Final UI should undergo brand pass to avoid “template” look.

---

## 4) What Should Generally NOT Be Sourced as-is from Free/Open Source

## 4.1 Core Narrative Writing and Final Dialogue

- Must remain original due to tone, philosophical coherence, and canon fidelity.
- Open text corpora can inform research, not final authored voice.

## 4.2 Signature Worldbuilding Content

- Plateau culture writing,
- Sophene voice scenes,
- Governor trials,
- ending sequences,
- key memory shards.

These are product-defining differentiators and should be authored internally.

## 4.3 Hero Art and Brand-Defining Assets

- Hero models, distinctive shaders, final key art, and cinematic compositions should be custom.

## 4.4 Licensed-Risk Assets with Unclear Provenance

- Avoid scraped packs, uncertain “free” repositories, or unclear attribution chains.

---

## 5) Recommended Sourcing Matrix (Build vs. Buy vs. Open)

- **Open-source first:**
  - CI/CD, data validation, scripting, telemetry stack, automation.
- **Hybrid (open + custom):**
  - narrative pipeline, UI framework, QA tooling, audio processing.
- **Custom-first:**
  - story content, final art direction, cinematic presentation, key audio identity.

---

## 6) Immediate Actionable Task List

## 6.1 Week 1 License & Provenance Setup

- [ ] Create `THIRD_PARTY_LICENSES.md` with dependency inventory.
- [ ] Define accepted licenses (e.g., MIT/BSD/Apache-2.0 preferred).
- [ ] Define restricted licenses requiring legal review.
- [ ] Add “source + license + attribution” fields to asset import checklist.

## 6.2 Week 2 Toolchain Baseline

- [ ] Stand up open-source CI pipeline and artifact retention.
- [ ] Add schema validators for dialogue/quest content.
- [ ] Add automated save-state regression scripts.
- [ ] Integrate observability stack for nightly builds.

## 6.3 Week 3 Prototype Content Strategy

- [ ] Tag all prototype assets as `TEMP_OPEN` or `FINAL_CUSTOM`.
- [ ] Replace ambiguous-license placeholders.
- [ ] Build replacement backlog for all `TEMP_OPEN` assets required before beta.

## 6.4 Ongoing Governance

- [ ] Dependency review every sprint.
- [ ] License scan in CI on each release branch.
- [ ] Attribution bundle generation for shipped builds.

---

## 7) Quality and Legal Guardrails

- No asset enters production branch without source provenance.
- No dependency enters runtime without license classification.
- No final scene ships with unresolved placeholder content unless explicitly waived.
- Keep an “Open-source risk board” with owner + due date for each flagged item.

---

## 8) Bottom Line for METAXY

You can pull a **large percentage of development and production infrastructure** from free/open-source sources (tooling, pipelines, validation, QA, observability, utilities) with little creative downside.

You should **not** outsource the game’s identity-defining layers (writing voice, Governor encounters, Sophene scenes, hero art direction, final score identity) to generic open assets if premium quality and canonical integrity are priorities.

Best strategy: **Open-source for the factory, bespoke for the soul.**
