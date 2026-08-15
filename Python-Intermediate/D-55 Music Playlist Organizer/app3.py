import os

try:
    from mutagen import File
except ImportError:
    File = None

def scan_directory(directory, extensions=('.mp3', '.flac', '.wav', '.m4a', '.aac', '.ogg')):
    music_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                music_files.append(os.path.join(root, file))
                
    return music_files

def extract_metadata(file_path):
    # Default fallback dari nama file (Format: Artist - Title.ext)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    if " - " in base_name:
        parts = base_name.split(" - ", 1)
        fallback_artist = parts[0].strip()
        fallback_title = parts[1].strip()
    else:
        fallback_artist = "Unknown Artist"
        fallback_title = base_name

    fallback_genre = "Unknown Genre"

    try:
        if File is not None:
            audio = File(file_path, easy=True)
            if audio:
                title = audio.get("title", [fallback_title])[0]
                artist = audio.get("artist", [fallback_artist])[0]
                genre = audio.get("genre", [fallback_genre])[0]
                
                return {
                    "title": title,
                    "artist": artist,
                    "genre": genre,
                    "path": file_path
                }
    except Exception as e:
        pass

    # Mengembalikan fallback jika file berupa dummy tanpa header audio asli
    return {
        "title": fallback_title,
        "artist": fallback_artist,
        "genre": fallback_genre,
        "path": file_path
    }

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(base_dir, "dummy_music")
    
    files = scan_directory(directory)
    print(f"Found {len(files)} music files.\n")
    
    for f in files:
        metadata = extract_metadata(f)
        if metadata:
            print(f"Title: {metadata['title']:<25} | Artist: {metadata['artist']:<20} | Genre: {metadata['genre']}")