A better **next project** is a **Banking Management System**. It introduces the same next-level concepts without being another appointment-based system.

## 🏦 Project: Simple Banking Management System

This can introduce:

* **Lists & dictionaries** — customer/account data
* **Functions** — separate banking operations
* **CRUD** — create, view, update, delete
* **Unique account numbers**
* **PIN validation**
* **Deposit & withdrawal**
* **Balance checking**
* **Transaction history**
* **Transfer money between accounts**
* **Input validation**
* **JSON file handling** — save data permanently
* **Error handling** with `try/except`

### Example menu

```text
================================
       SIMPLE BANKING SYSTEM
================================

1. Create Account
2. Login
3. Check Balance
4. Deposit Money
5. Withdraw Money
6. Transfer Money
7. Transaction History
8. View Account
9. Exit

Choose an option:
```

### Example account structure

```python
account = {
    "account_number": "ACC1001",
    "name": "John Mwangi",
    "pin": "1234",
    "balance": 5000,
    "transactions": []
}
```

A transaction could be:

```python
{
    "type": "Deposit",
    "amount": 2000,
    "balance": 7000
}
```

### The progression would be excellent for students

**Project 1 — Movie Recommendation**

> Lists → dictionaries → input/output → loops → conditions → functions

**Project 2 — Hospital Appointment**

> Lists → dictionaries → functions → search → update → menu

**Project 3 — Banking System**

> CRUD → validation → authentication → transactions → JSON → error handling

Then we can move to:

**Project 4 — Inventory Management System**

> JSON → CRUD → stock calculations → reports

**Project 5 — Student Management System**

> Records → searching → sorting → statistics → JSON

**Project 6 — Mini E-commerce System**

> Products → cart → orders → payments simulation → JSON

The **Banking Management System** is the one I'd build next because it gives students a strong introduction to **real-world data processing, validation, authentication, transactions, and persistent storage** before they encounter databases.


import json
import os
import random

# ==========================================
#       SIMPLE BANKING MANAGEMENT SYSTEM
# ==========================================

FILE_NAME = "bank_data.json"


# ==========================================
# LOAD DATA FROM JSON FILE
# ==========================================

def load_accounts():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


# ==========================================
# SAVE DATA TO JSON FILE
# ==========================================

def save_accounts():

    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


# ==========================================
# GENERATE ACCOUNT NUMBER
# ==========================================

def generate_account_number():

    while True:

        number = random.randint(1000, 9999)

        account_number = "ACC" + str(number)

        # Check whether account already exists
        exists = False

        for account in accounts:

            if account["account_number"] == account_number:
                exists = True

        if exists == False:
            return account_number


# ==========================================
# CREATE ACCOUNT
# ==========================================

def create_account():

    print("\n========== CREATE ACCOUNT ==========")

    name = input("Enter your full name: ")

    # Validate PIN
    while True:

        pin = input("Create a 4-digit PIN: ")

        if len(pin) == 4 and pin.isdigit():
            break

        print("PIN must contain exactly 4 digits.")

    account_number = generate_account_number()

    new_account = {
        "account_number": account_number,
        "name": name,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }

    accounts.append(new_account)

    save_accounts()

    print("\nAccount created successfully!")
    print("Account Number:", account_number)


# ==========================================
# FIND ACCOUNT
# ==========================================

def find_account(account_number):

    for account in accounts:

        if account["account_number"] == account_number:
            return account

    return None


# ==========================================
# LOGIN
# ==========================================

def login():

    print("\n========== LOGIN ==========")

    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")

    account = find_account(account_number)

    if account is not None:

        if account["pin"] == pin:

            print("\nLogin successful!")
            print("Welcome,", account["name"])

            return account

    print("\nInvalid account number or PIN.")

    return None


# ==========================================
# CHECK BALANCE
# ==========================================

def check_balance(account):

    print("\n========== ACCOUNT BALANCE ==========")

    print("Account Number:", account["account_number"])
    print("Account Holder:", account["name"])
    print("Balance: KES", account["balance"])


# ==========================================
# DEPOSIT MONEY
# ==========================================

def deposit_money(account):

    print("\n========== DEPOSIT MONEY ==========")

    try:

        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:

            print("Amount must be greater than zero.")
            return

        account["balance"] += amount

        transaction = {
            "type": "Deposit",
            "amount": amount,
            "balance": account["balance"]
        }

        account["transactions"].append(transaction)

        save_accounts()

        print("\nDeposit successful!")
        print("New Balance: KES", account["balance"])

    except ValueError:

        print("Please enter a valid amount.")


# ==========================================
# WITHDRAW MONEY
# ==========================================

def withdraw_money(account):

    print("\n========== WITHDRAW MONEY ==========")

    try:

        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:

            print("Amount must be greater than zero.")
            return

        if amount > account["balance"]:

            print("Insufficient balance.")
            return

        account["balance"] -= amount

        transaction = {
            "type": "Withdrawal",
            "amount": amount,
            "balance": account["balance"]
        }

        account["transactions"].append(transaction)

        save_accounts()

        print("\nWithdrawal successful!")
        print("New Balance: KES", account["balance"])

    except ValueError:

        print("Please enter a valid amount.")


# ==========================================
# TRANSFER MONEY
# ==========================================

def transfer_money(account):

    print("\n========== TRANSFER MONEY ==========")

    receiver_number = input(
        "Enter receiver account number: "
    )

    receiver = find_account(receiver_number)

    if receiver is None:

        print("Receiver account does not exist.")
        return

    if receiver["account_number"] == account["account_number"]:

        print("You cannot transfer money to yourself.")
        return

    try:

        amount = float(input("Enter amount to transfer: "))

        if amount <= 0:

            print("Amount must be greater than zero.")
            return

        if amount > account["balance"]:

            print("Insufficient balance.")
            return

        # Remove money from sender
        account["balance"] -= amount

        # Add money to receiver
        receiver["balance"] += amount

        # Sender transaction
        sender_transaction = {
            "type": "Transfer Sent",
            "amount": amount,
            "to": receiver["account_number"],
            "balance": account["balance"]
        }

        # Receiver transaction
        receiver_transaction = {
            "type": "Transfer Received",
            "amount": amount,
            "from": account["account_number"],
            "balance": receiver["balance"]
        }

        account["transactions"].append(sender_transaction)

        receiver["transactions"].append(receiver_transaction)

        save_accounts()

        print("\nTransfer successful!")
        print("KES", amount, "sent to", receiver["name"])

    except ValueError:

        print("Please enter a valid amount.")


# ==========================================
# TRANSACTION HISTORY
# ==========================================

def transaction_history(account):

    print("\n========== TRANSACTION HISTORY ==========")

    transactions = account["transactions"]

    if len(transactions) == 0:

        print("No transactions found.")
        return

    for transaction in transactions:

        print("\nType:", transaction["type"])
        print("Amount: KES", transaction["amount"])
        print("Balance: KES", transaction["balance"])

        if "to" in transaction:

            print("To:", transaction["to"])

        if "from" in transaction:

            print("From:", transaction["from"])


# ==========================================
# ACCOUNT INFORMATION
# ==========================================

def account_information(account):

    print("\n========== ACCOUNT INFORMATION ==========")

    print("Account Number:", account["account_number"])
    print("Name:", account["name"])
    print("Balance: KES", account["balance"])


# ==========================================
# USER BANKING MENU
# ==========================================

def banking_menu(account):

    while True:

        print("\n================================")
        print("        BANKING MENU")
        print("================================")

        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Account Information")
        print("7. Logout")

        choice = input("\nChoose an option: ")

        if choice == "1":

            check_balance(account)

        elif choice == "2":

            deposit_money(account)

        elif choice == "3":

            withdraw_money(account)

        elif choice == "4":

            transfer_money(account)

        elif choice == "5":

            transaction_history(account)

        elif choice == "6":

            account_information(account)

        elif choice == "7":

            print("\nYou have been logged out.")

            break

        else:

            print("\nInvalid option. Please try again.")


# ==========================================
# MAIN PROGRAM
# ==========================================

accounts = load_accounts()


while True:

    print("\n")
    print("==========================================")
    print("       SIMPLE BANKING SYSTEM")
    print("==========================================")

    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        create_account()

    elif choice == "2":

        account = login()

        if account is not None:

            banking_menu(account)

    elif choice == "3":

        print("\nThank you for using our banking system.")
        break

    else:

        print("\nInvalid choice. Please select 1-3.")
