from dataclasses import dataclass


@dataclass
class Player:
    x: float
    y: float
    speed: float = 55.0
    size: int = 12

    def move(self, dx: float, dy: float, dt: float, blocked) -> None:
        nx = self.x + dx * self.speed * dt
        ny = self.y + dy * self.speed * dt

        half = self.size / 2

        if not blocked(nx - half, self.y - half) and not blocked(nx + half, self.y + half):
            self.x = nx
        if not blocked(self.x - half, ny - half) and not blocked(self.x + half, ny + half):
            self.y = ny
