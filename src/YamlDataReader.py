# -*- coding: utf-8 -*-
import yaml
from src.DataReader import DataReader
from src.Types import DataType


class YamlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as f:
            raw_data = yaml.safe_load(f)

        if raw_data is None:
            raw_data = []

        students: DataType = {}
        for item in raw_data:
            if not isinstance(item, dict):
                continue
            for student, subjects in item.items():
                students[student] = [
                    (subj, int(score)) for subj, score in subjects.items()
                ]
        return students
