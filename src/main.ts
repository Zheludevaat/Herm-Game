import Phaser from 'phaser';
import { INTERNAL_HEIGHT, INTERNAL_WIDTH, SCALE } from './core/constants';
import { SCENES } from './game/scenes/BootScene';

const app = document.getElementById('app');

if (!app) {
  throw new Error('Missing #app container');
}

const config: Phaser.Types.Core.GameConfig = {
  type: Phaser.AUTO,
  width: INTERNAL_WIDTH,
  height: INTERNAL_HEIGHT,
  parent: app,
  backgroundColor: '#101820',
  pixelArt: true,
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH,
    zoom: SCALE,
  },
  physics: {
    default: 'arcade',
    arcade: {
      debug: false,
    },
  },
  scene: SCENES,
};

new Phaser.Game(config);
