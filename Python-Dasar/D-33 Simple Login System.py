import tkinter as tk
from tkinter import messagebox

# Main menu window
root = tk.Tk()
root.title("D-33 Simple Login Examples")
root.geometry("320x320")
root.resizable(False, False)

# Case 1: Message Box examples
def open_message_boxes():
    messagebox.showinfo("Title", "This is an information message", parent=root)
    messagebox.showwarning("Warning", "This is a warning message", parent=root)
    messagebox.showerror("Error", "This is an error message", parent=root)
    response = messagebox.askyesno("Question", "Do you want to continue?", parent=root)
    print("Response:", response)

# Case 2: Validation Example
def open_validation_example():
    win = tk.Toplevel(root)
    win.title("Validation Example")
    win.geometry("300x200")
    win.resizable(False, False)

    tk.Label(win, text="Enter something:").pack(pady=5)
    entry = tk.Entry(win)
    entry.pack(pady=10)

    def validate_input():
        user_input = entry.get()
        if user_input.strip() == "":
            messagebox.showerror("Error", "Input cannot be empty", parent=win)
        else:
            messagebox.showinfo("Success", f"You entered: {user_input}", parent=win)

    tk.Button(win, text="Submit", command=validate_input).pack(pady=10)

# Case 4: Simple Login
def open_simple_login():
    win = tk.Toplevel(root)
    win.title("Simple Login")
    win.geometry("300x200")
    win.resizable(False, False)

    USERNAME = "admin"
    PASSWORD = "12341234"

    tk.Label(win, text="Username:").pack()
    username_entry = tk.Entry(win)
    username_entry.pack()

    tk.Label(win, text="Password:").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username == USERNAME and password == PASSWORD:
            messagebox.showinfo("Login Success", "Welcome, Admin!!", parent=win)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.", parent=win)

    tk.Button(win, text="Login", command=login).pack(pady=10)

# Case 5: Simple Login System
def open_login_system():
    win = tk.Toplevel(root)
    win.title("Simple Login System")
    win.geometry("400x300")
    win.configure(bg="#f0f4c3")
    win.resizable(False, False)

    USER_CREDENTIALS = {
        "admin": "admin123",
        "user": "12341234"
    }

    tk.Label(win, text="Login System", font=("Arial", 20), bg="#f0f4c3").pack(pady=20)
    tk.Label(win, text="Username", font=("Arial", 12), bg="#f0f4c3").pack()
    username_entry = tk.Entry(win, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(win, text="Password:", font=("Arial", 12), bg="#f0f4c3").pack()
    password_entry = tk.Entry(win, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            messagebox.showinfo("Login Success", f"Welcome, {username}!!", parent=win)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password", parent=win)

    def clear():
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    tk.Button(win, text="Login", command=login, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)
    tk.Button(win, text="Clear", command=clear, font=("Arial", 12), bg="#f44336", fg="white").pack(pady=5)
    tk.Button(win, text="Close", command=win.destroy, font=("Arial", 12), bg="#607d8b", fg="white").pack(pady=10)

# Main menu
tk.Label(root, text="Pilih kasus yang ingin dijalankan:", font=("Arial", 12)).pack(pady=15)

tk.Button(root, text="Case 1: Message Boxes", width=30, command=open_message_boxes).pack(pady=5)

tk.Button(root, text="Case 2: Validation Example", width=30, command=open_validation_example).pack(pady=5)

tk.Button(root, text="Case 4: Simple Login", width=30, command=open_simple_login).pack(pady=5)

tk.Button(root, text="Case 5: Simple Login System", width=30, command=open_login_system).pack(pady=5)

tk.Button(root, text="Tutup", width=30, command=root.destroy).pack(pady=15)

root.mainloop()
