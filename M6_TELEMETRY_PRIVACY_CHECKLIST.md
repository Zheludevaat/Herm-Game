# M6 Telemetry + Privacy Checklist

Use this checklist before each release candidate cut.

## Data collection policy

- [x] No PII is collected by prototype runtime telemetry.
- [x] Save payload stores only gameplay state (`player`, `soul`, `level`, schema version).
- [x] Save file is local-only and never uploaded by default.

## Logging safeguards

- [x] Regression suite output contains command status only.
- [x] Tests avoid secrets and external endpoints.
- [x] Error output reviewed for accidental sensitive payloads.

## Release checks

- [x] Run `python scripts/run_m6_regression_suite.py` on release candidate commit.
- [x] Verify save migration tests cover beta fixtures and legacy unversioned save payloads.
- [x] Confirm runbook ownership and on-call rotation before launch.
