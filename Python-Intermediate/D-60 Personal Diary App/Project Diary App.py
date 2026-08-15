import os
import getpass
from datetime import datetime
from cryptography.fernet import Fernet

# --- Key Management ---

def generate_key():
    """Generate a new encryption key and save it to secret.key."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Load the encryption key from secret.key. Generate one if not found."""
    if not os.path.exists("secret.key"):
        generate_key()
    return open("secret.key", "rb").read()

# --- Encryption / Decryption ---

def encrypt_text(text):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(text.encode())

def decrypt_text(encrypted_text):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_text).decode()

# --- Authentication ---

def authenticate_user():
    correct_password = "mypassword"  # Setting password
    password = getpass.getpass("Password: ")
    if password == correct_password:
        print("Access Granted")
        return True
    else:
        print("Access Denied")
        return False

# --- Diary Functions ---

ENTRIES_DIR = "entries"

def ensure_entries_dir():
    os.makedirs(ENTRIES_DIR, exist_ok=True)

def create_entry():
    title = input("Enter the title of your diary entry: ")
    date = input("Enter the date of your diary entry (YYYY-MM-DD): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    content = input("Enter the content of your diary entry: ")

    # Encrypt content
    encrypted_content = encrypt_text(content)

    # Save to file
    file_name = f"{title}_{date}.txt"
    file_path = os.path.join(ENTRIES_DIR, file_name)
    with open(file_path, "wb") as file:
        file.write(encrypted_content)

    print(f"Diary entry '{file_name}' created successfully!")

def list_entries():
    ensure_entries_dir()
    entries = [e for e in os.listdir(ENTRIES_DIR) if e.endswith(".txt")]
    if not entries:
        print("No diary entries found.")
    else:
        print("\n--- Diary Entries ---")
        for entry in entries:
            print(f"  - {entry}")
        print("---------------------")

def read_entry():
    list_entries()
    file_name = input("Enter the name of the entry to read: ")
    file_path = os.path.join(ENTRIES_DIR, file_name)

    try:
        with open(file_path, "rb") as file:
            encrypted_content = file.read()
            decrypted_content = decrypt_text(encrypted_content)
            print("\n--- Entry Content ---")
            print(decrypted_content)
            print("---------------------\n")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

# --- Main ---

def main():
    if not authenticate_user():
        return

    ensure_entries_dir()

    while True:
        print("\n--- Personal Diary App ---")
        print("1. Create Entry")
        print("2. List Entries")
        print("3. Read Entry")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_entry()
        elif choice == "2":
            list_entries()
        elif choice == "3":
            read_entry()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()