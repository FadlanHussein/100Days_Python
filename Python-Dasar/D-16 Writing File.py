from ast import keyword
import os
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir,"..", "0.sample","journal.txt")

# %% Kasus 1 Writting File

with open (file_path,"w") as file:
    file.write("Day 1: Today I Learned about writing files in pyhton. \n")

# %% Kasus 2 Appen File

with open (file_path, "a") as file:
    file.write("Day 2: Today I Learned about Appen files in pyhton. \n")

# %% Kasus 3 try erorr

try: 
    with open("../0.sample", "w") as file:
        file.write("This is a new note")
except PermissionError:
    print("You do not have permission to write to the file.")

# %% Kasus 4 Daily Journal Logger

# Step 1: Define the journal file
JOURNAL_FILE = '0.sample/journal.txt'
# Step 2: Add a new entry
def add_entry():
    entry = input("Silahkan masukan catatan Anda hari ini: ")
    with open(JOURNAL_FILE,"a") as file:
        file.write(entry + '\n')
    print("Anda telah berhasil menambahkan catatan")

# Step 3: View all entries
def view_entries():
    try:
        with open(JOURNAL_FILE, 'r') as file:
            content = file.read()
            if content:
                print("\n---- Your Journal ----")
                print(content)
            else:
                print("Belum ada catatan sebelumnya")
    except FileNotFoundError:
        print("Belum ada file catatan")

# Step 4: Search entries by keryword
def search_entries():
    keyword = input("Masukkan kata kunci pencarian: ")
    try: 
        with open(JOURNAL_FILE,'r') as file:
            content= file.readlines()
            found = False
            print("\n ---- Search Result ----")
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
                if not found:
                    print("No Matching entries found")
    except FileNotFoundError:
        print("No Journal file found. Add an entry first")

# Step 5: Display Menu
def show_menu():
    print("\n===== DAILY JOURNAL MENU =====")
    print("1. Tambah Catatan")
    print("2. Lihat Catatan")
    print("3. Cari Catatan berdasarkan Kata Kunci")
    print("4. Keluar")



# Step 6: Main program Loop
while True:
    show_menu()
    choice = input("Enter Your Choice (1/2/3/4): ")
    if choice == '1':
        add_entry()
    elif choice == '2':
        view_entries()
    elif choice == '3':
        search_entries()
    elif choice == '4':
        print("Exiting the Journal App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# %%
