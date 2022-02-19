from models.Subject import Subject
from models.Teacher import Teacher
from models.Student import Student

class School:
    def __init__(self, subjects_name:list, password:str):
        self.__subjects = {}
        for name in subjects_name:
            tmp_subject = Subject(name)
            self.__subjects.update({tmp_subject.number: tmp_subject})
        self.__teachers = {}
        self.__students = {}
        self.__password = password

    def check_password(self,password):
        if password == self.__password:
            return True
        return False

    def add_teacher(self,surname: str, firstname: str, lastname: str, subject: Subject):
        new_teacher = Teacher(surname,firstname,lastname,subject)
        self.__teachers.update({new_teacher.teacher_number:new_teacher})

    def delete_teacher(self,teacher_number):
        self.__teachers.pop(teacher_number)

    def get_teacher(self,teacher_number):
        return self.__teachers[teacher_number]








a = Subject('russian')
b = Subject('eng')
name = 'math'
c = Subject(name)

