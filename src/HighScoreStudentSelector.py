# -*- coding: utf-8 -*-
import random
from .Types import DataType


class HighScoreStudentSelector:
    MIN_SCORE = 76
    MIN_SUBJECTS = 3

    def __init__(self, data: DataType):
        self.data = data
        self.qualified_students = []

    def get_student(self) -> str | None:
        self.qualified_students = []
        for student, subjects in self.data.items():
            high_count = sum(1 for _, score in subjects if score >= self.MIN_SCORE)
            if high_count >= self.MIN_SUBJECTS:
                self.qualified_students.append(student)

        if not self.qualified_students:
            return None

        return random.choice(self.qualified_students)