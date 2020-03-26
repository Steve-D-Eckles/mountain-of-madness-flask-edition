from random import randint

class Scene(object):
    def __init__(self):
        self.result = []

    def enter(self):
        self.result.append("Oops, this scene isn't done!")

class MountainExterior(Scene):
    def enter(self):
        self.result.append("""
        You are Otaku Jeff, an adventurer of little renown.
        You have traveled far to the south of your homeland in search of treasure
        and glory. After many days of traveling through flat, boring plains; dank,
        dreadful bogs; and dense, dark forests, you at last arrive at your destination:
        the fabled Mountain of Madness. Inside is said to dwell a powerful sorcerer
        and his ragtag band of minions and deadly beasts. You ready your sword and
        steel yourself for the trials ahead.\n
        """)
        self.result.append("""
        After some observation of the mountain from afar, you notice a small cave
        entrance on its northern face. It's midday, but you don't see any guards from your
        vantage point. Would you like to:
        \t-APPROACH the cave
        \t-SEARCH for another entrance
        \t-WAIT until nightfall
        """)

        return self.result
