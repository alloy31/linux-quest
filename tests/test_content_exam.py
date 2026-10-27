import random
import unittest
from collections import Counter

from linux_quest.app import content_errors
from linux_quest.campaign import MISSIONS
from linux_quest.exam import score_exam, select_exam, shuffle_choices
from linux_quest.lessons import OFFICIAL_COVERAGE, TOPICS
from linux_quest.questions import QUESTIONS


class ContentTests(unittest.TestCase):
    def test_official_topics_have_lessons_missions_and_original_assessments(self):
        self.assertEqual(content_errors(), [])
        covered = {t for m in MISSIONS for t in m.topics}
        for row in OFFICIAL_COVERAGE.values():
            for topic in row:
                self.assertIn(topic, covered)
                self.assertTrue(TOPICS[topic].lesson)
                self.assertGreaterEqual(sum(q.topic == topic for q in QUESTIONS), 4)

    def test_each_chapter_has_a_capstone_and_advanced_adds_conditions(self):
        self.assertEqual(Counter(m.chapter for m in MISSIONS), Counter({i: 4 for i in range(1, 11)}))
        for chapter in range(1, 11):
            self.assertTrue(any(m.boss for m in MISSIONS if m.chapter == chapter))
        for m in MISSIONS:
            if m.kind != "scenario":
                self.assertLess(len(m.conditions("beginner")), len(m.conditions("intermediate")))
                self.assertLess(len(m.conditions("intermediate")), len(m.conditions("advanced")))

    def test_variants_are_rendered_in_goals(self):
        for m in MISSIONS:
            for v in m.variants:
                for goal in m.conditions("advanced", v):
                    self.assertNotIn("{v}", str(goal))


class ExamTests(unittest.TestCase):
    def test_fixed_sizes_unique_questions_and_second_exam_subject_distribution(self):
        for seed in range(10):
            first = select_exam(1, random.Random(seed))
            second = select_exam(2, random.Random(seed))
            self.assertEqual(len({q.id for q in first}), 50)
            self.assertEqual(len({q.id for q in second}), 80)
            self.assertEqual(sum(TOPICS[q.topic].section == "use" for q in second), 32)
            self.assertTrue(all(1 in q.stages for q in first))

    def test_subject_failure_overrides_passing_total_score(self):
        questions = select_exam(2, random.Random(7))
        answers = {i: q.answer for i, q in enumerate(questions[:48])}
        result = score_exam(2, questions, answers)
        self.assertEqual(result["score"], 60)
        self.assertFalse(result["passed"])
        self.assertEqual(result["failed_sections"], ["리눅스 활용"])

    def test_exact_sixty_percent_and_unequal_subject_cutoffs(self):
        questions = select_exam(2, random.Random(7))
        answers = {i: questions[i].answer for i in list(range(35)) + list(range(48, 61))}
        self.assertTrue(score_exam(2, questions, answers)["passed"])
        # 19/48 is below 40%, although 19+32 reaches 60% overall.
        answers = {i: questions[i].answer for i in list(range(19)) + list(range(48, 80))}
        self.assertFalse(score_exam(2, questions, answers)["passed"])

    def test_shuffle_keeps_correct_answer_and_uses_multiple_positions(self):
        q = QUESTIONS[0]
        positions = set()
        for seed in range(20):
            shuffled = shuffle_choices(q, random.Random(seed))
            self.assertEqual(shuffled.choices[shuffled.answer], q.choices[q.answer])
            positions.add(shuffled.answer)
        self.assertEqual(positions, set(range(4)))

    def test_unanswered_questions_are_included_in_denominator(self):
        questions = select_exam(1, random.Random(0))
        result = score_exam(1, questions, {i: q.answer for i, q in enumerate(questions[:30])})
        self.assertTrue(result["passed"])
        self.assertEqual(result["score"], 60)
        self.assertFalse(score_exam(1, questions, {})["passed"])
