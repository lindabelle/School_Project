from models.Human import Human
from models.Subject import Subject


class Teacher(Human):

    def __init__(self, surname: str, firstname: str, lastname: str, subject: Subject, mark: int, student_number: int):
        super().__init__(surname, firstname, lastname)
        self.__subject = subject

    def __str__(self):
        return f"{super().__str__()}, {self.__subject}"

    @property
    def subject(self):
        return self.__subject
