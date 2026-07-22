# %% Kasus Constructors

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

# Create an object
book1 = Book("1984", "George Owell")
book1.display_info()

# %% Kasus 2 Using Method

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}, New Balance: ${self.balance}")

# Create an object

account1 = BankAccount("John Doe", 1000)
account1.deposit(500)

# %% Kasus 3 Class Methods vs Static Method

class Utility:
    app_version = "1.0"

    @classmethod
    def get_version(cls):
        print(f"App Version : {cls.app_version}")

    @staticmethod
    def greet():
        print("Hello! Welcome to the app.")

Utility.get_version()
Utility.greet()

# %% Kasus 4 Encapsulation and Validation

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Invalid deposit amount")
    
    def get_balance(self):
        return self