# stage2_student_menu.py
students = []

while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter Name: ")
        students.append(name)

    elif choice == '2':
        print("Students:", students)

    elif choice == '3':
        break