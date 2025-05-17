import random
import os
import time
from PlaySong import play_song, stop_current_song, is_playing

def shuffle_and_play(songs):
    if not songs:
        # Notify the user if the song list is empty
        print("Song list is empty!")
        return
    
    # Filter out songs with missing files
    valid_songs = []
    for song in songs:
        if song.get('file') and os.path.exists(song['file']):
            valid_songs.append(song)
        else:
            print(f"Warning: File not found for {song['title']} - {song['artist']}")
    
    if not valid_songs:
        print("No valid songs found to play!")
        return
    
    # Shuffle the songs
    shuffled_songs = valid_songs[:]
    random.shuffle(shuffled_songs)

    print("\nShuffled Songs:")
    # Display the shuffled song list
    for song in shuffled_songs:
        print(f"- {song['title']} - {song['artist']}")  # Print the title and artist of each song
    
    print("\nSongs are playing...")

    try:
        # Play each song in the shuffled list
        for song in shuffled_songs:
            print(f"\nNow Playing: {song['title']} - {song['artist']}")  # Display the current song being played
            if song.get('file'):  # Check if the song has a valid file path
                if play_song(song['file']):
                    # Wait for the song to finish or user input
                    while is_playing():
                        if input("\nPress Enter to skip to next song, 'q' to quit: ").lower() == 'q':
                            stop_current_song()
                            return
                        break
            else:
                print(f"File for {song['title']} is missing!")  # Notify the user if the file is missing

    except KeyboardInterrupt:
        # Gracefully handle when the user interrupts playback
        print("\nSong playback stopped.")
        stop_current_song()
