import os
import re
from lyricsgenius import Genius
import spotipy
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
# util.prompt_for_user_token("quotethehero",
#                            scope,
#                            client_id=os.environ['SPOTIPY_CLIENT_ID'],
#                            client_secret='your-spotify-client-secret',
#                            redirect_uri='your-app-redirect-url')


# Given a spotify link returns the name

def get_values(link, lyrics=None):
    track = spotifyObject.track(link)
    title = track['name']
    artist = track['artists'][0]['name']
    try:
        dict = {
            "title": title,
            "artist": artist,
            "lyrics": genius.search_song(title, artist).lyrics

        }
        return dict
    except:
        # If song has no lyrics or is not in the genius database, then return no lyrics value
        dict = {
            "title": title,
            "artist": artist
        }
        return dict


def get_tracks(link):
    tracks = spotifyObject.playlist(link)
    items = tracks["tracks"]["items"]
    arr = []
    for item in items:
        item = item["track"]["uri"]
        arr.append(item)

    return arr

# playlist_name = f"Samples in {album_title} by {album_artist}"
# sp.user_playlist_create(username, name=playlist_name)



# Checks if a song has a specifc unacceptable word
def has_expletive(word, lyrics):
    if re.search(r'\b' + word + r'\b', lyrics):
        return True
    return False


# Returns list of unacceptable words
def expletives(lyrics):
    return list((filter(lambda x: has_expletive(x, lyrics), banned)))
