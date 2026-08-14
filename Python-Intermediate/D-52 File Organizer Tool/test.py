import os

def create_folders(base_path):
    folders = ['Images','Videos','Docs','Music','Others']
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
    return folders

def organize_files(base_path):
    folders = create_folders(base_path)