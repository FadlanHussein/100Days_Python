import tkinter as tk
from tkinter import messagebox


# %% Kasus 1: Using Listbox for Dynamic Lists

def case_1():
    root = tk.Tk()
    root.title("Listbox Example")
    root.geometry("300x300")

    listbox = tk.Listbox(root)
    listbox.pack(pady=10)

    listbox.insert(tk.END, "Task 1")
    listbox.insert(tk.END, "Task 2")

    def get_selected():
        selected = listbox.get(tk.ACTIVE)
        print("Selected:", selected)

    button = tk.Button(root, text="Get Selected", command=get_selected)
    button.pack(pady=10)

    root.mainloop()


# %% Kasus 2: Scrollbar Integration

def case_2():
    root = tk.Tk()
    root.title("Listbox with Scrollbar")
    root.geometry("300x300")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=10)
    listbox.pack()

    scrollbar.config(command=listbox.yview)

    for i in range(1, 21):
        listbox.insert(tk.END, f"Item {i}")

    root.mainloop()


# %% Kasus 3: Handling User Actions (Add, Delete, Clear)

def case_3():
    root = tk.Tk()
    root.title("Listbox Management")
    root.geometry("300x300")

    listbox = tk.Listbox(root)
    listbox.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    def add_item():
        item = entry.get()
        if item:
            listbox.insert(tk.END, item)
            entry.delete(0, tk.END)

    def delete_item():
        selected = listbox.curselection()
        if selected:
            listbox.delete(selected[0])

    add_button = tk.Button(root, text="Add Item", command=add_item)
    add_button.pack(pady=5)

    delete_button = tk.Button(root, text="Delete Item", command=delete_item)
    delete_button.pack(pady=5)

    root.mainloop()


# %% Kasus 4: To-Do List GUI

def case_4():
    root = tk.Tk()
    root.title("To-Do List App")
    root.geometry("420x280")
    root.configure(bg="#e3f3fd")

    task_listbox = tk.Listbox(root, height=10, width=35)
    task_listbox.pack(pady=10)

    task_entry = tk.Entry(root, font=("Arial", 12), width=30)
    task_entry.pack(pady=5)

    def add_task():
        task = task_entry.get()
        if task.strip():
            task_listbox.insert(tk.END, task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Task cannot be empty")

    def delete_task():
        selected = task_listbox.curselection()
        if selected:
            task_listbox.delete(selected[0])
        else:
            messagebox.showerror("Error", "Select a task to delete")

    def clear_tasks():
        task_listbox.delete(0, tk.END)

    title_label = tk.Label(root, text="To-Do List", font=("Arial", 24), bg="#e3f3fd")
    title_label.pack(pady=10)

    button_frame = tk.Frame(root, bg="#e3f3fd")
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Arial", 12), bg="#4caf50", fg="white")
    add_button.grid(row=0, column=0, padx=5)

    delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Arial", 12), bg="#e53935", fg="white")
    delete_button.grid(row=0, column=1, padx=5)

    clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks, font=("Arial", 12), bg="#1e88e5", fg="white")
    clear_button.pack(pady=10)

    root.mainloop()


# Jalankan case 4 secara default agar file bisa ditampilkan dan dipahami.
if __name__ == "__main__":
    case_4()
