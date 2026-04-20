export type RectZone = {
  x: number;
  y: number;
  w: number;
  h: number;
};

export type MoonChamberMap = {
  room: RectZone;
  spawn: { x: number; y: number };
  memoryNode: { x: number; y: number };
  gate: { x: number; y: number };
  sophene: { x: number; y: number };
  walls: RectZone[];
  chasm: RectZone;
  bridge: RectZone;
};

export const MOON_CHAMBER_MAP: MoonChamberMap = {
  room: { x: 10, y: 10, w: 300, h: 160 },
  spawn: { x: 40, y: 90 },
  memoryNode: { x: 250, y: 90 },
  gate: { x: 296, y: 90 },
  sophene: { x: 66, y: 90 },
  walls: [
    { x: 128, y: 30, w: 24, h: 120 },
    { x: 192, y: 90, w: 60, h: 16 },
  ],
  chasm: { x: 148, y: 70, w: 44, h: 40 },
  bridge: { x: 160, y: 86, w: 20, h: 8 },
};
