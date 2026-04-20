from __future__ import annotations

from .progression import ACT_BY_NAME
from .state import SoulState

SPOKEN_FIELDS = {
    "moon_threshold": "moon_spoken",
    "mercury_entry": "mercury_spoken",
    "venus_sanctum": "venus_spoken",
    "mars_forge": "mars_spoken",
}

TRIAL_FIELDS = {
    "moon_threshold": "moon_trial_passed",
    "mercury_entry": "mercury_trial_passed",
    "venus_sanctum": "venus_trial_passed",
    "mars_forge": "mars_trial_passed",
}


def spoken_in_level(level_name: str, state: SoulState) -> bool:
    field_name = SPOKEN_FIELDS.get(level_name)
    if not field_name:
        return False
    return bool(getattr(state, field_name, False))


def mark_spoken_in_level(level_name: str, state: SoulState) -> None:
    field_name = SPOKEN_FIELDS.get(level_name)
    if field_name:
        setattr(state, field_name, True)


def trial_passed_in_level(level_name: str, state: SoulState) -> bool:
    field_name = TRIAL_FIELDS.get(level_name)
    if not field_name:
        return False
    return bool(getattr(state, field_name, False))


def mark_trial_passed(level_name: str, state: SoulState) -> None:
    field_name = TRIAL_FIELDS.get(level_name)
    if field_name:
        setattr(state, field_name, True)


def completed_side_quests_for_level(level_name: str, state: SoulState) -> int:
    prefix = f"{level_name}:"
    return sum(1 for quest_id in state.completed_side_quests if quest_id.startswith(prefix))


def relic_for_level(level_name: str) -> str:
    return str(ACT_BY_NAME[level_name]["relic"])


def relic_collected_for_level(level_name: str, state: SoulState) -> bool:
    return relic_for_level(level_name) in state.relics_collected


def objective_line(level_name: str, state: SoulState, clarity_goal: int, memory_goal: int) -> str:
    spoken_state = "Y" if spoken_in_level(level_name, state) else "N"
    trial_state = "Y" if trial_passed_in_level(level_name, state) else "N"
    relic_state = "Y" if relic_collected_for_level(level_name, state) else "N"
    side_quests = completed_side_quests_for_level(level_name, state)
    quest_text = str(ACT_BY_NAME[level_name]["quest_text"])
    return (
        f"{quest_text} "
        f"[Talk {spoken_state} | Trial {trial_state} | Relic {relic_state} | SQ {side_quests}/1 | Clr {state.clarity}/{clarity_goal} | Mem {state.memory_shards}/{memory_goal}]"
    )
