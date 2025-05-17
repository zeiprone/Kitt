from PlaySong import play_song

def search_songs(songs, search_query):

    search_query = search_query.lower()  # Convert search query to lowercase for case-insensitive comparison
    results = []
    
    for song in songs:
        # Check if the search query matches the song's title or artist
        if search_query in song['title'].lower() or search_query in song['artist'].lower():
            results.append(song)
    
    return results

def display_search_results(results):

    if not results:
        # If no matching songs are found, notify the user
        print("No songs found.")
    else:
        print("\nSearch Results:")
        # Display each song in the results with a numbered list
        for index, song in enumerate(results, start=1):
            print(f"{index}. {song['title']} - {song['artist']}")
        
        # Allow the user to select a song to play
        try:
            choice = int(input("\nEnter the number of the song you want to play (0 to cancel): "))
            
            if choice == 0:
                # User cancels the search
                print("Search cancelled.")
            elif 1 <= choice <= len(results):
                # Play the selected song if the choice is valid
                selected_song = results[choice - 1]
                print(f"\nNow playing: {selected_song['title']} - {selected_song['artist']}")
                play_song(selected_song['file'])  # Call the play_song function to play the song
            else:
                # Handle invalid number inputs
                print("Invalid choice.")
        except ValueError:
            # Handle non-numeric inputs
            print("Please enter a valid number.")
