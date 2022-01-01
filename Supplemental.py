import os
from lyricsgenius import Genius
import re
banned = ''
with open('banned.txt') as f:
     banned = f.read().splitlines()
token = os.environ['token']
genius = Genius(token)
def get_lyrics(artist,title):
  lyrics = genius.search_song(title, artist).lyrics
  return lyrics
def has_expletive(word,lyrics): #Very strong feeling that this
  if re.search(r'\b' + word + r'\b', lyrics):
    return True
  return False 
def expletives(lyrics):
    return(list((filter (lambda x: has_expletive(x,lyrics), banned))))

