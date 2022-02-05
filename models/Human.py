class Human:
    def __init__(self, surname: str, firstname: str, lastname: str):
        self._surname = surname
        self._firstname = firstname
        self._lastname = lastname

    def __str__(self):
        return f"{self._surname}, {self._firstname},{self._lastname}"

    @property
    def surname(self):
        return self._surname

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname
