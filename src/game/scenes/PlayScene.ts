import Phaser from 'phaser';
import { DIALOGUE, type DialogueKey } from '../../content/dialogue';
import { MOON_CHAMBER_MAP } from '../../content/maps/moonChamber';
import { MOON_OBJECTIVES } from '../../content/quests/moonObjectives';
import { COLORS, INTERNAL_HEIGHT, INTERNAL_WIDTH } from '../../core/constants';
import { clearSave, loadSave, setCheckpoint, setScenePosition, type SaveData, writeSave } from '../../core/save';
import { drawTiledArea, ensurePixelArtTextures } from '../art/pixelArt';
import { QuestTracker } from '../systems/quest';
import { playUiSound } from '../systems/audio';
import { intersectsRect, renderMapBase } from '../systems/mapRenderer';
import { fadeIn, fadeToScene } from '../systems/transition';

type DialogueState = 'hidden' | 'active';

const clamp = (value: number, min: number, max: number): number => Phaser.Math.Clamp(value, min, max);

export class PlayScene extends Phaser.Scene {
  private player!: Phaser.GameObjects.Image;
  private sophene!: Phaser.GameObjects.Image;
  private cursors!: Phaser.Types.Input.Keyboard.CursorKeys;
  private wasd!: { [key: string]: Phaser.Input.Keyboard.Key };
  private interactKey!: Phaser.Input.Keyboard.Key;
  private witnessKey!: Phaser.Input.Keyboard.Key;
  private resetKey!: Phaser.Input.Keyboard.Key;
  private pauseKey!: Phaser.Input.Keyboard.Key;

  private interactable!: Phaser.GameObjects.Image;
  private bridge!: Phaser.GameObjects.Image;
  private exitGate!: Phaser.GameObjects.Image;

  private witnessText!: Phaser.GameObjects.Text;
  private uiText!: Phaser.GameObjects.Text;
  private objectiveText!: Phaser.GameObjects.Text;
  private gateHintText!: Phaser.GameObjects.Text;

  private dialogueBox!: Phaser.GameObjects.Container;
  private dialogueText!: Phaser.GameObjects.Text;

  private dialogueState: DialogueState = 'hidden';
  private witnessActive = false;
  private saveData!: SaveData;
  private quest = new QuestTracker(MOON_OBJECTIVES);

  private readonly playerSize = 12;
  private lastPositionSaveAt = 0;

  constructor() {
    super('play');
  }

  create(): void {
    this.saveData = setCheckpoint(loadSave(), 'play');
    ensurePixelArtTextures(this);
    fadeIn(this);

    this.cameras.main.setBackgroundColor(COLORS.background);

    renderMapBase(this, MOON_CHAMBER_MAP);
    drawTiledArea(
      this,
      'tile-chasm',
      MOON_CHAMBER_MAP.chasm.x,
      MOON_CHAMBER_MAP.chasm.y,
      MOON_CHAMBER_MAP.chasm.w,
      MOON_CHAMBER_MAP.chasm.h
    );

    this.add.text(12, 8, 'METAXY Prototype — Moon Chamber', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: COLORS.text,
    });

    this.add.text(12, INTERNAL_HEIGHT - 62, 'ESC: pause   R: reset save', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#a8b6dc',
    });

    this.player = this.add.image(this.saveData.playPosition.x, this.saveData.playPosition.y, 'player-idle');
    this.player.setOrigin(0.5);

    this.sophene = this.add.image(MOON_CHAMBER_MAP.sophene.x, MOON_CHAMBER_MAP.sophene.y, 'sophene-npc');
    this.add.text(MOON_CHAMBER_MAP.sophene.x - 12, MOON_CHAMBER_MAP.sophene.y - 18, 'Sophene', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#c2d9ff',
    });

    this.bridge = this.add.image(
      MOON_CHAMBER_MAP.bridge.x + MOON_CHAMBER_MAP.bridge.w / 2,
      MOON_CHAMBER_MAP.bridge.y + MOON_CHAMBER_MAP.bridge.h / 2,
      'bridge'
    );
    this.bridge.setVisible(false);

    this.interactable = this.add.image(MOON_CHAMBER_MAP.memoryNode.x, MOON_CHAMBER_MAP.memoryNode.y, 'memory-node');

    this.add.text(MOON_CHAMBER_MAP.memoryNode.x - 26, MOON_CHAMBER_MAP.memoryNode.y - 16, 'Memory Node', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: COLORS.text,
    });

    this.exitGate = this.add.image(MOON_CHAMBER_MAP.gate.x, MOON_CHAMBER_MAP.gate.y, 'gate-locked');

    this.gateHintText = this.add.text(228, 108, 'Gate locked', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#99abcf',
    });

    this.witnessText = this.add.text(12, 18, 'Witness: OFF (Q)', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#c9d3ff',
    });

    this.objectiveText = this.add.text(12, 28, '', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: '#f0f4ff',
      lineSpacing: 2,
    });

    this.cursors = this.input.keyboard!.createCursorKeys();
    this.wasd = this.input.keyboard!.addKeys('W,A,S,D') as { [key: string]: Phaser.Input.Keyboard.Key };
    this.interactKey = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.E);
    this.witnessKey = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.Q);
    this.resetKey = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.R);
    this.pauseKey = this.input.keyboard!.addKey(Phaser.Input.Keyboard.KeyCodes.ESC);

    this.uiText = this.add.text(12, INTERNAL_HEIGHT - 52, '', {
      fontFamily: 'monospace',
      fontSize: '8px',
      color: COLORS.text,
    });

    this.dialogueText = this.add.text(14, INTERNAL_HEIGHT - 38, '', {
      fontFamily: 'monospace',
      fontSize: '8px',
      wordWrap: { width: INTERNAL_WIDTH - 28 },
      color: COLORS.text,
    });

    const boxBg = this.add.rectangle(INTERNAL_WIDTH / 2, INTERNAL_HEIGHT - 19, INTERNAL_WIDTH - 8, 34, 0x000000, 0.75);
    boxBg.setStrokeStyle(1, 0x63739f);
    this.dialogueBox = this.add.container(0, 0, [boxBg, this.dialogueText]);

    if (this.saveData.firstNodeSeen) this.quest.markDone('touch_node');
    if (this.saveData.moonQuestComplete) {
      this.quest.markDone('open_witness');
      this.quest.markDone('cross_chasm');
    }

    this.updateGateState();
    this.updateObjectives();
    this.updateUi();
    this.say('intro');
  }

  update(time: number, delta: number): void {
    this.updateWitness(delta);
    this.animateSprites(time);

    if (Phaser.Input.Keyboard.JustDown(this.pauseKey)) {
      this.scene.launch('pause_menu');
      this.scene.pause();
      return;
    }

    if (Phaser.Input.Keyboard.JustDown(this.resetKey)) {
      clearSave();
      playUiSound(this, 'confirm');
      this.say('resetSave');
      this.scene.restart();
      return;
    }

    if (Phaser.Input.Keyboard.JustDown(this.witnessKey)) {
      this.toggleWitness();
    }

    const speed = 0.075 * delta;
    let dx = 0;
    let dy = 0;

    if (this.cursors.left.isDown || this.wasd.A.isDown) dx -= speed;
    if (this.cursors.right.isDown || this.wasd.D.isDown) dx += speed;
    if (this.cursors.up.isDown || this.wasd.W.isDown) dy -= speed;
    if (this.cursors.down.isDown || this.wasd.S.isDown) dy += speed;

    const candidateX = clamp(this.player.x + dx, 16, INTERNAL_WIDTH - 16);
    const candidateY = clamp(this.player.y + dy, 20, INTERNAL_HEIGHT - 20);

    if (!this.isBlocked(candidateX, this.player.y)) this.player.x = candidateX;
    if (!this.isBlocked(this.player.x, candidateY)) this.player.y = candidateY;

    if (time - this.lastPositionSaveAt > 250) {
      this.saveData = setScenePosition(this.saveData, 'play', { x: this.player.x, y: this.player.y });
      this.lastPositionSaveAt = time;
    }

    const nearNode = Phaser.Math.Distance.Between(
      this.player.x,
      this.player.y,
      this.interactable.x,
      this.interactable.y
    ) < 24;

    const nearSophene = Phaser.Math.Distance.Between(this.player.x, this.player.y, this.sophene.x, this.sophene.y) < 22;

    if (Phaser.Input.Keyboard.JustDown(this.interactKey)) {
      if (nearNode) {
        this.handleInteraction();
      } else if (nearSophene) {
        this.say('sopheneHint');
      }
    }

    if (!this.quest.isDone('cross_chasm') && this.player.x > 205 && this.player.y > 80 && this.player.y < 100) {
      this.quest.markDone('cross_chasm');
      this.saveData.moonQuestComplete = this.quest.isComplete();
      this.updateGateState();
      this.updateObjectives();
      this.updateUi();
      playUiSound(this, 'objective');
      this.say('questComplete');
    }

    const nearGate = Phaser.Math.Distance.Between(this.player.x, this.player.y, this.exitGate.x, this.exitGate.y) < 20;
    if (nearGate && this.quest.isComplete() && Phaser.Input.Keyboard.JustDown(this.interactKey)) {
      playUiSound(this, 'confirm');
      this.say('enterGate');
      this.time.delayedCall(220, () => fadeToScene(this, 'threshold'));
    }
  }

  private animateSprites(time: number): void {
    this.player.setScale(1 + Math.sin(time / 180) * 0.015);
    this.sophene.y = MOON_CHAMBER_MAP.sophene.y + Math.sin(time / 420) * 0.8;
  }

  private updateWitness(delta: number): void {
    const seconds = delta / 1000;

    if (this.witnessActive) {
      this.saveData.coherence = Math.max(0, this.saveData.coherence - 8 * seconds);
      if (this.saveData.coherence <= 0.01) {
        this.saveData.coherence = 0;
        this.witnessActive = false;
        this.bridge.setVisible(false);
        playUiSound(this, 'deny');
        this.say('autoDrop');
      }
    } else {
      this.saveData.coherence = Math.min(100, this.saveData.coherence + 4 * seconds);
    }

    this.witnessText.setText(`Witness: ${this.witnessActive ? 'ON' : 'OFF'} (Q)`);
    this.updateUi(false);
  }

  private isBlocked(nextX: number, nextY: number): boolean {
    for (const wall of MOON_CHAMBER_MAP.walls) {
      if (intersectsRect(nextX, nextY, this.playerSize, this.playerSize, wall)) return true;
    }

    if (intersectsRect(nextX, nextY, this.playerSize, this.playerSize, MOON_CHAMBER_MAP.chasm)) {
      const onBridge = intersectsRect(nextX, nextY, this.playerSize, this.playerSize, MOON_CHAMBER_MAP.bridge);
      if (!(this.witnessActive && onBridge)) return true;
    }

    return false;
  }

  private updateGateState(): void {
    const unlocked = this.quest.isComplete();
    this.exitGate.setTexture(unlocked ? 'gate-open' : 'gate-locked');
    this.gateHintText.setText(unlocked ? 'Gate ready (E)' : 'Gate locked');
    this.gateHintText.setColor(unlocked ? '#bfe7ff' : '#99abcf');
  }

  private toggleWitness(): void {
    if (!this.witnessActive && this.saveData.coherence <= 5) {
      playUiSound(this, 'deny');
      this.say('lowCoherence');
      return;
    }

    this.witnessActive = !this.witnessActive;
    this.bridge.setVisible(this.witnessActive);

    if (this.witnessActive) {
      this.quest.markDone('open_witness');
      this.updateObjectives();
      this.updateUi();
      playUiSound(this, 'confirm');
      this.say('witnessOn');
    } else {
      playUiSound(this, 'move');
      this.say('witnessOff');
    }
  }

  private handleInteraction(): void {
    const firstTime = !this.saveData.firstNodeSeen;

    this.saveData.firstNodeSeen = true;
    this.saveData.clarity += 1;
    this.quest.markDone('touch_node');
    this.updateObjectives();
    this.updateUi();

    playUiSound(this, firstTime ? 'objective' : 'confirm');
    this.say(firstTime ? 'nodeFirst' : 'nodeRepeat');
  }

  private say(key: DialogueKey): void {
    this.dialogueState = 'active';
    this.dialogueText.setText(DIALOGUE[key]);
    this.dialogueBox.setVisible(true);
  }

  private updateObjectives(): void {
    this.objectiveText.setText(this.quest.lines().join('\n'));
  }

  private updateUi(write = true): void {
    this.uiText.setText(
      `Coherence: ${Math.round(this.saveData.coherence)}   Clarity: ${this.saveData.clarity}   Quest: ${
        this.quest.isComplete() ? 'Complete' : 'In Progress'
      }`
    );

    if (write) writeSave(this.saveData);
  }
}
