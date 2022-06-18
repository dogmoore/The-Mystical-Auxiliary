import yaml
import os
import sys
from assests.sound.asyncSound import Sounds

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

# from character_types.characterClass import *
# from saves.loadSaves import load
# from user import MainCharacter
# from userinput import check

# TODO add color
# TODO add a confirmation when selecting class along with a short description
# TODO finish building out character classes
# TODO add more to Afari.txt for world building
# TODO flags for saving
# TODO enemy health and list
# TODO ally health and list
# TODO saving points(beds?)
# TODO use PyQT for GUI

# FLAGS
# flag 1: intro
starterTownName = 'Fallburn'

validClasses = ['mage', 'swordsman', 'bowman', 'rogue', 'thief', 'assassin', 'untrained']


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Mystical Auxiliary")

        self.setGeometry(500, 300, 800, 500)
        self.startScreen()
        self.setStyleSheet('background-color: #323233')

    def startScreen(self):
        title = QLabel('The Mystical Auxiliary', self)
        title.move(100, 0)  # change to setGeometry
        title.setStyleSheet('color: white')

        cont = QPushButton('Continue', self)
        cont.setStyleSheet('background-color: #4f4f4f')
        cont.move(50, 100)  # change to setGeometry
        cont.clicked.connect(self.ContOnClick)

        new_game = QPushButton('New Game', self)
        new_game.setStyleSheet('background-color: #4f4f4f')
        new_game.move(50, 130)  # change to setGeometry
        new_game.clicked.connect(self.NewGameOnClick)

        load_game = QPushButton('Load Game', self)
        load_game.setStyleSheet('background-color: #4f4f4f')
        load_game.move(50, 160)  # change to setGeometry
        load_game.clicked.connect(self.LoadOnClick)

        footer = QLabel('Programmed by dogmoore', self)
        footer.setStyleSheet('color: #4f4f4f')
        footer.move(300, 400)  # change to setGeometry

    async def NewGameOnClick(self):
        await Sounds.buttonPush()

    async def ContOnClick(self):
        await Sounds.buttonPush()

    async def LoadOnClick(self):
        await Sounds.buttonPush()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
