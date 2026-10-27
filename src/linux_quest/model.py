from dataclasses import dataclass, field


DIFFICULTIES = {"beginner": "초급", "intermediate": "중급", "advanced": "고급"}


@dataclass(frozen=True)
class Topic:
    id: str
    title: str
    section: str
    lesson: str


@dataclass(frozen=True)
class Question:
    id: str
    topic: str
    stem: str
    choices: tuple[str, ...]
    answer: int
    explanation: str
    stages: tuple[int, ...] = (1, 2)


@dataclass(frozen=True)
class Mission:
    id: str
    chapter: int
    title: str
    story: str
    topics: tuple[str, ...]
    objective: str
    setup: str = ""
    goals: tuple[dict, ...] = ()
    extra: tuple[dict, ...] = ()
    advanced: tuple[dict, ...] = ()
    hints: tuple[str, ...] = ()
    example: str = ""
    debrief: str = ""
    clue: str = ""
    kind: str = "lab"
    boss: bool = False
    network: bool = False
    prerequisites: tuple[str, ...] = ()
    question_ids: tuple[str, ...] = ()
    variants: tuple[str, ...] = ("a", "b", "c")

    def conditions(self, difficulty: str, variant: str = "a") -> list[dict]:
        selected = list(self.goals)
        if difficulty != "beginner":
            selected.extend(self.extra)
        if difficulty == "advanced":
            selected.extend(self.advanced)
        return [{k: v.replace("{v}", variant) if isinstance(v, str) else v
                 for k, v in goal.items()} for goal in selected]


@dataclass
class CheckResult:
    success: bool
    unmet: list[str] = field(default_factory=list)
