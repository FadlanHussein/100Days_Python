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

# %% Kasus 7 Project HR: Candidate & Bonus Manager

# Step 1 Filtering Usia
work_experience = [0, 1, 2, 3, 4, 5, 6, 7]
lolos_screening = [exp for exp in work_experience if exp> 2]
print (f"Total kandidat lolos screening awal: {lolos_screening}")



# %% Kasus 8  Project HR Data Analyst Challenge

# Struktur data : name, age, work-exp, grade-tes, grade-interview
kandidat = [
    ("Siti Aminah", 28, 4, 90, 80), 
    ("Hadi Tjahjanto", 30, 5, 85, 88), 
    ("Agus Harimurti", 25, 2, 95, 92),
    ("Arif Alfiansyah", 27, 3, 87, 90),
    ("Budi Santoso", 31, 7, 92, 88),
    ("Citra Kirana", 29, 6, 78, 85),
    ("Dewi Persik", 24, 2, 88, 91),
    ("Eka Gustiwana", 30, 5, 91, 89),
    ("Mira Lesmana", 29, 6, 93, 90),
    ("Rio Dewanto", 32, 7, 89, 87),
    ("Nita Thalia", 25, 2, 90, 88),
    ("Hadi Tjahjanto", 28, 4, 92, 89),
    ("Indah Permatasari", 31, 6, 88, 86),
    ("Rian D'Masiv", 27, 3, 91, 88),
    ("Sari Roti", 30, 5, 94, 91),
    ("Yoga Pratama", 26, 2, 87, 85),
    ("Dewi Persik", 29, 6, 93, 90),
    ("Joko Saputra", 33, 7, 89, 87),
    ("Yanti Kusuma", 25, 2, 90, 88),
    ("Agus Harimurti", 28, 4, 92, 89),
    ("Lina Jubaedah", 31, 6, 88, 86),
    ("Roni Setiawan", 27, 3, 91, 88),
    ("Mona Ratuliu", 30, 5, 94, 91),
    ("Vino G Bastian", 26, 2, 87, 85),
    ("Sita Nursanti", 29, 6, 93, 90),
    ("Bima Arya", 33, 7, 89, 87)
]

# Jawaban Kasus 8:
# Syarat: Umur < 30, Pengalaman >= 3, Nilai Tes >= 85
# Labeling: Jika Interview >= 90 -> "Fast Track", else -> "Standar"
kandidat_terpilih = [
    f"{k[0]} - Fast Track" if k[4]>=90 
    else f"{k[0]} - standard"
    for k in kandidat if k[1] < 35 and k[2] >=2 and k[3] >=80
]
print("\n--- Hasil Seleksi Final ---")
for nama in kandidat_terpilih:
    print(nama)

# %%
