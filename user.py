from character_types import *


class MainCharacter:
    def __init__(self, name, class_type, gender):
        self.name = name
        self.class_type = class_type
        self.gender = gender

    def name(self):
        return self.name()

    def classType(self):
        return self.class_type()

    @staticmethod
    def gold(add=0, subtract=0):
        money = 0
        if add > 0:
            money += add
        elif subtract > 0:
            money -= subtract
        return money

    def spells(self):
        if self.class_type == 'mage':
            spells = ["magic bolt", "magic shield"]
        else:
            spells = []
        return spells
