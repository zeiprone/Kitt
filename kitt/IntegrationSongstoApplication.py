import json
import os

# Save songs to a JSON file
def save_songs_to_file(songs, filename="songs.json"):

    with open(filename, "w") as file:
        json.dump(songs, file, indent=4)  # Write songs to file in JSON format
    print("Songs have been saved to the file.")

# Load songs from a JSON file
def load_songs_from_file(filename="songs.json"):

    try:
        with open(filename, "r") as file:
            songs = json.load(file)  # Read songs from file in JSON format
        return songs
    except FileNotFoundError:
        print("File not found. A new file will be created.")  # Error message if file does not exist
        return []  # Return an empty list if the file is missing

# Function to add a new song
def add_song(songs, title, artist, album, file):
    # Check if file exists
    if not os.path.exists(file):
        print(f"Error: File not found - {file}")
        return False
        
    # Get absolute path of the file
    abs_file_path = os.path.abspath(file)
    
    song_id = len(songs) + 1
    songs.append({
        "id": song_id,
        "title": title,
        "artist": artist,
        "album": album,
        "file": abs_file_path
    })
    save_songs_to_file(songs)
    return True
