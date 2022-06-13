from character_types import *


class MainCharacter:
    def __init__(self, name, type, gender):
        self.name = name
        self.type = type
        self.gender = gender

    def name(self):
        return self.name()

    def type(self):
        return self.type()

    @staticmethod
    def gold(add=0, subtract=0):
        money = 0
        if add > 0:
            money += add
        elif subtract > 0:
            money -= subtract
        return money

    def spells(self):
        if self.type == 'mage':
            spells =["magic bolt", "magic shield"]
        else:
            spells = []
        return spells