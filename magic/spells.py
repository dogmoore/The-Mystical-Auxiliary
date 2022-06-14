import random


def randomNumGen(i, x):
    return random.randint(i, x)


CRIT = 1.5
crit = False
success = False


class Cast:
    # offensive
    @staticmethod
    def magicBolt(chance=False, damage=False):  # base mage
        if chance:  # 95% success-base
            if randomNumGen(1, 100) <= 95:
                success = True
            return success
        elif damage:  # 5-20 damage
            if randomNumGen(1, 1000) >= 900:  # 1 in 10 chance of crit
                crit = True
            if crit:
                return randomNumGen(5, 20) * CRIT
            else:
                return randomNumGen(5, 20)

    @staticmethod
    def fireball(chance=False, damage=False):  # pyromancer
        if chance:  # 85% success-base
            if randomNumGen(1, 100) <= 85:
                success = True
            return success
        if damage:  # 10-30 damage
            if randomNumGen(1, 1000) >= 900:  # 1 in 10 chance of crit
                crit = True
            if crit:
                return randomNumGen(10, 30) * CRIT
            else:
                return randomNumGen(10, 30)

    @staticmethod
    def meteorShower(chance=False, damage=False):  # pyromancer
        pass

    @staticmethod
    def iceBolt():
        pass

    @staticmethod
    def lightning():
        pass

    # defensive

    @staticmethod
    def magicShield(chance=False, defence=False):  # 100% success-base
        pass

    # ally summoning

    @staticmethod
    def raiseUndead():  # necromancer
        pass

    # field modifying

    @staticmethod
    def convertTundra():
        pass

    # enemy manipulation

    @staticmethod
    def freeze():
        pass
