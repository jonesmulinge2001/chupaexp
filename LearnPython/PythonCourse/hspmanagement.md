# ==========================================
#       HOSPITAL APPOINTMENT SYSTEM
# ==========================================

# List containing patient appointment dictionaries
appointments = [
    {
        "patient": "John Mwangi",
        "age": 25,
        "doctor": "Dr. Kamau",
        "department": "General Medicine",
        "date": "25/08/2026",
        "time": "10:00 AM",
        "status": "Confirmed"
    },
    {
        "patient": "Mary Wanjiku",
        "age": 32,
        "doctor": "Dr. Achieng",
        "department": "Pediatrics",
        "date": "26/08/2026",
        "time": "11:00 AM",
        "status": "Confirmed"
    }
]


# ==========================================
# FUNCTION 1: Display all appointments
# ==========================================

def show_appointments():

    print("\n========== ALL APPOINTMENTS ==========")

    if len(appointments) == 0:
        print("There are no appointments.")
        return

    for appointment in appointments:

        print("\nPatient:", appointment["patient"])
        print("Age:", appointment["age"])
        print("Doctor:", appointment["doctor"])
        print("Department:", appointment["department"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print("Status:", appointment["status"])


# ==========================================
# FUNCTION 2: Book an appointment
# ==========================================

def book_appointment():

    print("\n========== BOOK APPOINTMENT ==========")

    patient = input("Enter patient name: ")

    age = int(input("Enter patient age: "))

    print("\nDepartments:")
    print("1. General Medicine")
    print("2. Pediatrics")
    print("3. Cardiology")
    print("4. Dental")

    department_choice = input("Choose department: ")

    if department_choice == "1":
        department = "General Medicine"
        doctor = "Dr. Kamau"

    elif department_choice == "2":
        department = "Pediatrics"
        doctor = "Dr. Achieng"

    elif department_choice == "3":
        department = "Cardiology"
        doctor = "Dr. Otieno"

    elif department_choice == "4":
        department = "Dental"
        doctor = "Dr. Hassan"

    else:
        print("Invalid department.")
        return

    date = input("Enter appointment date (DD/MM/YYYY): ")

    time = input("Enter appointment time: ")

    # Create a new appointment
    new_appointment = {
        "patient": patient,
        "age": age,
        "doctor": doctor,
        "department": department,
        "date": date,
        "time": time,
        "status": "Confirmed"
    }

    # Add appointment to the list
    appointments.append(new_appointment)

    print("\nAppointment booked successfully!")
    print("Patient:", patient)
    print("Doctor:", doctor)
    print("Date:", date)
    print("Time:", time)


# ==========================================
# FUNCTION 3: Search appointment
# ==========================================

def search_appointment():

    print("\n========== SEARCH APPOINTMENT ==========")

    name = input("Enter patient name: ").lower()

    found = False

    for appointment in appointments:

        if name in appointment["patient"].lower():

            print("\nAppointment Found!")
            print("------------------")

            print("Patient:", appointment["patient"])
            print("Doctor:", appointment["doctor"])
            print("Department:", appointment["department"])
            print("Date:", appointment["date"])
            print("Time:", appointment["time"])
            print("Status:", appointment["status"])

            found = True

    if found == False:
        print("\nNo appointment found.")


# ==========================================
# FUNCTION 4: Cancel appointment
# ==========================================

def cancel_appointment():

    print("\n========== CANCEL APPOINTMENT ==========")

    name = input("Enter patient name: ").lower()

    found = False

    for appointment in appointments:

        if name == appointment["patient"].lower():

            appointment["status"] = "Cancelled"

            print("\nAppointment cancelled successfully.")

            found = True
            break

    if found == False:
        print("\nAppointment not found.")


# ==========================================
# FUNCTION 5: Show today's appointments
# ==========================================

def show_department_appointments():

    print("\n========== SEARCH BY DEPARTMENT ==========")

    department = input("Enter department: ").lower()

    found = False

    for appointment in appointments:

        if appointment["department"].lower() == department:

            print("\nPatient:", appointment["patient"])
            print("Doctor:", appointment["doctor"])
            print("Date:", appointment["date"])
            print("Time:", appointment["time"])
            print("Status:", appointment["status"])

            found = True

    if found == False:
        print("\nNo appointments found for this department.")


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    print("\n")
    print("==========================================")
    print("       HOSPITAL APPOINTMENT SYSTEM")
    print("==========================================")

    print("1. View all appointments")
    print("2. Book an appointment")
    print("3. Search appointment")
    print("4. Cancel appointment")
    print("5. Search by department")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        show_appointments()

    elif choice == "2":

        book_appointment()

    elif choice == "3":

        search_appointment()

    elif choice == "4":

        cancel_appointment()

    elif choice == "5":

        show_department_appointments()

    elif choice == "6":

        print("\nThank you for using the Hospital Appointment System.")
        break

    else:

        print("\nInvalid choice. Please select 1-6.")

















        Let's build it at the **same beginner-to-intermediate level**, but use it to introduce a few new concepts: **nested dictionaries, appointment status, search, validation, functions, and menu-driven programs**.

## 🏥 Hospital Appointment System

```python
# ==========================================
#       HOSPITAL APPOINTMENT SYSTEM
# ==========================================

# List containing patient appointment dictionaries
appointments = [
    {
        "patient": "John Mwangi",
        "age": 25,
        "doctor": "Dr. Kamau",
        "department": "General Medicine",
        "date": "25/08/2026",
        "time": "10:00 AM",
        "status": "Confirmed"
    },
    {
        "patient": "Mary Wanjiku",
        "age": 32,
        "doctor": "Dr. Achieng",
        "department": "Pediatrics",
        "date": "26/08/2026",
        "time": "11:00 AM",
        "status": "Confirmed"
    }
]


# ==========================================
# FUNCTION 1: Display all appointments
# ==========================================

def show_appointments():

    print("\n========== ALL APPOINTMENTS ==========")

    if len(appointments) == 0:
        print("There are no appointments.")
        return

    for appointment in appointments:

        print("\nPatient:", appointment["patient"])
        print("Age:", appointment["age"])
        print("Doctor:", appointment["doctor"])
        print("Department:", appointment["department"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print("Status:", appointment["status"])


# ==========================================
# FUNCTION 2: Book an appointment
# ==========================================

def book_appointment():

    print("\n========== BOOK APPOINTMENT ==========")

    patient = input("Enter patient name: ")

    age = int(input("Enter patient age: "))

    print("\nDepartments:")
    print("1. General Medicine")
    print("2. Pediatrics")
    print("3. Cardiology")
    print("4. Dental")

    department_choice = input("Choose department: ")

    if department_choice == "1":
        department = "General Medicine"
        doctor = "Dr. Kamau"

    elif department_choice == "2":
        department = "Pediatrics"
        doctor = "Dr. Achieng"

    elif department_choice == "3":
        department = "Cardiology"
        doctor = "Dr. Otieno"

    elif department_choice == "4":
        department = "Dental"
        doctor = "Dr. Hassan"

    else:
        print("Invalid department.")
        return

    date = input("Enter appointment date (DD/MM/YYYY): ")

    time = input("Enter appointment time: ")

    # Create a new appointment
    new_appointment = {
        "patient": patient,
        "age": age,
        "doctor": doctor,
        "department": department,
        "date": date,
        "time": time,
        "status": "Confirmed"
    }

    # Add appointment to the list
    appointments.append(new_appointment)

    print("\nAppointment booked successfully!")
    print("Patient:", patient)
    print("Doctor:", doctor)
    print("Date:", date)
    print("Time:", time)


# ==========================================
# FUNCTION 3: Search appointment
# ==========================================

def search_appointment():

    print("\n========== SEARCH APPOINTMENT ==========")

    name = input("Enter patient name: ").lower()

    found = False

    for appointment in appointments:

        if name in appointment["patient"].lower():

            print("\nAppointment Found!")
            print("------------------")

            print("Patient:", appointment["patient"])
            print("Doctor:", appointment["doctor"])
            print("Department:", appointment["department"])
            print("Date:", appointment["date"])
            print("Time:", appointment["time"])
            print("Status:", appointment["status"])

            found = True

    if found == False:
        print("\nNo appointment found.")


# ==========================================
# FUNCTION 4: Cancel appointment
# ==========================================

def cancel_appointment():

    print("\n========== CANCEL APPOINTMENT ==========")

    name = input("Enter patient name: ").lower()

    found = False

    for appointment in appointments:

        if name == appointment["patient"].lower():

            appointment["status"] = "Cancelled"

            print("\nAppointment cancelled successfully.")

            found = True
            break

    if found == False:
        print("\nAppointment not found.")


# ==========================================
# FUNCTION 5: Show today's appointments
# ==========================================

def show_department_appointments():

    print("\n========== SEARCH BY DEPARTMENT ==========")

    department = input("Enter department: ").lower()

    found = False

    for appointment in appointments:

        if appointment["department"].lower() == department:

            print("\nPatient:", appointment["patient"])
            print("Doctor:", appointment["doctor"])
            print("Date:", appointment["date"])
            print("Time:", appointment["time"])
            print("Status:", appointment["status"])

            found = True

    if found == False:
        print("\nNo appointments found for this department.")


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    print("\n")
    print("==========================================")
    print("       HOSPITAL APPOINTMENT SYSTEM")
    print("==========================================")

    print("1. View all appointments")
    print("2. Book an appointment")
    print("3. Search appointment")
    print("4. Cancel appointment")
    print("5. Search by department")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        show_appointments()

    elif choice == "2":

        book_appointment()

    elif choice == "3":

        search_appointment()

    elif choice == "4":

        cancel_appointment()

    elif choice == "5":

        show_department_appointments()

    elif choice == "6":

        print("\nThank you for using the Hospital Appointment System.")
        break

    else:

        print("\nInvalid choice. Please select 1-6.")
```

## What students learn from this project

This project is useful because it introduces several concepts naturally:

### 1. Lists

```python
appointments = [
    {...},
    {...}
]
```

The list stores multiple appointments.

### 2. Dictionaries

Each appointment is represented by a dictionary:

```python
{
    "patient": "John Mwangi",
    "age": 25,
    "doctor": "Dr. Kamau",
    "department": "General Medicine",
    "date": "25/08/2026",
    "time": "10:00 AM",
    "status": "Confirmed"
}
```

### 3. Updating dictionary values

Students learn that dictionaries can be changed:

```python
appointment["status"] = "Cancelled"
```

### 4. Adding data to a list

```python
appointments.append(new_appointment)
```

### 5. Searching

```python
if name in appointment["patient"].lower():
```

### 6. Functions

The application is divided into manageable functions:

```text
show_appointments()
book_appointment()
search_appointment()
cancel_appointment()
show_department_appointments()
```

### 7. Menu-driven application

The `while True` loop keeps the application running until the user chooses **Exit**.

---

### Next level 🚀

For the **next version**, I would not jump straight to databases. Add:

1. **Patient registration**
2. **Doctor registration**
3. **Unique patient ID**
4. **Unique appointment ID**
5. **Prevent double-booking**
6. **Appointment rescheduling**
7. **Appointment history**
8. **Save appointments to a JSON file**

That version would introduce **file handling, JSON, validation, and CRUD operations** while still keeping the project understandable to students.
