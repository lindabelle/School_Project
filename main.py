from models.Teacher import Teacher
from models.Student import Student
from models.Subject import Subject

subjects = [Subject("English"), Subject("Math"), Subject("Biology")]
teachers = [Teacher("Petrov", "Petr", "Petrovich", subjects[0]), Teacher("Ivanov", "Ivan", "Petrovich", subjects[1]),
            Teacher("Sidorov", "Ivan", "Petrovich", subjects[2])]
students = [Student("Petrov2", "Petr2", "Petrovich2",1,subjects), Student("Sidorov2", "Petr2", "Petrovich2",1,subjects)]

teachers[0].set_mark(10, 1, students)
teachers[1].set_mark(4, 1, students)
students[0].get_mark(8, teachers[2])
print(students[0])
