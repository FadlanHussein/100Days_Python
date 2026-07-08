#%% Kasus 1 pembagian (Division)
try:
    num = int(input(" Ketikkan angka : "))
    result = 10 / num
    print("Hasil: ", result)
except ZeroDivisionError:
    print("Error: Anda tidak boleh membagi dengan angka 0")
else:
    print("Pembagian berhasil", result)
finally:
    print("Error: Anda bukan mengetikkan angka")
    
#%% Kasus 2 format lengkap try-except
try:
    # Taruh kode yang berpotensi error disini
    print("Kode ini dijalankan jika tidak terjadi error")
    pass
except Exception:
    # Taruh kode untuk menangani error disini
    print("Terjadi error")
else:
    # Kode ini dijalankan jika tidak ada error
    pass
finally:
    # Kode ini akan selalu dijalankan
    print("Program selesai")

#%% Kasus 3
try:
    num = int(input("Ketikkan angka: "))
    result = 10 / num
    print("Hasil: ", result)
except (ZeroDivisionError, ValueError):
    print("Error: Anda bukan mengetikkan angka")


#%% Kasus 4 Materi terkait penarikan 
def withdraw(amount):
    if amount < 0:
        raise ValueError("Penarikan tidak boleh negatif")
    print(f"Withdraw berhasil, Rp{amount}")
    
    #Code ini akan menjalankan penarikan
    try:
        withdraw (-50)
    except  ValueError as e:
        print(e)

#%% Kasus 5 safe calculator

#step 1: Mendifinisikan fungsi-fungsi di kalkulator
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        raise ZeroDivisionError ("Tidak dapat memproses pembagian dengan angka 0")
    return x/y

#step 2 : Membuat menu tombol
def show_menu():
    print("\n=== SIMPLE CALCULATOR ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

#step 3 : Program Utama
while True:
    show_menu()
    choice = input("Masukkan pilihan (1-5): ")

    if choice == "5":
        print("Terima kasih sudah menggunakan kalkulator!")
        break

    try:
        num1 = float(input("Masukkan Angka Pertama: "))
        num2 = float(input("Masukkan Angka Kedua: "))
    except ValueError:
        print("Input tidak valid, Harap masukkan angka")
        continue

    if choice == "1":
        print(f"Hasil: {add(num1, num2)}")
    elif choice == "2":
        print(f"Hasil: {substract(num1, num2)}")
    elif choice == "3":
        print(f"Hasil: {multiply(num1, num2)}")
    elif choice == "4":
        try:
            print(f"Hasil: {divide(num1, num2)}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    else:
        print("Pilihan tidak valid")

