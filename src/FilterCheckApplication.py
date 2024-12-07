from flask import Flask
from authorization.spotifyUserAuthoriation import get_spotify_client

app = Flask(__name__)

@app.route("/")
def hello_world():
    sp = get_spotify_client()
    print(sp.current_user())
    return "<p>Hello</p>" # + sp.current_user()