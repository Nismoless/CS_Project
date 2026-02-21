import random
import os
import csv

def generate_data_csv(rand_file_name, no_entries):
  # rand_file_name: the name of the random 
  # no_entries: the number of entries in the file
  
  file_name = "temp.csv" # temp file to hold the generated entries
  with open(file_name, 'w', encoding='UTF8') as f:
    writefile = csv.writer(f)
    for i in range(1, no_entries+1):
        track_name = "track name"+str(i)
        artist_name = "artist name" 
        artist_count = 1
        release_year = 1
        release_month = 1
        in_spotify_chart = 1
        streams = 1
        in_apple_charts = 1
        bpm = 1
        song_id = str(i)
        row = [track_name, artist_name, artist_count, release_year, release_month, in_spotify_chart, streams, in_apple_charts, bpm, song_id]
        writefile.writerow(row)
   
  # randmize the entries in the file
  with open(file_name,'r') as source:
    csvreader = csv.reader(source)
    data = [ (random.random(), line) for line in csvreader ]
  data.sort()
  with open(rand_file_name,'w') as csvfile:
    writefile = csv.writer(csvfile)
    for _, line in data:
        writefile.writerow(line)

  # removing the temp file, not needed anymore
  os.remove(file_name)