# Real-World Project: Grade Calculator
print("Grade Calculator")

students = int(input("Enter the number of students to calculate their grade: "))
for i in range(students):
    print("\nStudent", i + 1)
    name = input("Enter the name of the student: ")
    score = int(input("Enter their score (0-100): "))

    if score > 70:
        grade = "A"
    elif score > 60:
        grade = "B"
    elif score > 50:
        grade = "C"
    else:
        grade = "F"
    

    if score == 0:
        continue

    if score < 30:
        break
    
    print(f"{name}: {score}: {grade}")
