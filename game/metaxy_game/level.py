from __future__ import annotations

import json
from pathlib import Path


class Level:
    def __init__(
        self,
        grid: list[str],
        tile_size: int = 16,
        spawn_point: tuple[int, int] | None = None,
        npc_point: tuple[int, int] | None = None,
    ):
        self.grid = grid
        self.tile_size = tile_size
        self.height = len(grid)
        self.width = len(grid[0]) if grid else 0
        self.spawn_point = spawn_point
        self.npc_point = npc_point

    @classmethod
    def from_json(cls, path: Path) -> "Level":
        data = json.loads(path.read_text(encoding="utf-8"))
        metadata = data.get("metadata", {})
        spawn = _parse_point(metadata.get("spawn"))
        npc = _parse_point(metadata.get("npc"))
        return cls(grid=data["grid"], tile_size=data.get("tile_size", 16), spawn_point=spawn, npc_point=npc)

    def is_blocked(self, x: float, y: float) -> bool:
        tx = int(x // self.tile_size)
        ty = int(y // self.tile_size)
        if tx < 0 or ty < 0 or tx >= self.width or ty >= self.height:
            return True
        return self.grid[ty][tx] == "#"

    def find_markers(self, marker: str) -> list[tuple[int, int]]:
        positions: list[tuple[int, int]] = []
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == marker:
                    positions.append((x * self.tile_size + self.tile_size // 2, y * self.tile_size + self.tile_size // 2))
        return positions


def _parse_point(value: object) -> tuple[int, int] | None:
    if not isinstance(value, dict):
        return None
    x = value.get("x")
    y = value.get("y")
    if isinstance(x, int) and isinstance(y, int):
        return (x, y)
    return None
