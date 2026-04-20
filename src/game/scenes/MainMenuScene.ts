import Phaser from 'phaser';
import { INTERNAL_HEIGHT, INTERNAL_WIDTH } from '../../core/constants';
import { clearSave, loadSave, setSfxVolume, type SaveData } from '../../core/save';
import { ensurePixelArtTextures } from '../art/pixelArt';
import { playUiSound } from '../systems/audio';
import { fadeIn, fadeToScene } from '../systems/transition';

type MenuItem = {
  label: string;
  action: () => void;
};

export class MainMenuScene extends Phaser.Scene {
  private items: MenuItem[] = [];
  private labels: Phaser.GameObjects.Text[] = [];
  private cursor = 0;
  private saveData!: SaveData;
  private volumeText!: Phaser.GameObjects.Text;

  constructor() {
    super('main_menu');
  }

  create(): void {
    ensurePixelArtTextures(this);
    fadeIn(this, 260);
    this.saveData = loadSave();

    this.cameras.main.setBackgroundColor(0x0d1324);
    this.add.rectangle(INTERNAL_WIDTH / 2, INTERNAL_HEIGHT / 2, 300, 160, 0x18233d).setStrokeStyle(2, 0x6d87b7);

    this.add.text(22, 20, 'METAXY: The Soul\'s Ascent', {
      fontFamily: 'monospace',
      fontSize: '12px',
      color: '#e8eeff',
    });

    this.add.text(22, 36, `Playtest Build - Checkpoint: ${this.saveData.checkpoint.toUpperCase()}`, {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#adc3e8',
    });
    const continueScene = this.saveData.checkpoint;

    this.items = [
      {
        label: 'Start Moon Chamber',
        action: () => {
          playUiSound(this, 'confirm');
          fadeToScene(this, 'play');
        },
      },
      {
        label: 'Continue',
        action: () => {
          playUiSound(this, 'confirm');
          fadeToScene(this, continueScene);
        },
      },
      {
        label: 'Clear Save Data',
        action: () => {
          playUiSound(this, 'confirm');
          clearSave();
          this.scene.restart();
        },
      },
    ];

    this.labels = this.items.map((item, index) =>
      this.add.text(38, 70 + index * 16, item.label, {
        fontFamily: 'monospace',
        fontSize: '9px',
        color: '#dce5ff',
      })
    );

    this.volumeText = this.add.text(22, 124, '', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#bfd7ff',
    });
    this.refreshVolumeText();

    this.add.text(22, 138, 'Arrows/W,S: navigate  Enter/E: select  [/]: volume', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#93b7ec',
    });

    this.refreshSelection();

    const up = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.UP);
    const down = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.DOWN);
    const w = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.W);
    const s = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.S);
    const enter = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.ENTER);
    const e = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.E);
    const leftBracket = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.OPEN_BRACKET);
    const rightBracket = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.CLOSED_BRACKET);

    up.on('down', () => this.move(-1));
    w.on('down', () => this.move(-1));
    down.on('down', () => this.move(1));
    s.on('down', () => this.move(1));
    enter.on('down', () => this.select());
    e.on('down', () => this.select());
    leftBracket.on('down', () => this.adjustVolume(-0.1));
    rightBracket.on('down', () => this.adjustVolume(0.1));
  }

  private move(direction: -1 | 1): void {
    this.cursor = (this.cursor + direction + this.items.length) % this.items.length;
    playUiSound(this, 'move');
    this.refreshSelection();
  }

  private select(): void {
    this.items[this.cursor]?.action();
  }

  private adjustVolume(delta: number): void {
    this.saveData = setSfxVolume(this.saveData, this.saveData.sfxVolume + delta);
    playUiSound(this, 'move');
    this.refreshVolumeText();
  }

  private refreshVolumeText(): void {
    this.volumeText.setText(`SFX Volume: ${Math.round(this.saveData.sfxVolume * 100)}%`);
  }

  private refreshSelection(): void {
    this.labels.forEach((label, index) => {
      const selected = index === this.cursor;
      label.setText(`${selected ? '>' : ' '} ${this.items[index].label}`);
      label.setColor(selected ? '#bfe7ff' : '#dce5ff');
    });
  }
}
