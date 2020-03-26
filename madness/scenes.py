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
        """)
        self.result.append('-APPROACH the cave')
        self.result.append('-SEARCH for another entrance')
        self.result.append('-WAIT until nightfall')

        self.result.append(False)

        return self.result

class FirstFork(Scene):

    def enter(self):
        self.result.append("""
        The light lessens as you descend a steady slope into the depths of the cave.
        You see a fork in the tunnel ahead, but your limited dark vision does not allow
        you to see far down either path ahead of you. Will you:
        """)
        self.result.append('-Take the path on the LEFT')
        self.result.append('-Take the path on the RIGHT')

        self.result.append(False)

        return self.result

class ExteriorApproach(Scene):

    def enter(self):
        self.result.append("""
        You stride boldly towards the cave. As you approach, two GOBLIN GUARDS
        emerge from the darkness. They are chittering in a language that you do not understand,
        but you have seen enough combat to understand the cruel gleam in their eyes.
        You must fight!
        """)

        if randint(1, 100) < 10:
            self.result.append("""
            Somehow, the small goblins with frail, rusted blades and rotting hide armor
            were able to get the better of you. Your last thoughts are of all the people
            at home who you hope never find out that you lost to a couple of measly runts.
            """)
            self.result.append(True)
            return self.result
        else:
            self.result.append("""
            You dispatch the goblins with ease, and you are now free to head deeper
            into the cave.
            """)
            obj = FirstFork()
            more = obj.enter()
            for text in more:
                self.result.append(text)
            return self.result

class ExteriorWait(Scene):

    def enter(self):
        self.result.append("""
        As the sun begins to set, you become aware of the toll your recent journey
        has taken on your body. However, you are in good shape and accustomed to travel,
        so it surprises you slightly when your eyelids grow heavy and begin to droop.
        Too late you realize your mistake: there are Mela flowers growing in the
        undergrowth around you! You recall hearing about these dangerous flowers
        in your youth: their pollen causes intense drowsiness in most mammals.
        You struggle to pull yourself away from the area lest prolonged exposure
        cause an unending slumber. You collapse some thirty feet away in a small
        clearing and drift to sleep...
        """)

        if randint(1,100) < 34:
            self.result.append("""
            You are unlucky. You are discovered in the night by two patrolling
            GOBLIN GUARDS. The only mercy you experience is that the pollen-induced slumber
            prevented you from feeling the sword enter your back. Your adventure is over.
            """)
            self.result.append(True)
            return self.result
        else:
            self.result.append("""
            You are lucky.
            You awaken in the early dawn hours with nothing worse to show for last
            night's misadventure than a stiff back from sleeping on the cold ground.
            You decide that you have no option other than to proceed into the mountain through
            the cave entrance that you saw yesterday. You cautiously approach the low, wide opening.
            As you draw closer to the threshold, you see crude wooden chairs around a small table
            indicating that this area is typically occupied. You are relieved to find no guards
            in the immediate area; you surmise that they must be out on patrol and decide to continue
            deeper into the cave.
            """)
            obj = FirstFork()
            more = obj.enter()
            for text in more:
                self.result.append(text)
            return self.result

class ExteriorSearch(Scene):

    def enter(self):
        self.result.append("""
        You trace a wide, slow path through the local flora surrounding the mountain.
        After several hours of searching, you find yourself back where you started with
        nothing more accomplished than sore feet and dashed hopes. Night approaches...
        """)
        obj = ExteriorWait()
        more = obj.enter()
        for text in more:
            self.result.append(text)
        return self.result

class FirstForkRight(Scene):

    def enter(self):
        self.result.append("""
        You head down the tunnel to the right. After only a few moments of walking,
        you come upon a closed wooden door. The door is locked, but you could try
        to ram it down with your shoulder. Would you like to:
        """)
        self.result.append('-RAM the door')
        self.result.append('-Turn BACK')

        self.result.append(False)

        return self.result

class Pit(Scene):

    def enter(self):
        self.result.append("""
        The rusted bolt on the other side of the door breaks free from the wall
        with a resounding crack as you barrel at full force into the door. The door
        flies open and you fall headlong into the room as your momentum carries you
        forward; however, you quickly realize that the ground won't be able to break
        your fall because there isn't any ground here at all! You are unable to
        stop yourself from being impaled on the spikes at the bottom of the pit trap.
        Your adventure is over.
        """)
        self.result.append(True)
        return self.result

class DoorRam(Scene):

    def enter(self):
        self.result.append("""You ready yourself to ram the door.""")

        if randint(1, 100) < 85:
            self.result.append("""You fail to get the door open. Try AGAIN or go BACK""")
            self.result.append(False)
            return self.result
        else:
            obj = Pit()
            more = obj.enter()
            for text in more:
                self.result.append(text)
            return self.result

class FirstForkLeft(Scene):

    def enter(self):
        self.result.append("You find out the game isn't finished in this direction")
        self.result.append("I guess you're just dead then")
        self.result.append(True)

        return self.result
