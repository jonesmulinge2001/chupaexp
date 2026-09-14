# demonstrating inheritance
# base class / parent class
class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def eat(self):
        print("{} is eating".format(self.name))
        print(f'{self.name} is eating')

    def sleep(self):
        print("{} is sleeping".format(self.name))
        print(f"{self.name} is sleeping")

# derived class / child class
class Dog(Animal): # syntax for inheritance is class DerivedClass(BaseClass):
    # derived class Dog inherits from base class Animal
    def __init__(self, name, color, age, sound):
        super().__init__(name, color, age)# super() constructor is used to call the __init__ method of the base class
        self.sound = sound

    def makeSound(self):
        print("{} says {}".format(self.name, self.sound)) 
        print(f"{self.name} says {self.sound}")

    def eat(self):
        print("{} is eating dog food".format(self.name))
        print(f"{self.name} is eating dog food")

# derived class
class Cat(Animal):
    def __init__(self, name, color, age, sound):
        super().__init__(name, color, age)
        self.sound = sound

    def makeSound(self):
        print("{} says {}".format(self.name, self.sound))
        print(f"{self.name} says {self.sound}")

    def sleep(self):
        print("{} is sleeping on the couch".format(self.name))
        print(f"{self.name} is sleeping on the couch")

# create instances of the classes
dog1 = Dog("Fido", "brown", 3)
dog1.makeSound() # output: Fido says Woof
dog1.eat() # output: Fido is eating dog food
dog1.sleep() # output: Fido is sleeping

# cat = Cat("Whiskers", "black", 2)
# cat.makeSound() # output: Whiskers says Meow
# cat.eat() # output: Whiskers is eating
# cat.sleep() # output: Whiskers is sleeping on the couch