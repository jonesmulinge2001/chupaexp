# Aggregation functions for data processing
# concept where one class contains a reference to another class, 
# but both classes can exist independently of each other. 
# It represents a "has-a" relationship.

# Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def display(self):
        print(f"Employee Name: {self.name}")

# company class
class Company:
    def __init__(self, company_name, employee):
        self.company_name = company_name
        self.employee = employee
    
    def show(self):
        print(f"Company Name: {self.company_name}")
        self.employee.display()

# creating objects independently
employee1 = Employee("John Doe", "Software Engineer")

# creating company object with employee object
company1 = Company("Tech Solutions", employee1)

company1.show()