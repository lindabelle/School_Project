from models.Teacher import Teacher
from models.Student import Student
from models.Subject import Subject
from models.School import School
import src


# subjects = [Subject("English"), Subject("Math"), Subject("Biology")]
# teachers = [Teacher("Petrov", "Petr", "Petrovich", subjects[0]), Teacher("Ivanov", "Ivan", "Petrovich", subjects[1]),
#             Teacher("Sidorov", "Ivan", "Petrovich", subjects[2])]
# students = [Student("Petrov2", "Petr2", "Petrovich2",1,subjects), Student("Sidorov2", "Petr2", "Petrovich2",1,subjects)]
#
# teachers[0].set_mark(10, 1, students)
# teachers[1].set_mark(4, 1, students)
# students[0].get_mark(8, teachers[2])
# print(students[0])

def input_name():
    name = input("firstname: ")
    surname = input("surname: ")
    lastname = input("lastname: ")
    return name, surname, lastname


def choice_subject(school: School):
    for key in school.subjects:
        print(school.subjects[key])
    try:
        choice = int(input("Number subject: "))
        return school.subjects[choice]
    except Exception as e:
        print(e)


def work_admin(school: School):
    while True:
        choice = input(src.main_amin_choice)
        if choice == '1':
            name, surname, lastname = input_name()
            school.add_teacher(surname, name, lastname, choice_subject(school))
        elif choice == '2':
            for key in school.teachers:
                print(school.teachers[key])
            try:
                choice = int(input("Number teacher: "))
                school.delete_teacher(choice)
            except Exception as e:
                print(e)
        elif choice == '3':
            name, surname, lastname = input_name()
            school.add_student(surname, name, lastname, 1)
        elif choice == '4':
            for key in school.students:
                print(school.students[key])
                try:
                    choice = int(input("Number student: "))
                    school.delete_student(choice)
                except Exception as e:
                    print(e)
        else:
            break


def work_student(school: School):
    while True:
        try:
            number = int(input("Student number: "))
            student = school.get_student(number)
            choice = input("1. Get information. 2. Get marks")
            if choice == "1":
                print(student)
            elif choice == "2":
                for i in student.diary:
                    print(i)
            else:
                break
        except Exception as e:
            print(e)


def work_teacher(school: School):
    while True:
        try:
            number = int(input("Teacher number: "))
            teacher = school.teachers[number]
            choice = input("1. Get information. 2. Set mark")
            if choice == "1":
                print(teacher)
            elif choice == "2":
                for key in school.students:
                    print(school.students[key])
                number = int(input("Student number"))
                mark = int(input("Mark: "))
                teacher.set_mark(mark, number, school.students)
            else:
                break
        except Exception as e:
            print(e)


def main():
    school = School(src.subjects_name, src.password)
    while True:
        choice = input('Choose your option: 1 - administrator, 2- student, 3 - teacher')
        if choice == '1':
            try:
                password = input('Insert your password')
                if school.check_password(password):
                    work_admin(school)
            except Exception as e:
                print(e)

        elif choice == "2":
            work_student(school)

        elif choice == "3":
            work_teacher(school)

        else:
            break


main()
