import json
import tempfile
import unittest
from pathlib import Path

from game.metaxy_game.level import Level
from game.metaxy_game.player import Player
from game.metaxy_game.save import SAVE_SCHEMA_VERSION, load_game, migrate_save_data, save_game
from game.metaxy_game.state import SoulState
import game.metaxy_game.save as save_module


class LevelAndSaveTests(unittest.TestCase):
    def test_level_contains_expected_markers(self) -> None:
        for level_name in ("moon_threshold.json", "mercury_entry.json", "venus_sanctum.json", "mars_forge.json"):
            level = Level.from_json(Path("game/data") / level_name)
            self.assertGreater(len(level.find_markers("M")), 0)
            self.assertGreater(len(level.find_markers("T")), 0)
            self.assertGreater(len(level.find_markers("H")), 0)
            self.assertGreater(len(level.find_markers("G")), 0)
            self.assertGreater(len(level.find_markers("R")), 0)
            self.assertIsNotNone(level.spawn_point)
            self.assertIsNotNone(level.npc_point)

    def test_save_round_trip_with_level_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            original_save_path = save_module.SAVE_PATH
            save_module.SAVE_PATH = Path(tmpdir) / "savegame.json"
            try:
                player = Player(x=33, y=44)
                soul = SoulState(
                    coherence=77,
                    clarity=8,
                    memory_shards=3,
                    moon_completed=True,
                    mercury_completed=True,
                    venus_completed=True,
                    mars_completed=True,
                    moon_spoken=True,
                    mercury_spoken=True,
                    venus_spoken=True,
                    mars_spoken=True,
                    calling="Reformer",
                    reception_complete=True,
                    verbs_mastered=["Witness", "Name"],
                    completed_side_quests=["moon_threshold:50:66"],
                    relics_collected=["Moon Mirror Shard", "Mercury Quill"],
                    final_ending="soft",
                    high_contrast=True,
                    reduced_flash=True,
                    ui_font_size=14,
                )
                save_game(player, soul, "mars_forge")
                loaded = load_game()
            finally:
                save_module.SAVE_PATH = original_save_path

        self.assertIsNotNone(loaded)
        player_data, soul_data, level_name = loaded  # type: ignore[misc]
        self.assertEqual(level_name, "mars_forge")
        self.assertEqual(int(player_data["x"]), 33)
        self.assertEqual(int(player_data["y"]), 44)
        self.assertTrue(soul_data.moon_completed)
        self.assertTrue(soul_data.mercury_spoken)
        self.assertTrue(soul_data.mars_completed)
        self.assertTrue(soul_data.mars_spoken)
        self.assertEqual(soul_data.calling, "Reformer")
        self.assertTrue(soul_data.reception_complete)
        self.assertEqual(soul_data.verbs_mastered, ["Witness", "Name"])
        self.assertEqual(soul_data.completed_side_quests, ["moon_threshold:50:66"])
        self.assertEqual(soul_data.relics_collected, ["Moon Mirror Shard", "Mercury Quill"])
        self.assertEqual(soul_data.final_ending, "soft")
        self.assertTrue(soul_data.high_contrast)
        self.assertTrue(soul_data.reduced_flash)
        self.assertEqual(soul_data.ui_font_size, 14)

    def test_beta_save_fixtures_migrate_and_load(self) -> None:
        fixture_dir = Path("tests/fixtures")

        with tempfile.TemporaryDirectory() as tmpdir:
            original_save_path = save_module.SAVE_PATH
            save_module.SAVE_PATH = Path(tmpdir) / "savegame.json"
            try:
                for fixture_name in ("beta_save_v1.json", "beta_save_v2.json"):
                    payload = json.loads((fixture_dir / fixture_name).read_text(encoding="utf-8"))
                    save_module.SAVE_PATH.write_text(json.dumps(payload), encoding="utf-8")
                    loaded = load_game()
                    self.assertIsNotNone(loaded)
                    player_data, soul_data, level_name = loaded  # type: ignore[misc]
                    self.assertIn(level_name, {"moon_threshold", "mercury_entry"})
                    self.assertIsInstance(int(player_data["x"]), int)
                    self.assertIsInstance(int(player_data["y"]), int)
                    self.assertGreaterEqual(soul_data.clarity, 0)
            finally:
                save_module.SAVE_PATH = original_save_path

    def test_migrate_legacy_save_without_version(self) -> None:
        legacy = {
            "player": {"x": 1, "y": 2},
            "soul": {"clarity": 3},
        }
        migrated = migrate_save_data(legacy)
        self.assertEqual(migrated["schema_version"], SAVE_SCHEMA_VERSION)
        self.assertEqual(migrated["level"], "moon_threshold")


if __name__ == "__main__":
    unittest.main()
