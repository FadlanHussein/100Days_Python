import os 
import shutil
from datetime import datetime

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def copy_file(source, destination):
    shutil.copy2(source, destination)

def create_backup_directory(base_backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(base_backup_dir, f"backup_{timestamp}")
    os.makedirs(backup_dir, exist_ok=True)
    return backup_dir

def backup_files(source_dir, backup_dir):
    files = list_files(source_dir)
    for file in files:
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(backup_dir, file)
        copy_file(source_path, destination_path)
        print(f"Backuped {source_path} to {destination_path}")
    return files

def write_log(backup_dir, log_file, files):
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
    with open(log_file, "w", encoding="utf-8") as log_f:
        log_f.write(f"Backup created at: {datetime.now()}\n")
        log_f.write(f"Total files: {len(files)}\n\n")
        for file in files:
            log_f.write(f"  - {file}\n")



def main():
    # Pastikan working directory berada di folder script ini
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("Welcome to the Automated Backup Tool!")
    source_dir = input("Enter the source directory: ")
    base_backup_dir = input("Enter the base backup directory: ")
    log_file = input("Enter the log file path: ")

    # Validasi source directory
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    # Buat base_backup_dir jika belum ada
    os.makedirs(base_backup_dir, exist_ok=True)
    
    try:
        backup_dir = create_backup_directory(base_backup_dir)
        files = backup_files(source_dir, backup_dir)
        write_log(backup_dir, log_file, files)
        print(f"Backup completed successfully! Log saved to {log_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()