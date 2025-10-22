import pytest
from src.YAMLDataReader import YAMLDataReader


@pytest.fixture
def sample_yaml(tmp_path):
    content = """
- Иванов Иван Иванович:
    математика: 67
    литература: 100
    программирование: 91
- Петров Петр Петрович:
    математика: 78
    химия: 87
    социология: 61
    """
    file_path = tmp_path / "data.yaml"
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)


def test_read_data_returns_dict(sample_yaml):
    reader = YAMLDataReader()
    data = reader.read(sample_yaml)
    assert isinstance(data, dict)
    assert "Иванов Иван Иванович" in data
    assert "Петров Петр Петрович" in data


def test_read_student_scores(sample_yaml):
    reader = YAMLDataReader()
    data = reader.read(sample_yaml)
    ivanov_scores = data["Иванов Иван Иванович"]
    assert ("математика", 67) in ivanov_scores
    assert ("литература", 100) in ivanov_scores
    assert ("программирование", 91) in ivanov_scores

    petrov_scores = data["Петров Петр Петрович"]
    assert ("математика", 78) in petrov_scores
    assert ("химия", 87) in petrov_scores
    assert ("социология", 61) in petrov_scores
