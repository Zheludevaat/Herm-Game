# M6 Launch Day Runbook

This runbook covers launch-day monitoring, triage, and hotfix flow for the METAXY prototype line.

## 1) Pre-launch gate (T-24h to T-1h)

1. Run the M6 regression suite:
   - `python scripts/run_m6_regression_suite.py`
2. Verify latest build has migrated save compatibility from beta fixtures.
3. Confirm telemetry/privacy checklist status in `M6_TELEMETRY_PRIVACY_CHECKLIST.md`.
4. Freeze non-launch branches and protect `work` from force pushes.

## 2) Launch monitoring windows

- **Window A (0-2h):** release engineer + gameplay engineer on point.
- **Window B (2-12h):** QA lead + narrative/system owner.
- **Window C (12-48h):** normal triage rotation.

During each window, capture:

- blocker defects (P0/P1),
- save/load errors,
- unexpected progression blockers,
- accessibility regressions.

## 3) Hotfix triage protocol

1. Reproduce and classify severity:
   - P0: crash/data loss/progression hard-lock,
   - P1: major feature unusable,
   - P2+: non-blocking.
2. Open issue with:
   - reproducible steps,
   - expected vs actual,
   - build/hash,
   - save file attached if relevant.
3. Patch on `hotfix/*` branch from current launch tag.
4. Run `python scripts/run_m6_regression_suite.py` before merge.
5. Deploy patch and append incident summary to release notes.

## 4) Save compatibility escalation path

If any save migration defect is found:

1. Stop further rollout.
2. Add failing fixture under `tests/fixtures/`.
3. Add regression test in `tests/test_level_and_save.py`.
4. Patch `game/metaxy_game/save.py` migration logic.
5. Re-run full M6 suite before restoring rollout.
