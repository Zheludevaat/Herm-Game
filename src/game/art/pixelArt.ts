import Phaser from 'phaser';

function createTexture(
  scene: Phaser.Scene,
  key: string,
  width: number,
  height: number,
  draw: (g: Phaser.GameObjects.Graphics) => void
): void {
  if (scene.textures.exists(key)) return;
  const g = scene.add.graphics();
  draw(g);
  g.generateTexture(key, width, height);
  g.destroy();
}

export function ensurePixelArtTextures(scene: Phaser.Scene): void {
  createTexture(scene, 'tile-floor', 16, 16, (g) => {
    g.fillStyle(0x263a4d, 1);
    g.fillRect(0, 0, 16, 16);
    g.fillStyle(0x2f465e, 1);
    g.fillRect(0, 0, 16, 2);
    g.fillRect(0, 0, 2, 16);
    g.fillStyle(0x354f69, 1);
    for (let y = 2; y < 16; y += 4) {
      for (let x = 2; x < 16; x += 4) {
        g.fillRect(x, y, 1, 1);
      }
    }
  });

  createTexture(scene, 'tile-wall', 16, 16, (g) => {
    g.fillStyle(0x1d2d3d, 1);
    g.fillRect(0, 0, 16, 16);
    g.fillStyle(0x2d465c, 1);
    g.fillRect(0, 0, 16, 2);
    g.fillRect(0, 0, 2, 16);
    g.fillStyle(0x162432, 1);
    g.fillRect(0, 14, 16, 2);
    g.fillRect(14, 0, 2, 16);
  });

  createTexture(scene, 'tile-chasm', 16, 16, (g) => {
    g.fillStyle(0x060b14, 1);
    g.fillRect(0, 0, 16, 16);
    g.fillStyle(0x111a2c, 1);
    g.fillRect(0, 0, 16, 1);
    g.fillRect(0, 15, 16, 1);
    g.fillStyle(0x1b2940, 1);
    g.fillRect(3, 3, 1, 1);
    g.fillRect(11, 6, 1, 1);
    g.fillRect(7, 12, 1, 1);
  });

  createTexture(scene, 'player-idle', 16, 16, (g) => {
    g.fillStyle(0x000000, 1);
    g.fillRect(4, 2, 8, 12);
    g.fillStyle(0xffd681, 1);
    g.fillRect(5, 3, 6, 4);
    g.fillStyle(0x3c5a8a, 1);
    g.fillRect(5, 7, 6, 6);
    g.fillStyle(0xaed4ff, 1);
    g.fillRect(6, 8, 4, 2);
    g.fillStyle(0x5d4230, 1);
    g.fillRect(5, 2, 6, 1);
  });



  createTexture(scene, 'sophene-npc', 16, 16, (g) => {
    g.fillStyle(0x000000, 1);
    g.fillRect(4, 2, 8, 12);
    g.fillStyle(0xd9e6ff, 1);
    g.fillRect(5, 3, 6, 4);
    g.fillStyle(0x7f99c7, 1);
    g.fillRect(5, 7, 6, 6);
    g.fillStyle(0xeef4ff, 1);
    g.fillRect(6, 8, 4, 2);
    g.fillStyle(0x93b8ff, 1);
    g.fillRect(3, 6, 1, 5);
    g.fillRect(12, 6, 1, 5);
  });

  createTexture(scene, 'memory-node', 16, 16, (g) => {
    g.fillStyle(0x0b1220, 1);
    g.fillRect(1, 1, 14, 14);
    g.fillStyle(0x7bd389, 1);
    g.fillRect(3, 3, 10, 10);
    g.fillStyle(0xb7ffd7, 1);
    g.fillRect(5, 5, 6, 6);
    g.fillStyle(0xe6fff3, 1);
    g.fillRect(7, 7, 2, 2);
  });

  createTexture(scene, 'bridge', 20, 8, (g) => {
    g.fillStyle(0x8ea9c9, 1);
    g.fillRect(0, 0, 20, 8);
    g.fillStyle(0xc8daf2, 1);
    g.fillRect(0, 0, 20, 1);
    g.fillStyle(0x5f7696, 1);
    for (let x = 2; x < 20; x += 4) {
      g.fillRect(x, 1, 1, 6);
    }
  });

  createTexture(scene, 'gate-locked', 8, 36, (g) => {
    g.fillStyle(0x40577a, 1);
    g.fillRect(0, 0, 8, 36);
    g.fillStyle(0x96afdc, 1);
    g.fillRect(0, 0, 8, 1);
    g.fillRect(0, 35, 8, 1);
    g.fillStyle(0x2d3e57, 1);
    for (let y = 2; y < 34; y += 4) g.fillRect(2, y, 4, 1);
  });



  createTexture(scene, 'portal-gate', 12, 20, (g) => {
    g.fillStyle(0x0c1222, 1);
    g.fillRect(0, 0, 12, 20);
    g.fillStyle(0x6cc8ff, 1);
    g.fillRect(1, 1, 10, 18);
    g.fillStyle(0xb9ecff, 1);
    g.fillRect(3, 3, 6, 14);
    g.fillStyle(0x6f9fd1, 1);
    g.fillRect(0, 0, 12, 1);
    g.fillRect(0, 19, 12, 1);
  });

  createTexture(scene, 'gate-open', 8, 36, (g) => {
    g.fillStyle(0x5ea7d8, 1);
    g.fillRect(0, 0, 8, 36);
    g.fillStyle(0xbfedff, 1);
    g.fillRect(0, 0, 8, 1);
    g.fillRect(0, 35, 8, 1);
    g.fillStyle(0xdff7ff, 1);
    for (let y = 3; y < 34; y += 5) g.fillRect(3, y, 2, 1);
  });
}

export function drawTiledArea(
  scene: Phaser.Scene,
  textureKey: string,
  x: number,
  y: number,
  w: number,
  h: number
): void {
  for (let yy = y; yy < y + h; yy += 16) {
    for (let xx = x; xx < x + w; xx += 16) {
      const tile = scene.add.image(xx + 8, yy + 8, textureKey);
      tile.setOrigin(0.5);
      tile.setDepth(-5);
    }
  }
}
