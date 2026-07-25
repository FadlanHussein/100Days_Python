# %% Static and Class Method
class Calculator:
    base_value = 100

    @staticmethod
    def add(value1, value2):
        return value1 + value2

    @classmethod
    def multiply_base(cls, multiplier):
        return cls.base_value + multiplier

# Using Static Method
print(Calculator.add(4, 5))

# Using Class Method
print(Calculator.multiply_base(2))
    
# %% Kasus 2 Use Static vs Class Method


class Utility:
    @staticmethod
    def greet_user(name):
        print(f"Hello, {name}")

Utility.greet_user("John")

class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 10

Counter.increment()
print(Counter.count)
# %% Kasus 3 Inventory Management System

class Inventory:
    total_items = 0

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        Inventory.total_items += quantity

    # Instance Method: Show Product Details
    def show_product_details(self):
        print("\n---- Product Details ----")
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

    # Instance Method: Sell Product
    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Inventory.total_items -= amounT
            print(f"{amount} {self.product_name} (s) sold.")
        else:
            print("Insufficient quantity")

        

        
        
