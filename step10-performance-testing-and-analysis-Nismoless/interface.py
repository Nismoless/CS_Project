from song import Song
class Interface:
    @staticmethod
    def inventory_cl(inventory):
        print("*****************************************")
        print("* Explore Spotify's most streamed songs *")
        print("*****************************************")

        menu_option = 1

        while menu_option != 0:
            print("[0] - Exit")
            print("[1] - Search For Songs")
            print("[2] - Add/Delete/Edit")

            menu_option = int(input("Choose a sub-menu:"))

            if menu_option == 1:

                search_option = 1
                while search_option != 0:
                    print("[0] - back")
                    print("[1] - search by ID")
                    print("[2] - search by track name")
                    print("[3] - search by artist name")
                    print("[4] - search in range of # streams")

                    search_option = int(input("Choose an option:"))
                    
                    # Fabian V. - Option 1: search by ID
                    if search_option == 1:
                        print("Search by ID")
                        user_search_id = int(input("Enter ID Number:")) # User enters an id to search
                        song = inventory.search_by_id(user_search_id) # User's entered id is searched
                        if song: # If the song is found
                            print(song)
                        else: # If the song does not exist
                            print("Song Not Found")
                   
                    # Fabian V. - Option 2: Search by track name
                    elif search_option == 2:
                        track_name = input("Enter track name:")
                        song = inventory.search_by_name(track_name)
                        if song:
                            for songs in song:
                                print(songs)
                        else:
                            print("Song Not Found")

                    # search by artist names - Rob Eusanio
                    elif search_option == 3:
                        artist_name = input("Enter artist name: ")
                        songs = inventory.search_by_artist(artist_name=artist_name) # gets list of songs by arist
                        if songs:
                            for song in songs: # prints all songs by artist
                                print(song)
                        else: # if no songs found
                            print("Songs not found")
                    # search by range of streams - Rob Eusanio
                    elif search_option == 4:
                        streams_lower = int(input("Enter lowest # in range of streams: ")) 
                        streams_upper = int(input("Enter highest # in range of streams: "))
                        songs = inventory.search_by_streams(streams_lower=streams_lower, streams_upper=streams_upper)  # get list of songs by # streams
                        if songs:
                            for song in songs: # prints all songs in range
                                print(song)
                        else: # if no songs in range
                            print("Songs not found")
                    elif search_option != 0:
                        print("Invalid Syntax")
   

            elif menu_option == 2:
                storage_option = 1
                while storage_option != 0:    
                    print("[0] - back")
                    print("[1] - add item")
                    print("[2] - delete item")
                    print("[3] - edit item")
                    #if,elif chain with functions for submenu 2 below here
                    storage_option = int(input("Choose an option: "))    #prompts the user to choose a storage option and converts the input to an integer - Jonathan Cervantes
                    if storage_option == 0:    #Back Option/Invalid Option Handling
                        print("Returning To Main Menu")    #the if statement checks the value and if the value is 0 we go back to the main menu
                    elif storage_option == 1:    #if input is 1 we call add_item from the Interface class
                        track_name = input("Enter Track Name: ")    #promts the user for the track name
                        artist_count = int(input("Enter # of Artists: "))    #prompts the user for # of artists
                        artistnames = []    #sets up a list that can handle varying numbers of artists
                        for i in range (artist_count):    #creates the loop
                            artist_name = input("Enter Artist Name: ")    #prompts the user for the artist/s name
                            artistnames.append(artist_name)    #adds this to the list
                        release_year = int(input("Enter Year Song Was Released: "))    #prompts the user for the year song was released
                        release_month = int(input("Enter Month Song Was Released: "))   #prompts the user for the month song was released
                        in_spotify_chart = int(input("Enter Song Placement In Spotify Charts: "))    #prompts the user for the song placement in spotify charts
                        streams = int(input("Enter # of Streams: "))    #prompts the user for the number of streams and then converts the information to an integer using int()
                        in_apple_charts = int(input("Enter Placement in Apple Charts: "))    #prompts the user for the song placement in apple charts
                        bpm = int(input("Enter Song BPM: "))   #prompts the user for the bpm of the song
                        song_id = int(input("Enter Song ID: "))    #prompts the user for the unique id of the song
                        song = Song(track_name,artistnames,artist_count, streams, in_apple_charts, bpm, release_year, release_month, in_apple_charts, song_id)
                        inventory.add_item(song)
                        #inventory.add_item({'Song ID': song_id, 'Track Name': track_name, 'Artist Name': artistnames, 'Streams': streams, 'Artist Count': artist_count, 'Release Year': release_year, 'Release Month': release_month, 'In Spotify Charts': in_spotify_chart, 'In Apple Charts': in_apple_charts, 'BPM': bpm})    #Creates a new song using the inputs and adds it to the inventory list
        
                        print("Song Added")    #Prints a confirmation statement
 
                    elif storage_option == 2:    #Jonathan Cervantes - if input is 2 we call the delete_item from the Interface class
                        song_id = int(input("Enter Song ID for the Song You Would Like to Delete: "))    #prompts the user for the unique song id for the song they would like to delete
                        song = inventory.delete_song(song_id)    #calls the delete_song function
                        if song:    #checks if song id input holds a value
                            print("Song Deleted")    #if it holds a value the song is deleted
                        else:    #if the song id holds no value or doesnt exist
                            print("Song ID Not Found")    #prints out a statement letting the user know the song id wasnt able to be found
                    
                    elif storage_option == 3:    #Jonathan Cervantes - if input is 3 we call the edit_item from the Interface class
                        song_id = int(input("Enter Song ID for the Song You Would Like to Edit: "))
                        song = inventory.search_by_id(song_id)    #searches inventory for a song based on input id
                        if song:     #loop checks if the song was found                  
                            track_name = input("Enter Track Name: ")    #promts the user for the track name
                            artist_count = int(input("Enter # of Artists: "))    #prompts the user for # of artists
                            artistnames = []    #makes an empty list to store the names
                            for i in range (artist_count):    #starts loop
                                artist_name = input("Enter Artist Name: ")    #prompts the user for the artist/s name
                                artistnames.append(artist_name)    #appends artist_name to artistnames
                            release_year = int(input("Enter Year Song Was Released: "))    #prompts the user for the year song was released
                            release_month = int(input("Enter Month Song Was Released: "))   #prompts the user for the month song was released
                            in_spotify_chart = int(input("Enter Song Placement In Spotify Charts: "))    #prompts the user for the song placement in spotify charts
                            streams = int(input("Enter # of Streams: "))    #prompts the user for the number of streams and then converts the information to an integer using int()
                            in_apple_charts = int(input("Enter Placement in Apple Charts: "))    #prompts the user for the song placement in apple charts
                            bpm = int(input("Enter Song BPM: "))   #prompts the user for the bpm of the song
                            song = Song(track_name,artistnames,artist_count, streams, in_apple_charts, bpm, release_year, release_month, in_apple_charts, song_id)
                            inventory.edit_item({'Song ID': song_id, 'Track Name': track_name, 'Artist Name': artistnames, 'Streams': streams, 'Artist Count': artist_count, 'Release Year': release_year, 'Release Month': release_month, 'In Spotify Charts': in_spotify_chart, 'In Apple Charts': in_apple_charts, 'BPM': bpm})    #Creates a new song using the inputs and adds it to the inventory list
                        else:
                            print("Song ID Not Found")    #prints this message if song id isnt found
                    else:    #if the input doesn't line up with any of the predisposed input values then we print invalid syntax as a form of error handling
                        print("Invalid Syntax")