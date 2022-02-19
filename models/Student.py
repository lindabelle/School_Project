from models.Human import Human
from models.SubjectMark import SubjectMark


class Student(Human):
    __counter = 1

    def __init__(self, surname: str, firstname: str, lastname: str, grade: int, subjects: list):
        super().__init__(surname, firstname, lastname)
        self.__grade = grade
        self.__student_number = Student.__counter
        Student.__counter += 1
        self.__diary = []
        for subject in subjects:
            self.__diary.append(SubjectMark(subject))

    def get_mark(self, mark, teacher):
        for subject_mark in self.__diary:
            if subject_mark.subject is teacher.subject:
                subject_mark.mark = mark
                break


    def diary_average(self):
        average = list(filter(lambda i: i.mark > 0, self.__diary))
        return sum(i.mark for i in average) / len(average)

    def __str__(self):
        return f"{self.__student_number},{super().__str__(), self.diary_average()}"

    @property
    def student_number(self):
        return self.__student_number

    @property
    def grade(self):
        return self.__grade

