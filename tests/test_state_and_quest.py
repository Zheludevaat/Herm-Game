import unittest

from game.metaxy_game.codex import unlocked_entries
from game.metaxy_game.endings import evaluate_ending
from game.metaxy_game.quest import (
    completed_side_quests_for_level,
    mark_trial_passed,
    objective_line,
    relic_collected_for_level,
    spoken_in_level,
    trial_passed_in_level,
)
from game.metaxy_game.state import SoulState
from game.metaxy_game.verbs import VERBS, apply_verb
from game.metaxy_game.dialogue import resolve_choice
from game.metaxy_game.progression import ACTS, next_act_name
import importlib.util


class StateAndQuestTests(unittest.TestCase):
    def test_spoken_flags_default_false(self) -> None:
        state = SoulState()
        self.assertFalse(spoken_in_level("moon_threshold", state))
        self.assertFalse(spoken_in_level("mercury_entry", state))
        self.assertFalse(spoken_in_level("venus_sanctum", state))
        self.assertFalse(spoken_in_level("mars_forge", state))

    def test_objective_line_contains_talk_and_progress(self) -> None:
        state = SoulState(
            clarity=4,
            memory_shards=2,
            moon_spoken=True,
            completed_side_quests=["moon_threshold:1:2"],
            relics_collected=["Moon Mirror Shard"],
        )
        line = objective_line("moon_threshold", state, clarity_goal=3, memory_goal=1)
        self.assertIn("Talk Y", line)
        self.assertIn("Trial N", line)
        self.assertIn("Relic Y", line)
        self.assertIn("SQ 1/1", line)
        self.assertIn("Clr 4/3", line)
        self.assertIn("Mem 2/1", line)
        self.assertEqual(completed_side_quests_for_level("moon_threshold", state), 1)
        self.assertTrue(relic_collected_for_level("moon_threshold", state))

    def test_codex_unlocks_bonds_after_all_spoken(self) -> None:
        state = SoulState(
            moon_spoken=True,
            mercury_spoken=True,
            venus_spoken=True,
            mars_spoken=True,
            calling="Scholar",
            reception_complete=True,
            completed_side_quests=["moon_threshold:1:1"],
        )
        entries = unlocked_entries(state)
        self.assertTrue(any("resident testimonies" in entry for entry in entries))
        self.assertTrue(any(entry.startswith("Calling:") for entry in entries))
        self.assertTrue(any(entry.startswith("Reception:") for entry in entries))
        self.assertTrue(any(entry.startswith("Side Quests:") for entry in entries))

    def test_apply_verb_marks_mastery_and_changes_state(self) -> None:
        state = SoulState(coherence=60, clarity=0)
        message = apply_verb(state, VERBS[0])
        self.assertIn("Witness", message)
        self.assertIn("Witness", state.verbs_mastered)
        self.assertGreaterEqual(state.clarity, 1)

    def test_accessibility_font_cycle_bounds(self) -> None:
        state = SoulState(ui_font_size=12)
        state.cycle_font_size(1)
        self.assertEqual(state.ui_font_size, 14)
        state.cycle_font_size(1)
        self.assertEqual(state.ui_font_size, 14)
        state.cycle_font_size(-5)
        self.assertEqual(state.ui_font_size, 10)

    def test_collect_relic_only_once(self) -> None:
        state = SoulState()
        self.assertTrue(state.collect_relic("Moon Mirror Shard"))
        self.assertFalse(state.collect_relic("Moon Mirror Shard"))
        self.assertEqual(state.relics_collected, ["Moon Mirror Shard"])



    def test_trial_state_helpers(self) -> None:
        state = SoulState()
        self.assertFalse(trial_passed_in_level("moon_threshold", state))
        mark_trial_passed("moon_threshold", state)
        self.assertTrue(trial_passed_in_level("moon_threshold", state))

    def test_dialogue_uses_level_pack(self) -> None:
        state = SoulState()
        result = resolve_choice(1, state, "mars_forge")
        self.assertIn("Mars veteran", result.line)
        self.assertGreaterEqual(state.clarity, 1)


    def test_progression_acts_loaded_from_data(self) -> None:
        self.assertGreaterEqual(len(ACTS), 4)
        self.assertEqual(next_act_name("moon_threshold"), "mercury_entry")
        self.assertEqual(next_act_name("mercury_entry"), "venus_sanctum")
        self.assertEqual(next_act_name("venus_sanctum"), "mars_forge")
        self.assertIsNone(next_act_name("mars_forge"))


    def test_pixel_art_surfaces_render(self) -> None:
        if importlib.util.find_spec("pygame") is None:
            self.skipTest("pygame is not installed in test environment")
        from game.metaxy_game.art import player_sprite, npc_sprite, tile_surface

        floor = tile_surface("moon_threshold", "floor", 16)
        wall = tile_surface("mars_forge", "wall", 16)
        player = player_sprite("venus_sanctum", 0)
        npc = npc_sprite("mercury_entry", 1)
        self.assertEqual(floor.get_size(), (16, 16))
        self.assertEqual(wall.get_size(), (16, 16))
        self.assertEqual(player.get_size(), (12, 12))
        self.assertEqual(npc.get_size(), (12, 12))

    def test_ending_evaluation_prefers_true_path(self) -> None:
        state = SoulState(
            mars_completed=True,
            clarity=14,
            memory_shards=5,
            verbs_mastered=[verb.name for verb in VERBS],
            completed_side_quests=[
                "moon_threshold:1:1",
                "mercury_entry:1:1",
                "venus_sanctum:1:1",
                "mars_forge:1:1",
            ],
        )
        self.assertEqual(evaluate_ending(state), "true")


if __name__ == "__main__":
    unittest.main()
