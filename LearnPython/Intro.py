def getRisk():
    salary = float(input("Enter your salary: "))
    age = int(input("Enter your age: "))
    # catch division by zero error (exception handling)
    try:
        risk = salary / age
        print(f"Your risk is: {risk}")
    except ZeroDivisionError:
            print("Age cannot be zero. Please enter a valid age.")
            return None

# call the function to test it
getRisk()
