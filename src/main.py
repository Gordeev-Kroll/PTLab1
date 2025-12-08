# -*- coding: utf-8 -*-
import argparse
import sys

from src.CalcRating import CalcRating
from src.YamlDataReader import YamlDataReader
from src.HighScoreStudentSelector import HighScoreStudentSelector


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p", dest="path", type=str, required=True, help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = YamlDataReader()
    students = reader.read(path)

    selector = HighScoreStudentSelector(students)
    result = selector.get_student()

    # print("Qualified Students:", selector.qualified_students)

    if result:
        print(result)
    else:
        print("Нет таких студентов")


if __name__ == "__main__":
    main()
