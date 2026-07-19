# %% Kasus 1 Json Files

import json
import os

# Letak path file json
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir,"..", "0.sample", "json_data.json")

# fungsi untuk membaca data dari file .json

def load_data():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:

# jika file belum ada list kosong
        return []
    except json.JSONDecoderEror:

# Jika file kosong atau format rusak, kembalikan list kosong
        print("Peringatan: File JSON kosong. Memulai dengan data kosong")
        return[]

# Jika untuk menyimpan data ke file JSON

def save_data(data):
    with open(file_path, "w") as file:
        json.dump(data, file,indent=4)

# %% Kasus 2
import json
import os

# Letak path file json
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir,"..", "0.Sample", "json_data.json")

with open(file_path, 'r') as file:
    task = json.load(file)
    print(task)



# %% Kasus 3 Mengolah data ulang
task.append({"task": "Belajar menulis file JSON dengan Python",
    "status": "Incomplete"})
with open(file_path, 'w') as file:
    json.dump(task, file, indent=4)
print("Data berhasil disimpan!")
# %% Kasus 4 Menambahkan sajian data

task.append ({"task": "Memperkaya daya JSON", "status": "succes"})
with open(file_path, 'a') as file:
    json.dump(task, file, indent=4)
print("Data berhasil ditambahkan!!")

# %% Kasus 5
import json
import os
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "0.Sample", "json_data.json")
# Baca file dulu agar variabel 'task' terdefinisi di sel ini
with open(file_path, 'r') as file:
    task = json.load(file)
# Tampilkan data satu per satu
print("--- DAFTAR TUGAS ---")
for item in task:
    print(f"- Tugas: {item['task']} | Status: {item['status']}")

# %% Kasus 6 Mini To-Do App Using JSON

import json
import os

# Tentukan path file secara dinamis agar aman masuk ke folder 0.Sample
base_dir = os.path.dirname(__file__)
TASK_FILE = os.path.join(base_dir, "..", "0.Sample", "D-18_ToDo_App.json")

# Pastikan file tasks terbuat jika belum ada
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, 'w') as file:
        json.dump([], file)  # Harus list kosong [], bukan dictionary kosong {}

# Step 1 : Load Tasks From JSON
def load_tasks():  # Diperbaiki dari load_task menjadi load_tasks
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Step 2 : Save Tasks to JSON
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

# Step 3: Add a new task
def add_task():
    task_name = input("Enter the task name: ").strip()
    tasks = load_tasks()
    tasks.append({"task": task_name, "status": "Incomplete"})
    save_tasks(tasks)
    print(f"Task '{task_name}' added successfully!")

# Step 4: View All Tasks
def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("\n---- To-Do List ----")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['task']} - {task['status']}")
    else:
        print("No task found.")

# Step 5: Update Task Status
def update_status():
    tasks = load_tasks()  # Diperbaiki dari load tasks()
    view_tasks()
    try:
        # Diperbaiki dari '= 1' menjadi '- 1' agar sesuai indeks list Python (0-based)
        task_index = int(input("Enter the task number to update: ")) - 1
        # Diperbaiki dari 'o' (huruf) ke '0' (angka) dan 'task_undex' ke 'task_index'
        if 0 <= task_index < len(tasks):
            new_status = input("Enter the new status (complete/incomplete): ").strip()
            # Diperbaiki dari tasks() ke tasks[] dan tasks_index ke task_index
            tasks[task_index]['status'] = new_status
            save_tasks(tasks)
            print("Task status updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Step 6: Delete a Task
def delete_task():  # Diperbaiki dari delete_tasks menjadi delete_task
    tasks = load_tasks()
    view_tasks()
    try:
        # Diperbaiki dari '= 1' menjadi '- 1'
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Task '{deleted_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Step 7: Display Menu
def display_menu():  # Diperbaiki dari display.menu menjadi display_menu
    print("\n---- Mini To-Do App ----")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update Task status")
    print("4. Delete a task")
    print("5. Exit")

# Step 8: Main Program Loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_status()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")



# %%
