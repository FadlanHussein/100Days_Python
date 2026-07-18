# %% Kasus 1 Reading data csv
import csv
from pathlib import Path

base_dir = Path(__file__).resolve().parent
csv_path = base_dir.parent/'0.Sample'/'student.csv'
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

