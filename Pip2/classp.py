# introducing classes in python

class Dog: # syntax for creating a class
    def __init__(self, name, age): # initialization method / constructor
        # self references the current object
        self.name = name
        self.age = age

    # method 1
    def bark(self):
        print("woof!")

    # method 2
    def get_name(self):
        print(f"{self.name}")
        return self.name
        

    # method 3
    def get_age(self):
        print(f"{self.age}")
        return self.age

    # method 4
    def set_age(self, age):
        self.age = age

# creating an object of the class Dog
d = Dog("Tim", 34)
# accessing the methods of the class Dog
d.bark() # calling the method bark()
print(d.get_name())
print(d.get_age())
# d.set_age(23)
# print(d.get_age())