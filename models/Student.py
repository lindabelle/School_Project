from models.Human import Human
from models.Subject import Subject


class Student(Human):
    counter = 1

    def __init__(self, surname: str, firstname: str, lastname: str, grade: int):
        super().__init__(surname, firstname, lastname)
        self.__grade = grade
        self.__student_number = Student.counter
        Student.counter += 1

    def __str__(self):
        return f"{self.__student_number},{super().__str__()}"

    @property
    def student_number(self):
        return self.__student_number

    @property
    def grade(self):
        return self.__grade
