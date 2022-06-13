import random

def randomNumGen(min, max):
    return random.randint(min, max)

CRIT = 1.5
crit = False
success = False

class cast():
    def __init__():
        pass

# offensive
    def magicBolt(chance=False, damage=False): # base mage
        if chance: # 95% success-base
            if randomNumGen(1, 100) <= 95:
                success =  True
            return success
        elif damage: # 5-20 damage
            if randomNumGen(1, 1000) >= 900: # 1 in 10 chance of crit
                crit = True
            if crit:
                return  randomNumGen(5, 20) * CRIT
            else:
                return  randomNumGen(5, 20)

    def fireball(chance=False, damage=False): # pyromancer
        if chance: # 85% success-base
            if randomNumGen(1, 100) <= 85:
                success = True
            return success
        if damage: # 10-30 damage
            if randomNumGen(1, 1000) >= 900: # 1 in 10 chance of crit
                crit = True
            if crit:
                return randomNumGen(10,30) * CRIT
            else:
                return randomNumGen(10,30)

    def meteorShower(chance=False, damage=False): # pyromancer
        pass

    def iceBolt():
        pass

    def lightning():
        pass

# defensive
    def magicShield(chance=False, defence=False): # 100% success-base
        pass

# ally summoning
    def raiseUndead(): # necromancer
        pass


# field modifying
    def convertTundra():
        pass

# enemy manipulation
    def freeze():
        pass