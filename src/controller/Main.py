from src.model.Supplemental import *
import json
def init():


def main():
    print("Hello this is FCC Checker!")
    print("Would you like to check a song or a playlist?")
    option = input("Type S for Song and P for Playlist: ").lower()
    if option == "s":
        track = input("Spotify Song link: ")
        print(song(track))
    elif option == "p":
        tracks = input("Spotify Playlist link: ")
        print(*playlist(tracks), sep='\n')
    else:
        print(f' Error: Unknown option "{option}"')
        main()


def song(track):

    dict = get_values(track)
    title = dict["title"]
    artist = dict["artist"]
    try:
        bad_words = ", ".join(expletives(dict["lyrics"]))
        if not bad_words:
            return f"{title} by {artist} is acceptable on the air waves"
        return f"{title} by {artist} is unacceptable on the air waves due to word(s) {bad_words}"
    except:
        return f"Song is not in Genius Database"

def playlist(plist):
    songs = get_tracks(plist)
    arr = []
    for track in songs:
        arr.append(song(track))
    return arr



main()
