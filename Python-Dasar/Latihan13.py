# %% List Comprehension

# %% Kasus 1
# [expression for item in iterable if condition]

squares = [x**2 for x in range (10)]
print(squares)

# %% Kasus 2

numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)
# %% kasus 3

numbers = [1, 2, 3, 4, 5, 6, 7]
evens = [x for x in numbers if x % 2 == 0]
print(evens)
# %% Kasus 4

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
short_names = [name for name in names if len(name) <= 3]
print(short_names)
# %% Kasus 5

Matriks = [1, 2, 3, 4, 5, 6, 7]
labels = ["Even" if x % 2 == 0 else "edd" for x in Matriks]
print(labels)

# %% Kasus 6 Project Student Grade Manager

# Step 1: Get Student Scores

student_scores = input("Enter student scores separated by commas: ")
scores = [int(scores) for scores in student_scores.split(",")]

# Step 2: Assign Grades Using List Comprehension

grades = [
        ("A" if score >= 90 else 
        "B" if score >=80 else 
        "C" if score >= 70 else 
        "D" if score >= 60 else 
        "F") for score in scores]

# Step 3: Filter Passing and Faillinf Student
passing_students = [score for score in scores if score >=60]
failing_students = [score for score in scores if score <60]

# Step 4: Print Results
print ("\n ---- Passing and Faillinf Students ---- ")
print (f"Passing Students: {passing_students}")
print (f"Failing Students: {failing_students}")

# %%
