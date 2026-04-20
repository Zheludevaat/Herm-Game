from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    window_width: int = 640
    window_height: int = 576
    logical_width: int = 160
    logical_height: int = 144
    scale: int = 4
    title: str = "METAXY: Prototype"
    target_fps: int = 60


CFG = Config()

# Four-tone GBC-inspired palette
PALETTE = {
    "bg0": (224, 248, 208),
    "bg1": (136, 192, 112),
    "bg2": (52, 104, 86),
    "bg3": (8, 24, 32),
    "accent": (248, 224, 88),
}
