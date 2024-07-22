'''
add student details
update student details
delete student details
view student details
exit
'''

students = {}

# add student
def add_student():
    roll = int(input("Enter the roll number of the student: "))
    name = input("Enter the name of the student: ")
    marks = float(input("Enter the marks of the student: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student details added successfully.")

# update student
def update_student():
    roll = int(input("Enter the roll number of the student: "))
    if roll in students:
        name = input("Enter the name of the student: ")
        marks = float(input("Enter the marks of the student: "))
        students[roll] = {"name": name, "marks": marks}
        print("Student details updated successfully.")
    else:
        print("Student details not found.")

# delete student
def delete_student():
    roll = int(input("Enter the roll number of the student: "))
    if roll in students:
        del students[roll]
        print("Student details deleted successfully.")
    else:
        print("Student details not found.")

# view student
def view_student():
    if students:
        print("Student details:")
        for roll, details in students.items():
            print(f"Roll number: {roll}")
            print(f"Name: {details['name']}")
            print(f"Marks: {details['marks']}")
            print()
    else:
        print("No student details found.")

# main
while True:
    print("1. Add student details")
    print("2. Update student details")
    print("3. Delete student details")
    print("4. View student details")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        update_student()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        view_student()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
    print()

print("Thank you for using our student grade management system!")

