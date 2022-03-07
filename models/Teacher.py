from models.Human import Human
from models.Subject import Subject



class Teacher(Human):
    __counter = 1

    def __init__(self, surname: str, firstname: str, lastname: str, subject: Subject):
        super().__init__(surname, firstname, lastname)
        self.__subject = subject
        self.__teacher_number = Teacher.__counter
        Teacher.__counter += 1

    def set_mark(self, mark, student_number, students):
        students[student_number].get_mark(mark, self)

    def __str__(self):
        return f"{self.__teacher_number}, {super().__str__()}, {self.__subject}"

    @property
    def subject(self):
        return self.__subject

    @property
    def teacher_number(self):
        return self.__teacher_number
