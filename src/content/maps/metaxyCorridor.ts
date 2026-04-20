import type { RectZone } from './moonChamber';

export type MetaxyCorridorMap = {
  room: RectZone;
  spawn: { x: number; y: number };
  returnGate: { x: number; y: number };
  onwardGate: { x: number; y: number };
  walls: RectZone[];
};

export const METAXY_CORRIDOR_MAP: MetaxyCorridorMap = {
  room: { x: 10, y: 10, w: 300, h: 160 },
  spawn: { x: 36, y: 90 },
  returnGate: { x: 20, y: 90 },
  onwardGate: { x: 298, y: 90 },
  walls: [
    { x: 92, y: 24, w: 18, h: 124 },
    { x: 208, y: 24, w: 18, h: 124 },
  ],
};
