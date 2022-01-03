import sys

from PySide6.QtWidgets import QApplication, QPushButton, QLabel
from PySide6.QtCore import Slot


from Supplemental import *
import sys
import os
from PySide6.QtWidgets import QApplication,  QMainWindow
    #, QWidget, QPushButton, QMessageBox, QLabel,
from design import Ui_MainWindow





def run():
    print("Swag")
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()

    sys.exit(app.exec())



if __name__ == '__main__':
    run()

def song():
    name = input("Artist: ")
    title = input("Song: ")
    lyrics = get_lyrics(name, title)
    bad_words = ", ".join(expletives(lyrics))
    if not bad_words:
        return "This song is acceptable on the air waves"
    return f"Due to word(s) {bad_words} this song is unacceptable on the air waves"


print(song())
