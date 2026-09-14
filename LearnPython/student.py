# class variable = shared among all instances of the class
# defined outside of any instance methods / constructors, but inside the class definition
# allow you to define attributes that are shared among all instances of a class, rather than being unique to each instance. This can be useful for defining constants or default values that apply to all objects of a class.

class Student:
    # define a class variable for the school name
    school_name = "ABC High School" 
    number_of_students = 0   

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.attendance = 0
        Student.number_of_students += 1


    def attend_class(self):
        self.attendance += 1
        print(f"{self.name} has attended class. Total attendance: {self.attendance}")
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, School: {Student.school_name}, Attendance: {self.attendance}")
    
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s grade has been updated to {self.grade}")

# create instances of the Student class
student_1 = Student("Alice", 15, "10th")
student_2 = Student("Bob", 16, "11th")
print(student_1.school_name) # Output: ABC High School
print(student_2.school_name) # Output: ABC High School

print(student_1.attend_class()) # Output: Alice has attended class. Total attendance: 1
print(student_2.display_info()) # Output: Name: Bob, Age: 16, Grade: 11th, School: ABC High School, Attendance: 0

print(f'My class has {Student.number_of_students} students') # Output: 2