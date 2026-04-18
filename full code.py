# ==============================
# SAPAS - FULL PROJECT
# ==============================

import json
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
        self.marks = {}   # dynamic subjects
        self.attendance = {"present": 0, "total": 0}
        self.logs = []

    def add_marks(self, subject, score):
        if len(self.marks) >= 3 and subject not in self.marks:
            print("Only 3 subjects allowed!")
            return

        if 0 <= score <= 100:
            self.marks[subject] = score
        else:
            print("Invalid marks!")

    def add_attendance(self, present, total):
        if present <= total:
            self.attendance["present"] = present
            self.attendance["total"] = total
        else:
            print("Invalid attendance")

    def add_log(self, remark):
        self.logs.append(remark)

    def attendance_percentage(self):
        if self.attendance["total"] == 0:
            return 0
        return (self.attendance["present"] / self.attendance["total"]) * 100

    def total_marks(self):
        return sum(self.marks.values())

    def display(self):
        print("\n--- Student ---")
        print("ID:", self.sid)
        print("Name:", self.name)
        print("Class:", self.student_class)
        print("Gender:", self.gender)
        print("Marks:", self.marks)
        print("Total:", self.total_marks())
        print("Attendance %:", round(self.attendance_percentage(), 2))
        print("Logs:", self.logs)


# ==============================
# STORAGE
# ==============================

def save_json(students):
    data = [s.__dict__ for s in students]
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
        print("Class Average:", round(np.mean(scores), 2))
    else:
        print("No data available")


def subject_average(students):
    df = pd.DataFrame([s.marks for s in students])
    print("\nSubject Average:\n", df.mean().round(2))


def topper(students):
    max_score = -1
    top_student = None
    for s in students:
        total = s.total_marks()
        if total > max_score:
            max_score = total
            top_student = s
    if top_student:
        print("Topper:", top_student.name, "with", max_score, "marks")


# ==============================
# VISUALIZATION
# ==============================

def bar_chart(student):
    subjects = list(student.marks.keys())
    marks = list(student.marks.values())
    plt.bar(subjects, marks)
    plt.title(f"{student.name} - Subject Scores")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()


def pie_chart(student):
    labels = ["Present", "Absent"]
    present = student.attendance["present"]
    total = student.attendance["total"]
    sizes = [present, total - present]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title(f"{student.name} - Attendance")
    plt.show()


def line_chart(student):
    marks = list(student.marks.values())
    plt.plot(marks, marker='o')
    plt.title(f"{student.name} - Performance Trend")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
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
    print("2. Add Marks (Max 3 Subjects)")
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
                while True:
                    print(f"Current subjects: {list(s.marks.keys())}")
                    subject = input("Enter subject name (or 'done' to stop): ")
                    if subject.lower() == "done":
                        break
                    marks = float(input("Enter marks: "))
                    s.add_marks(subject, marks)

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
        print("Data Saved Successfully!")
        break

    else:
        print("Invalid choice! Try again.")
