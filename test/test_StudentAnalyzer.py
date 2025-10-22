import pytest
from src.StudentAnalyzer import StudentAnalyzer
from src.Types import DataType


@pytest.fixture
def sample_data() -> DataType:
    return {
        "Иванов Иван": [("математика", 90), ("литература", 90)],
        "Петров Петр": [("математика", 85), ("химия", 90)],
        "Сидоров Сидор": [("математика", 90),
                          ("литература", 90), ("программирование", 90)],
    }


def test_find_student_with_all_90_exists(sample_data):
    analyzer = StudentAnalyzer(sample_data)
    student = analyzer.find_student_with_all_90()
    assert student is not None
    assert student[0] in ["Иванов Иван", "Сидоров Сидор"]
    assert all(score == 90 for _, score in student[1])


def test_find_student_with_all_90_not_exists():
    data = {
        "Иванов Иван": [("математика", 80), ("литература", 90)],
        "Петров Петр": [("математика", 85), ("химия", 90)],
    }
    analyzer = StudentAnalyzer(data)
    student = analyzer.find_student_with_all_90()
    assert student is None
