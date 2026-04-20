import Phaser from 'phaser';
import { drawTiledArea } from '../art/pixelArt';

export type RectZone = { x: number; y: number; w: number; h: number };

export type RenderableMap = {
  room: RectZone;
  walls: RectZone[];
};

export function renderMapBase(scene: Phaser.Scene, map: RenderableMap, bgColor = 0x1b2a39): void {
  scene
    .add.rectangle(map.room.x + map.room.w / 2, map.room.y + map.room.h / 2, map.room.w, map.room.h, bgColor)
    .setStrokeStyle(2, 0x3d5572)
    .setDepth(-20);

  drawTiledArea(scene, 'tile-floor', map.room.x, map.room.y, map.room.w, map.room.h);
  for (const wall of map.walls) {
    drawTiledArea(scene, 'tile-wall', wall.x, wall.y, wall.w, wall.h);
  }
}

export function intersectsRect(x: number, y: number, width: number, height: number, rect: RectZone): boolean {
  const halfW = width / 2;
  const halfH = height / 2;

  return !(
    x + halfW <= rect.x ||
    x - halfW >= rect.x + rect.w ||
    y + halfH <= rect.y ||
    y - halfH >= rect.y + rect.h
  );
}
