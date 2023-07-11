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
from utils import config # it hosts the credentials for the Spotify API

# VARIABLES


# Authenticating with Spotipy: authenticate without signing
# All we need are the IDs, client and secret. Then, we can create our "Spotify" object.

# Authentication - without user
client_credentials_manager = SpotifyClientCredentials(
    client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
