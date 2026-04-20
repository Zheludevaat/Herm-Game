import Phaser from 'phaser';
import { COLORS, INTERNAL_HEIGHT, INTERNAL_WIDTH } from '../../core/constants';
import { fadeIn, fadeToScene } from '../systems/transition';

export class ThresholdScene extends Phaser.Scene {
  constructor() {
    super('threshold');
  }

  create(): void {
    fadeIn(this);
    this.cameras.main.setBackgroundColor(0x0d1324);

    const panel = this.add.rectangle(INTERNAL_WIDTH / 2, INTERNAL_HEIGHT / 2, 280, 130, 0x1a2740, 0.95);
    panel.setStrokeStyle(2, 0x6d87b7);

    this.add.text(18, 36, 'Threshold Reached', {
      fontFamily: 'monospace',
      fontSize: '12px',
      color: COLORS.text,
    });

    this.add.text(18, 62, 'You completed the Moon prototype objective loop.', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#d7defb',
    });

    this.add.text(18, 76, 'Next step: transition to authored Moon hub content.', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#d7defb',
    });

    this.add.text(18, 102, 'Press ENTER to continue into the Metaxy corridor.', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#9cc6ff',
    });

    const enterKey = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.ENTER);
    enterKey.once('down', () => {
      fadeToScene(this, 'metaxy');
    });

    panel.setDepth(-1);
  }
}
