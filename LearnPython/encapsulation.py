class BankAccount():
    def __init__(self):
        self.__balance = 9000
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"You deposited {amount}")
        print(f"Your balance is {self.__balance}")

account = BankAccount()
account.deposit(10000)