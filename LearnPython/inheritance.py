# Inheritance
# parent class
class UniversityUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def login(self):
        print(f"{self.name} has logged in with email: {self.email}")
    
    def display_info(self):
        print(f"Name: { self.name} Email: {self.email}")
    
# child class
class Student(UniversityUser):
        def __init__(self, name, email, student_id, course):
             # call the constructor of the parent class
             super().__init__(name, email)
             self.student_id = student_id
             self.course = course
        
        def submit_assignment(self):
             print(f"{self.name} has submitted the assignment for course: {self.course}")

# Another Child class
class Lecturer(UniversityUser):
    def __init__(self, name, email, lecturer_id, subject):
        # call the constructor of the parent class
        super().__init__(name, email)
        self.lecturer_id = lecturer_id
        self.subject = subject
    
    def grade_assignment(self):
        print(f"{self.name} has graded the assignment for subject: {self.subject}")
    
    def teach_class(self):
        print(f"{self.name} is teaching the class for subject: {self.subject}")


# create instances of the Student and Lecturer classes
student = Student(
    'Jonathan', 
    'jon@gmail.com', 
    'S123', 
    'Computer Science'
    )

lecturer = Lecturer(
    "Dr. Jane",
    "jane@example.com",
    "STF001",
    "Computer Science"
)

# call methods from the parent and child classes
student.submit_assignment()
student.display_info()
lecturer.display_info()

student.login()
lecturer.login()