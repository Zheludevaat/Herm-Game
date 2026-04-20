import Phaser from 'phaser';
import { loadSave } from '../../core/save';

type UiSound = 'move' | 'confirm' | 'deny' | 'objective';

function getAudioContext(scene: Phaser.Scene): AudioContext | null {
  const manager = scene.sound as Phaser.Sound.NoAudioSoundManager | Phaser.Sound.HTML5AudioSoundManager | Phaser.Sound.WebAudioSoundManager;
  if ('context' in manager && manager.context) return manager.context;
  return null;
}

function tone(scene: Phaser.Scene, frequency: number, durationMs: number, volume: number): void {
  const ctx = getAudioContext(scene);
  if (!ctx) return;

  const osc = ctx.createOscillator();
  const gain = ctx.createGain();

  osc.type = 'square';
  osc.frequency.value = frequency;

  gain.gain.setValueAtTime(0.0001, ctx.currentTime);
  gain.gain.exponentialRampToValueAtTime(Math.max(0.0001, volume), ctx.currentTime + 0.01);
  gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + durationMs / 1000);

  osc.connect(gain);
  gain.connect(ctx.destination);

  osc.start();
  osc.stop(ctx.currentTime + durationMs / 1000 + 0.01);
}

export function playUiSound(scene: Phaser.Scene, kind: UiSound): void {
  const volume = loadSave().sfxVolume;
  if (volume <= 0) return;

  switch (kind) {
    case 'move':
      tone(scene, 440, 45, volume * 0.25);
      break;
    case 'confirm':
      tone(scene, 660, 70, volume * 0.35);
      break;
    case 'deny':
      tone(scene, 220, 90, volume * 0.35);
      break;
    case 'objective':
      tone(scene, 660, 65, volume * 0.25);
      scene.time.delayedCall(75, () => tone(scene, 880, 90, volume * 0.28));
      break;
  }
}
