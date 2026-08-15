import os
import shutil
import json
from mutagen import File

def scan_directory(directory, extensions=('.mp3', '.flac', '.wav', '.m4a', '.aac', '.ogg')):
    music_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                music_files.append(os.path.join(root, file))
    return music_files

def extract_metadata(file_path):
    # Ekstraksi fallback dari nama file (Format: Artist - Title.ext)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    fallback_artist = base_name.split(" - ")[0].strip() if " - " in base_name else "Unknown Artist"
    fallback_title = base_name.split(" - ")[1].strip() if " - " in base_name else base_name

    try:
        audio = File(file_path, easy=True)
        if audio:
            return {
                "title": audio.get("title", [fallback_title])[0],
                "artist": audio.get("artist", [fallback_artist])[0],
                "album": audio.get("album", ["Unknown Album"])[0],
                "genre": audio.get("genre", ["Unknown Genre"])[0]
            }
    except Exception:
        pass

    # Fallback jika file audio berupa dummy / tidak memiliki tag ID3
    return {
        "title": fallback_title,
        "artist": fallback_artist,
        "album": "Unknown Album",
        "genre": "Unknown Genre"
    }

def organize_files(music_files, output_directory):
    moved_files = []
    for file in music_files:
        metadata = extract_metadata(file)
        if metadata:
            artist = metadata["artist"]
            album = metadata["album"]

            # Define the destination folder: output_directory/artist/album/
            artist_folder = os.path.join(output_directory, artist)
            album_folder = os.path.join(artist_folder, album)

            # Create the directories if they don't exist
            os.makedirs(album_folder, exist_ok=True)

            # Move the file
            destination = os.path.join(album_folder, os.path.basename(file))
            shutil.move(file, destination)
            print(f"Moved: {file} -> {destination}")

            metadata["path"] = destination
            moved_files.append(metadata)

    return moved_files

def save_summary_to_json(music_metadata_list, output_json_file):
    with open(output_json_file, 'w', encoding='utf-8') as f:
        json.dump(music_metadata_list, f, indent=4)
    print(f"\nSummary saved to: {output_json_file}")

def main():
    print("Welcome to the Music Playlist Organizer!")
    
    # Path default jika ditekan Enter langsung
    base_dir = os.path.dirname(os.path.abspath(__file__))
    default_input = os.path.join(base_dir, "dummy_music")
    default_output = os.path.join(base_dir, "Organized_Music")

    music_directory = input(f"Enter the path to your music directory (default: dummy_music): ").strip() or default_input
    output_directory = input(f"Enter the path for the organized music directory (default: Organized_Music): ").strip() or default_output

    if not os.path.exists(music_directory):
        print(f"Directory '{music_directory}' not found!")
        return

    music_files = scan_directory(music_directory)
    if not music_files:
        print("No music files found.")
        return

    print(f"\nFound {len(music_files)} music files.")
    
    organized_data = organize_files(music_files, output_directory)
    json_path = os.path.join(output_directory, "music_summary.json")
    save_summary_to_json(organized_data, json_path)
    
    print("Music organization complete!")

if __name__ == '__main__':
    main()
