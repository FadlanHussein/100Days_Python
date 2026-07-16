import os

# %% Kasus 1
base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir, "filename.txt"), "r") as files:
    content = files.read()
    print(content)

# %% Kasus 2
try:
    with open(os.path.join(base_dir, "filename.txt"), "r") as files:
        content = files.read()
        print(content)
except FileNotFoundError:
    print("File not found")

# %% Kasus 3
# Reviewer App

def load_recipes(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            recipes = content.split("\n\n")
            recipes_dict = {}
            for recipe in recipes:
                lines = recipe.strip().split("\n")
                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingridients = lines[1].replace('Ingredients: ', '').strip()
                    instrucions = lines[2].replace('Instructions: ', '').strip()
            return recipes_dict
    except FileNotFoundError:
        print("File not Found.")
        return ()

def show_menu():
    print("\n---- Recipe Viewer Menu ----")
    print("1. View Recipe by Name")
    print("2. List All Recipe")
    print("3. Exit")

def view_recipe(recipes):
    name = input("Enter the name of the recipe:").strip()
    if name in recipes:
        print(f"\n---- Recipe {name} Details ----")
        print(f"Ingredients: {recipes[name]['ingredients']}")
        print(f"Ingredients: {recipes[name]['instructions']}")
    else:
        print("Recipe not found")

recipe_file = "recipes.txt"
recipes = load_recipes(recipe_file)

while True:
    show_menu()
    choice = input("Enter Your Choice (1/2/3)")
    if choice == '1':
        view_recipe(recipes)
    elif choice == '2':
        print("\n--- All Recipes ----")
        for name in recipes:
            print(name)
    elif choice == '3':
            print ("Existinf the program: ")
            break

# %%
