from models.Human import Human
from models.Subject import Subject
from models.SubjectMark import SubjectMark


class Teacher(Human):

    def __init__(self, surname: str, firstname: str, lastname: str, subject: Subject):
        super().__init__(surname, firstname, lastname)
        self.__subject = subject

    def set_mark(self, mark,student_number, students_list):
        for student in students_list:
            if student_number == student.student_number:
                student.get_mark(mark,self)
                break


    def __str__(self):
        return f"{super().__str__()}, {self.__subject}"

    @property
    def subject(self):
        return self.__subject






