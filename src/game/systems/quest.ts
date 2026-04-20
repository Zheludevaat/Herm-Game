export type ObjectiveId = 'touch_node' | 'open_witness' | 'cross_chasm';

export type Objective = {
  id: ObjectiveId;
  text: string;
  done: boolean;
};

export class QuestTracker {
  private objectives: Objective[];

  constructor(seedObjectives: Objective[]) {
    this.objectives = seedObjectives.map((item) => ({ ...item }));
  }

  markDone(id: ObjectiveId): void {
    const objective = this.objectives.find((item) => item.id === id);
    if (objective) objective.done = true;
  }

  isDone(id: ObjectiveId): boolean {
    return this.objectives.some((item) => item.id === id && item.done);
  }

  isComplete(): boolean {
    return this.objectives.every((item) => item.done);
  }

  lines(): string[] {
    return this.objectives.map((item) => `${item.done ? '✓' : '•'} ${item.text}`);
  }
}
