import lyricsgenius
import json
import pandas as pd
from config import SECRET_KEY

df=pd.read_csv('hip_hop_list.csv')
# print(df.head())

genius = lyricsgenius.Genius(SECRET_KEY)
# print(SECRET_KEY)

lyrics = []

for index, row in df.iterrows():
    # print(row['Title'])
    song = genius.search_song(row['Title'], row['Artist'])
    if song is not None:
        # print(song.lyrics)
        # with open(f'{row["Title"]}.txt', 'w') as f:
        #     f.write(song.lyrics)
        song_dict={
            'Title' : row["Title"],
            'Artist': row["Artist"],
            'Year': row["song_release_date"],
            'Lyrics' : song.lyrics
        }
        lyrics.append(song_dict)
    else:
        print(f'The {row["Title"]} is missing')

with open('hipHop_romance_lyrics.json', 'w') as outfile:
    json.dump(lyrics, outfile)

        

# artist = genius.search_artist("Stevie Nicks", max_songs=1, sort="title")

# print(song.lyrics)
