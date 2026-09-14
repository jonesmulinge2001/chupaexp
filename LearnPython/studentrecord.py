import csv
import json

# a list to store students
students = []

# function to add a student to the list
def add_student():
    print("\nAdd a new student")
    student_id = input("Enter student ID: ")

    # check if student ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists. Please try again.")
            return

    name  = input("Enter student name: ")
    age   = input("Enter student age: ")
    marks = input("Enter student marks: ")
    course = input("Enter student course: ")

    # create a student dictionary and add it to the list
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks,
        "course": course
    }

    # append the student to the list
    students.append(student)
    print("Student added successfully!")

    # view the list of students
def view_students():
    print("\n------Student Records-----")
    if len(students) == 0:
        print("No student records found.")
        return
    
    for student in students:
        print("----------------")
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Marks: {student['marks']}")
        print(f"Course: {student['course']}")

# search for a student by ID
def search_student():
    print("\nSearch for a student")
    student_id = input("Enter student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("----------------")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Marks: {student['marks']}")
            print(f"Course: {student['course']}")
            return

    print("Student not found.")

# update a student record
def update_student():
    print("\nUpdate a student record")
    student_id = input("Enter student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            print(f"Current Name: {student['name']}")
            new_name = input("Enter new name (leave blank to keep current): ")
            if new_name:
                student["name"] = new_name

            print(f"Current Age: {student['age']}")
            new_age = input("Enter new age (leave blank to keep current): ")
            if new_age:
                student["age"] = new_age

            print(f"Current Marks: {student['marks']}")
            new_marks = input("Enter new marks (leave blank to keep current): ")
            if new_marks:
                student["marks"] = new_marks

            print(f"Current Course: {student['course']}")
            new_course = input("Enter new course (leave blank to keep current): ")
            if new_course:
                student["course"] = new_course

            print("Student record updated successfully!")
            return

    print("Student not found.")


# delete a student record
def delete_student():
    print("\nDelete a student record")
    student_id = input("Enter student ID to delete: ")

    for i, student in enumerate(students):
        if student["id"] == student_id:
            del students[i]
            print("Student record deleted successfully!")
            return

    print("Student not found.")

# save to a CSV file
def save_to_csv():
    with open("students.csv", "w", newline="") as csvfile:
        fieldnames = [
            "id", 
            "name", 
            "age", 
            "marks", 
            "course"
            ]
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for student in students:
            writer.writerow(student)
    print("Student records saved to students.csv successfully!")


# load from a CSV file
def load_from_csv():
    try:
        with open("students.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row["age"] = int(row["age"])  # convert age to integer
                row["marks"] = float(row["marks"])
                students.append(row)
        print("Student records loaded from students.csv successfully!")
    except FileNotFoundError:
        print("No CSV file found. Starting with an empty student list.")


# save to a JSON file
def save_to_json():
    with open("students.json", "w") as jsonfile:
        json.dump(students, jsonfile, indent=4)
    print("Student records saved to students.json successfully!")

# load from a JSON file
def load_from_json():
    try:
        with open("students.json", "r") as jsonfile:
            loaded_students = json.load(jsonfile)
            students.clear()  # clear the current list before loading
            students.extend(loaded_students)  # add the loaded students to the list
        print("Student records loaded from students.json successfully!")
    except FileNotFoundError:
        print("No JSON file found. Starting with an empty student list.")

# main menu
def main():
    while True:
        print("\n------Student Record Management System-----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save to CSV")
        print("7. Load from CSV")
        print("8. Save to JSON")
        print("9. Load from JSON")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            save_to_csv()
        elif choice == "7":
            load_from_csv()
        elif choice == "8":
            save_to_json()
        elif choice == "9":
            load_from_json()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# start the program
main()                
    