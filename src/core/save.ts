export type SceneCheckpoint = 'play' | 'metaxy';

export type SavedPosition = {
  x: number;
  y: number;
};

export type SaveData = {
  clarity: number;
  coherence: number;
  firstNodeSeen: boolean;
  moonQuestComplete: boolean;
  checkpoint: SceneCheckpoint;
  sfxVolume: number;
  playPosition: SavedPosition;
  metaxyPosition: SavedPosition;
};

const SAVE_KEY = 'metaxy_web_save_v1';

export const defaultSaveData = (): SaveData => ({
  clarity: 0,
  coherence: 100,
  firstNodeSeen: false,
  moonQuestComplete: false,
  checkpoint: 'play',
  sfxVolume: 0.5,
  playPosition: { x: 40, y: 90 },
  metaxyPosition: { x: 36, y: 90 },
});

const clampPosition = (pos: Partial<SavedPosition> | undefined, fallback: SavedPosition): SavedPosition => ({
  x: typeof pos?.x === 'number' ? pos.x : fallback.x,
  y: typeof pos?.y === 'number' ? pos.y : fallback.y,
});

export function loadSave(): SaveData {
  const raw = window.localStorage.getItem(SAVE_KEY);
  if (!raw) return defaultSaveData();

  try {
    const parsed = JSON.parse(raw) as Partial<SaveData>;
    const fallback = defaultSaveData();

    return {
      clarity: typeof parsed.clarity === 'number' ? parsed.clarity : 0,
      coherence: typeof parsed.coherence === 'number' ? parsed.coherence : 100,
      firstNodeSeen: parsed.firstNodeSeen === true,
      moonQuestComplete: parsed.moonQuestComplete === true,
      checkpoint: parsed.checkpoint === 'metaxy' ? 'metaxy' : 'play',
      sfxVolume: typeof parsed.sfxVolume === 'number' ? Math.min(1, Math.max(0, parsed.sfxVolume)) : 0.5,
      playPosition: clampPosition(parsed.playPosition, fallback.playPosition),
      metaxyPosition: clampPosition(parsed.metaxyPosition, fallback.metaxyPosition),
    };
  } catch {
    return defaultSaveData();
  }
}

export function writeSave(data: SaveData): void {
  window.localStorage.setItem(SAVE_KEY, JSON.stringify(data));
}

export function clearSave(): void {
  window.localStorage.removeItem(SAVE_KEY);
}

export function setCheckpoint(data: SaveData, checkpoint: SceneCheckpoint): SaveData {
  const next = { ...data, checkpoint };
  writeSave(next);
  return next;
}

export function setSfxVolume(data: SaveData, sfxVolume: number): SaveData {
  const next = { ...data, sfxVolume: Math.min(1, Math.max(0, sfxVolume)) };
  writeSave(next);
  return next;
}

export function setScenePosition(
  data: SaveData,
  scene: SceneCheckpoint,
  position: SavedPosition
): SaveData {
  const key = scene === 'play' ? 'playPosition' : 'metaxyPosition';
  const next = {
    ...data,
    [key]: position,
  } as SaveData;

  writeSave(next);
  return next;
}
