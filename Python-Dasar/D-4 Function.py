# %% Kasus 1
def function_name():
    # Kode block inside the function
    print("hello from function")

function_name()
# %% Kasus 2
def greet():
    print("Hello, welcome to the pyhton")
greet()
# %% kasus 3
def greet_user(name):
    print(f"hello {name}, wellcome to the python")
    
greet_user("Fadlan")

# %% kasus 4
def add(a, b):
    return a + b

result = add(5, 4)
print(f"The sum is: {result}")

# %% kasus 5
def multiply(a, b):
    return a * b

result2 = multiply(3, 4)
print(f"The product is: {result2}")

# %% kasus 6
import random
#step 1: define the math question function
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    oprator = random.choice(['+', '-', '*'])
    question = f"What is {num1} {oprator} {num2}? "
    answer = eval(f"{num1} {oprator} {num2}")
    return question, answer
#step 2: main quiz game function
def math_quiz():
    score = 0
    rounds = 5

    print("Welcome to the Math Quiz")
    print("you will be presented with math problems, and you need to provide the correct answers.")

    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"Question {i+1}: {question}")
        user_answer = int(input("Your Answer: "))
        if user_answer == correct_answer:
            print("Correct")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    print("\n--- Game Over! ---")
    print(f"Your Final score is: {score}/{rounds}")
    if score == rounds:
        print("Congratulations! You get all the questions correct.")
    elif score >= rounds // 2:
        print("Good job! You did well")
    else:
        print("keep practicing! You can do better next time.")

# step 3 run quiz
math_quiz()
# %% Kasus 7 Pyhton Brain Trainer

import random
import time
import os

def bersihkan_layar():
    # Menghapus teks di terminal agar angka memori tersembunyi
    # 'cls' untuk Windows, 'clear' untuk macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def game_hitung_cepat():
    bersihkan_layar()
    print("=== Game 1: HITUNG CEPAT ===")
    print("Selesaikan matematika cepat")
    input("Tekan Enter untuk memulai!")

    skor = 0
    waktu_mulai = time.time()
    #Mencatat waktu mulai game

    for i in range(10):
        soal1 = random.randint(10,50)
        #Angka lebih besar agar menantang
        soal2 = random.randint(10,50)
        #Memilih operator secara acak
        operator = random.choice(['+', '-', '*'])
        jawaban_benar = eval(f"{soal1} {operator} {soal2}")

        print(f"\n[soal {i+1}] berapa hasil dari : {soal1} {operator} {soal2}?")

        try:
            jawaban_user = int(input(" jawaban anda: "))
            if jawaban_user == jawaban_benar:
                print("jawaban benar!")
                skor += 1
            else:
                print(f"Jawaban salah! jawaban yang benar: {jawaban_benar}")
        except ValueError:
            print("Input harus berupa angka, jika selain itu akan eror")
    
    waktu_selesai = time.time()
    #Mencatat waktu selesai game
    total_waktu = round(waktu_selesai - waktu_mulai,2)

    print("\n==== Hasil Akhir ====")
    print(f" Skor Anda : {skor}/10")
    print(f"Total Waktu: {total_waktu} detik")

    input("\nTekan Enter untuk kembali ke menu awal.")

def game_input_angka():
    bersihkan_layar()
    print("=== Game stage 2 ===")
    print("Mengingat soal yang muncul sesaat")
    input("Tekan enter untuk memulai")

    skor = 0
    panjang_digit = 4
    #Nilai awal loop
    for ronde in range(8):
        waktu_tampil = panjang_digit - 1 
        # 1. Membuat angka acak sepanjang 'panjang_digit'
        angka_acak = "".join([str(random.randint(0,9)) for _ in range(panjang_digit)])
        
        # 2. Menampilkan angka acak tersebut
        bersihkan_layar()
        print(f"ingat angka ini: {angka_acak}")

        # 3. Menunggu selama waktu_tampil, lalu hapus angka dari layar
        time.sleep(waktu_tampil)
        bersihkan_layar()

        # 4. Meminta jawaban dari pengguna
        jawaban_user = input("jawaban anda: ")

        # 5. Pengecekan jawaban (Harus menjorok ke dalam loop 'for')
        if jawaban_user == angka_acak:
            print("benarr")
            skor += 1
            panjang_digit += 1 # Menambah panjang digit
            time.sleep(1)
        else:
            print("salah")
            print("permainan berakhir")
            time.sleep(2)
            break

    # 6. Menampilkan skor akhir setelah keluar dari permainan
    bersihkan_layar()
    print("\n==== GAME SELESAI ====")
    print(f"Skor Anda: {skor}/8")
    print("Terima kasih sudah bermain!")
    input("\ntekan enter untuk kembali ke menu")

def menu_kasus_7():
    while True:
        bersihkan_layar()
        print("================================")
        print("      MENU GAME KASUS 7         ")
        print("================================")
        print("1. Game Hitung Cepat (Speed Math)")
        print("2. Game Mengingat Angka (Memory)")
        print("3. Keluar")
        print("================================")
        
        pilihan = input("Pilih menu (1/2/3): ")
        if pilihan == '1':
            game_hitung_cepat()
        elif pilihan == '2':
            game_input_angka()
        elif pilihan == '3':
            break

# Menjalankan menu Kasus 7
if __name__ == "__main__":
    menu_kasus_7()
