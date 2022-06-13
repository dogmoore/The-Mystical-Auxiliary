from magic.spells import cast
import yaml
import user


class userInput():
    def __init__(self, arg1):
        self.input = arg1

    def check(self):
        if user.spells.includes(self.input):
            if cast.magicBolt(chance=True):
                return cast.magicBolt(damage=True) # FIXME add crit return
        if self.input.startsWith('travel'):
            return print('TRAVEL')
