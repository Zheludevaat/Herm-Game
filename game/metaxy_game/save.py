from __future__ import annotations

import json
from pathlib import Path

from .player import Player
from .state import SoulState

SAVE_PATH = Path(__file__).resolve().parents[1] / "savegame.json"
SAVE_SCHEMA_VERSION = 2


def migrate_save_data(raw_data: dict) -> dict:
    version = int(raw_data.get("schema_version", 1))
    data = dict(raw_data)

    if version < 2:
        # v1 did not store schema version and could omit level.
        data.setdefault("level", "moon_threshold")
        data["schema_version"] = 2
        version = 2

    if version != SAVE_SCHEMA_VERSION:
        raise ValueError(f"Unsupported save schema version: {version}")
    return data


def save_game(player: Player, soul: SoulState, level_name: str) -> None:
    payload = {
        "schema_version": SAVE_SCHEMA_VERSION,
        "player": {"x": player.x, "y": player.y},
        "soul": soul.to_dict(),
        "level": level_name,
    }
    SAVE_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_game() -> tuple[dict, SoulState, str] | None:
    if not SAVE_PATH.exists():
        return None
    raw_data = json.loads(SAVE_PATH.read_text(encoding="utf-8"))
    data = migrate_save_data(raw_data)
    player = data.get("player", {"x": 40, "y": 40})
    soul = SoulState.from_dict(data.get("soul", {}))
    level = str(data.get("level", "moon_threshold"))
    return player, soul, level
