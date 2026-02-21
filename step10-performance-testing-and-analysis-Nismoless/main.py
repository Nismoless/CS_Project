from song import Song
from hashdict import HashDict
from irshashdict import IRSystemHashDict
from randomfiles import *
from analysis import *

def test_hashdict():
    #test init
    test_hashdict = HashDict()
    song1 = Song(track_name="test1", artist_name=["test1"], artist_count=1, streams=1, in_apple_charts=1, in_spotify_chart=1, bpm=1, release_year=1, release_month=1, song_id=230950)
    song2 = Song(track_name="test2", artist_name=["test2"], artist_count=1, streams=1, in_apple_charts=1, in_spotify_chart=1, bpm=1, release_year=1, release_month=1, song_id=230952)
    song3 = Song(track_name="test3", artist_name=["test3"], artist_count=1, streams=1, in_apple_charts=1, in_spotify_chart=1, bpm=1, release_year=1, release_month=1, song_id=230951)
    #test set item (_insert)
    test_hashdict[song1.song_id] = song1
    test_hashdict[song2.song_id] = song2
    test_hashdict[song3.song_id] = song3
    print(test_hashdict[song1.song_id])
    #test contains (_find)
    if song1.song_id in test_hashdict:
        print("__contains__ working correctly. item id"  + str(song1.song_id) +  "is found in lldict")
    #test pop (_remove)
    test_hashdict.pop(song1.song_id)
    if song1.song_id not in test_hashdict:
        print("item deleted successfully")

def test_get_item(system):
    system.load_data("spotify-2023-uid.csv")
    song_dict = system._dict_items
    # song1 = Song(track_name="test1", artist_name=["test1"], artist_count=1, streams=1, in_apple_charts=1, in_spotify_chart=1, bpm=1, release_year=1, release_month=1, song_id=230950968451298605)
    # song_dict._sortedlist=[song1]
    # song_dict._size=len(song_dict._sortedlist)
    all_songs = song_dict.values()
    for song in all_songs:
        print(song.track_name)

def test_irsystem(system):
    # Fabian V. - Test load data
    #test load data
    system.load_data("spotify-2023-uid.csv")
    #test search by id
    # print(system.search_by_id(3))
    #test search by track name
    list = system.search_by_name("Crown")
    for song in list:
        print(song)
    #test search by artist
    list = system.search_by_artist("Kendrick Lamar")
    for song in list:
        print(song)
    #test search by streams
    list = system.search_by_streams(1000000, 2000000)
    for song in list:
        print(song)
    #test add item
    song=Song(track_name="test1", artist_name=["test1"], artist_count=1, release_year=1, release_month=1, in_spotify_chart=1, streams=1, in_apple_charts=1, bpm=120, song_id=129070707070979876843)
    system.add_item(song)
    print(system.search_by_id(129070707070979876843))
    #test edit item
    song=Song(track_name="test1", artist_name=["test1"], artist_count=1, release_year=1, release_month=1, in_spotify_chart=1, streams=6, in_apple_charts=1, bpm=120, song_id=129070707070979876843)
    system.edit_item(song._song_id, song)
    print(system.search_by_id(129070707070979876843))
    #test delete item
    system.delete_item(song) 
    if system.search_by_id(129070707070979876843) == None:
        print("deleted successfully")
    #test write back
    system._write_back('spotify-2023-uid.csv')   

if __name__ == "__main__":
    no_queries = 1000
    no_entries = 100000
    file_name = "rand_file_"+str(no_entries)+".csv"
    generate_data_csv(file_name, no_entries)
    song_inventory_analysis(file_name, no_entries, no_entries)
    system = IRSystemHashDict()
    # test_get_item(system)
    #test_hashdict()
    #test_irsystem(system)