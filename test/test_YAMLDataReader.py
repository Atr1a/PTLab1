import pytest
from src.YAMLDataReader import YAMLDataReader


@pytest.fixture
def sample_yaml(tmp_path):
    content = """
    students:
      - name: "Atria"
        rating: 95
      - name: "Sky"
        rating: 87
    """
    file_path = tmp_path / "data.yaml"
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)


def test_read_data_returns_dict(sample_yaml):
    reader = YAMLDataReader()
    data = reader.read(sample_yaml)
    assert isinstance(data, dict)
    assert "students" in data


def test_read_data_parses_values(sample_yaml):
    reader = YAMLDataReader()
    data = reader.read(sample_yaml)
    assert data["students"][0]["name"] == "Atria"
    assert data["students"][1]["rating"] == 87
