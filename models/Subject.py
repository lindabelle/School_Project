class Subject:
    number_counter = 1

    def __init__(self, name: str):
        self.__number = Subject.number_counter
        Subject.number_counter += 1
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return f"{self.__number}: {self.__name}"
