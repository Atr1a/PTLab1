# -*- coding: utf-8 -*-
from src.Types import DataType
from typing import Optional, Tuple, List


class StudentAnalyzer:

    def __init__(self, data: DataType):
        self.data: DataType = data

    def find_student_with_all_90(
            self) -> Optional[Tuple[str, List[Tuple[str, int]]]]:

        for student, subjects in self.data.items():
            if all(score == 90 for _, score in subjects):
                return student, subjects
        return None

    def print_student_with_all_90(self) -> None:

        result = self.find_student_with_all_90()
        if result:
            name, subjects = result
            print(f"Student with 90 in all subjects: {name}")
            for subj, score in subjects:
                print(f"  {subj}: {score}")
        else:
            print("No student has 90 in all subjects.")
