# ==========================================
# LATIHAN 1: PROGRAM INTERAKTIF DATA DIRI
# ==========================================

print("=== SILAKAN ISI DATA DIRI ANDA ===")

# 1. Input Data (String)
name = input("Masukkan Nama Lengkap Anda: ")

# 2. Input Data (Integer) - menggunakan int() untuk mengubah input teks menjadi angka bulat
age = int(input("Masukkan Umur Anda (Angka): "))

# 3. Input Data (Float) - menggunakan float() untuk mengubah input teks menjadi angka desimal
height = float(input("Masukkan Tinggi Badan Anda dalam cm (Contoh: 175.5): "))

# 4. Input Data (Boolean) - mengecek apakah jawaban user adalah "ya"
is_hr_input = input("Apakah Anda seorang HR professional? (ya/tidak): ")
is_hr = is_hr_input.lower() == "ya"

# ==========================================
# MENAMPILKAN HASILNYA
# ==========================================
print("\n=== HASIL PROSES PROGRAM ===")
print(f"Hello, my name is {name}.")
print(f"I am {age} years old.")
print(f"My height is {height} cm.")

if is_hr:
    print("I am an HR professional.")
else:
    print("I am not an HR professional.")

# ==========================================
# MENAMPILKAN TIPE DATA
# ==========================================
print("\n=== TIPE DATA VARIABEL ANDA ===")
print(f"name   : {type(name)}")
print(f"age    : {type(age)}")
print(f"height : {type(height)}")
print(f"is_hr  : {type(is_hr)}")
