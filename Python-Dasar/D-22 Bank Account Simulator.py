# %% Kasus 1 Class and Objects
class Car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"This is a {self.brand}: {self.model}")

# Create an object
my_car = Car("Tesla", "Model 3")
my_car.display_info()

your_car = Car("Honda", "Accord")
your_car.display_info()

# %% Kasus 2 Class Attributes and Methods

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Create objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

dog1.bark()
dog2.bark()
# %% Kasus 3 Constructor (__init__methods)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = name
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

person1 = Person("John", 25)
person1.greet()

# %% Kasus 4 Multiple Objects (Bank Simulator)

