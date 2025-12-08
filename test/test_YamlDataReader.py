# -*- coding: utf-8 -*-
import pytest
import yaml
from src.YamlDataReader import YamlDataReader
from src.Types import DataType


class TestYamlDataReader:
    @pytest.fixture()
    def yaml_content_and_expected(self) -> tuple[list[dict], DataType]:
        raw_yaml_list = [
            {
                "Иванов Константин Дмитриевич": {
                    "математика": 91,
                    "химия": 100
                }
            },
            {
                "Петров Петр Семенович": {
                    "русский язык": 87,
                    "литература": 78
                }
            }
        ]

        expected: DataType = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91),
                ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87),
                ("литература", 78)
            ]
        }

        return raw_yaml_list, expected

    @pytest.fixture()
    def filepath_and_data(
        self, yaml_content_and_expected: tuple[list[dict], DataType], tmp_path
    ) -> tuple[str, DataType]:
        file_path = tmp_path / "data.yaml"

        with open(file_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(yaml_content_and_expected[0],
                           f, allow_unicode=True, sort_keys=False)

        return str(file_path), yaml_content_and_expected[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        result = YamlDataReader().read(filepath_and_data[0])
        assert result == filepath_and_data[1]

    def test_read_empty_file(self, tmp_path):
        file_path = tmp_path / "empty.yaml"
        file_path.write_text("", encoding="utf-8")
        result = YamlDataReader().read(str(file_path))
        assert result == {}

    def test_read_invalid_yaml(self, tmp_path):
        file_path = tmp_path / "invalid.yaml"
        file_path.write_text("invalid: [yaml", encoding="utf-8")
        with pytest.raises(yaml.YAMLError):
            YamlDataReader().read(str(file_path))
