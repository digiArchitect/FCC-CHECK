import os
from lyricsgenius import Genius
token = os.environ['token']
genius = Genius(token)
def get_lyrics(artist,title):
  lyrics = genius.search_song(title, artist).lyrics
  return lyrics
  

banned = ["shit", "piss", "fuck", "cunt", "cocksucker", "motherfucker", "tits", "weed", "beer", "sake", "damn", "bitch"]
def has_expletive(word,lyrics): #Very strong feeling that this 
  if (lyrics.find(word) == -1):
    return False
  return True 
def expletives(lyrics):
    return(list((filter (lambda x: has_expletive(x,lyrics), banned))))
