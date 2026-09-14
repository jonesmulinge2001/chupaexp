
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

# Function to display all appointments
def show_appointments():
    try:
        print("\n--- All Appointments ---")
        for appointment in appointments:
            print(f"Patient: {appointment['patient']}")
            print(f"Age: {appointment['age']}")
            print(f"Doctor: {appointment['doctor']}")
            print(f"Department: {appointment['department']}")
            print(f"Date: {appointment['date']}")
            print(f"Time: {appointment['time']}")
            print(f"Status: {appointment['status']}")
            # print(f"Nurse: {appointment['nurse']}") # This line will raise a KeyError since 'nurse' is not defined in the appointment dictionaries.
            print("-------------------------")
    except Exception as e:
        print(f"An error occurred while displaying appointments: {e}")


# function to validate user inputs
def validate_user_input(message):
    while True:
        patient = input(message).strip().lower() # input("Enter patient name: ").strip().lower()
        if len(patient) > 0:
            return patient
        else:
            print("Invalid input. Please enter a valid name.")

# function to book appointment
def book_appointment():
    try:
        print("\n--- Book Appointment ---")
        # reuse the validate_user_input function to get valid patient name
        patient = validate_user_input("Enter patient name: ")
        # get user age and validate it using try-except block and  use validate_user_input fucntion to get valid age
        try:
            age = validate_user_input("Enter patient age: ") # age is a string now
            age = int(age) # cast age to integer
        except ValueError:
            print("Invalid age. Please enter a valid number.")
            return

        # Department selection
        print("\nSelect Department:")
        print("1. General Medicine")
        print("2. Pediatrics")
        print("3. Orthopedics")
        print("4. Cardiology")
        print("5. Dental")
        department_choice = input("Enter your choice (1-5): ").strip()
        if department_choice == "1":
            department = "General Medicine"
            doctor = "Dr. Kamau"
        elif department_choice == "2":
            department = "Pediatrics"
            doctor = "Dr. Achieng"
        elif department_choice == "3":
            department = "Orthopedics"
            doctor = "Dr. Otieno"
        elif department_choice == "4":
            department = "Cardiology"
            doctor = "Dr. Njeri"
        elif department_choice == "5":
            department = "Dental"
            doctor = "Dr. Mwende"
        else:
            print("Invalid department")

        #  get appointment date and time
        date = input("Enter appointment date (dd/mm/yyyy): ").strip()
        if not date:
            print("Invalid date. Please enter a valid date.")
            return
        time  = input("Enter appointment time (hh:mm AM/PM): ").strip()
        if not time:
            print("Invalid time. Please enter a valid time.")
            return

        # Create appointment dictionary
        new_appointment = {
            "patient": patient,
            "age": age,
            "doctor": doctor,
            "department": department,
            "date": date,
            "time": time,
            "status": "Confirmed"
        }

        # append the new appointment to the appointments list
        appointments.append(new_appointment)
        print("Appointment booked!")
        print(f"Patient: {patient}")
        print(f"Doctor: {doctor}")
        print(f"Date: {date}")
        print(f"Time: {time}")
    except Exception as e:
        print(f"An error occurred while booking appointment: {e}")

# fucntion to search for an appointment by patient name
def search_appointment():
    try:
        patient = validate_user_input("Enter patient name to search for appointment: ")
        found  = False
        found_appointments = [] # list to store found appointments for the patient
        for appointment in appointments:
            if patient == appointment['patient'].lower():
                found_appointments.append(appointment)
                found = True
                print("\n--- Appointment Found ---")
                print(f"Patient: {appointment['patient']}")
                print(f"Doctor: {appointment['doctor']}")
                print(f"date: {appointment['date']}")
                print(f"Time: {appointment['time']}")
                print(f"Status: {appointment['status']}")
                print(f"Nurse: {appointment.get('nurse', 'N/A')}") # Use .get() to avoid KeyError if 'nurse' is not present
    except KeyError:
        print("Error: Appointment data is missing a required field.")
    if found == False:
        print("No appointment found for patient:", patient)

# cancel appointment
def cancel_appointment():
    try:
        patient = validate_user_input("Enter patient name to cancel appointment: ")
        found = False
        for appointment in appointments:
            if patient == appointment['patient'].lower():
                found = True
                confirm = ["Yes", "y"]
                confirmation = input("Are you sure you want to cancel the appointment? (Y): ").strip()
                if confirmation not in confirm: # if confirmation is not in the confirm list, then cancel the cancellation process
                    print("Could not cancel the appointment.")
                    break
                appointment['status'] = "Cancelled"
                # appointments.remove(appointment)
                print(f"Appointment cancelled for patient:", {patient})
                break
        if not found:
            print("No appointment found for patient:", patient)
    except Exception as e:
        print(f"An error occurred while cancelling appointment: {e}")

# function to show department appointments
def show_department_appointments():
    try:
        print("\n--- Department Appointments ---")
        print("1. General Medicine")
        print("2. Pediatrics")
        print("3. Orthopedics")
        print("4. Cardiology")
        print("5. Dental")
        department_choice = validate_user_input("Enter your choice (1-5): ")
        if department_choice == "1":
            department = "General Medicine"
        elif department_choice == "2":
            department = "Pediatrics"
        elif department_choice == "3":
            department = "Orthopedics"
        elif department_choice == "4":
            department = "Cardiology"
        elif department_choice == "5":
            department = "Dental"
        else:
            print("Invalid department choice.")
            return

        found = False # flag to check if any appointments were found for the selected department
        for appointment in appointments:
            if appointment['department'].lower() == department.lower():
                found = True # set found to True if an appointment is found for the selected department
                print("\n--- Appointment ---")
                print(f"Patient: {appointment['patient']}")
                print(f"Doctor: {appointment['doctor']}")
                print(f"Date: {appointment['date']}")
                print(f"Time: {appointment['time']}")
                print(f"Status: {appointment['status']}")
                print("-------------------------")
        if not found: # if no appointments were found for the selected department, print a message
            print(f"No appointments found for the {department} department.")
    except Exception as e:
        print(f"An error occurred while displaying department appointments: {e}")

# Main Program (Entry point)
def main():
    while True:
        print("\n--- Hospital Appointment System ---")
        print("1. Show All Appointments")
        print("2. Book Appointment")
        print("3. Search Appointment")
        print("4. Cancel Appointment")
        print("5. Show Department Appointments")
        print("6. Exit")

        choice = validate_user_input("Enter your choice (1-6): ")

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
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": # check if the script is being run directly (not imported)
    main() # call the main function to start the program