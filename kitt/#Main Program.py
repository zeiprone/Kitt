# Import required modules and functions from other files
from ShufflePlay import shuffle_and_play
from IntegrationSongstoApplication import load_songs_from_file, add_song
from PlaySong import play_song, stop_current_song, is_playing
from VoiceControl import VoiceController
import threading

# Global variables
current_song_index = 0
songs = []

def handle_voice_command(command):
    global current_song_index, songs
    
    if not songs:
        voice_controller.speak("Sistemde şarkı bulunamadı")
        return
        
    if command == "play":
        if 0 <= current_song_index < len(songs):
            song = songs[current_song_index]
            voice_controller.speak(f"{song['title']} çalınıyor")
            play_song(song['file'])
        else:
            voice_controller.speak("Çalınacak şarkı bulunamadı")
            
    elif command == "stop":
        stop_current_song()
        voice_controller.speak("Müzik durduruldu")
        
    elif command == "next":
        current_song_index = (current_song_index + 1) % len(songs)
        song = songs[current_song_index]
        voice_controller.speak(f"Sonraki şarkı: {song['title']}")
        play_song(song['file'])
        
    elif command == "previous":
        current_song_index = (current_song_index - 1) % len(songs)
        song = songs[current_song_index]
        voice_controller.speak(f"Önceki şarkı: {song['title']}")
        play_song(song['file'])
        
    elif command == "shuffle":
        voice_controller.speak("Şarkılar karıştırılıyor")
        shuffle_and_play(songs)

# Main function to run the music playback console
def main():
    global songs, voice_controller
    
    # Load existing songs from a file into the application
    songs = load_songs_from_file()
    
    # Initialize voice controller
    voice_controller = VoiceController()
    
    # Start voice control in a separate thread
    voice_thread = threading.Thread(target=voice_controller.start_voice_control, args=(handle_voice_command,))
    voice_thread.daemon = True
    voice_thread.start()
    
    # Main menu loop
    while True:
        # Display the main menu options
        print("\n--- Music Playback Console ---")
        print("1. Add Song to System From Your Computer")
        print("2. View and Play Songs")
        print("3. Shuffle and Play Songs")
        print("4. Stop Current Song")
        print("5. Exit")

        # Get user's choice
        choice = input("Choose an option (1-5): ")

        # Option 1: Add a new song to the system
        if choice == "1":
            try:
                title = input("Enter song title: ")
                artist = input("Enter artist: ")
                album = input("Enter album: ")
                file = input("Enter the song file path: ")
                if add_song(songs, title, artist, album, file):
                    print(f"Song '{title}' has been added successfully!")
                    voice_controller.speak(f"{title} başarıyla eklendi")
            except Exception as e:
                print(f"Error adding song: {e}")
            
        # Option 2: View and play songs
        elif choice == "2":
            if not songs:
                print("\nNo songs available in the system.")
                continue
                
            print("\nAvailable Songs:")
            print("-" * 50)
            for i, song in enumerate(songs, 1):
                print(f"{i}. {song['title']} - {song['artist']}")
                print(f"   Album: {song['album']}")
                print("-" * 50)
            
            while True:
                try:
                    song_choice = input("\nEnter the number of the song you want to play (or 'b' to go back): ")
                    if song_choice.lower() == 'b':
                        break
                    
                    song_index = int(song_choice) - 1
                    if 0 <= song_index < len(songs):
                        current_song_index = song_index
                        selected_song = songs[song_index]
                        print(f"\nPlaying: {selected_song['title']} - {selected_song['artist']}")
                        if play_song(selected_song['file']):
                            # Wait for the song to finish or user input
                            while is_playing():
                                if input("\nPress Enter to stop, 'n' for next song: ").lower() == 'n':
                                    break
                                stop_current_song()
                                break
                    else:
                        print("Invalid song number. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        # Option 3: Shuffle and play songs
        elif choice == "3":
            if not songs:
                print("\nNo songs available to shuffle.")
                continue
            shuffle_and_play(songs)
            
        # Option 4: Stop current song
        elif choice == "4":
            stop_current_song()
            
        # Option 5: Exit the application
        elif choice == "5":
            stop_current_song()
            print("Exiting...")
            break
            
        # Invalid input handling
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
