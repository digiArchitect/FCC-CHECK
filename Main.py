#Steps!
#                       Part One!
#1. Given a word check whether or not it equals a bad word   
#2. Given a list of lyrics, return whether or not they have certain banned words
#2b. Lyrics in this case is defined as a list of strings
#            _______________________________________________________
#                       Part Two!
#1. Given a word and a list of bad words, return the bad word it is equal too (if applicabble)
#2. Given lyrics and a list of bad words, return all the bad words within the lyrics (if applicable)
#           ________________________________________________________


# List of common banned words by FCC standards
bannedwords = ["shit", "piss", "fuck", "cunt", "cocksucker", "motherfucker", "tits", "weed", "beer", "damn", "bitch"]
#Two example words one which is banned the other which is not
exWord1 = "hey" 
exWord2 = "shit"
# bad_word: String List-of Strings -> Boolean
#Given a word checks whether or not it is a bad word
def expletive(word, banned):
   return word in banned
print("This should return false: " + str(expletive(exWord1, bannedwords))) #returns false
print("This should return true: " + str(expletive(exWord2, bannedwords))) #return true

#Two versions of the same lyrics, one of which contains an expletive and one of which does not
lyrics1 = ['Hey,', 'I', 'just', 'met', 'you', 'and', 'this', 'is', 'crazy']
lyrics2 = ['Hey,', 'I', 'just', 'met', 'you', 'and', 'this', 'is', 'crazy', 'fuck']
#has_expletive: |List-of Strings||List-of Strings| -> Boolean
# Given lyrics and a list of banned words, returns whether or not there are any curse words.
def has_expletive(lyrics, banned):
    for x in lyrics:
       if expletive(x, banned):
           return True
    return False
print("This should return false: " + str(has_expletive(lyrics1,bannedwords))) # Value is false
print("This should return true: " + str(has_expletive(lyrics2,bannedwords))) # Value is true 
    




    
    
