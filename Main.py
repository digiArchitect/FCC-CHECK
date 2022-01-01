from Supplemental import *


def song():
    name = input("Artist: ")
    title = input("Song: ")
    lyrics = get_lyrics(name, title)
    bad_words = ", ".join(expletives(lyrics))
    if not bad_words:
        return "This song is acceptable on the air waves"
    return f"Due to word(s) {bad_words} this song is unacceptable on the air waves"


print(song())
