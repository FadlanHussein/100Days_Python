#%% pyrefly: ignore [missing-import]
file =open("data-latihan8.txt", "r")
file.read()
print(file)
file.close()

#%% Kasus 2 membaca dokumen dari file

with open("../0.Sample/data-latihan8.txt", "r") as file:
    content = file.read()
    print(content)

# %% Kasus 3 mengubah note di dokumen file latihan 8
with open("../0.Sample/data-latihan8.txt", "w") as file:
    file.write(" This is a new note. \n")

# %% Kasus 4 menambahkan note di dokumen file latihan 8
with open("../0.Sample/data-latihan8.txt", "a") as file:
    file.write("  This is a new second update. \n")


# %% Kasus 5 Membuat aplikasi note sederhana
#Langkah pertama : membuat nama file
FILE_NAME = "../0.Sample/Mynotes.txt"
#Langkah kedua : membuat menu
def show_menu():
    print("\n===== APLIKASI NOTES SEDERHANA =====")
    print("1. Tambah Note")
    print("2. Lihat Note")
    print("3. Hapus Note")
    print("4. Keluar")
#Langkah ketiga : Menambahkan catatan
def add_note ():
    note = input ("Ketikan Catatan Anda: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Catatan telah ditambahkan")
#Langkah keempat : Melihat seluruh catatan
def view_note ():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.read()
            if notes:
                print("\n==== DAFTAR CATATAN ===")
                print(notes)
            else:
                print("\n Catatan ditemukan")
    except FileNotFoundError:
        print("\n File tidak ditemukan")
#Langkah kelima menghapus catatan
def delete_note():
    confirm = input("Apakah anda yakin menghapus catatan ini")
    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            pass
        print("Semua catatan telah dihapus")
    else:
        print("Penghapusan dibatalkan")
#Langkah keenam: Main Program Loop
while True:
    show_menu()
    choice = input("Silahkan masukkan pilihan (1-4): ")
    if choice == "1":
        add_note()
    elif choice == "2":
        view_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        print("Keluar dari aplikasi notes sederhana")
        break
    else:
        print("Pilihan tidak valid, silahkan pilih 1 sampai 4")

# %%
