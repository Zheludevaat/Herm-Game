from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Check:
    name: str
    cmd: list[str]


CHECKS: tuple[Check, ...] = (
    Check("validate game data", ["python", "scripts/validate_game_data.py"]),
    Check("unit tests", ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"]),
    Check("compile runtime and tests", ["python", "-m", "compileall", "game/metaxy_game", "tests"]),
)


def run_check(check: Check) -> int:
    print(f"[M6] Running: {check.name}")
    print(f"[M6] Command: {' '.join(check.cmd)}")
    result = subprocess.run(check.cmd, check=False)
    if result.returncode != 0:
        print(f"[M6] FAILED: {check.name} (exit {result.returncode})")
        return result.returncode
    print(f"[M6] PASSED: {check.name}")
    return 0


def main() -> int:
    for check in CHECKS:
        code = run_check(check)
        if code != 0:
            return code
    print("[M6] Gold candidate regression suite pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
