# %% Kasus 1 Reading data csv
import csv
from pathlib import Path

base_dir = Path(__file__).resolve().parent
csv_path = base_dir.parent/'0.Sample'/'student.csv'
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# %% Kasus 2 Menuliskan kode pada file student.csv

import csv
from pathlib import Path

base_dir = Path(__file__).resolve().parent
csv_path = base_dir.parent/'0.Sample'/'student.csv'
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('Name', 'Math', 'Science', 'English'))
    writer.writerow(('Daisy', 88, 92, 85))
    writer.writerow(('Khuscshie', 90, 75, 75))
    
# %% Kasus 3 Menambahkan line baru

import csv
from pathlib import Path

base_dir = Path(__file__).resolve().parent
csv_path = base_dir.parent/'0.Sample'/'student.csv'

with open(csv_path, 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=(['Name', 'Math', 'Science', 'English']))
    writer.writeheader()
    writer.writerow({'Name': 'Fadlan', 'Math': 98, 'Science': 96, 'English': 95})
    

# %% Kasus 4 Student Report Generator

import csv
from pathlib import Path

base_dir = Path(__file__).resolve().parent
input_path = base_dir.parent/'0.Sample'/'D-17 Input Generator.csv'
output_path -base_dir.parent/'0.Sample'/'D-17 Report Generator.csv'

# Step 1: Read student data anda calculate averages

def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            student_reports = []
            
            for row in reader:
                name = row ['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])
                average = round((math + science + english) / 3, 2)
                status = "Pass" if average >= 60 else "Fail"

                student_reports.append({
                    'Name': name,
                    'Math': math,
                    'Science': science,
                    'English': english,
                    'Average': average,
                    'Status': status,
                })
        

# Step 2: Write processed data to a new CSV
            with open(output_file, 'w', newline ='') as outfile:
                fieldnames = ['Name', 'Math', 'Science', 'English', 'Average', 'Status']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writerheader()
                writer.writerows(student_reports)

                print(f"Student report generated in (output_file) successfully.")

    except.FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
    except KeyError:
        print("Error: Invalid coloumn names in the input file")
    except Exception as e:
        print(f"An error occured: {e}")

# Step 3: Main Program
input_file = 'D-17 Input Generator.csv'
output_file = 'D-17 Report Generator.csv'

process_student_data(input_file, output_file)
