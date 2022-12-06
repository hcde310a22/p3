from lyricsgenius import Genius
import json
import csv

key = 'w-59mN-elcgR5fCXv4kxkWNzTk1g5rtbH54OyvxMK7I8BTc6D1lWUJz9_2sT3WKD'

print("Input an artist name: ")

artist_name = input()

genius = Genius(key)
artist = genius.search_artist(artist_name, max_songs=1)
artist.save_lyrics(f"lyrics.json")
print("-----------------------------------------------------------------")
with open(f"lyrics.json") as f:
    data = json.load(f)


print("Input a word/phrase: ")

phrase = input()

songs = data['songs']
lyrics_to_songs = dict()

f = open(f"{artist_name}_{phrase}.csv", "w")

writer = csv.writer(f)

header1 = ["Artist: ", artist_name]
header2 = ["Phrase: ", phrase]

writer.writerow(header1)
writer.writerow(header2)

writer.writerow(["Songs"])


for song in songs:
    lyrics_to_songs[song['lyrics']] = song['full_title']

print("Songs that contain your phrase: ")

i = 1
for lyric in lyrics_to_songs.keys():
    if phrase in lyric:
        song_name = lyrics_to_songs[lyric]
        print(f"    {song_name}")
        writer.writerow([i, song_name])
        i += 1

f.close()