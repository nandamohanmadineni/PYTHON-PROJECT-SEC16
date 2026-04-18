# models/record.py week-7

class Record:
    def __init__(self, rid):
        self.rid = rid

class Student(Record):
    def __init__(self, rid, name):
        super().__init__(rid)
        self.name = name

s = Student("101", "Ram")
print(s.rid, s.name)