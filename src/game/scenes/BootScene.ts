import Phaser from 'phaser';
import { MainMenuScene } from './MainMenuScene';
import { MetaxyScene } from './MetaxyScene';
import { PauseMenuScene } from './PauseMenuScene';
import { PlayScene } from './PlayScene';
import { ThresholdScene } from './ThresholdScene';

export class BootScene extends Phaser.Scene {
  constructor() {
    super('boot');
  }

  create(): void {
    this.scene.start('main_menu');
  }
}

export const SCENES = [BootScene, MainMenuScene, PlayScene, ThresholdScene, MetaxyScene, PauseMenuScene];
