Absolutely. Since you're training to become an industry-ready Python full-stack developer, I'll teach these sessions as if you're in a professional bootcamp. Every concept will include:

* Simple explanations
* Real-world analogies
* Industry best practices
* Real project examples
* Hands-on coding
* Mini challenges
* Common interview questions
* Best practices used by companies

---

# SESSION 7 — OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON

---

# What is Object-Oriented Programming?

Imagine you're building an **E-commerce Website**.

Your application has:

* Users
* Products
* Orders
* Payments
* Reviews

Instead of creating hundreds of separate variables, we group related data and behavior together.

Example:

Instead of

```python
user_name = "John"
user_email = "john@gmail.com"
user_password = "123"

def login():
    pass

def logout():
    pass
```

We create a **User object**.

```python
class User:
    ...
```

Everything about the user stays together.

Think of a class as a blueprint.

Think of an object as the real house built from the blueprint.

---

# Real World Example

Blueprint

```
Car
```

Real Cars

```
Toyota
Mercedes
BMW
Tesla
```

All came from one blueprint.

Exactly how Python classes work.

---

# Creating Your First Class

```python
class Student:
    pass
```

This class currently does nothing.

Let's create an object.

```python
student1 = Student()

print(student1)
```

Output

```
<__main__.Student object at 0x...>
```

Python created an object in memory.

---

# Constructor (**init**)

When creating a student, we usually want

* name
* registration number
* course

Python gives us the constructor.

```python
class Student:

    def __init__(self, name, reg_no, course):
        self.name = name
        self.reg_no = reg_no
        self.course = course
```

Create objects

```python
student1 = Student(
    "Alice",
    "CS001",
    "Computer Science"
)

student2 = Student(
    "Brian",
    "CS002",
    "Software Engineering"
)
```

Access attributes

```python
print(student1.name)
print(student2.course)
```

Output

```
Alice
Software Engineering
```

---

# What is self?

Many beginners fear this.

It simply means

> "This current object."

Example

```python
student1.name
```

Python internally becomes

```python
Student.name(student1)
```

So

```python
self.name
```

means

```
This object's name.
```

---

# Methods

Objects also perform actions.

Example

```python
class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")
```

Usage

```python
alice = Student("Alice")

alice.greet()
```

Output

```
Hello, I'm Alice
```

---

# Real Project Example

Hospital System

```python
class Patient:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_in(self):
        print(f"{self.name} has checked in.")
```

Usage

```python
patient = Patient("David", 25)

patient.check_in()
```

---

# Encapsulation

Users should not freely modify sensitive data.

Example

Bad

```python
account.balance = -100000
```

Instead

```python
class BankAccount:

    def __init__(self):
        self.__balance = 0
```

Notice

```python
__balance
```

Double underscore means

Private.

---

Access safely

```python
class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

Usage

```python
account = BankAccount()

account.deposit(500)

print(account.get_balance())
```

Output

```
500
```

---

# Inheritance

Suppose we have

```
Student
Lecturer
Administrator
```

All have

* name
* email
* login()

Instead of repeating code...

Create

```python
class User:
```

Then inherit.

---

Example

```python
class User:

    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} logged in")
```

Student inherits

```python
class Student(User):

    def study(self):
        print("Studying...")
```

Usage

```python
student = Student("Alice")

student.login()
student.study()
```

Output

```
Alice logged in
Studying...
```

---

# Multi-level Inheritance

```
Person

↓

Employee

↓

Manager
```

Example

```python
class Person:
    pass

class Employee(Person):
    pass

class Manager(Employee):
    pass
```

---

# Method Overriding

Parent

```python
class Animal:

    def speak(self):
        print("Some sound")
```

Child

```python
class Dog(Animal):

    def speak(self):
        print("Woof")
```

Usage

```python
dog = Dog()

dog.speak()
```

Output

```
Woof
```

---

# super()

Suppose we inherit but still want the parent's constructor.

```python
class User:

    def __init__(self, name):
        self.name = name
```

Child

```python
class Student(User):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
```

---

# Composition

One of the most important concepts in real software.

Instead of saying

```
A Car IS an Engine
```

We say

```
A Car HAS an Engine
```

---

Example

```python
class Engine:

    def start(self):
        print("Engine started")
```

Car

```python
class Car:

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Driving...")
```

Usage

```python
car = Car()

car.drive()
```

Output

```
Engine started
Driving...
```

---

# Why Composition is Better

Imagine

Hospital System

Patient

Doctor

Appointment

Prescription

A Patient **has** Appointments.

An Appointment **has** a Doctor.

A Doctor **has** Patients.

This is composition.

---

# Composition vs Inheritance

Inheritance

```
Student IS A User
```

Composition

```
Order HAS A Customer
```

Rule

Use inheritance when there is an **"is-a"** relationship.

Use composition when there is a **"has-a"** relationship.

---

# Dataclasses

Normal class

```python
class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
```

Python automatically provides a shorter way.

```python
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
```

Usage

```python
p = Product(1, "Laptop", 65000)

print(p)
```

Output

```
Product(id=1, name='Laptop', price=65000)
```

Benefits

* Less code
* Cleaner
* Automatic constructor
* Automatic representation
* Automatic equality comparison

Widely used in FastAPI and modern Python applications.

---

# Dunder Methods

"Dunder" means **Double Under** (`__method__`).

Examples:

* `__init__`
* `__str__`
* `__repr__`
* `__len__`
* `__eq__`
* `__add__`

---

## **str**()

Without it

```python
print(product)
```

Output

```
<__main__.Product object at ...>
```

Better

```python
class Product:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
```

Output

```
Laptop
```

---

## **len**()

```python
class Playlist:

    def __init__(self):
        self.songs = []

    def __len__(self):
        return len(self.songs)
```

Usage

```python
playlist = Playlist()

print(len(playlist))
```

---

## **eq**()

```python
class Product:

    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id
```

---

# Real Project

## E-Commerce System

```python
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float


class Cart:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total(self):
        return sum(product.price for product in self.products)


cart = Cart()

cart.add_product(Product(1, "Laptop", 65000))
cart.add_product(Product(2, "Mouse", 1500))
cart.add_product(Product(3, "Keyboard", 3000))

print(cart.total())
```

Output

```
69500
```

This demonstrates **composition** (`Cart` has `Product` objects) and `@dataclass`.

---

# Mini Project — University Student Management System

**Requirements**

Create:

* `Person`
* `Student`
* `Lecturer`
* `Course`
* `Department`

Use:

* Inheritance (`Student`, `Lecturer` inherit from `Person`)
* Composition (`Department` has many `Course` objects; `Student` has many `Course` objects)
* `@dataclass` for `Course`
* `__str__` for readable output
* Methods to enroll students, assign lecturers, and list courses

---

# Interview Questions

**1. What is OOP?**

> A programming paradigm that organizes code into objects combining data and behavior.

**2. Difference between Class and Object?**

* Class: Blueprint.
* Object: Instance created from the blueprint.

**3. What is Inheritance?**

> Reusing and extending behavior from a parent class.

**4. What is Composition?**

> Building classes from other classes using a "has-a" relationship.

**5. When should you use Composition instead of Inheritance?**

> Use composition when objects own or contain other objects. It is generally more flexible and reduces tight coupling.

---

# SESSION 8 — CLEAN CODE & ERROR HANDLING

Professional software isn't judged only by whether it works—it should also be readable, maintainable, and resilient.

---

# Single Responsibility Principle (SRP)

A function should do **one thing well**.

❌ Poor design:

```python
def register_user(name, email):
    # Validate input
    # Save to database
    # Send welcome email
    # Write to log
    pass
```

This function has too many responsibilities.

---

## Better Design

```python
def validate_user(name, email):
    if not name:
        raise ValueError("Name is required")


def save_user(user):
    print("Saving user...")


def send_welcome_email(email):
    print(f"Email sent to {email}")


def register_user(name, email):
    validate_user(name, email)
    user = {"name": name, "email": email}
    save_user(user)
    send_welcome_email(email)
```

Each function has one clear responsibility.

---

# DRY (Don't Repeat Yourself)

❌ Before

```python
student_total = student_fee + student_hostel
lecturer_total = lecturer_fee + lecturer_hostel
visitor_total = visitor_fee + visitor_hostel
```

✅ After

```python
def calculate_total(fee, hostel):
    return fee + hostel

student_total = calculate_total(student_fee, student_hostel)
lecturer_total = calculate_total(lecturer_fee, lecturer_hostel)
visitor_total = calculate_total(visitor_fee, visitor_hostel)
```

---

# KISS (Keep It Simple, Stupid)

❌ Overcomplicated

```python
if len(users) > 0:
    return True
else:
    return False
```

✅ Simple

```python
return bool(users)
```

---

# YAGNI (You Aren't Gonna Need It)

Don't build features until they're actually needed.

❌

```python
class Payment:
    def pay_with_bitcoin(self):
        pass

    def pay_with_dogecoin(self):
        pass

    def pay_with_alien_currency(self):
        pass
```

If your application only accepts M-Pesa today, implement M-Pesa first. Add other payment methods when the business requires them.

---

# Error Handling with try/except

```python
try:
    age = int(input("Age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid number.")
```

---

# Multiple Exceptions

```python
try:
    result = 10 / int(input("Number: "))
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

---

# finally

Runs whether an exception occurs or not.

```python
file = None

try:
    file = open("users.txt")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    if file:
        file.close()
```

---

# Custom Exceptions

Create meaningful errors for your domain.

```python
class InsufficientFundsError(Exception):
    """Raised when an account lacks enough balance."""
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                "Insufficient account balance."
            )

        self.balance -= amount
```

Usage

```python
account = BankAccount(1000)

try:
    account.withdraw(2000)
except InsufficientFundsError as error:
    print(error)
```

---

# Logging Instead of print()

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Application started")
logging.warning("Low disk space")
logging.error("Database connection failed")
```

Why logging?

* Different severity levels
* Timestamps
* Easy to write to files
* Essential for debugging production systems

---

# Real Project Example — ATM

```python
import logging

logging.basicConfig(level=logging.INFO)


class InsufficientFundsError(Exception):
    pass


class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance.")

        self.balance -= amount
        logging.info("Withdrawal successful: %s", amount)
        return self.balance


atm = ATM(5000)

try:
    remaining = atm.withdraw(1500)
    print(f"Remaining balance: {remaining}")
except (ValueError, InsufficientFundsError) as error:
    logging.error(error)
```

---

# Before and After Refactor

### Before

```python
def process_order(order):
    if order:
        if order["paid"]:
            if order["items"]:
                total = 0
                for item in order["items"]:
                    total += item["price"]
                print(total)
```

Problems:

* Deep nesting
* Hard to read
* Mixed responsibilities

---

### After

```python
def calculate_total(items):
    return sum(item["price"] for item in items)


def process_order(order):
    if not order:
        raise ValueError("Order is required.")

    if not order["paid"]:
        raise ValueError("Order has not been paid.")

    total = calculate_total(order["items"])
    print(total)
```

This version follows SRP, avoids unnecessary nesting, and is easier to test.

---

# Mini Project — Library Management System

Build a small console application with the following:

* `Book` as a `@dataclass`
* `Library` class that stores books (composition)
* Methods to add, borrow, return, and list books
* `BookNotAvailableError` custom exception
* Logging for borrowing and returning books
* Clean functions that each perform one responsibility
* Meaningful `__str__` methods for readable output

This project combines OOP, composition, dataclasses, custom exceptions, logging, SRP, DRY, KISS, and error handling—very similar to patterns used in production systems built with frameworks such as Django and FastAPI.

---

# Key Takeaways

* A **class** is a blueprint; an **object** is an instance of that blueprint.
* Use **inheritance** for **"is-a"** relationships and **composition** for **"has-a"** relationships.
* `@dataclass` reduces boilerplate for data-centric classes.
* Dunder methods (`__str__`, `__eq__`, `__len__`, etc.) make your classes integrate naturally with Python.
* Follow **SRP**, **DRY**, **KISS**, and **YAGNI** to produce clean, maintainable code.
* Use **custom exceptions** to express business rules clearly.
* Prefer the **logging** module over `print()` in production applications.
* Write small, focused functions that are easy to test and reuse.

These two sessions cover the OOP and clean-code foundations expected in professional Python development and are directly applicable to building real-world applications such as e-commerce systems, hospital management systems, banking platforms, university portals, and REST APIs with Django or FastAPI.
