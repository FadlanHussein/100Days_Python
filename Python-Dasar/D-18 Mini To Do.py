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

# %%
