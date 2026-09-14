# Python Classes and Exception Handling
import random # import the random module
class Bank: # Bank is the class name (blue print / plan)
    # class variables (shared by all instances of the class)
    location = "Nairobi" # class variable

    account_numbers = [] # class variable to store account numbers

    def generate_random_pin(self): # a method to generate a random pin number using math module and random module
        pin = random.randint(1000, 9999) # generate a random number between 1000 and 9999
        print(f"Your generated pin is: {pin}") # print the generated pin number
    
    def generate_account_number(self): # a method to generate a random account number using math module and random module
        account_number = random.randint(1000000000, 9999999999) # generate a random number between 1000000000 and 9999999999
        while account_number in Bank.account_numbers: # check if the generated account number already exists in the list of account numbers
            account_number = random.randint(1000000000, 9999999999) # generate a new random number if the generated account number already exists
        Bank.account_numbers.append(account_number) # add the generated account number to the list of account numbers

    # create a method to validate account number input
    def validate_account_number(self, account_number): # a method to validate account number input
        pass

    def register(self, name, account_number): # self is a reference to the current instance of the class
        self.name = name # instance variable
        self.account_number = account_number # instance variable
        self.balance = 0 # instance variable
        print(f"Account registered successfully for {self.name} with account number {self.account_number}. Initial balance: {self.balance}")
    
    def deposit(self, amount, account_number): # a method to deposit money into the account
        try:
            amount = float(amount) # convert / cast amount to float
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            self.balance += amount # add amount to balance (self.balance = self.balance + amount)
            print(f"Successfully deposited {amount} to account {account_number}. New balance: {self.balance}")
        except ValueError as e: # catch the ValueError exception and print the error message
            print(f"Error: {e}")

    def sendMoney(self, amount, account_number): # a method to send money to another account
        try:
            amount = float(amount) # convert / cast amount to float
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if amount > self.balance:
                raise ValueError("Insufficient balance.")
            self.balance -= amount # deduct amount from balance (self.balance = self.balance - amount)
            print(f"Successfully sent {amount} to account {account_number}. New balance: {self.balance}")
        except ValueError as e: # catch the ValueError exception and print the error message
            print(f"Error: {e}")
        
    def withdraw(self, amount, account_number):
        try:
            amount = float(amount) # convert / cast amount to float
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if amount > self.balance:
                raise ValueError("Insufficient balance.")
            self.balance -= amount # deduct amount from balance (self.balance = self.balance - amount)
            print(f"Successfully withdrew {amount} from account {account_number}. New balance: {self.balance}")
        except ValueError as e: # catch the ValueError exception and print the error message
            print(f"Error: {e}")
    
    def check_balance(self, account_number):
        print(f"Account {account_number} balance: {self.balance}")

    def validate_account_number(self, account_number):
        """
        Validate the account number input.
        Checks if the account number is a 10-digit number and exists in the system.
        """
        try:
            # Convert to string if it's not already
            account_number = str(account_number)
            
            # Check if it's exactly 10 digits
            if len(account_number) != 10:
                raise ValueError("Account number must be exactly 10 digits long.")
            
            # Check if it contains only digits
            if not account_number.isdigit():
                raise ValueError("Account number must contain only digits.")
            
            # Check if the account number exists in the system
            if account_number not in Bank.account_numbers:
                raise ValueError(f"Account number {account_number} does not exist in the system.")
            
            print(f"Account number {account_number} is valid.")
            return True
            
        except ValueError as e:
            print(f"Validation Error: {e}")
            return False

# create multiple instances / objects of the Bank class
kcb_bank = Bank() # create an instance of the Bank class
equity_bank = Bank() # create an instance of the Bank class
# accessing class variable using the class name
print(kcb_bank.location) # accessing class variable using the instance of the class

# calling / invoking the register method to register a new account
kcb_bank.register("Karlos", "1234567890") # calling the register method to register a new account
equity_bank.register("Alice", "1234567890") # calling the register method to register a new account
kcb_bank.deposit(2000, "1234567890") # calling the deposit method to deposit money into the account
kcb_bank.sendMoney(500, "0987654321") # calling the sendMoney method to send money to another account
kcb_bank.withdraw(1000, "1234567890") # calling the withdraw method to withdraw money from the account
