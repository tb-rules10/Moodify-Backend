import json
import random
import pandas as pd
import time

data = pd.read_csv("./Cleaned_Bollywood_dataset.csv")
data2 = pd.read_csv("./NewDataSet.csv")
query = {"1" : "HindiHipHop", "2" : "EnglishHipHop", "3" : "EnglishOld", "4" : "Classical",}

def df_to_json(df,):
    song_list = []
    for i in df.index:
        song_list.append(json.dumps({
            "videoId": df.loc[i, "videoId"],
            "title": df.loc[i, "Song-Name"],
            "thumbnailUrl": df.loc[i, "channelTitle"],
            "channelTitle": df.loc[i, "Singer/Artists"]
        }))
    return song_list


def get_songs_by_emotion(emotion):
    df = data[data["emotion"] == emotion]
    df = df.sample(n=10)
    return df_to_json(df)


def get_daily_mix_playlists(id):
    playlist = dailyMix[int(id)-1]
    return df_to_json(playlist)


def get_albums(id):
    genre = query[id]
    print(genre)
    print(type(genre))
    df = data2[data2["Genre"] == genre]
    df = df.sample(n=25)
    print(df)
    return df_to_json(df)


def update_value():
    while True:
        global dailyMix
        dailyMix = []
        for i in range(6):
            sample = data.sample(n=25, replace=False)
            dailyMix.append(sample)
        print("Daily Playlists Fetched")
        time.sleep(24 * 60 * 60)  

