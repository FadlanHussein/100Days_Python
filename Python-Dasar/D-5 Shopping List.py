#  %% kasus 1
shopping_list = ["Milk", "Bread", "Eggs"]
shopping_list.extend(["Juice", "Butter"])
shopping_list.insert(1, "Bread")
print(shopping_list[1])
print(shopping_list)
items_to_remove = ["Bread", "Juice", "Milk"]
for item in items_to_remove:
    shopping_list.remove(item)
    print(f"- Saya baru saja membuang list belanjaan {item}") 
# %% kasus 2 Shopping list App
# Step 1: Instalasi kebutuhan list belanja
shopping_list = []

# Step 2: Daftar Fitur Belanja
def show_menu():
    print("\n===== Fitur Belanja =====")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Belanja")
    print("4. Clear Barang")
    print("5. Keluar")

# Step 3: Mesin Utama Program
while True:
    show_menu()
    choice = input("Pilih menu (1-5): ")

    if choice == "3":
        print("\n---- List Belanja Saat Ini ----")
        if not shopping_list:
            print("List Belanja anda masih kosong")
        else:
            # comment: Mencetak item
            for index, item in enumerate(shopping_list):
                print(f"{index+1}. {item}")
    elif choice == "1":
        item = input("Masukkan nama barang: ")
        shopping_list.append(item)
        print(f"{item} berhasil ditambahkan")
    elif choice == "2":
        item = input("Masukkan nama barang yang ingin dihapus: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} berhasil dihapus")
        else:
            print(f"Barang '{item}' tidak ditemukan di daftar belanja")
    elif choice == "4":
        confirm = input("Apakah Anda yakin ingin mengosongkan seluruh daftar belanja? (y/n): ")
        if confirm.lower() == 'y':
            shopping_list.clear()
            print("Seluruh daftar belanja berhasil dibersihkan")
        else:
            print("Batal mengosongkan daftar belanja")
    elif choice == "5":
        print("Terimakasih telah menggunakan aplikasi ini")
        break
    else:
        print("Pilihan tidak valid, silahkan coba lagi")
# %%
