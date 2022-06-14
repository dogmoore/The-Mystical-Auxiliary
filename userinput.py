from magic.spells import Cast
import yaml
import user


class UserInput:
    def __init__(self, arg1):
        self.input = arg1

    def check(self):
        if user.spells.includes(self.input):  # FIXME
            if Cast.magicBolt(chance=True):
                return Cast.magicBolt(damage=True)  # FIXME add crit return
        if self.input.startsWith('travel'):
            return print('TRAVEL')
