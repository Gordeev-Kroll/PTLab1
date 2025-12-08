# -*- coding: utf-8 -*-
import pytest
from src.HighScoreStudentSelector import HighScoreStudentSelector
from src.Types import DataType


class TestHighScoreStudentSelector:
    @pytest.fixture
    def sample_data(self) -> DataType:
        return {
            "Иванов А.А.": [("математика", 90), ("физика", 85), ("химия", 76)],
            "Петров Б.Б.": [("математика", 70), ("физика", 80), ("химия", 75)],
            "Сидоров В.В.": [("математика", 88), ("физика", 90), ("химия", 95), ("информатика", 82)],
            "Козлов Г.Г.": [("математика", 60), ("физика", 65), ("химия", 70)],
        }

    def test_finds_at_least_one_student(self, sample_data):
        selector = HighScoreStudentSelector(sample_data)
        result = selector.get_student()
        assert result is not None
        assert result in sample_data

    def test_finds_multiple_and_returns_random(self, sample_data, monkeypatch):
        calls = []
        def fake_choice(seq):
            calls.append(seq)
            return seq[0]
        monkeypatch.setattr("random.choice", fake_choice)

        selector = HighScoreStudentSelector(sample_data)
        selector.get_student()
        assert "Иванов А.А." in calls[0]
        assert "Сидоров В.В." in calls[0]

    def test_no_student_meets_criteria(self):
        data: DataType = {
            "Студент1": [("а", 70), ("б", 75)],
            "Студент2": [("в", 60)],
        }
        selector = HighScoreStudentSelector(data)
        assert selector.get_student() is None