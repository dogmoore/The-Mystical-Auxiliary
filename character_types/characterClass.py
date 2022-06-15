class Mage:
    def __init__(self):
        self.className = 'Novice Mage'

    def className(self):
        return self.className

    @staticmethod
    def description():
        desc = 'The Mage class in entrusted with protecting the lands they live on from mystical threats that no one can foresee.'
        stat = 'stats:\npowerful in magic\nfairly weak physically\ndecent speed\nfantastic people person\nnot very stealthy'
        return desc + stat

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
        base_stats = {
            "magic": 150,
            "strength": 50,
            "speed": 70,
            "charisma": 80,
            "stealth": 40
        }
        return base_stats[stat]


class Swordsman:
    def __init__(self):
        self.className = 'Novice Swordsman'

    def className(self):
        return self.className

    @staticmethod
    def desc():
        desc = 'Swordsmen are the protectors of where they live whether it be a small village or the kingdom capital. A few go on to join the Church and become paladins or join the Royal Guard and become Knights or Guards.'
        stat = 'stats:\nWeak in magicka.\nvery strong\ndecent speed\ndecent people person\nnot very stealthy'
        return desc + stat

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
        base_stats = {
            "magic": 10,
            "strength": 150,
            "speed": 70,
            "charisma": 70,
            "stealth": 20
        }
        return base_stats[stat]


class Bowman:
    def __init__(self):
        self.className = 'Bowman'

    def ClassName(self):
        return self.className

    @staticmethod
    def desc():
        desc = ''
        stat = ''
        return desc + stat

    @staticmethod
    def inv():
        inv = []
        return inv

    @staticmethod
    def skills():
        skills = []
        return skills

    @staticmethod
    def stats():
        base_stats = {

        }
        return base_stats

class Rogue:
    def __init__(self):
        self.className = 'Rogue'


class Thief:
    def __init__(self):
        self.className = 'Thief'


class Assassin:
    def __init__(self):
        self.className = 'Assassin'


class Untrained:
    def __init__(self):
        self.className = 'Untrained'
