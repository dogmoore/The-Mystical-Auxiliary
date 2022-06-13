class Mage():
    def __init__(self):
        self.className = 'Novice Mage'

    def className(self):
        return self.className

    @staticmethod
    def description():
        desc = 'The Mage class in entrusted with protecting the lands they live on from mystical threats that no one can foresee\nstats:\npowerful in magic\nfairly weak physically\ndecent speed\nfantastic people person\nnot very stealthy'
        return desc

    @staticmethod
    def inv(selection):
        inv = ["mage robes", "mage boots", "grimoire", "dagger"]
        return inv[selection]

    @staticmethod
    def skills(selection):
        skills = ["magic bolt", "magic shield", "swing dagger", "hide", "run"]
        return skills[selection]

    @staticmethod
    def stats(stat):
        baseStats = {
            "magic": 150,
            "strength": 50,
            "speed": 70,
            "charisma": 80,
            "stealth": 40
        }
        return baseStats[stat]

class Swordsman():
    def __init__(self):
        self.className = 'Novice Swordsman'
    
    def className(self):
        return self.className

    @staticmethod
    def inv(selection):
        inv = ["Plate Armor", "sword", "metal shield", "dagger"]
        return inv[selection]

    @staticmethod
    def skills(selection):
        skills = ["swing sword", "swing dagger", "block", "dodge", "swing sword(heavy)", "hide", "run"]
        return skills[selection]

    @staticmethod
    def stats(stat):
        baseStats = {
            "magic": 10,
            "strength": 150,
            "speed": 70,
            "charisma": 70,
            "stealth": 20
        }
        return baseStats[stat]

class Bowman():
    def __init__(self):
        self.className = 'Bowman'

class Rogue():
    def __init__(self):
        self.className = 'Rogue'

class Theif():
    def __init__(self):
        self.className = 'Theif'

class Assassin():
    def __init__(self):
        self.className = 'Assassin'

class Untrained():
    def __init__(self):
        self.className = 'Untrained'
