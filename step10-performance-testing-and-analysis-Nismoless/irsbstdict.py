from song import Song  
import csv
from irsystemabs import IRSystemAbstract
from bstdict import BSTDict, _BSTNode


class IRSystemBST(IRSystemAbstract):
    def __init__(self):
        self._dict_items = BSTDict()  

   
    def search_by_id(self, item_id): # Rob Eusanio (given)
        """Return an item object matching the given unique identifier, or None if not found."""
        if item_id in self._dict_items:  # searching through the dictionary using the magic method
            return self._dict_items[item_id]
        return None

    def search_by_name(self, track_name): # Rob Eusanio
        """Return all songs matching the given song name, or None if not found."""
        all_songs = self._dict_items.values()
        song_list = []
        # finds all songs matching name
        for song in all_songs:
            if song.track_name == track_name:
                song_list.append(song)
        # return all songs matching name or none
        if len(song_list) > 0:
            return song_list
        return None
    
    def search_by_artist(self, artist_name): # Rob Eusanio
        """Return all songs matching the given artist name, or None if not found."""
        # stores all values from bst in list
        all_songs = self._dict_items.values()
        song_list = []
        # find all songs by artist
        for song in all_songs:
            if artist_name in song.artist_name:
                song_list.append(song)
        # return all songs by artist or none if empty
        if len(song_list) > 0:
            return song_list
        return None
        
    def search_by_streams(self, streams_lower, streams_upper): # Rob Eusanio
        """Return all songs within the given range of streams, or None if none found."""
        all_songs = self._dict_items.values()
        song_list = []
        # find all songs with streams in range
        for song in all_songs:
            if song.streams >= streams_lower and song.streams <= streams_upper:
                song_list.append(song)
        # return songs in range or none if empty
        if len(song_list) > 0:
            return song_list
        return None
    
    #Fabian V. - Load data from csv into Dictionary
    def load_data(self, item_information_file):
        """Load item data from a file and populate the item list."""
        with open(item_information_file, mode ='r')as file:
                reader = csv.reader(file)
                columns_to_convert=[2,3,4,5,6,7,8,9]
                # This iterates through the csv, allowing us to convert the necessary rows in our original csv

                for index, row in enumerate(reader):
                    if index != 0:
                        for col in columns_to_convert:
                            try:
                                row[col]=int(row[col])
                            except ValueError:
                                row = row
                        song = Song()
                        song.track_name = row[0]
                        song.artist_name = row[1].split(',') # split artists into a list
                        song.artist_count = row[2]
                        song.release_year = row[3]
                        song.release_month = row[4]
                        song.in_spotify_chart = row[5]
                        song.streams = row[6]
                        song.in_apple_charts = row[7]
                        song.bpm = row[8]
                        song.song_id = row[9]
                        print(song)
                        self._dict_items[song.song_id] = song

    #Fabian V. - Delete Item functionality
    def delete_item(self, song): # delete_item abstract method, parameters are self and song
            song_name = song.track_name # We get the track name before the song is deleted
            key = song.song_id # Here we set the key equal to the song's id, which was just passed in as an argument
            if key in self._dict_items: # If the key exists in _dict_items
                self._dict_items.pop(key) # We will use the bstdict pop method, which takes the key we just created
                print(f"{song_name} deleted") # Alert the user that the song was deleted
            else:
                print(f"Song with ID {key} not found") # Let user know the song was not found

    def add_item(self, song):#Jonathan Cervantes - Add Item/Node
        key=song.song_id#the id of the song is taken and stored as a variable
        self._dict_items[key]=song #If the key/identifier exists then the song that corresponds with the input key in self.dict_items is updated
        return song#Returns the song object that was added to the BST
    
    def edit_item(self, key, song):#Jonathan Cervantes - Edit Item
            if key not in self._dict_items:#checks if the key/identifier exists
                raise KeyError("Song With Given ID Does Not Exist")#Error Message in case it doesn't exist
            self.dict_items[key]=song#If the key/identifier exists then the song that corresponds with the input key in self.dict_items is updated

    def _write_back(self, item_information_file):#Jonathan Cervantes - Writes Song Data from a BST to a CSV
        with open(item_information_file,"w", newline='') as csvfile:#Used "w" for write mode to be opened
            writer = csv.writer(csvfile)#Writes rows to the new file
            songlist=self._dict_items.values()
            for song in songlist:
                artist_names = ",".join(song.artist_name)#Lets us have multiple song artists on one song by combining them to a single string
                writer.writerow([song.track_name, artist_names, str(song.artist_count), str(song.release_year), str(song.release_month), str(song.in_spotify_chart), str(song.streams), str(song.in_apple_charts), str(song.bpm), str(song.song_id)])#writes a row for each song using their characteristics

    def __str__(self):
        all_songs = self._dict_items.values
        for song in all_songs:
            print(song)