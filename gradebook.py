# Initialize an empty dictionary of student grades
student_grades = {}

# Function to add a student and grade
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student '{name}' added with grade {grade}.")

# Function to remove a student
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student '{name}' removed.")
    else:
        print(f"Student '{name}' not found.")

# Function to display all students and their grades
def display_students():
    print("Gradebook:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

# Function to update a student's grade
def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student '{name}' updated with grade {grade}.")
    else:
        print(f"Student {name} not found.") 


# Add some students
add_student("Tom", "B")
add_student("Amy", "A")
add_student("Elise", "A")
add_student("Joe", "C")
add_student("Dan", "A")

# Display students and their grades
display_students()

# Update a student's grade
update_grade("Amy", "F")
update_grade("Sarah", "A")

# Remove a student
remove_student('Tom')
remove_student('Bob')

# Display students and their grades again
display_students()