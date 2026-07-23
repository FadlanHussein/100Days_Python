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