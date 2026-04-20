import unittest
from unittest.mock import patch

import play


class LauncherTests(unittest.TestCase):
    def test_pygame_available_true_when_spec_found(self) -> None:
        with patch("play.importlib.util.find_spec", return_value=object()):
            self.assertTrue(play._pygame_available())

    def test_pygame_available_false_when_spec_missing(self) -> None:
        with patch("play.importlib.util.find_spec", return_value=None):
            self.assertFalse(play._pygame_available())

    def test_install_dependencies_uses_requirements_file(self) -> None:
        with patch("play.subprocess.run") as run_mock:
            play._install_dependencies()
        run_mock.assert_called_once()
        called_args, called_kwargs = run_mock.call_args
        self.assertIn("-r", called_args[0])
        self.assertIn(str(play.REQUIREMENTS_PATH), called_args[0])
        self.assertEqual(called_kwargs["cwd"], play.PROJECT_ROOT)
        self.assertTrue(called_kwargs["check"])

    def test_launch_game_runs_game_main(self) -> None:
        with patch("play.subprocess.run") as run_mock:
            play._launch_game()
        run_mock.assert_called_once_with(
            [play.sys.executable, "main.py"],
            cwd=play.GAME_DIR,
            check=True,
        )


if __name__ == "__main__":
    unittest.main()
