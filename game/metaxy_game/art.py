from __future__ import annotations

from functools import lru_cache

import pygame

THEMES: dict[str, dict[str, tuple[int, int, int]]] = {
    "moon_threshold": {
        "floor": (215, 224, 237),
        "wall": (118, 130, 152),
        "shadow": (72, 84, 104),
        "highlight": (240, 246, 255),
        "accent": (156, 176, 214),
        "npc": (123, 92, 182),
        "sky_top": (170, 188, 220),
        "sky_bottom": (224, 233, 246),
    },
    "mercury_entry": {
        "floor": (204, 216, 198),
        "wall": (108, 128, 112),
        "shadow": (61, 77, 70),
        "highlight": (228, 240, 222),
        "accent": (134, 159, 139),
        "npc": (160, 88, 130),
        "sky_top": (150, 170, 152),
        "sky_bottom": (216, 228, 209),
    },
    "venus_sanctum": {
        "floor": (235, 211, 204),
        "wall": (156, 109, 109),
        "shadow": (99, 64, 70),
        "highlight": (250, 236, 230),
        "accent": (205, 148, 150),
        "npc": (108, 88, 158),
        "sky_top": (210, 165, 172),
        "sky_bottom": (245, 224, 216),
    },
    "mars_forge": {
        "floor": (229, 198, 176),
        "wall": (149, 95, 74),
        "shadow": (89, 51, 38),
        "highlight": (245, 220, 203),
        "accent": (198, 124, 98),
        "npc": (97, 84, 146),
        "sky_top": (171, 109, 87),
        "sky_bottom": (235, 203, 182),
    },
}


def theme_for_level(level_name: str) -> dict[str, tuple[int, int, int]]:
    return THEMES.get(level_name, THEMES["moon_threshold"])


def draw_backdrop(surface: pygame.Surface, level_name: str, frame: int) -> None:
    theme = theme_for_level(level_name)
    top = theme["sky_top"]
    bottom = theme["sky_bottom"]
    width, height = surface.get_size()

    for y in range(height):
        t = y / max(1, height - 1)
        color = (
            int(top[0] * (1 - t) + bottom[0] * t),
            int(top[1] * (1 - t) + bottom[1] * t),
            int(top[2] * (1 - t) + bottom[2] * t),
        )
        pygame.draw.line(surface, color, (0, y), (width, y))

    # twinkling stars/runes
    sparkle = theme["highlight"]
    for i in range(8):
        x = (17 * i + frame * 2) % width
        y = (11 * i + 7) % (height // 2)
        surface.set_at((x, y), sparkle)


@lru_cache(maxsize=256)
def tile_surface(level_name: str, kind: str, size: int, variant: int = 0) -> pygame.Surface:
    theme = theme_for_level(level_name)
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    base = theme["wall"] if kind == "wall" else theme["floor"]
    surf.fill(base)

    # checker dithering + variant micro-noise
    dither = theme["highlight"] if kind == "floor" else theme["shadow"]
    for y in range(0, size, 2):
        for x in range((y // 2 + variant) % 2, size, 2):
            surf.set_at((x, y), dither)

    # edge lighting for depth
    edge = theme["accent"]
    pygame.draw.line(surf, edge, (0, 0), (size - 1, 0))
    pygame.draw.line(surf, edge, (0, 0), (0, size - 1))
    if kind == "wall":
        pygame.draw.line(surf, theme["shadow"], (0, size - 1), (size - 1, size - 1))
        pygame.draw.line(surf, theme["shadow"], (size - 1, 0), (size - 1, size - 1))
    return surf


@lru_cache(maxsize=32)
def marker_sprite(level_name: str, marker_kind: str, frame: int) -> pygame.Surface:
    theme = theme_for_level(level_name)
    surf = pygame.Surface((8, 8), pygame.SRCALPHA)
    pulse = frame % 2
    accent = theme["accent"]
    light = theme["highlight"]
    dark = theme["shadow"]

    if marker_kind == "memory":
        pygame.draw.circle(surf, accent, (4, 4), 3)
        pygame.draw.circle(surf, light, (4, 4), 1 + pulse)
    elif marker_kind == "dissonance":
        pygame.draw.rect(surf, dark, (1, 1, 6, 6), 1)
        pygame.draw.line(surf, dark, (1, 1), (6, 6), 1)
        pygame.draw.line(surf, dark, (6, 1), (1, 6), 1)
    elif marker_kind == "threshold":
        pygame.draw.rect(surf, accent, (1, 1, 6, 6), 1)
        pygame.draw.rect(surf, light, (2, 2, 4, 4), 1)
    elif marker_kind == "shrine":
        pygame.draw.circle(surf, light, (4, 4), 3, 1)
        pygame.draw.rect(surf, accent, (3, 2 + pulse, 2, 4), 0)
    elif marker_kind == "trial":
        pygame.draw.rect(surf, dark, (1, 1, 6, 6), 1)
        pygame.draw.rect(surf, accent, (2 + pulse, 2, 3, 4), 0)
    elif marker_kind == "relic":
        pygame.draw.rect(surf, accent, (2, 1, 4, 6), 1)
        pygame.draw.rect(surf, light, (3, 2 + pulse, 2, 2), 0)
        pygame.draw.line(surf, dark, (2, 6), (5, 6), 1)
    else:  # side quest
        pygame.draw.rect(surf, accent, (2, 2, 4, 4), 1)
        pygame.draw.rect(surf, light, (3, 3, 2, 2), 0)
    return surf


@lru_cache(maxsize=16)
def player_sprite(level_name: str, frame: int) -> pygame.Surface:
    theme = theme_for_level(level_name)
    surf = pygame.Surface((12, 12), pygame.SRCALPHA)
    robe = theme["accent"]
    shadow = theme["shadow"]
    face = theme["highlight"]
    trim = theme["npc"]

    bob = frame % 2

    # outline
    pygame.draw.rect(surf, shadow, (2, 1 + bob, 8, 10), 1)

    # hood + face
    pygame.draw.rect(surf, shadow, (3, 1 + bob, 6, 4))
    pygame.draw.rect(surf, face, (4, 2 + bob, 4, 2))

    # robe body
    pygame.draw.rect(surf, robe, (2, 5 + bob, 8, 5))
    pygame.draw.rect(surf, trim, (5, 6 + bob, 2, 4))

    # feet
    pygame.draw.rect(surf, shadow, (3, 10, 2, 2))
    pygame.draw.rect(surf, shadow, (7, 10, 2, 2))
    return surf


@lru_cache(maxsize=16)
def npc_sprite(level_name: str, frame: int) -> pygame.Surface:
    theme = theme_for_level(level_name)
    surf = pygame.Surface((12, 12), pygame.SRCALPHA)
    robe = theme["npc"]
    shadow = theme["shadow"]
    face = theme["highlight"]

    bob = (frame + 1) % 2

    pygame.draw.rect(surf, shadow, (2, 1 + bob, 8, 10), 1)
    pygame.draw.rect(surf, shadow, (3, 1 + bob, 6, 4))
    pygame.draw.rect(surf, face, (4, 2 + bob, 4, 2))
    pygame.draw.rect(surf, robe, (2, 5 + bob, 8, 5))
    pygame.draw.rect(surf, shadow, (3, 10, 2, 2))
    pygame.draw.rect(surf, shadow, (7, 10, 2, 2))

    # shoulder rune
    pygame.draw.rect(surf, theme["accent"], (8, 6 + bob, 2, 2))
    return surf
