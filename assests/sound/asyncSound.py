from playsound import playsound


class Sounds:
    def __init__(self):
        pass

    @staticmethod
    async def buttonPush():
        await playsound('mixkit-light-spell-873.wav')