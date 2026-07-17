# if condition : do something if condition true
#else : do something if condition false
#elseif : do something if condition true and previous condition false
# %% Kasus 1
# Kita harus mendefinisikan variabel 'number' terlebih dahulu agar tidak terjadi NameError
number = int(input("Masukkan sebuah angka: "))

if number > 5:
    print("Number is greater than 5")
elif number == 5:
    print("Number is equal to 5")
else:
    print("Number is less than 5")

# %% Kasus 2

a = int(input("masukkan nilai a:"))
b = int(input("masukkan nilai b:"))

if a > 5 or b < 20:
    print("salah satu kondisi benar")
else:
    print("kondisi salah")


# %% Kasus 3

# Rumus template perulangan:
# for variable in range(start, stop, step):  
#     # code to repeat

for i in range(0, 10, 2):
    print(i)



# %% Kasus 4

# dengan rumus pengkondisian while loop
# code to repeat

import time
for i in range (10, 0, -2):
    print(i)
    time.sleep(2)
print ("happy new year")
# %% Kasus 5
# countdown timer
import time

# step 1: get user input for countdown start
start = int(input("masukkan waktu hitung mundur:"))
# step 2: countdown using a while loop
print ("\n--- Countdown Begins ---")
while start > 0:
    print(start)
    time.sleep(1)
    start -= 1
# step 3: Print Final Message
print ("Countdown Complete!!!")
# %% Kasus 6
# Sistem kasir sederhana

total_belanja = 0
tambah_barang = True

print("=== Selamat Datang Di Toko Fadlan ===")
print("Ketik harga barang untuk mulai")
print("Ketik 'selesai' jika sudah selesai belanja")



# 1. Perulangan untuk memasukan harga barang

while tambah_barang == True:
    nama_barang = input("masukkan nama barang: ")
    # Jika kasir mengetik 'selesai', maka perulaangan berhenti
    if nama_barang.lower() == 'selesai':
        tambah_barang = False
    else:
    # Jika bukan 'selesai', baru minta harga dan hitung total belanja
        harga = int(input(f"masukkan harga {nama_barang} Rp: "))
        total_belanja += harga
        print("Total Belanja Saat Ini: Rp", total_belanja)
        print()
    # tambahkan harga ke total belanja
print(f"\nTotal belanja awal: Rp{total_belanja}")

# 2. Cek status member
status_member = input("apakah punya kartu member?(ya/tidak):")
# 3. Hitung diskon menggunakan logika AND dan OR
if total_belanja >= 100000 and status_member == "ya" :
    diskon = total_belanja * 0.10 #diskon 10%
    print ("Selamat! Anda dapat diskon member sebesar: Rp", diskon)
elif total_belanja >= 200000 and status_member =="ya" :
    diskon = total_belanja * 0.20 #diskon 20%
    print ("Selamat! Anda dapat diskon member sebesar: Rp", diskon)
else:
    diskon = 0
    print("Anda tidak mendapat diskon")

# 4. Tampilkan total bayar setelah diskon
total_bayar = total_belanja - diskon
print(f"Total yang harus dibayar: Rp {int(total_bayar)}")
print("======================")
