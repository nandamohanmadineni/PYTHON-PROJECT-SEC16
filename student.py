# models/student.py  week-6

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.marks = {}

    def add_marks(self, subject, score):
        self.marks[subject] = score

    def display(self):
        print(self.sid, self.name, self.marks)

s = Student("101", "Ram")
s.add_marks("Math", 95)
s.display()