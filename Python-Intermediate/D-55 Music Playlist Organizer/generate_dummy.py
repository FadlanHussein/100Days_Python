import os

# Daftar dummy file musik dengan format: (Nama File, Genre/Kategori perkiraan)
dummy_music_files = [
    # Format: Artist - Title (Genre)
    "Queen - Bohemian Rhapsody.mp3",
    "Michael Jackson - Billie Jean.mp3",
    "Coldplay - Yellow.mp3",
    "Coldplay - Viva La Vida.wav",
    "Taylor Swift - Blank Space.mp3",
    "Taylor Swift - Love Story.flac",
    "Avicii - Wake Me Up.mp3",
    "Martin Garrix - Animals.mp3",
    "Eminem - Lose Yourself.mp3",
    "Beethoven - Symphony No. 5.wav",
    "Mozart - Fur Elise.flac",
    "Sheila On 7 - Dan.mp3",
    "Peterpan - Ada Apa Denganmu.mp3",
    "Tulus - Hati-Hati di Jalan.m4a",
    "Pamungkas - To the Bone.mp3",
    "Unknown - Audio Track 01.aac",
    "Lofi Hip Hop - Chill Beats.ogg",
    "sample_podcast_episode_1.mp3"
]

def generate_dummy_files(target_dir="dummy_music"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(base_dir, target_dir)
    
    os.makedirs(folder_path, exist_ok=True)
    
    for filename in dummy_music_files:
        file_path = os.path.join(folder_path, filename)
        # Buat file kosong (dummy)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Dummy audio content for {filename}")
            
    print(f"[OK] Berhasil membuat {len(dummy_music_files)} dummy file musik di folder: '{target_dir}'")

if __name__ == "__main__":
    generate_dummy_files()
