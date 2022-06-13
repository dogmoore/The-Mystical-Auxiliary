import random

def randomNumGen(min, max):
    return random.randint(min, max)

class cast():
    def __init__():
        pass

    @staticmethod
    def magicBolt(chance=False, damage=False):
        if chance: # 95% success-base
            success = False
            if randomNumGen(1, 100) <= 95:
                success =  True
            return success
        elif damage: # 5-20 damage
            crit = False
            if randomNumGen(1, 1000) >= 900:
                crit = True
            if crit:
                return  randomNumGen(5, 20) * 1.5
            else:
                return  randomNumGen(5, 20)

    @staticmethod
    def magicShield(chance=False, defence=False): # 100% success-base
        pass