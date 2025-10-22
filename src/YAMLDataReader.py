
# -*- coding: utf-8 -*-
import yaml
from src.DataReader import DataReader
from src.Types import DataType


class YAMLDataReader(DataReader):

    def read(self, path: str) -> DataType:
        """Читает YAML в формате:
        - Имя Фамилия:
            предмет1: оценка1
            предмет2: оценка2
        и возвращает DataType: dict[str, list[tuple[str,int]]]
        """
        with open(path, 'r', encoding='utf-8') as file:
            raw_data = yaml.safe_load(file)

        data: DataType = {}
        for student_dict in raw_data:
            for name, subjects in student_dict.items():
                data[name] = [
                    (subject, score) for subject, score in subjects.items()
                ]
        return data
