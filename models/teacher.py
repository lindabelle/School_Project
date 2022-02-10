class Teacher(Human):
    list_of_marks = []

    def __init__(self, subject: str, mark: int, student_number: int):
        self.__subject = subject
        self._mark = mark
        self.__student_number = student_number

    def __str__(self):
        return f"{self.__subject},{self._mark},{self.__student_number}"

    @property
    def subject(self):
        return self.__subject

    @property
    def mark(self):
        return self._mark

    @property
    def student_number(self):
        return self.__student_number

    def add_mark(self, new_mark):
        Teacher.list_of_marks.append(new_mark)

    def delete_mark(self):
        if len(Teacher.list_of_marks) < 1:
            raise ValueError
        Teacher.list_of_marks.remove[]  # тут pop не подходит, тк нужно удалить отметку не последнюю,а ошибочную
