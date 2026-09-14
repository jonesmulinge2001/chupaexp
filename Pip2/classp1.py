# more into classes in python and objects simulating bank
# Bank Account Simulation in Python

class BankAccount: # creating a class BankAccount
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount # balance = balance + amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        # if amount < 0 and amount <= self.balance:
        if 0 < amount <= self.balance: # if amount is greater than 0 and amount is less than or equal to balance
            self.balance -= amount # balance = balance - amount (100 / 50 = 50)
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ${self.balance}")

# Example usage by creating an object of the class BankAccount
account1 = BankAccount("John Dee", 1000) 
# calling the method display_balance()
account1.display_balance()

account1.deposit(500)
account1.withdraw(200)
account1.display_balance()