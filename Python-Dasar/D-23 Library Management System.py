# %% Kasus Constructors

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

# Create an object
book1 = Book("1984", "George Orwell")
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
        return self.__balance

account = Account("John Doe", 1990)
account.deposit(500)
print(f"Account Balance: ${account.get_balance()}")

# %% Kasus 5 Library Management System

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library")

    # view all books
    def view_books(self):
        if not self.books:
            print("No books in the library")
        else:
            print("\n---- Library Catalog ----")
            for book in self.books:
                book.display_info()

    # borrow a book
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    print(f"Book '{title}' is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"Book '{title}' has been borrowed. Enjoy reading.")
                return
        print(f"Book '{title}' is not available for borrowing")

    # return book
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Book '{title}' has been returned")
                else:
                    print(f"Book '{title}' is already available.")
                return
        print(f"Book '{title}' is not in the library.")

# Main Program
library = Library()

while True:
    print("\n---- Library Management System ----")
    print("1. Add book")
    print("2. View books")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        library.add_book(title, author)
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)
    elif choice == "4":
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif choice == "5":
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
