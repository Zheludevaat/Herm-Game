# METAXY — Codex-Optimized Full Game Build Plan (Task List)

This is the production task list for building a full, high-quality version of **METAXY: The Soul's Ascent** from prototype through launch.

It is optimized for execution by iterative AI-assisted development (Codex + human review): small vertical slices, strict acceptance criteria, data-first content pipelines, and continuous playtest validation.

---

## Format Mandate (Project-Wide)

- This build plan targets a **2D retro Game Boy Color-style, level-based game**.
- All milestones assume pixel-art production, tilemap workflows, sprite animation, and room/level progression.
- Any task that implies 3D third-person production should be converted to equivalent 2D implementation work.

---

## 0) Operating Rules (Non-Negotiable)

- Canon truth-state stays Hermetic (cosmos as school, not prison).
- Progression is release/recognition, not loot/stat inflation.
- Daimon and Governor constraints are system-enforced, not only narrative text.
- Every shipped task must map to at least one of:
  - core loop quality,
  - canonical fidelity,
  - production scalability,
  - player readability/accessibility.

---

## 1) Delivery Strategy

## Milestone Sequence

1. **M0 Foundations** — engine, CI, state architecture, authoring pipeline.
2. **M1 Vertical Slice (Act I complete)** — prove game feel + thesis.
3. **M2 Core Systems Lock** — all verbs/systems generalized and reusable.
4. **M3 Content Production (Acts II–VII)** — scalable act factory.
5. **M4 Alpha** — full game playable end-to-end.
6. **M5 Beta** — content final, performance + bug + accessibility polish.
7. **M6 Gold Master** — cert-ready release candidate.

## Cadence

- 2-week sprints.
- Each sprint ends with:
  - playable build,
  - regression pass,
  - narrative/state validation,
  - updated risk register.

---

## 2) M0 Foundations (Weeks 1–8)

## 2.1 Technical Foundation

- [ ] Create 2D engine project architecture (Godot 4 recommended) for traversal, dialogue, state, UI, quests, and encounters.
- [ ] Set up deterministic save schema versioning and migration layer.
- [ ] Build content tag taxonomy:
  - garment relevance,
  - sphere/plateau zone IDs,
  - dialogue intent,
  - ending flags,
  - silence-compatible lines.
- [ ] Implement CI:
  - build validation,
  - data linting (missing tags/invalid IDs),
  - smoke test map load.

## 2.2 Narrative/Data Pipeline

- [ ] Integrate Ink (or equivalent) with variable bridge to gameplay state.
- [ ] Build dialogue compiler checks:
  - unreachable nodes,
  - invalid conditions,
  - unresolved localization keys.
- [ ] Define quest-node JSON schema + validation tools.

## 2.3 Core Runtime Systems (V1)

- [ ] Coherence system skeleton (resource + obscuration reset).
- [ ] Clarity earn/spend hooks.
- [ ] Garment Weight data model (7 channels, weighted modifiers).
- [ ] Resonance Profile matrix + hidden scoring.
- [ ] Memory Lattice structure (21 shards scaffold).
- [ ] Daimon Bond variable channel.

## 2.4 UX Foundation

- [ ] Input remapping framework.
- [ ] Subtitle framework (speaker colors + scaling).
- [ ] UI state machine (calm, exploration, encounter, dialogue, trial).
- [ ] Accessibility menu skeleton and persisted profile settings.

## Exit Criteria (M0)

- [ ] Fresh profile can boot, save/load, and preserve all core state fields.
- [ ] Dialogue + quest data fail fast in CI on schema errors.
- [ ] One graybox tilemap level supports traversal, dialogue, and obscuration reset.

---

## 3) M1 Vertical Slice — Act I End-to-End (Weeks 9–18)

## 3.1 Playable Scope

- [ ] Prologue (3 calling variants) with early death sequence.
- [ ] Reception tutorial with Four Elemental Guardians ritual.
- [ ] First Sophene conversation + boundary behavior rules.
- [ ] Metaxy traversal segment to Act I threshold.
- [ ] Mirror's Palace hub with one side quest and one cracking-question quest.
- [ ] Moon Governor trial (Selenos) with pass/fail loops.
- [ ] Post-trial reunion bridge with Sophene.

## 3.2 Mechanics in Slice

- [ ] Base verbs: Walk, Observe, Converse, Remember, Still.
- [ ] Moon verb: Witness (works in traversal/dialogue/puzzle/trial).
- [ ] Coherence tuning v1 for recovery + obscuration readability.
- [ ] Garment Weight impact on dialogue variants + traversal feel.

## 3.3 Quality Gates

- [ ] 60 FPS target on target PC/mobile profile with pixel-perfect rendering.
- [ ] Zero blocker bugs in critical path.
- [ ] New players can explain core thesis after 60 minutes (playtest KPI).

## Exit Criteria (M1)

- [ ] Complete Act I loop playable without dev commands.
- [ ] Canonical rules demonstrably enforced by systems.
- [ ] Stakeholders approve “fun + clarity + fidelity” baseline.

---

## 4) M2 Core Systems Lock (Weeks 19–30)

## 4.1 Systems Completion

- [ ] Implement remaining sphere verbs:
  - Name, Attune, Expose, Stand, Weigh, Release.
- [ ] Ensure each verb has reusable APIs for:
  - traversal interaction,
  - dialogue action,
  - puzzle logic,
  - trial mechanics.
- [ ] Implement relic system and temptation trade-offs.
- [ ] Implement codex unlocks based on lived encounters only.

## 4.2 Encounter Framework

- [ ] Dissonance encounter framework + authoring templates.
- [ ] Resonance duel framework (timing + dialogue hybrid).
- [ ] Governor trial framework (act-specific logic + reusable shell).

## 4.3 Progression & End-State Logic

- [ ] Full ending state graph (True/Reincarnation/Vow-Return/Soft/False).
- [ ] Meta “Return to Last Threshold” flow.
- [ ] Hint system for repeated obscuration (optional).

## Exit Criteria (M2)

- [ ] All core systems feature-complete and stable.
- [ ] Designers can author new quest/encounter content without engineering support.

---

## 5) M3 Content Production Factory (Acts II–VII) (Weeks 31–62)

Repeat per act with a strict “Act Factory” checklist.

## 5.1 Per-Act Task Template (Run 6 times)

- [ ] Threshold district graybox -> art pass.
- [ ] Major Plateau hub + attached district implemented.
- [ ] 2–4 side quests implemented and state-tested.
- [ ] 3 memory shards authored + integrated.
- [ ] Cracking question quest complete.
- [ ] Governor trial implemented + tuned.
- [ ] Sophene boundary reunion scene integrated.
- [ ] Act-specific codex entries gated by encounter triggers.
- [ ] Audio motif + ambiance pass.
- [ ] Accessibility and readability pass.

## 5.2 Shared Production Tasks

- [ ] Build “plateau distortion matrix” to prevent tonal repetition.
- [ ] Run narrative compression pass (avoid overwritten dialogue).
- [ ] Validate every quest has mechanical consequence.
- [ ] Ensure one joyful memory shard per act.

## Exit Criteria (M3)

- [ ] Acts II–VII playable in sequence with branching state persistence.
- [ ] All seven Governor trials complete and beatable.

---

## 6) M4 Alpha (Weeks 63–78)

## 6.1 Content Complete Requirements

- [ ] All critical path content integrated.
- [ ] All endings playable from valid state paths.
- [ ] Full codex content integrated with unlock logic.
- [ ] VO temp/final coverage for critical path scenes.

## 6.2 Alpha Stabilization Tasks

- [ ] Narrative state audit (dead flags, conflicting conditions, softlocks).
- [ ] Performance pass (tile streaming hitches, overdraw, draw-call batching, memory).
- [ ] Difficulty pass across Story/Standard/Contemplative.
- [ ] Accessibility parity pass on all Governor trials.

## Exit Criteria (M4)

- [ ] Full game completable without progression blockers.
- [ ] Crash rate within alpha target threshold.

---

## 7) M5 Beta & Certification (Weeks 79–92)

- [ ] Bug triage burn-down with daily tracking.
- [ ] Localization lock + integration testing.
- [ ] Final UI polish and consistency checks.
- [ ] Audio final mix, silence cue validation, subtitle timing QC.
- [ ] Platform compliance and certification prep.
- [ ] Marketing capture build with spoiler-safe pathways.

## Exit Criteria (M5)

- [ ] No cert blockers.
- [ ] No P0/P1 unresolved defects.
- [ ] Final narrative and systems sign-off.

---

## 8) M6 Gold Master & Launch Readiness (Weeks 93–96)

- [x] Gold candidate regression suite pass (scripted gate: `python scripts/run_m6_regression_suite.py`).
- [x] Save compatibility verification from prior beta builds (fixture coverage in `tests/fixtures/` + `tests/test_level_and_save.py`).
- [x] Final telemetry/privacy checks (`M6_TELEMETRY_PRIVACY_CHECKLIST.md`).
- [ ] Launch day patch branch prepared.
- [x] Runbook for live hotfix triage (`M6_LAUNCH_RUNBOOK.md`).

---

## 9) Cross-Discipline Task Backlog (Always Active)

## Design

- [ ] Maintain question-first act design docs.
- [ ] Ensure every mechanic expresses partial-truth tension.
- [ ] Audit for progression-by-release adherence.

## Narrative

- [ ] Keep Sophene voice consistency sheet and lint pass.
- [ ] Add “what truth/what avoidance” annotation per scene.
- [ ] Enforce concise line-length and silence cadence.

## Engineering

- [ ] Maintain deterministic state replay test.
- [ ] Expand automated tests for branching conditions.
- [ ] Keep build times and cook times within sprint targets.

## Art/Audio

- [ ] Maintain act-specific style bible deltas.
- [ ] Track readability in high-symbolism scenes.
- [ ] Ensure each Governor has distinct visual/audio signature.

## QA

- [ ] Branch-path matrix testing per act.
- [ ] Accessibility scenario checklists.
- [ ] Soak tests for save/load across long sessions.

---

## 10) Codex-Oriented Implementation Rules (How Tasks Are Executed)

To maximize reliable AI-assisted output quality:

- Work in vertical slices, not giant rewrites.
- Every ticket must include:
  - objective,
  - changed files/modules,
  - acceptance tests,
  - rollback plan.
- Prefer data-driven authoring over hardcoded logic.
- Add guardrails before adding content volume.
- Never add new mechanics without explicit mapping to game pillars.

Definition of Done for each ticket:

- [ ] Feature implemented.
- [ ] Automated/static checks pass.
- [ ] Manual playtest scenario passed.
- [ ] Telemetry/logging hooks present (if applicable).
- [ ] Documentation updated.

---

## 11) Risk Register (Actionable)

- **Abstraction risk:** mitigate with concrete interaction goals per scene.
- **Dialogue bloat risk:** mitigate with line budgets + silence alternatives.
- **State explosion risk:** mitigate with schema validation + replay tests.
- **Repetitive acts risk:** mitigate with plateau distortion matrix and act-specific mechanic emphasis.
- **Canonical drift risk:** mitigate with canon checklist in PR template.
- **Performance risk:** mitigate with per-sprint profiling budgets.

---

## 12) Immediate Next 12 Sprint Task List (Execution Start)

## Sprints 1–2

- [ ] Project scaffolding, CI, save schema, dialogue integration.
- [ ] Graybox tilemap traversal + camera rails + input remap baseline.

## Sprints 3–4

- [ ] Coherence/Clarity/Garment systems v1.
- [ ] Inquiry-wheel dialogue UI and variable wiring.

## Sprints 5–6

- [ ] Prologue + reception tutorial implementation.
- [ ] Sophene interaction framework + boundary constraints.

## Sprints 7–8

- [ ] Mirror's Palace hub and first quest content.
- [ ] Witness verb full integration.

## Sprints 9–10

- [ ] Selenos trial prototype to production quality.
- [ ] Act I polish + usability + first external playtests.

## Sprints 11–12

- [ ] M1 hardening and sign-off.
- [ ] M2 planning and backlog decomposition for Acts II–VII.

---

## 13) Production KPIs

- Time to first meaningful choice: < 10 minutes.
- First clear understanding of core thesis: < 60 minutes.
- Mainline completion target: 28–35 hours.
- Completionist target: 40–50 hours.
- Critical path blocker defects at beta: 0.
- Crash-free sessions at release target: 99%+.

---

## 14) Ownership Map (Recommended)

- **Game Director:** canonical fidelity + pillar enforcement.
- **Narrative Director:** dialogue system quality + arc cohesion.
- **Design Lead:** verbs, encounter quality, progression loops.
- **Tech Director:** architecture, tooling, performance, CI.
- **Production Lead:** milestone delivery and scope control.
- **QA Lead:** branching integrity + accessibility regression.

---

## 15) Final Instruction to Team

When scope pressure rises, protect in this order:

1. Sophene boundary scenes
2. Governor trials
3. Garment/Clarity/Coherence systems
4. Memory lattice
5. Act count integrity

Cut aesthetics or optional breadth first; never cut the systems that carry the metaphysical truth-state.
