from __future__ import annotations

from .state import SoulState


def unlocked_entries(state: SoulState) -> list[str]:
    entries = ["Cosmology: The cosmos is a school."]
    if state.calling:
        entries.append(f"Calling: {state.calling}")
    if state.reception_complete:
        entries.append("Reception: The Four Guardians received your passage.")
    if state.memory_shards >= 1:
        entries.append("Moon: Memory reveals resonance.")
    if state.clarity >= 3:
        entries.append("Inquiry: Naming distortion grants clarity.")

    if state.moon_completed:
        entries.append("Threshold: Moon passage completed.")
    if state.mercury_completed:
        entries.append("Threshold: Mercury archive stabilized.")
    if state.venus_completed:
        entries.append("Threshold: Venus vow resolved.")
    if state.mars_completed:
        entries.append("Threshold: Mars forge aligned.")

    if state.verbs_mastered:
        entries.append(f"Verbs: {len(state.verbs_mastered)}/7 awakened.")
    if len(state.verbs_mastered) == 7:
        entries.append("Verbs: All seven channels integrated.")
    if state.completed_side_quests:
        entries.append(f"Side Quests: {len(state.completed_side_quests)} insights integrated.")
    if state.relics_collected:
        entries.append(f"Relics: {len(state.relics_collected)} integrated.")
    if state.final_ending:
        entries.append(f"Ending: {state.final_ending}")

    testimony_count = sum(
        int(flag)
        for flag in (state.moon_spoken, state.mercury_spoken, state.venus_spoken, state.mars_spoken)
    )
    if testimony_count == 4:
        entries.append("Bonds: You witnessed all resident testimonies.")
    return entries
