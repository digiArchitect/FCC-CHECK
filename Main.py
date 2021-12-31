

#Steps!
#                       Part One!
#1. Given a word check whether or not it equals a bad word done!
#2. Given a list of lyrics, return whether or not they have certain banned words done!
#2b. Lyrics in this case is defined as a list of strings 
#            _______________________________________________________
#                       Part Two!
#1. Given lyrics and a list of bad words, return all the bad words within the lyrics (if applicable) done!
#2. Create an acceptable list of lyrics
#           ______________________________________________________
# Part Three!
#1. Add Genius Capability which fetches lyrics from a song and analyzes if it has unnacetable words
# Part Four!
#1. Add Spotify and Youtube capability 
#2. Takes the song from spotify/youtube, fetches lyrics using part 3 and then produces if its acceptable
# Part Five!
#1. Make this work with playlists

from lyricsgenius import Genius
import os
token = os.environ['token']
genius = Genius(token)
# List of common banned words by FCC standards
banned = ["shit", "piss", "fuck", "cunt", "cocksucker", "motherfucker", "tits", "weed", "beer", "sake", "damn", "bitch"]
#Two example words one which is banned the other which is not
exWord1 = "hey" 
exWord2 = "shit"
# bad_word: String List-of Strings -> Boolean
#Given a word checks whether or not it is a bad word
def expletive(word):
   return word in banned
print("This should return false: " + str(expletive(exWord1))) #returns false
print("This should return true: " + str(expletive(exWord2))) #return true

#Two versions of the same lyrics, one of which contains an expletive and one of which does not
lyrics1 = ['Hey,', 'I', 'just', 'met', 'you', 'and', 'this', 'is', 'crazy']
lyrics2 = ['Hey,', 'I', 'just', 'met', 'you', 'and', 'this', 'is', 'crazy', 'fuck']
#has_expletive: |List-of Strings||List-of Strings| -> Boolean
# Given lyrics and a list of banned words, returns whether or not there are any curse words.
def has_expletive(lyrics): #Very strong feeling that this could be optimized further
    for x in lyrics:
       if expletive(x):
           return True
    return False
print("This should return false: " + str(has_expletive(lyrics1))) # Value is false
print("This should return true: " + str(has_expletive(lyrics2))) # Value is true 
#list_of_expletives: |List-of Strings|-> |List-of Strings|  
def list_of_expletives(lyrics):
    return(list((filter (lambda x: expletive(x), lyrics))))
print (list_of_expletives(lyrics1))
print (list_of_expletives(lyrics2))

#MaybeString:
  #String
  #False
#def checkWords(song): #Returns MaybeString
  
  # if (list_of_expletives(lyrics,banned) ==

 # return False





    
    
