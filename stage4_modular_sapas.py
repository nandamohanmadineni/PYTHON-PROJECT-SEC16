# stage4_modular_sapas.py
def add_student(name, marks):
    return {"name": name, "marks": marks}

def display(student):
    print(student["name"], student["marks"])

s1 = add_student("Ram", 90)
display(s1)