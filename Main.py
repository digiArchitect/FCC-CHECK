from Supplemental import *

def song():
    song = input("Spotify Song link: ")
    lyrics = get_lyrics(song)
    bad_words = ", ".join(expletives(lyrics))
    if not bad_words:
        return "This song is acceptable on the air waves"
    return f"Due to word(s) {bad_words} this song is unacceptable on the air waves"
print(song())
