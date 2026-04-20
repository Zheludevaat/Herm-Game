from dataclasses import asdict, dataclass, field


@dataclass
class SoulState:
    coherence: int = 100
    clarity: int = 0
    memory_shards: int = 0
    moon_completed: bool = False
    mercury_completed: bool = False
    venus_completed: bool = False
    mars_completed: bool = False
    moon_spoken: bool = False
    mercury_spoken: bool = False
    venus_spoken: bool = False
    mars_spoken: bool = False
    moon_trial_passed: bool = False
    mercury_trial_passed: bool = False
    venus_trial_passed: bool = False
    mars_trial_passed: bool = False
    calling: str = ""
    reception_complete: bool = False
    verbs_mastered: list[str] = field(default_factory=list)
    completed_side_quests: list[str] = field(default_factory=list)
    relics_collected: list[str] = field(default_factory=list)
    final_ending: str = ""
    high_contrast: bool = False
    reduced_flash: bool = False
    ui_font_size: int = 12

    def gain_clarity(self, amount: int) -> None:
        self.clarity = max(0, self.clarity + amount)

    def lose_coherence(self, amount: int) -> None:
        self.coherence = max(0, self.coherence - amount)

    def recover_coherence(self, amount: int) -> None:
        self.coherence = min(100, self.coherence + amount)

    def gain_memory_shard(self, amount: int = 1) -> None:
        self.memory_shards = max(0, self.memory_shards + amount)
        self.gain_clarity(amount)

    def mark_verb(self, verb_name: str) -> None:
        if verb_name not in self.verbs_mastered:
            self.verbs_mastered.append(verb_name)

    def complete_side_quest(self, quest_id: str) -> bool:
        if quest_id in self.completed_side_quests:
            return False
        self.completed_side_quests.append(quest_id)
        return True

    def collect_relic(self, relic_name: str) -> bool:
        if relic_name in self.relics_collected:
            return False
        self.relics_collected.append(relic_name)
        return True

    def cycle_font_size(self, delta: int) -> None:
        allowed = [10, 12, 14]
        current_index = allowed.index(self.ui_font_size) if self.ui_font_size in allowed else 1
        current_index = max(0, min(len(allowed) - 1, current_index + delta))
        self.ui_font_size = allowed[current_index]

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "SoulState":
        return cls(
            coherence=int(data.get("coherence", 100)),
            clarity=int(data.get("clarity", 0)),
            memory_shards=int(data.get("memory_shards", 0)),
            moon_completed=bool(data.get("moon_completed", False)),
            mercury_completed=bool(data.get("mercury_completed", False)),
            venus_completed=bool(data.get("venus_completed", False)),
            mars_completed=bool(data.get("mars_completed", False)),
            moon_spoken=bool(data.get("moon_spoken", False)),
            mercury_spoken=bool(data.get("mercury_spoken", False)),
            venus_spoken=bool(data.get("venus_spoken", False)),
            mars_spoken=bool(data.get("mars_spoken", False)),
            moon_trial_passed=bool(data.get("moon_trial_passed", False)),
            mercury_trial_passed=bool(data.get("mercury_trial_passed", False)),
            venus_trial_passed=bool(data.get("venus_trial_passed", False)),
            mars_trial_passed=bool(data.get("mars_trial_passed", False)),
            calling=str(data.get("calling", "")),
            reception_complete=bool(data.get("reception_complete", False)),
            verbs_mastered=[str(item) for item in data.get("verbs_mastered", [])],
            completed_side_quests=[str(item) for item in data.get("completed_side_quests", [])],
            relics_collected=[str(item) for item in data.get("relics_collected", [])],
            final_ending=str(data.get("final_ending", "")),
            high_contrast=bool(data.get("high_contrast", False)),
            reduced_flash=bool(data.get("reduced_flash", False)),
            ui_font_size=int(data.get("ui_font_size", 12)),
        )
