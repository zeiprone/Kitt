# PlaySong.py
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

def play_song(file_path):
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File not found - {file_path}")
            return False
            
        # Stop any currently playing music
        pygame.mixer.music.stop()
        
        # Load and play the new song
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Now playing: {file_path}")
        return True
        
    except Exception as e:
        print(f"Error playing song: {e}")
        return False

def stop_current_song():
    try:
        pygame.mixer.music.stop()
        print("Music stopped")
    except:
        pass

def is_playing():
    return pygame.mixer.music.get_busy()

