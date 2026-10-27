import random
from dataclasses import replace

from .lessons import TOPICS
from .questions import QUESTIONS


def shuffle_choices(question, rng=None):
    rng = rng or random
    indices = list(range(4))
    rng.shuffle(indices)
    return replace(question, choices=tuple(question.choices[i] for i in indices),
                   answer=indices.index(question.answer))


def select_exam(stage, rng=None):
    rng = rng or random
    eligible = [q for q in QUESTIONS if stage in q.stages]
    if stage == 1:
        selected = rng.sample(eligible, 50)
    elif stage == 2:
        ops = [q for q in eligible if TOPICS[q.topic].section != "use"]
        use = [q for q in eligible if TOPICS[q.topic].section == "use"]
        selected = rng.sample(ops, 48) + rng.sample(use, 32)
    else:
        raise ValueError("시험 차수는 1 또는 2입니다.")
    return [shuffle_choices(q, rng) for q in selected]


def score_exam(stage, questions, answers):
    sections = {}
    correct = 0
    for index, question in enumerate(questions):
        section = "리눅스 일반" if stage == 1 else (
            "리눅스 활용" if TOPICS[question.topic].section == "use" else "리눅스 운영 및 관리")
        score = sections.setdefault(section, {"correct": 0, "total": 0})
        score["total"] += 1
        if answers.get(index) == question.answer:
            correct += 1
            score["correct"] += 1
    for value in sections.values():
        value["percent"] = round(value["correct"] * 100 / value["total"], 2)
    total = round(correct * 100 / len(questions), 2)
    failed_sections = [name for name, value in sections.items()
        if stage == 2 and value["correct"] * 100 < value["total"] * 40]
    return {"stage": stage, "correct": correct, "total": len(questions), "score": total,
            "sections": sections, "failed_sections": failed_sections,
            "passed": correct * 100 >= len(questions) * 60 and not failed_sections}
