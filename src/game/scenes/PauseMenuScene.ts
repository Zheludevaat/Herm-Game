import Phaser from 'phaser';
import { COLORS, INTERNAL_HEIGHT, INTERNAL_WIDTH } from '../../core/constants';
import { clearSave } from '../../core/save';
import { playUiSound } from '../systems/audio';

export class PauseMenuScene extends Phaser.Scene {
  constructor() {
    super('pause_menu');
  }

  create(): void {
    this.add.rectangle(INTERNAL_WIDTH / 2, INTERNAL_HEIGHT / 2, INTERNAL_WIDTH, INTERNAL_HEIGHT, 0x000000, 0.6);

    const panel = this.add.rectangle(INTERNAL_WIDTH / 2, INTERNAL_HEIGHT / 2, 250, 124, 0x1a2740, 0.95);
    panel.setStrokeStyle(2, 0x6d87b7);

    this.add.text(54, 40, 'PAUSED', {
      fontFamily: 'monospace',
      fontSize: '12px',
      color: COLORS.text,
    });

    this.add.text(54, 58, 'ESC / ENTER: Resume', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#dce5ff',
    });

    this.add.text(54, 70, 'R: Clear save + Restart room', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#dce5ff',
    });

    this.add.text(54, 82, 'M: Main menu', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#dce5ff',
    });

    this.add.text(54, 94, 'Controls: Move WASD/Arrows, E Interact, Q Witness', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#9cc6ff',
    });

    const esc = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.ESC);
    const enter = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.ENTER);
    const reset = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.R);
    const menu = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.M);

    esc.on('down', () => { playUiSound(this, 'move'); this.resumePlay(); });
    enter.on('down', () => { playUiSound(this, 'confirm'); this.resumePlay(); });
    menu.on('down', () => {
      playUiSound(this, 'confirm');
      this.scene.stop();
      this.scene.stop('threshold');
      this.scene.stop('metaxy');
      this.scene.stop('play');
      this.scene.start('main_menu');
    });

    reset.on('down', () => {
      playUiSound(this, 'confirm');
      clearSave();
      this.scene.stop();
      this.scene.stop('threshold');
      this.scene.stop('metaxy');
      this.scene.stop('play');
      this.scene.start('play');
    });
  }

  private resumePlay(): void {
    this.scene.stop();
    this.scene.resume('play');
  }
}
