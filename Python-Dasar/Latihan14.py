# Random Password Generator

# %% Kasus 1
import math
print(math.sqrt(16))
# %% Kasus 2
import random
print(random.randint(1, 20))

# %% Kasus 3 
from random import choices
print(choices(["Apple", "Banana", "Cherry"]))
# %% Kasus 4

import random as f
print(f.randint(1, 10))

# %% Kasus 5

import random
password = ''.join(random.choices('qwertyuiopasdfghjklzxcvbnm', k=10))
print(password)

# %% Kasus 6 Random Password Generator

import random, string

# Step 1: Define Password Generation Function
def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    # Step 2: Character sets for the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()<>?/"

    # Step 3: Ensure at least one of each character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Step 4: Fill the remaining length with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Step 5: Shuffle the password to make it more random
    random.shuffle(password)

    # Step 6: Convert the list to a string and return
    return ''.join(password)

# Step 7: User Interaction

try:
    length = int(input("Enter the desired password length (minimun 4): "))
    password = generate_password(length)
    print("Generate Password:", password)
except ValueError as e:
    print(e)
# %%
