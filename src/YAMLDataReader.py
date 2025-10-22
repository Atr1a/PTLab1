import yaml
from src.DataReader import DataReader

class YAMLDataReader(DataReader):
    def read(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return data
