
def has_expletive(lyrics): #Very strong feeling that this could be optimized further
    for x in lyrics:
       if expletive(x):
           return True
    return False


def expletive(word):
   return word in banned



# List of common banned words by FCC standards

#Two example words one which is banned the other which is not
exWord1 = "hey" 
exWord2 = "shit"
# bad_word: String List-of Strings -> Boolean


lyrics2 = "Hey I just met you and this is crazy bitch"
