import os
import shutil

def create_folders(base_path):
    folders = ['Images','Videos','Docs','Music','Others']
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
    return folders

def move_file(file_path, base_path, folder_name):
    target_folder = os.path.join(base_path, folder_name)
    shutil.move(file_path, target_folder)

def get_folder_for_file(file_name):
    file_extentions = {
        'Images': ['.jpg','.jpeg','.png','.gif','.bmp','.svg','.webp'],
        'Videos': ['.mp4','.mkv','.avi','.mov','.flv','.wmv','.webm'],
        'Docs': ['.pdf','.doc','.docx','.txt','.ppt','.pptx','.xls','.xlsx'],
        'Music': ['.mp3','.wav','.aac','.flac','.m4a','.ogg','.wma']   
    }
    ext = os.path.splitext(file_name)[1].lower()
    for folder, extensions in file_extentions.items():
        if ext in extensions:
            return folder
    return "Others"

def organize_files(base_path):
    folders = create_folders(base_path)
    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)
        if os.path.isfile(file_path):
            folder_name = get_folder_for_file(filename)
            move_file(file_path, base_path, folder_name)
    print("Files organized successfully!")

def main():
    print("Welcome to the File Organizer Tool!!")
    base_path = input("Enter the path of the folder to organize: ")
    if not os.path.exists(base_path):
        print("Folder not found!")
        return
    organize_files(base_path)

if __name__ == "__main__":
    main()