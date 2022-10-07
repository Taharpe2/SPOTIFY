import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import create_engine
import pandas as pd
import requests
import json
from datetime import datetime
import datetime



USER_ID = " Enter Email Heree   " Spotify username 
TOKEN = "  aaaa " # Spotify API token


# Get Spotify Token from https://developer.spotify.com/console/get-recently-played/
# 


def data_validation(df: pd.DataFrame) -> bool:
    # check if empty
    if df.empty:
        print("No songs Downloaded. Finish Execution")
        return False

    #Check Primary Keys
    if pd.Series(df['played_at']).is_unique:
        pass
    else:
        raise Exception("Primary Key check is in violation")

    #null check
    if df.isnull().values.any():
        raise Exception("Nulls Found")

        
    return True





if __name__ == "__main__":

    headers = {
        "Accept" : "application/json"
        ,"Content-Type" : "application/json"
        ,"Authorization" : "Bearer {token}".format(token=TOKEN)
    }
    # Convert time to Unix timestamp in miliseconds      
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    # Download all songs you've listened to "after yesterday", which means in the last 24 hours      
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = r.json()

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extract data that I want to review

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    # Convert to Pandas Dataframe

    song_dict = {
        "song_name" : song_names,
        "artist_name" : artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps
    }
    
    song_df = pd.DataFrame(song_dict, columns = ["song_name","artist_name","played_at","timestamp"])

    #validate
    if data_validation(song_df):
        print("Data validated, proceed to load")


    


    ##load


        
    engine = sqlalchemy.create_engine('postgresql+psycopg2:username:password@host:port/database' )
    conn = psycopg2.connect( host = "" , database="", user="", password="",port="")
    cursor = conn.cursor()

    sql_query = """
            CREATE TABLE IF NOT EXISTS my_played_tracks(
                song_name VARCHAR(200),
                artist_name VARCHAR(200),
                played_at TIMESTAMPTZ,
                timestamp TIMESTAMPTZ,
                CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
            )
            """

    cursor.execute(sql_query)
    print("Opened database successfully")

    try:
        song_df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database")

    conn.commit()
    conn.close()
    print("Close database successfully")

