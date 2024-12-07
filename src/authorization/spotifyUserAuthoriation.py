import os
import spotipy
from flask import Flask, redirect, request
from flask.cli import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

def get_spotify_client():
    load_dotenv()
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
    if not client_id or not client_secret or not redirect_uri:
        raise ValueError("Spotify credentials are missing. Please check your .env file.")

    scope = "playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private"
    sp_oauth = spotipy.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,
                                        scope=scope)
    spot_token = sp_oauth.get_cached_token()

    # If there's no cached token, you'll need to perform the authorization flow
    if not spot_token:
        print("No cached token found. Please authorize the app.")
        # Redirect the user to the authorization URL
        auth_url = sp_oauth.get_authorize_url()
        spot_token = sp_oauth.get_access_token(request.args['code'])
    sp = spotipy.Spotify(auth=spot_token['access_token'])


    return sp
