# ==============================
# SAPAS - FULL PROJECT
# ==============================

import json
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# MODEL
# ==============================

class Student:
    def __init__(self, sid, name, student_class, gender):
        self.sid = sid
        self.name = name
        self.student_class = student_class
        self.gender = gender
        self.marks = {}
        self.attendance = {"present": 0, "total": 0}
        self.logs = []

    def add_marks(self, subject, score):
        if 0 <= score <= 100:
            self.marks[subject] = score
        else:
            print("Invalid marks")

    def add_attendance(self, present, total):
        self.attendance["present"] = present
        self.attendance["total"] = total

    def add_log(self, remark):
        self.logs.append(remark)

    def attendance_percentage(self):
        if self.attendance["total"] == 0:
            return 0
        return (self.attendance["present"] / self.attendance["total"]) * 100

    def display(self):
        print("\n--- Student ---")
        print(self.sid, self.name, self.student_class, self.gender)
        print("Marks:", self.marks)
        print("Attendance %:", self.attendance_percentage())
        print("Logs:", self.logs)


# ==============================
# STORAGE
# ==============================

def save_json(students):
    data = []
    for s in students:
        data.append(s.__dict__)
    with open("students.json", "w") as f:
        json.dump(data, f)

def load_json():
    students = []
    try:
        with open("students.json", "r") as f:
            data = json.load(f)
            for d in data:
                s = Student(d["sid"], d["name"], d["student_class"], d["gender"])
                s.marks = d["marks"]
                s.attendance = d["attendance"]
                s.logs = d["logs"]
                students.append(s)
    except:
        pass
    return students


# ==============================
# ANALYTICS
# ==============================

def class_average(students):
    scores = []
    for s in students:
        scores.extend(list(s.marks.values()))
    if scores:
        print("Class Average:", np.mean(scores))

def subject_average(students):
    df = pd.DataFrame([s.marks for s in students])
    print("\nSubject Average:\n", df.mean())

def topper(students):
    max_score = 0
    top_student = None
    for s in students:
        total = sum(s.marks.values())
        if total > max_score:
            max_score = total
            top_student = s
    if top_student:
        print("Topper:", top_student.name, max_score)


# ==============================
# VISUALIZATION
# ==============================

def bar_chart(student):
    subjects = list(student.marks.keys())
    marks = list(student.marks.values())
    plt.bar(subjects, marks)
    plt.title("Subject Scores")
    plt.show()

def pie_chart(student):
    labels = ["Present", "Absent"]
    present = student.attendance["present"]
    total = student.attendance["total"]
    sizes = [present, total - present]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Attendance")
    plt.show()

def line_chart(student):
    marks = list(student.marks.values())
    plt.plot(marks)
    plt.title("Performance Trend")
    plt.show()


# ==============================
# TEXT ANALYTICS
# ==============================

def analyze_logs(student):
    positive_words = ["good", "excellent", "well"]
    negative_words = ["bad", "poor", "low"]

    text = " ".join(student.logs).lower().split()

    pos = sum(1 for w in text if w in positive_words)
    neg = sum(1 for w in text if w in negative_words)

    print("Positive words:", pos)
    print("Negative words:", neg)


# ==============================
# MENU SYSTEM
# ==============================

students = load_json()

while True:
    print("\n==== SAPAS MENU ====")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. Add Attendance")
    print("4. Add Remark")
    print("5. View Students")
    print("6. Analytics")
    print("7. Visualize")
    print("8. Save & Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("ID: ")
        name = input("Name: ")
        cls = input("Class: ")
        gender = input("Gender: ")
        students.append(Student(sid, name, cls, gender))

    elif choice == "2":
        sid = input("Enter ID: ")
        for s in students:
            if s.sid == sid:
                sub = input("Subject: ")
                marks = float(input("Marks: "))
                s.add_marks(sub, marks)

    elif choice == "3":
        sid = input("Enter ID: ")
        for s in students:
            if s.sid == sid:
                p = int(input("Present days: "))
                t = int(input("Total days: "))
                s.add_attendance(p, t)

    elif choice == "4":
        sid = input("Enter ID: ")
        for s in students:
            if s.sid == sid:
                remark = input("Enter remark: ")
                s.add_log(remark)

    elif choice == "5":
        for s in students:
            s.display()

    elif choice == "6":
        class_average(students)
        subject_average(students)
        topper(students)

    elif choice == "7":
        sid = input("Enter ID: ")
        for s in students:
            if s.sid == sid:
                bar_chart(s)
                pie_chart(s)
                line_chart(s)
                analyze_logs(s)

    elif choice == "8":
        save_json(students)
        print("Data Saved!")
        break