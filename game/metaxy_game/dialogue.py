from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from .state import SoulState

INQUIRY_OPTIONS = [
    "Observe",
    "Ask",
    "Name",
    "Challenge",
    "Confess",
    "Release",
    "Remain Silent",
]


@dataclass
class DialogueResult:
    line: str
    clarity_delta: int = 0
    coherence_delta: int = 0


def resolve_choice(choice: int, state: SoulState, level_name: str) -> DialogueResult:
    mapping = _response_mapping(level_name)
    result = mapping.get(choice, DialogueResult("You hesitate."))
    if result.clarity_delta:
        state.gain_clarity(result.clarity_delta)
    if result.coherence_delta < 0:
        state.lose_coherence(abs(result.coherence_delta))
    elif result.coherence_delta > 0:
        state.recover_coherence(result.coherence_delta)
    return result


@lru_cache(maxsize=16)
def _response_mapping(level_name: str) -> dict[int, DialogueResult]:
    dialogue_path = Path(__file__).resolve().parents[1] / "data" / "dialogue" / f"{level_name}.json"
    if not dialogue_path.exists():
        return _default_mapping()

    payload = json.loads(dialogue_path.read_text(encoding="utf-8"))
    responses = payload.get("responses", [])
    if not isinstance(responses, list) or len(responses) != len(INQUIRY_OPTIONS):
        return _default_mapping()

    mapping: dict[int, DialogueResult] = {}
    for idx, response in enumerate(responses):
        if not isinstance(response, dict):
            continue
        mapping[idx] = DialogueResult(
            line=str(response.get("line", "You hesitate.")),
            clarity_delta=int(response.get("clarity_delta", 0)),
            coherence_delta=int(response.get("coherence_delta", 0)),
        )

    if len(mapping) != len(INQUIRY_OPTIONS):
        return _default_mapping()
    return mapping


def _default_mapping() -> dict[int, DialogueResult]:
    return {
        0: DialogueResult("You notice the mirror moves before your hand.", clarity_delta=1),
        1: DialogueResult("The resident asks: 'What are you protecting?'.", clarity_delta=1),
        2: DialogueResult("You name the distortion: image without witness.", clarity_delta=2),
        3: DialogueResult("You argue to avoid surrender and feel the split.", coherence_delta=-6),
        4: DialogueResult("You admit your fear of being unseen.", clarity_delta=2, coherence_delta=2),
        5: DialogueResult("You release one flattering story.", clarity_delta=3, coherence_delta=4),
        6: DialogueResult("Silence settles. You remain present.", coherence_delta=3),
    }
