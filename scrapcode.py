
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
import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QObject, Signal, Slot


class Talktomenice(QObject):
    talk = Signal(int)

    def __init__(self, parent=None):
        super().__init__(self, parent)
        self.speak[int].connect(self.say_something)



    @Slot(int)
    def say_something(self, arg):
        if isinstance(arg, int):
            print("Good job you did this right?")
        else:
            print("Wrong")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    someone = Talktomenice()
    someone.speak.emit(10)
  #  someone.speak[str].emit("Hello everybody!")
