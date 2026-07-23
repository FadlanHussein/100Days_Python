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

class Parent(Grandparent):
    pass
class Child(Parent):
    pass

child = Child()
child.display()

