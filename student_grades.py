# Student Grade Management System

def add_students():
    students = []
    num = int(input("Enter number of students: "))
    
    for _ in range(num):
        name = input("Enter student's name: ")
        marks = []
        for i in range(1, 4):
            mark = float(input(f"Enter marks for Subject {i}: "))
            marks.append(mark)
        avg = sum(marks) / 3
        students.append({'Name': name, 'Marks': marks, 'Average': avg})
    
    return students

def display_students(students):
    print("\n--- Student Details ---")
    for student in students:
        print(f"Name: {student['Name']}")
        print(f"Marks: {student['Marks']}")
        print(f"Average: {student['Average']:.2f}")
        print("-----------------------")

students = add_students()
display_students(students)
