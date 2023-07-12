"""
    Following this tutorial:
        - https://towardsdatascience.com/extracting-song-data-from-the-spotify-api-using-python-b1e79388d50

    To fetch some data from the Spotify API.
    Open the website in Incognito mode to read it as many times as you want.

    Here the steps:
    - Part I: (This article)
    - Part II: EDA and Clustering
    - Part III: Building a Song Recommendation System with Spotify
    - Part IV: Deploying a Spotify Recommendation Model with Flask

    This file takes into account Part I.
"""

# IMPORT PACKAGES
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils import config  # it hosts the credentials for the Spotify API
import pandas as pd
import numpy as np

# VARIABLES


# Authentication - without user login
# All we need are the IDs, client and secret. Then, we can create our "Spotify" object.
client_credentials_manager = SpotifyClientCredentials(
    client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET
)

# Spotipy object
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Extracting Tracks From a Playlist
playlist_link = (
    "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
)

# Split the link in multiple elements (https, //, open...)
playlist_URI = playlist_link.split("/")[-1].split("?")[0]

"""
    Get the uri of each track element inside the list.
    Why: A Uniform Resource Identifier (URI) is a unique sequence of 
    characters that identifies a logical or physical resource used by web technologies.

"""

track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
print("----------")
print("----------")

print(track_uris)
# convert2df = pd.DataFrame.from_dict(test)
# convert2df.to_csv("playlist_tracks.csv", index=False)

"""
    While we're here, we can also extract the name of each track, 
    the name of the album that it belongs to, and the popularity 
    of the track (which we expect to be high in this case — 
    we're looking at the most popular songs globally). 
    From the artist, we can find a genre (though not airtight — 
    artists can make songs in multiple genres), and an artist popularity score.
"""

# convert the for loop in multiple list comprehension
track_uri = [
    track["track"]["uri"] for track in sp.playlist_tracks(playlist_URI)["items"]
]


for track in sp.playlist_tracks(playlist_URI)["items"]:
    # URI
    track_uri = track["track"]["uri"]

    # Track name
    track_name = track["track"]["name"]

    # Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)

    # Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]

    # Album
    album = track["track"]["album"]["name"]

    # Popularity of the track
    track_pop = track["track"]["popularity"]
