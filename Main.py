from Supplemental import *
def song():
  name = input("Artist: ")
  title = input("Song: ")
  lyrics = get_lyrics(name,title)
  badWords = ", ".join(expletives(lyrics))
  if not badWords:
    return "This song is acceptable on the air waves"

  return f"Due to word(s) {badWords} this song is unacceptable on the air waves"   
   

print (song())








    
    
