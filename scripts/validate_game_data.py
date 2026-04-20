#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ALLOWED_TILES = {".", "#", "M", "X", "T", "H", "Q", "G", "R"}
INQUIRY_OPTIONS_COUNT = 7


def validate_level(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON ({exc})"]

    grid = data.get("grid")
    if not isinstance(grid, list) or not grid:
        return [f"{path}: missing non-empty 'grid' list"]

    row_width = len(grid[0])
    for idx, row in enumerate(grid):
        if not isinstance(row, str):
            errors.append(f"{path}: row {idx} is not a string")
            continue
        if len(row) != row_width:
            errors.append(f"{path}: row {idx} width {len(row)} != {row_width}")
        invalid = {char for char in row if char not in ALLOWED_TILES}
        if invalid:
            errors.append(f"{path}: row {idx} has invalid markers {sorted(invalid)}")

    tile_size = data.get("tile_size", 0)
    if tile_size <= 0:
        errors.append(f"{path}: tile_size must be > 0")

    metadata = data.get("metadata", {})
    if metadata and not isinstance(metadata, dict):
        errors.append(f"{path}: metadata must be an object")
    if isinstance(metadata, dict):
        for key in ("spawn", "npc"):
            point = metadata.get(key)
            if point is None:
                continue
            if not isinstance(point, dict):
                errors.append(f"{path}: metadata.{key} must be an object with x/y")
                continue
            x = point.get("x")
            y = point.get("y")
            if not isinstance(x, int) or not isinstance(y, int):
                errors.append(f"{path}: metadata.{key} x/y must be integers")
                continue
            tx = x // tile_size
            ty = y // tile_size
            if tx < 0 or ty < 0 or ty >= len(grid) or tx >= len(grid[0]):
                errors.append(f"{path}: metadata.{key} point out of bounds ({x},{y})")
            elif grid[ty][tx] == "#":
                errors.append(f"{path}: metadata.{key} must not be inside a wall tile")

    return errors


def validate_dialogue(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON ({exc})"]

    responses = data.get("responses")
    if not isinstance(responses, list) or len(responses) != INQUIRY_OPTIONS_COUNT:
        return [f"{path}: responses must be a list with {INQUIRY_OPTIONS_COUNT} entries"]

    for idx, response in enumerate(responses):
        if not isinstance(response, dict):
            errors.append(f"{path}: responses[{idx}] must be an object")
            continue
        line = response.get("line")
        if not isinstance(line, str) or not line.strip():
            errors.append(f"{path}: responses[{idx}].line must be a non-empty string")
        for delta_key in ("clarity_delta", "coherence_delta"):
            if delta_key in response and not isinstance(response[delta_key], int):
                errors.append(f"{path}: responses[{idx}].{delta_key} must be an integer")
    return errors


def validate_acts(path: Path, level_dir: Path, dialogue_dir: Path) -> tuple[list[str], list[dict[str, object]]]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON ({exc})"], []

    acts = payload.get("acts")
    if not isinstance(acts, list) or not acts:
        return [f"{path}: acts must be a non-empty list"], []

    required_fields = {"name", "label", "file", "dialogue_file", "goal", "dialogue_hint", "quest_text", "relic"}
    seen_names: set[str] = set()

    for idx, act in enumerate(acts):
        if not isinstance(act, dict):
            errors.append(f"{path}: acts[{idx}] must be an object")
            continue
        missing = required_fields.difference(act.keys())
        if missing:
            errors.append(f"{path}: acts[{idx}] missing fields {sorted(missing)}")
            continue

        name = str(act["name"])
        if name in seen_names:
            errors.append(f"{path}: duplicate act name '{name}'")
        seen_names.add(name)

        level_file = level_dir / str(act["file"])
        if not level_file.exists():
            errors.append(f"{path}: acts[{idx}] level file missing: {level_file}")

        dialogue_file = dialogue_dir / str(act["dialogue_file"])
        if not dialogue_file.exists():
            errors.append(f"{path}: acts[{idx}] dialogue file missing: {dialogue_file}")

        relic_name = act["relic"]
        if not isinstance(relic_name, str) or not relic_name.strip():
            errors.append(f"{path}: acts[{idx}].relic must be a non-empty string")

        goal = act["goal"]
        if not isinstance(goal, dict):
            errors.append(f"{path}: acts[{idx}].goal must be an object")
            continue
        for key, expected_type in (
            ("clarity", int),
            ("memory_shards", int),
            ("spoken", bool),
            ("side_quests", int),
            ("trial", bool),
        ):
            if key not in goal:
                errors.append(f"{path}: acts[{idx}].goal missing key '{key}'")
            elif not isinstance(goal[key], expected_type):
                errors.append(f"{path}: acts[{idx}].goal.{key} must be {expected_type.__name__}")

    return errors, [act for act in acts if isinstance(act, dict)]


def main() -> int:
    level_dir = Path("game/data")
    dialogue_dir = level_dir / "dialogue"
    level_paths = sorted(path for path in level_dir.glob("*.json") if path.name != "acts.json")
    if not level_paths:
        print("No level files found in game/data", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for level_path in level_paths:
        all_errors.extend(validate_level(level_path))

    acts_path = level_dir / "acts.json"
    if not acts_path.exists():
        all_errors.append(f"{acts_path}: missing")
        acts: list[dict[str, object]] = []
    else:
        act_errors, acts = validate_acts(acts_path, level_dir, dialogue_dir)
        all_errors.extend(act_errors)

    for act in acts:
        dialogue_file = dialogue_dir / str(act["dialogue_file"])
        if dialogue_file.exists():
            all_errors.extend(validate_dialogue(dialogue_file))

    if all_errors:
        print("Game data validation failed:", file=sys.stderr)
        for err in all_errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    print(f"Validated {len(level_paths)} level files, {len(acts)} acts, and {len(acts)} dialogue files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
