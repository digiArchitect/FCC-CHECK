# Code that I had originally used but found no longer useful
#has_expletive: |List-of Strings||List-of Strings| -> Boolean
# Given lyrics and a list of banned words, returns whether or not there are any curse words.
def has_expletive(lyrics): #Very strong feeling that this could be optimized further
    for x in lyrics:
       if expletive(x):
           return True
    return False
#print("This should return false: " + str(has_expletive(lyrics1))) # Value is false
#print("This should return true: " + str(has_expletive(lyrics2))) # Value is true 