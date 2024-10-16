## Some routines for importing into main notebook, for retrieving release
## dates from YouTube for use in lookup and subsequent analysis.

import pandas as pd

from youtubesearchpython import VideosSearch, ResultMode, Video
from tqdm.notebook import tqdm
from bs4 import BeautifulSoup
from datetime import datetime
import pprint as pp
import requests

import re
from googleapiclient.discovery import build

import time

API_KEY = "AIzaSyAgqZ4rPD2b3xADN3208YvfuLacN4s6_uA"
youtube = build('youtube', 'v3', developerKey=API_KEY)

def getUploadDateByAPI(video_id: str):
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    if response["items"]:
        return response["items"][0]["snippet"]["publishedAt"]
    return None

def getUploadDateByScraper(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the upload date in the meta tag
    date = soup.find("meta", itemprop="uploadDate")
    if date:
        return date["content"]
    return None

def getUploadDateByPlugin(url: str):
    info = Video.getInfo(url, mode=ResultMode.json)
    #pp.pprint(info['uploadDate'][:10])
    return info['uploadDate'][:10]

#pp.pprint(spotify_youtube_df_cleaned['url_youtube'])

def getYTDates(df, write_file=False):
    bad_row_indices = []
    
    vid_ids = []
    vid_dates = []
    
    trimmed_df = df.copy()
    trimmed_df['url_youtube'] = trimmed_df['url_youtube'].astype(str)
    
    #print(trimmed_df['url_youtube'])
    #getUploadDate(trimmed_df['url_youtube'])
    
    for i, row in tqdm(trimmed_df.iterrows(), total=trimmed_df.shape[0]):
        try:
            ret = getUploadDateByAPI(row['url_youtube'][-11:])
        except Exception as e:
            print(f"Encountered {type(e)} at {i}")
            continue
        else:
            if(ret == None):
                #print(f"Date retrieval failed at index {i}")
                print(i, end=" ")
                bad_row_indices.append(i)
                continue
            vid_ids.append(row['url_youtube'][-11:])
            
            date_obj = datetime.strptime(ret[:10], "%Y-%m-%d").date()
            vid_dates.append(date_obj)
        #print(row['url_youtube'])
    
    upload_date_lookup_df = pd.DataFrame()
    upload_date_lookup_df['vid_id'] = vid_ids
    upload_date_lookup_df['upload_date'] = vid_dates

    if write_file == True:
        timestr = time.strftime("%Y%m%d-%H%M%S") # add timestamp so no overwrites
        write_file_name = "./debug/upload_date_" + timestr + ".csv"
        upload_date_lookup_df.to_csv(write_file_name)

    return upload_date_lookup_df


def calcIndexLastRetrieved(calc_df, existing_data):
    existing_data_df = pd.read_csv(existing_data)
    #last_row = existing_df.tail(1)

    #vid_id = last_row['vid_id']
    vid_id = str(existing_data_df.iloc[-1]['vid_id'])

    ret_val = None
    
    for i, row in calc_df.iterrows():
        if vid_id in row['url_youtube']:
            ret_val = i
            break

    if ret_val == None:
        return None
        
    return ret_val

#def continueGetYTDates(df, write_file=False):
#    return
    

    
## Previous strategies/APIs attempted
##

'''
## PREVIOUSLY USED IN FOR LOOP
##
try:
    #ret = getUploadDate(row['url_youtube'])
    #ret = getUploadDateScraper(row['url_youtube'])
    ret = getUploadDateAPI(row['url_youtube'][-11:])
except Exception as e:
    print(e, f"at index: {i}")
    continue
else:
    #print(type(ret))
    vid_ids.append(row['url_youtube'][-11:])

    date_obj = datetime.strptime(ret[:10], "%Y-%m-%d").date()
    vid_dates.append(date_obj)
'''

'''
## ATTEMPT AT USING SPOTIPY TO QUERY RELEASE DATES - TIME OUT ERROR 429 ENCOUNTERED SO ABANDONED
##
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tqdm.notebook import tqdm

client_cred_manager = SpotifyClientCredentials(client_id="7f5bc70afe3a40c58dbfb3c303845ccb",
                                               client_secret="revoked")

sp = spotipy.Spotify(client_credentials_manager=client_cred_manager)

spotify_youtube_df['track_id'] = spotify_youtube_df['uri'].apply(lambda s: s.split(':')[-1])
#spotify_youtube_df.head(3)

processed_ids = []
retrieved_dates = []

error_indices = []

def getReleaseDate(track_id):
    #print(f"getting info for {track_id}")
    track_info = sp.track(track_id)
    release_date = track_info['album']['release_date']
    #print(release_date)
    return release_date

tqdm.pandas()

for i, row in tqdm(spotify_youtube_df.iterrows(), total=spotify_youtube_df.shape[0]):
    print(f"processing row {i}: {row['track_id']}")
    date = getReleaseDate(spotify_youtube_df['track_id'][i])
    print(date)
    

# printing to stdout during lookup too slow, progress bar used instead
#spotify_youtube_df['release_date'] = spotify_youtube_df['track_id'].progress_apply(get_release_date)
'''