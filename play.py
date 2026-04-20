from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
GAME_DIR = PROJECT_ROOT / "game"
REQUIREMENTS_PATH = GAME_DIR / "requirements.txt"


def _pygame_available() -> bool:
    return importlib.util.find_spec("pygame") is not None


def _launch_game() -> None:
    subprocess.run([sys.executable, "main.py"], cwd=GAME_DIR, check=True)


def _install_dependencies() -> None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(REQUIREMENTS_PATH)], cwd=PROJECT_ROOT, check=True)


def main() -> None:
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.title("METAXY Launcher")
    root.geometry("360x180")
    root.resizable(False, False)

    status_text = tk.StringVar(value="Ready to launch METAXY.")
    title = tk.Label(root, text="METAXY: Souls Ascent", font=("TkDefaultFont", 14, "bold"))
    subtitle = tk.Label(root, text="One-button launcher for playtests.")
    status = tk.Label(root, textvariable=status_text, wraplength=320, justify="left")
    title.pack(pady=(18, 6))
    subtitle.pack(pady=(0, 10))
    status.pack(padx=16, pady=(0, 12))

    def start_game() -> None:
        play_button.config(state=tk.DISABLED)
        try:
            if not _pygame_available():
                status_text.set("Installing runtime dependencies...")
                root.update_idletasks()
                _install_dependencies()
            status_text.set("Launching game...")
            root.update_idletasks()
            root.destroy()
            _launch_game()
        except subprocess.CalledProcessError as exc:
            play_button.config(state=tk.NORMAL)
            status_text.set("Launch failed.")
            messagebox.showerror("Launch failed", f"Could not start METAXY.\n\n{exc}")

    play_button = tk.Button(root, text="Play", width=16, command=start_game)
    play_button.pack(pady=6)
    tk.Button(root, text="Quit", width=16, command=root.destroy).pack(pady=(0, 10))

    root.mainloop()


if __name__ == "__main__":
    main()
