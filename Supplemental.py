import os
import re
from lyricsgenius import Genius
import spotipy
import json
import spotipy.util as util
from dotenv import load_dotenv

load_dotenv()
# Loads unacceptable fcc words into variables
with open('banned.txt') as f:
    banned = f.read().splitlines()
# Genius Properties:
token = os.environ['token']
genius = Genius(token)
# Spotify Properties:
scope = "user-read-currently-playing"
spotifyOAuth = spotipy.SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                    client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                                    redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'],
                                    scope=scope)
spottoken = spotifyOAuth.get_cached_token()
spotifyObject = spotipy.Spotify(auth=spottoken['access_token'])


# Given a spotify link returns the name
def get_lyrics(link):
    track = spotifyObject.track(link)
    title = track['name']
    artist = track['artists'][0]['name']
    lyrics = genius.search_song(title, artist).lyrics
    return lyrics


# Checks if a song has a specifc unacceptable word
def has_expletive(word, lyrics):
    if re.search(r'\b' + word + r'\b', lyrics):
        return True
    return False


# Returns list of unacceptable words
def expletives(lyrics):
    return list((filter(lambda x: has_expletive(x, lyrics), banned)))
