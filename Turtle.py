import random
from Animal import Animal


class Turtle(Animal):
    def __init__(self, posX, posY, world):
        super().__init__()
        self.myColor = (76, 153, 0)
        self.whoIAm = 'T'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(2)
        self.setInitiative(1)
	
    def action(self):
        chanceOfMove = random.randint(0, 100)
        if (chanceOfMove < 25):
            super().action()

    def defenced(self, enemyObject):
        if (enemyObject.getPower() < 5):
            return True
        return False
