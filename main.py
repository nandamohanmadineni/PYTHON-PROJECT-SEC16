#week-9
class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.marks = {}

    def add_marks(self, subject, score):
        self.marks[subject] = score

    def display(self):
        return {
            "ID": self.sid,
            "Name": self.name,
            "Marks": self.marks
        }