from song import Song
import csv

class InformationRetrievalSystem:
    def __init__(self):
        self.__list_items = []  # TODO: rename the list here 

    # Fabian - load data from csv and populate the list items
    def load_data(self, item_information_file):
        # CSV file needs a CSV reader, and we will use it to implement our functionality
        with open(item_information_file, newline='') as csvfile: 
            reader = csv.reader(csvfile)

            # We want these columns in the csv to be converted from str to int
            columns_to_convert=[2,3,4,5,6,7,8,9]
            
            # This iterates through the csv, allowing us to convert the necessary rows in our original csv
            for index, row in enumerate(reader):
                if index != 0:
                    for col in columns_to_convert:
                        try:
                            row[col]=int(row[col])
                        except ValueError:
                            row=row
                    song = Song(
                    track_name = row[0],
                    #split artists into a list
                    artist_name = row[1].split(','),
                    artist_count = row[2],
                    release_year = row[3],
                    release_month = row[4],
                    in_spotify_chart = row[5],
                    streams = row[6],
                    in_apple_charts = row[7],
                    bpm = row[8],
                    song_id = row[9]
                    )
                    self.__list_items.append(song)
                    
    # Fabian V - Delete song
    def delete_song(self, song_id):
        """Delete song based on unique identifier. Return the updated item object, or None if not found."""
        item = self.search_by_id(song_id)
        if item:
            # print("Song to delete: ", item)
            self.__list_items.remove(item)
            return item
        return None 
                      
    def search_by_id(self, song_id): # Rob Eusanio
        """Return an item object matching the given unique identifier, or None if not found."""
        # finds song with matching id
        for song in self.__list_items:
            if song.song_id == song_id:
                return song
        return None
    
    def search_by_name(self, track_name): # Rob Eusanio
        """Return all songs matching the given song name, or None if not found."""
        song_list = []
        # finds all songs matching name
        for song in self.__list_items:
            if song.track_name == track_name:
                song_list.append(song)
        # return all songs matching name or none
        if len(song_list) > 0:
            return song_list
        return None
    
    def search_by_artist(self, artist_name): # Rob Eusanio
        """Return all songs matching the given artist name, or None if not found."""
        song_list = []
        # find all songs by artist
        for song in self.__list_items:
            if artist_name in song.artist_name:
                song_list.append(song)
        # return all songs by artist or none if empty
        if len(song_list) > 0:
            return song_list
        return None
        
    def search_by_streams(self, streams_lower, streams_upper): # Rob Eusanio
        """Return all songs within the given range of streams, or None if none found."""
        song_list = []
        # find all songs with streams in range
        for song in self.__list_items:
            if song.streams >= streams_lower and song.streams <= streams_upper:
                song_list.append(song)
        # return songs in range or none if empty
        if len(song_list) > 0:
            return song_list
        return None

def edit_item(self, song_id, track_name, artist_name, artist_count, release_year, release_month, in_spotify_chart, streams, in_apple_charts, bpm):#Jonathan Cervantes - Edit
        """Edit item details by unique identifier. Return the updated item object, or None if not found."""
        item = self.search_by_id(song_id) #unique identifier for the song
        if item:
            item.track_name = track_name #name of the song
            item.artist_name = artist_name #name of the artist for the song
            item.artist_count = artist_count #how many artists are on song
            item.release_year = release_year #release year of song
            item.release_month = release_month #release month of song
            item.in_spotify_chart = in_spotify_chart #placement in spotify charts
            item.streams = streams #number of streams
            item.in_apple_charts = in_apple_charts #placement in apple charts
            item.bpm = bpm #beats per minute of the song
            return item #After everything is updated the song gets returned
            
        return None #if item isn't found it returns none
    
def add_item(self, song_id, track_name, artist_name, artist_count, release_year, release_month, in_spotify_chart, streams, in_apple_charts, bpm):#Jonathan Cervantes - Add - Creates a new song object
        """Add item details by unique identifier. Return the updated item object, or None if not found."""#describes what is happening with add song

        item = Song(
            track_name = track_name, #name of the song
            artist_name = artist_name, #name of the artist for the song
            artist_count = artist_count, #how many artists are on song
            release_year = release_year, #release year of song          
            release_month = release_month, #release month of song
            in_spotify_chart = in_spotify_chart, #placement in spotify charts
            streams = streams, #number of streams
            in_apple_charts = in_apple_charts, #placement in apple charts
            bpm = bpm, #beats per minute of the song
            song_id = song_id, #unique identifier for a song
                    )
        return item #returns newly made song object

def save_data(self, item_information_file):#Jonathan Cervantes - Save

        with open(item_information_file,"w", newline='') as csvfile: #Opens the specified file in writer
            writer = csv.writer(csvfile)#Creates the object that will be used to write data to the file
            writer.writerow(["track_name", "artist_names", "artist_count", "release_year", "release_month", "in_spotify_chart", "streams", "in_apple_charts", "bpm", "song_id"])#Creating the header row for the csv collumn names that are for the characteristics of the songs
            for song in self.__list_items:#loops through the song objects that are stored in self._list_items
                artist_names = ",".join(song.artist_name)#Lets us have multiple song artists on one song by combining them to a single string
                writer.writerow([song.track_name, artist_names, str(song.artist_count), str(song.release_year), str(song.release_month), str(song.in_spotify_chart), str(song.streams), str(song.in_apple_charts), str(song.bpm), str(song.song_id)])#writes a row for each song using their characteristics


def __str__(self):
        """Return a string representation of all items in the system."""
        inventory = ""
        for song in self.__list_items:
            inventory += str(song) + "\n"
        return inventory