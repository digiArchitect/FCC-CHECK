from lyricsgenius import Genius
import os
token = os.environ['token']
genius = Genius(token)
song = genius.search_song("Picking big sean up", "Chief Keef")
lyric = song.lyrics.split()
# List of common banned words by FCC standards
banned = ["shit", "piss", "fuck", "cunt", "cocksucker", "motherfucker", "tits", "weed", "beer", "sake", "damn", "bitch"]
#Two example words one which is banned the other which is not
exWord1 = "hey" 
exWord2 = "shit"
# bad_word: String List-of Strings -> Boolean
#Given a word checks whether or not it is a bad word
def expletive(word):
   return word in banned
#print("This should return false: " + str(expletive(exWord1))) #returns false
#print("This should return true: " + str(expletive(exWord2))) #return true

#Two versions of the same lyrics, one of which contains an expletive and one of which does not
#lyrics1 = ['Hey,', 'I', 'just', 'met', 'you', 'and', 'this', 'is', 'crazy']
#lyrics2 = ['Hey,', 'I', 'just', 'met', 'you', 'and', 'this', 'is', 'crazy', 'fuck']


#list_of_expletives: |List-of Strings|-> |List-of Strings|  
def list_of_expletives(lyrics):
    return(list((filter (lambda x: expletive(x), lyrics))))
print (list_of_expletives(lyric))
#print (list_of_expletives(lyrics1))
#print (list_of_expletives(lyrics2))

#MaybeString:
  #String
  #False
#def checkWords(song):
  
  
  # if (list_of_expletives(lyrics,banned) ==

 # return False





    
    
