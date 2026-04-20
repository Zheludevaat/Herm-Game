import Phaser from 'phaser';

export function fadeIn(scene: Phaser.Scene, duration = 180): void {
  scene.cameras.main.fadeIn(duration, 0, 0, 0);
}

export function fadeToScene(scene: Phaser.Scene, targetScene: string, duration = 220): void {
  scene.cameras.main.once(Phaser.Cameras.Scene2D.Events.FADE_OUT_COMPLETE, () => {
    scene.scene.start(targetScene);
  });

  scene.cameras.main.fadeOut(duration, 0, 0, 0);
}
