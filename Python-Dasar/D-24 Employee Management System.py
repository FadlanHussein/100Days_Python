# %% Kasus 1 Inheritance

# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child Class
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child class
class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog = Dog()
dog.sound()
cat = Cat()
cat.sound()

# %% Type of Inheritance
class Parent:
    def display(self):
        print("I am Parent Class")

class Child(Parent):
    pass

child = Child()
child.display()

# %% Type of Inheritance
class A:
    def method_a(self):
        print("I am method A")

class B:
    def method_b(self):
        print("I am method B")

class C(A, B):
    pass
obj = C()
obj.method_a()
obj.method_b()

# %% Type of Inheritance

class GrandParent:
    def display(self):
        print("I am Grand Parent class")

class Parent(GrandParent):
    pass
class Child(Parent):
    pass

child = Child()
child.display()

# %% Kasus 2 The Super () Function

class Animal:
    def __init__(self):
        print("Animal Created")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Created")

dog = Dog()


# %% Kasus 3 Method Overriding
class Vehicle:
    def fuel_type(self):
        print("Final type: Petrol/Diesel")

class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Fuel type: Electrical")

car = ElectricCar()
car.fuel_type()

# %% Kasus Project : Employee Management

# Base Class : Employee
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print("\n---- Employee Details ----")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.1
    
# Derived Class: Manager
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

    def calculate_bonus(self):
        return self.salary * 0.2

# Derived Class: Manager
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.5

# Main Program
employees = []

def add_employee():
    print("\n---- Choose Employee Type ----")
    print("1. Regular Employee")
    print("2. Manager")
    print("3. Developer")
    choice = int(input("Enter your choice: ").strip())

    name = input("Enter Your Name: ").strip()
    emp_id = input("Enter Employee ID: ").strip()
    salary = float(input("Enter Employee Salary: ").strip())

    if choice == 1:
        employees.append(Employee(name, emp_id, salary))
    elif choice == 2:
        department = input("Enter Department: ").strip()
        employees.append(Manager(name, emp_id, salary, department))
    elif choice == 3:
        programming_language = input("Enter Programming Language: ").strip()
        employees.append(Developer(name, emp_id, salary, programming_language))
    else:
        print("Invalid choice")

def display_all_employee():
    print("\n---- All Employee ----")
    for employee in employees:
        employee.display_info()
        print(f"Bonus: {employee.calculate_bonus()}")

# Menu
while True:
    print("\n---- Employee Management System ----")
    print("1. Add Employee")
    print("2. Display All Employee")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): ").strip())

    if choice == 1:
        add_employee()
    elif choice == 2:
        display_all_employee()
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Enter Choice")