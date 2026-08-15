import os

def scan_directory(directory, extensions=('.mp3', '.flac', '.wav', '.m4a', '.aac', '.ogg')):
    music_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                music_files.append(os.path.join(root, file))
                
    return music_files

# Mengambil path folder dummy_music secara tepat & dinamis
base_dir = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(base_dir, "dummy_music")

files = scan_directory(directory)
print(f"Found {len(files)} music files.")

# Tampilkan daftar file yang ditemukan
for f in files:
    print(f"- {os.path.basename(f)}")