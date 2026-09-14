# object - a bundle of related attributes and methods (data and functionality)
# example: a car object has attributes like color, make, model, and methods like start(), stop(), drive()
# you need a class to create an object, a class is a blueprint for creating objects (designing the layout and structure of the object)
class Car:
    # attributes
    # self is a reference to the current instance of the class, and is used to access variables that belong to the class.
    def __init__(self, make, model, year, color): # __init__ is a special method that is automatically called when a new object is created from a class. It initializes the object's attributes.
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0
    
        # methods
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.color} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't increment the odometer by negative miles!")