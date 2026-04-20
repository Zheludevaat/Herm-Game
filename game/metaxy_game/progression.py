from __future__ import annotations

import json
from pathlib import Path

_REQUIRED_FIELDS = {"name", "label", "file", "dialogue_file", "goal", "dialogue_hint", "quest_text", "relic"}


def _load_acts() -> tuple[dict[str, object], ...]:
    data_path = Path(__file__).resolve().parents[1] / "data" / "acts.json"
    payload = json.loads(data_path.read_text(encoding="utf-8"))
    acts = payload.get("acts")
    if not isinstance(acts, list) or not acts:
        raise ValueError("game/data/acts.json must contain a non-empty 'acts' list")

    normalized: list[dict[str, object]] = []
    seen_names: set[str] = set()
    for idx, act in enumerate(acts):
        if not isinstance(act, dict):
            raise ValueError(f"acts[{idx}] must be an object")
        missing = _REQUIRED_FIELDS.difference(act.keys())
        if missing:
            raise ValueError(f"acts[{idx}] missing required fields: {sorted(missing)}")
        name = str(act["name"])
        if name in seen_names:
            raise ValueError(f"duplicate act name: {name}")
        seen_names.add(name)
        relic = act.get("relic")
        if not isinstance(relic, str) or not relic.strip():
            raise ValueError(f"acts[{idx}].relic must be a non-empty string")
        normalized.append(act)
    return tuple(normalized)


ACTS = _load_acts()
ACT_INDEX = {str(act["name"]): idx for idx, act in enumerate(ACTS)}
ACT_BY_NAME = {str(act["name"]): act for act in ACTS}


def next_act_name(current_name: str) -> str | None:
    idx = ACT_INDEX[current_name]
    next_idx = idx + 1
    if next_idx >= len(ACTS):
        return None
    return str(ACTS[next_idx]["name"])
