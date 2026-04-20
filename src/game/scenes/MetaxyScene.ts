import Phaser from 'phaser';
import { DIALOGUE } from '../../content/dialogue';
import { METAXY_CORRIDOR_MAP } from '../../content/maps/metaxyCorridor';
import { INTERNAL_HEIGHT, INTERNAL_WIDTH } from '../../core/constants';
import { loadSave, setCheckpoint, setScenePosition, type SaveData } from '../../core/save';
import { ensurePixelArtTextures } from '../art/pixelArt';
import { playUiSound } from '../systems/audio';
import { intersectsRect, renderMapBase } from '../systems/mapRenderer';
import { fadeIn, fadeToScene } from '../systems/transition';

export class MetaxyScene extends Phaser.Scene {
  private player!: Phaser.GameObjects.Image;
  private cursors!: Phaser.Types.Input.Keyboard.CursorKeys;
  private wasd!: { [key: string]: Phaser.Input.Keyboard.Key };
  private interactKey!: Phaser.Input.Keyboard.Key;

  private leftGate!: Phaser.GameObjects.Image;
  private rightGate!: Phaser.GameObjects.Image;
  private hintText!: Phaser.GameObjects.Text;

  private readonly playerSize = 12;
  private saveData!: SaveData;
  private lastPositionSaveAt = 0;

  constructor() {
    super('metaxy');
  }

  create(): void {
    this.saveData = setCheckpoint(loadSave(), 'metaxy');
    ensurePixelArtTextures(this);
    fadeIn(this);

    this.cameras.main.setBackgroundColor(0x101729);
    renderMapBase(this, METAXY_CORRIDOR_MAP, 0x1b2440);

    this.leftGate = this.add.image(METAXY_CORRIDOR_MAP.returnGate.x, METAXY_CORRIDOR_MAP.returnGate.y, 'portal-gate');
    this.rightGate = this.add.image(METAXY_CORRIDOR_MAP.onwardGate.x, METAXY_CORRIDOR_MAP.onwardGate.y, 'portal-gate');

    this.player = this.add.image(this.saveData.metaxyPosition.x, this.saveData.metaxyPosition.y, 'player-idle');

    this.add.text(12, 10, 'Metaxy Corridor', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#d6e1ff',
    });

    this.hintText = this.add.text(12, INTERNAL_HEIGHT - 42, DIALOGUE.metaxyArrival, {
      fontFamily: 'monospace',
      fontSize: '8px',
      wordWrap: { width: INTERNAL_WIDTH - 24 },
      color: '#c2d5ff',
    });

    this.add.text(12, INTERNAL_HEIGHT - 56, 'E near gate: travel', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#8db9f0',
    });

    this.cursors = this.input.keyboard!.createCursorKeys();
    this.wasd = this.input.keyboard!.addKeys('W,A,S,D') as { [key: string]: Phaser.Input.Keyboard.Key };
    this.interactKey = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.E);
  }

  update(_time: number, delta: number): void {
    const speed = 0.075 * delta;
    let dx = 0;
    let dy = 0;

    if (this.cursors.left.isDown || this.wasd.A.isDown) dx -= speed;
    if (this.cursors.right.isDown || this.wasd.D.isDown) dx += speed;
    if (this.cursors.up.isDown || this.wasd.W.isDown) dy -= speed;
    if (this.cursors.down.isDown || this.wasd.S.isDown) dy += speed;

    const nx = Phaser.Math.Clamp(this.player.x + dx, 16, INTERNAL_WIDTH - 16);
    const ny = Phaser.Math.Clamp(this.player.y + dy, 20, INTERNAL_HEIGHT - 20);

    const blocked = METAXY_CORRIDOR_MAP.walls.some((w) => intersectsRect(nx, ny, this.playerSize, this.playerSize, w));
    if (!blocked) {
      this.player.x = nx;
      this.player.y = ny;
    }

    if (_time - this.lastPositionSaveAt > 250) {
      this.saveData = setScenePosition(this.saveData, 'metaxy', { x: this.player.x, y: this.player.y });
      this.lastPositionSaveAt = _time;
    }

    const nearLeft = Phaser.Math.Distance.Between(this.player.x, this.player.y, this.leftGate.x, this.leftGate.y) < 18;
    const nearRight = Phaser.Math.Distance.Between(this.player.x, this.player.y, this.rightGate.x, this.rightGate.y) < 18;

    if (nearLeft) this.hintText.setText(DIALOGUE.metaxyReturn);
    else if (nearRight) this.hintText.setText('Sophene: Onward gate is reserved for next act content.');
    else this.hintText.setText(DIALOGUE.metaxyArrival);

    if (Phaser.Input.Keyboard.JustDown(this.interactKey) && nearLeft) {
      playUiSound(this, 'confirm');
      fadeToScene(this, 'play');
    }
  }
}
