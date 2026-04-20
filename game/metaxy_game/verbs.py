from __future__ import annotations

from dataclasses import dataclass

from .state import SoulState


@dataclass(frozen=True)
class Verb:
    name: str
    description: str


VERBS: tuple[Verb, ...] = (
    Verb("Witness", "See what is present without distortion."),
    Verb("Name", "Give truthful language to what is hidden."),
    Verb("Attune", "Synchronize breath and intent with the field."),
    Verb("Expose", "Reveal contradiction beneath polished surfaces."),
    Verb("Stand", "Hold form under pressure without retaliation."),
    Verb("Weigh", "Measure consequence before acting."),
    Verb("Release", "Let go of what no longer belongs to you."),
)


def apply_verb(state: SoulState, verb: Verb, context: str = "traversal") -> str:
    state.mark_verb(verb.name)

    if verb.name == "Witness":
        state.gain_clarity(1)
        return "Witness: clarity sharpened."
    if verb.name == "Name":
        state.gain_clarity(2)
        return "Name: distortion identified."
    if verb.name == "Attune":
        state.recover_coherence(4)
        return "Attune: coherence restored."
    if verb.name == "Expose":
        state.gain_clarity(1)
        state.lose_coherence(2)
        return "Expose: truth cut through comfort."
    if verb.name == "Stand":
        state.recover_coherence(3)
        return "Stand: stance stabilized."
    if verb.name == "Weigh":
        state.gain_clarity(1)
        return "Weigh: consequence considered."
    if verb.name == "Release":
        state.gain_clarity(2)
        state.recover_coherence(2)
        return "Release: burden relinquished."

    return f"{verb.name}: no effect in {context}."
