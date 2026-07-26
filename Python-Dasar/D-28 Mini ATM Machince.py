# %% Kasus 1 OOP Principles

# Aunthenticate with PINs securely.
# Check account balance.
# Deposit money.
# Withdraw money with balance validation.
# Change PIN.
# Exit securely

# Classes Overview:

# BankAccount
# Attributes: account_number, pin, balance
# Methods: check_balance(), deposit(), withdraw(), change_pin()

# ATM
# Manages account authntication
# Provides the main menu for ussers.

# Concepts Applied:

# Encapsulation: Secure PIN handling and balance acces.
# Static Method: For utility tasks like PIN validation.
# Class Method: To maintain account-level settings.
# Ploymorphism: Flexibility in transaction operations.

# Mini ATM Machine

class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance

    # Validate Pin
    def validate_pin(self, entered_pin):
        return entered_pin == self.__pin

    # Check Balance
    def check_balance(self):
        print(f"Current Balance: {self.__balance}")

    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self__balance += amount
            print(f"Deposited {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Withdraw Money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdraw {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount")

    # Change Pin
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin):
            self.__pin = new_pin
            print("PIN changed succesfully.")
        else:
            print("Invalid old PIN. Ensure the old Pin is correct the new PIN is 4 digits")

class ATM:
    def __init__(self):
        self.accounts = {}

    # Create Account
    def create_account(self):
        account_number = input("Enter account number: ")
        pin =
        