from models.Human import Human
from models.SubjectMark import SubjectMark


class Student(Human):
    __counter = 1

    def __init__(self, surname: str, firstname: str, lastname: str, grade: int, subjects: dict):
        super().__init__(surname, firstname, lastname)
        self.__grade = grade
        self.__student_number = Student.__counter
        Student.__counter += 1
        self.__diary = []
        for key_number in subjects:
            self.__diary.append(SubjectMark(subjects[key_number]))

    def get_mark(self, mark, teacher):
        for subject_mark in self.__diary:
            if subject_mark.subject is teacher.subject:
                subject_mark.mark = mark
                break

    def diary_average(self):
        average = list(filter(lambda i: i.mark > 0, self.__diary))
        try:
            return sum(i.mark for i in average) / len(average)
        except ZeroDivisionError as e:
            print("No marks")


    def __str__(self):
        return f"{self.__student_number},{super().__str__(), self.diary_average()}"

    @property
    def student_number(self):
        return self.__student_number

    @property
    def grade(self):
        return self.__grade

    @property
    def diary(self):
        return self.__diary
