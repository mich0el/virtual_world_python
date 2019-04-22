import random
from Animal import Animal

class Antelope(Animal):

    def __init__(self, posX, posY, world):
        super().__init__()
        self.myColor = (255, 204, 153)
        self.whoIAm = 'A'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(4)
        self.setInitiative(4)
        self._moveLength = 2

    def defenced(self, enemyObject):
        chance = random.randint(0,100)
        if (chance <= 50):
            return True
        return False