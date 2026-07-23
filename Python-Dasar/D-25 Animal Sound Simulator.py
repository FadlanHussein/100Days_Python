# %% Kasus data dasar

class Animal:
    def make_sound(self):
        print("The animal make a sound")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows")

# Polymorphism in action

animal = [Dog(), Cat()]
for animal in animal:
    animal.make_sound()

# %% Kasus 2 Method Overriding in Polymorphism

class Shape:
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def area(self):
        print("Area of Circle: pi*r*r")

class Square(Shape):
    def area(self):
        print("Area of Square: side*side")

# Polumorphism in action

shapes = [Circle(), Square()]
for shape in shapes:
    shape.area()

# %% Kasus 3 Using Polymorphism in Python

class Bird:
    def make_sound(self):
        print("Bird chirps!")

class Duck:
    def make_sound(self):
        print("Duck quacks!")

def animal_sound(animal):
    animal.make_sound()

# Polymorphism in function arguments
bird = Bird()
duck = Duck()

animal_sound(bird)
animal_sound(duck)

# %% Kasus 4 Real-World Examples of Polymorphism
# Base Class
class Animals:
    def make_sound(self):
        print("Some generic animal sound")

# Devired Classes
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")

class Duck(Animal):
    def make_sound(self):
        print("Quack! Quack!")

# Polymorphism
class AnimalSoundSimulator:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animals, Animal):
            self.animals.append(animal)
            print(f"{animal.__class__,__name__} added to the simulator")
        else:
            print("Invalid animal type") 

    def make_all_sounds(self):
        if not self.animals:
            print("No animals in the simulator")
        else:
            print("\n---- Animal Sounds ----")
            for animal in self.animals:
                animal.make_sound()

# Main Program
simulator = AnimalSimulator()

while True:
    print("\n---- Animal Sound Simulator ----")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Cow")
    print("4. Add Duck")
    print("5. Make All Sound")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        simulator.add.append_animal(Dog())
    elif choice == '2':
        simulator.add_animal(Cat())
    elif choice == '3':
        simulator.add.append_animal(Cow())
    elif choice == '4':
        simulator.add_animal(Cow())
    elif choice == '5':
        simulator.add_animal(Duck())
    elif choice == '5':
        print("Exiting the simulator. Goodbye!!!")
        break
    else:
        print("Invalide choice. Please try again")
