# Exceptions in Python 

# try and except block
def getShopNumber():
    try:
        shopNumber = int(input("Shop Number: "))
        print(f"Your shop number is {shopNumber}")
    except ValueError:
        print("Invalid input")

# getShopNumber()

def getUserSalary():
    try:
        user_salary = int(input("Your Salary: "))
        if user_salary >= 50000:
            user_salary = user_salary + 10000
            print(f"Your salary has been increased to {user_salary}")
        else:
            print(f"Your salary remains to be {user_salary}")
    except ValueError:
        print("Provide a valid salary")        

# getUserSalary()

def creditEligibility():
    pays_consistently = False
    try:
        name = input("Your name: ")
        amount_requesting = float(input("Amount: "))
        age = int(input("Your age: "))
        if age > 25:
            if not pays_consistently:
                risk = amount_requesting / age
                print(f"{name} Your Credit Risk: {risk}")
    
    except ValueError:
        print("Enter a valid value")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Thanks for using our system")

# creditEligibility()

# def readContent():
#     try:
#         file_path = "C:\Users\Administrator\Downloads\Data"
#         with open(file_path, 'r') as file:
#             for line in file_path:
#                 print(line)
#     except ValueError:
#         print("No value found in your file")
#     except SyntaxError:
#         print("Errro occured during the operation")
#     except FileNotFoundError:
#         print("The file you are looking for is not found")
#     except FileExistsError:
#         print("File does not exist")

# readContent()


def withdraw(balance, amount_to_withdraw):
    if balance < amount_to_withdraw:
        raise ValueError("Insufficient balance")
    balance-=amount_to_withdraw
    print(f"Withdrawal: {amount_to_withdraw}")
    print(f"Balance: {balance}")

withdraw(2000, 5000)