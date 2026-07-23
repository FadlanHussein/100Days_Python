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

