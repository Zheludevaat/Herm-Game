export const DIALOGUE = {
  intro:
    'Sophene: Press Q for Witness. It reveals a hidden bridge and drains Coherence. Touch the Memory Node and then cross the chasm.',
  sopheneHint: 'Sophene: I will wait at each boundary. Cross by clarity, not speed.',
  witnessOn: 'Sophene: Witness opened. Some paths are true only while attention is sustained.',
  witnessOff: 'Sophene: Witness closed. Hold what you learned.',
  lowCoherence: 'Sophene: Not enough Coherence to open Witness. Pause and recover.',
  autoDrop: 'Sophene: Coherence depleted. Witness released automatically.',
  nodeFirst: 'Memory Node: First recognition recorded. Clarity +1. Save updated.',
  nodeRepeat: 'Memory Node: Recognition repeated. Clarity +1.',
  questComplete: 'Sophene: You crossed by seeing, not forcing. Objective complete. Reach the gate and press E.',
  enterGate: 'Sophene: Threshold opens. Continue.',
  resetSave: 'Sophene: Save cleared. Returning to first threshold state.',
  metaxyArrival: 'Sophene: This is the Metaxy corridor between acts. Continue when you are ready.',
  metaxyReturn: 'Sophene: You may revisit the Moon chamber to reflect.',
} as const;

export type DialogueKey = keyof typeof DIALOGUE;
