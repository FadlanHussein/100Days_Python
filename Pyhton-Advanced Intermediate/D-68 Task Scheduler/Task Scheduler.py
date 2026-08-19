import os
import json
import tkinter as tk
from tkinter import messagebox


# 1. Helper JSON
def load_tasks(file_path):
    try:
        with open(file_path, 'r') as f:
            task_data = json.load(f)
        return task_data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(tasks, f, indent=2)
    except IOError:
        print(f'Error saving tasks to {file_path}')


# 2. Inisialisasi Data
json_path = os.path.join(os.path.dirname(__file__), 'task.json')
tasks = load_tasks(json_path)

# 3. Inisialisasi Window Utama
root = tk.Tk()
root.title("Task Scheduler")
root.geometry("500x550")
root.resizable(False, False)

# 4. Form Input
form_frame = tk.Frame(root, padx=15, pady=10)
form_frame.pack(fill=tk.X)

title_label = tk.Label(form_frame, text="Task Title:", anchor="w")
title_label.pack(fill=tk.X, pady=(5, 2))
title_entry = tk.Entry(form_frame, font=("Arial", 10))
title_entry.pack(fill=tk.X, pady=(0, 10))

due_date_label = tk.Label(form_frame, text="Due Date (e.g. YYYY-MM-DD):", anchor="w")
due_date_label.pack(fill=tk.X, pady=(0, 2))
due_date_entry = tk.Entry(form_frame, font=("Arial", 10))
due_date_entry.pack(fill=tk.X, pady=(0, 10))

# 5. Listbox & Scrollbar
list_frame = tk.Frame(root, padx=15, pady=5)
list_frame.pack(fill=tk.BOTH, expand=True)

list_label = tk.Label(list_frame, text="Your Tasks:", font=("Arial", 10, "bold"), anchor="w")
list_label.pack(fill=tk.X, pady=(5, 2))

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(list_frame, font=("Arial", 10), yscrollcommand=scrollbar.set, height=10)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=task_listbox.yview)


# 6. Fungsi-Fungsi Aksi
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        is_completed = task.get('Completed', task.get('completed', False))
        status = "[✓]" if is_completed else "[ ]"
        task_display = f"{status} {task['title']} ({task['due_date']})"
        task_listbox.insert(tk.END, task_display)


def add_task():
    title = title_entry.get().strip()
    due_date = due_date_entry.get().strip()

    if not title or not due_date:
        messagebox.showwarning("Warning", "Title and Due Date cannot be empty!")
        return

    tasks.append({
        "title": title,
        "due_date": due_date,
        "Completed": False
    })
    save_tasks(tasks, json_path)
    update_task_list()

    title_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)


def mark_task_completed():
    selected_indices = task_listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("Info", "Please select a task to mark as completed.")
        return

    selected_index = selected_indices[0]
    tasks[selected_index]["Completed"] = True
    save_tasks(tasks, json_path)
    update_task_list()


def delete_task():
    selected_indices = task_listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("Info", "Please select a task to delete.")
        return

    selected_index = selected_indices[0]
    del tasks[selected_index]
    save_tasks(tasks, json_path)
    update_task_list()


# 7. Tombol-Tombol Aksi
add_button = tk.Button(form_frame, text="Add Task", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=add_task)
add_button.pack(fill=tk.X, pady=5)

action_frame = tk.Frame(root, padx=15, pady=10)
action_frame.pack(fill=tk.X)

complete_button = tk.Button(action_frame, text="Mark as Completed", bg="#2196F3", fg="white", font=("Arial", 10), command=mark_task_completed)
complete_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

delete_button = tk.Button(action_frame, text="Delete Task", bg="#f44336", fg="white", font=("Arial", 10), command=delete_task)
delete_button.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(5, 0))

# 8. Load data awal & Mainloop
update_task_list()

if __name__ == "__main__":
    root.mainloop()
