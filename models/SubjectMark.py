from models.Subject import Subject


class SubjectMark:
    def __init__(self, subject: Subject):
        self.subject = subject
        self.mark = 0

    def __str__(self):
        return f"{self.subject} - {self.mark}"
