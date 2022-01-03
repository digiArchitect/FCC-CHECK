from Supplemental import *
def main():
    print("Hello this is FCC Checker!")
    print("Would you like to check a song or a playlist?")
    option = input("Type S for Song and P for Playlist: ").lower()
    if option == "s":
        print(song())
    elif option == "p":
        print(playlist())
    else:
        print(f' Error: Unknown option "{option}"')


def song():
    song = input("Spotify Song link: ")
    dict = get_values(song)
    title = dict["title"]
    artist = dict["artist"]
    bad_words = ", ".join(expletives(dict["lyrics"]))
    if not bad_words:
        return f"{title} by {artist} is acceptable on the air waves"
    return f"{title} by {artist}  is unacceptable on the air waves due to word(s) {bad_words}"

def playlist():
    print("hey this is here!")
main()
