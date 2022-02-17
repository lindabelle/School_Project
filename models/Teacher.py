from models.Human import Human
from models.SubjectMark import SubjectMark


class Teacher(Human):

    def __init__(self, surname: str, firstname: str, lastname: str, subject: Subject, mark: int):
        super().__init__(surname, firstname, lastname)
        self.__subject = subject
        self.__mark = mark
        self.__journal = []
        for mark in subject:
            if mark == 0:
                raise ValueError
            else:
                self.__journal.append(mark)

    def __str__(self):
        return f"{super().__str__()}, {self.__subject}"

    @property
    def subject(self):
        return self.__subject

    @property
    def mark(self):
        return self.__mark




