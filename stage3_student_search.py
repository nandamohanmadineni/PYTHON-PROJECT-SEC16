# stage3_student_search.py

students = ["Ram", "Sita", "Krishna"]

search = input("Enter name: ").lower()

for s in students:
    if s.lower() == search:
        print("Found:", s)