# Mini Project Payroll System Sederhana

def show_menu():
    print("\n ----Project Payroll System Sederhana---- ")
    print("1. Masukkan ID & Nama Karyawan")
    print("2. Kalkulasi Gaji Bersih")
    print("3. Hitung bonus performa")
    print("4. Tampilkan Slip Gaji")
    print("5. Keluar")

while True:
    show_menu()
    choice = input ("Pilihlah nomor 1-5 : ")
    if choice == "1":
        try:
            id_karyawan = int(input("Masukkan ID Karywan: "))
            name_karyawan = input("Masukkan Nama Lengkap: ")
            gaji_pokok = int(input("Masukkan Gaji Pokok Karyawan: "))
            print(f">> Data Karyawan {name_karyawan} (ID: {id_karyawan}) telah berhasil ditambahkan")
        except ValueError:
            print("Input tidak valid, Pastikan anda memasukkan angka")
        continue
    if choice == "2":
        try:
            cek = name_karyawan
            gaji = float(input("Masukkan Gaji Pokok: Rp "))
            potongan = float(input("Masukkan persentase potongan (0 - 10): "))
            #potongan custom ini gaboleh minus
            if potongan < 0 or potongan >100:
                raise ValueError("Erro: Persentase potongan harus antara 0 sampai 10 (dalam nilai persentase)")
            nominal_potongan = gaji * (potongan / 100)
            gaji_bersih = gaji - nominal_potongan
            print(f"Gaji Karyawan sebesar: Rp {gaji_bersih}")
        except ValueError as e:
            print(f"Error: {e}")
        except NameError:
            print("Error : Anda harus memasukkan data karyawan terlebih dahulu")
        continue
    if choice == "3":
        try:
            cek = name_karyawan
            total_bonus = float(input("Masukkan Total Bonus Tim: Rp "))
            jumlah_anggota = float(int(input("Jumlah Anggota Tim: ")))
            bonus_per_orang = total_bonus / jumlah_anggota
            print(f"Berikut ini adalah bonus yang didapat oleh {name_karyawan} sebesar Rp {bonus_per_orang}")
        except ZeroDivisionError:
            print("Error: tidak bisa")
        except ValueError:
            print("Bonus harus berupa angka")
        except NameError:
            print("Error : Anda harus memasukkan data karyawan terlebih dahulu")
        continue
    if choice == "4":
        try:
            # Cek semua data wajib sebelum cetak slip
            cek = name_karyawan
            cek_gaji = gaji_bersih
            cek_bonus = bonus_per_orang
            print("\n=== Slip Gaji Karyawan ===")
            print(f" ID         : {id_karyawan}")
            print(f" Nama       : {name_karyawan}")
            print(f" Gaji Pokok : Rp {gaji_pokok}")
            print(f" Gaji Bersih: Rp {gaji_bersih:.2f}")
            print(f" Bonus      : Rp {bonus_per_orang:.2f}")
            print(f" Gaji Total : Rp {gaji_bersih + bonus_per_orang:.2f}")
            print("==========================")
        except NameError:
            print("Error: Data belum lengkap! Isi Menu 1, 2, dan 3 dulu ya bos.")
        continue
    if choice == "5":
        print("Terima kasih sudah menggunakan payroll sistem sederhana")
        break
