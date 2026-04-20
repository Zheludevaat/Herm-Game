from __future__ import annotations

from .state import SoulState

ENDING_KEYS = ("true", "reincarnation", "vow_return", "soft", "false")


def evaluate_ending(state: SoulState) -> str:
    mastered_verbs = len(state.verbs_mastered)
    side_quests = len(state.completed_side_quests)

    if (
        state.mars_completed
        and mastered_verbs >= 7
        and side_quests >= 4
        and state.clarity >= 14
        and state.memory_shards >= 5
    ):
        return "true"

    if state.mars_completed and mastered_verbs >= 5 and state.clarity >= 12:
        return "vow_return"

    if state.mars_completed and side_quests >= 3 and state.clarity >= 10:
        return "reincarnation"

    if state.mars_completed and state.clarity >= 8:
        return "soft"

    return "false"


def ending_label(ending_key: str) -> str:
    mapping = {
        "true": "True Ending",
        "reincarnation": "Reincarnation Ending",
        "vow_return": "Vow-Return Ending",
        "soft": "Soft Ending",
        "false": "False Ending",
    }
    return mapping.get(ending_key, "Unknown Ending")
