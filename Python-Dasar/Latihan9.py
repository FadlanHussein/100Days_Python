# Project Mini HRIS
import datetime

#Project ini terdiri dari 2 file
FILE_KARYAWAN = "0.Sample/hris_karyawan.txt"
FILE_ABSENSI = "0.Sample/hris_absensi.txt"

#Langkah pertama : membuat menu file
def show_menu():
    print("\n====MINI HRIS PROJECT====")
    print("1. Tambah Karyawan")
    print("2. Lihat Karyawan")
    print("3. Absensi Karyawan")
    print("4. Lihat Absensi Karyawan")
    print("5. Keluar")

#---- Menu 1 ----
def tambahan_karyawan():
    print("\n--- Onboarding Karyawan Baru---")
    nik = input("Masukkan NIK : ")
    name = input("Masukkan Nama Lengkap : ")
    jabatan = input("Masukkan Nama Jabatan : ")
    divisi = input("Masukkan Nama Divisi : ")
    Level = input("Masukkan level jabatan : ")

    master_data = f"{nik}|{name}|{jabatan}|{divisi}|{Level}\n"
    with open(FILE_KARYAWAN, "a") as file:
        file.write(master_data)
        print(f"Data karyawan {name}, {jabatan} telah berhasil ditambahkan")

#---- Menu 2 ----
def lihat_karyawan():
    print("\n--- Daftar Karyawan---")
    try:
        with open(FILE_KARYAWAN, "r") as file:
          karyawan = file.read()
          if karyawan:
            print("\n Daftar Nama Karyawan")
            print(karyawan)
          else:
            print("Belum ada data karyawan")
    except FileNotFoundError:
      print("Data Karyawan Tidak Tersedia")

#---- Menu 3 ----
def catat_absensi():
    print("\n---- Mesin absensi----")
    nik_absen = input("Masukan NIK Anda: ")
    try:
        with open(FILE_KARYAWAN, "r") as file:
            semua_data = file.read()
            if nik_absen in semua_data:
                waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data_absen = f"{nik_absen} | {waktu_sekarang}\n"
                with open (FILE_ABSENSI, "a") as file:
                    file.write(data_absen)
                    print(f"Absensi berhasil dicatat atas {nik_absen} - {waktu_sekarang}")
            else:
                print("NIK belum memiliki absen")
    except FileNotFoundError:
        print("Data NIK Karyawan tidak tersedia")

#---- Menu 4 ----
def lihat_absensi():
    print("\n--- Daftar Absensi Karyawan---")
    try:
        with open(FILE_ABSENSI, "r") as file:
            daftar_absensi = file.read()
            if daftar_absensi:
                print("\n Daftar Absensi Karyawan")
                print(daftar_absensi)
            else:
                print("Belum ada data absensi")
    except FileNotFoundError:
        print("Data Absensi tidak tersedia")

while True:
    show_menu()
    choice = input("Pilih 1-5 : ")
    if choice == "1":
        tambahan_karyawan()
    elif choice == "2":
        lihat_karyawan()
    elif choice == "3":
        catat_absensi()
    elif choice == "4":
        lihat_absensi()
    elif choice == "5":
        print("Terima kasih sudah menggunakan aplikasi mini hris")
        break
    else:
        print("Pilihan tidak valid, silahkan pilih 1 sampai 4")



    


    
     



    
