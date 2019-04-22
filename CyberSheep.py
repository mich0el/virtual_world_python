import random
from Sheep import Sheep


class CyberSheep(Sheep):
    def __init__(self, posX, posY, world):
        super().__init__(posX, posY, world)
        self.myColor = (0, 0, 255)
        self.myTextColor = (255, 0, 0)
        self.whoIAm = 'C'
        self.setPower(11)

    def newCoordinates(self):
        myTarget = self.targetDetection()
        if (myTarget != None):
            directionX = self.getPosX() - myTarget.getPosX()
            directionY = self.getPosY() - myTarget.getPosY()
            way = random.randint(0, 1)
            if way == 0:
                if directionX != 0:
                    self.setPosX(self.getPosX() + 1) if directionX < 0 else self.setPosX(self.getPosX() - 1)
                else:
                    self.setPosY(self.getPosY() + 1) if directionY < 0 else self.setPosY(self.getPosY() - 1)
            else:
                if directionY != 0:
                    self.setPosY(self.getPosY() + 1) if directionY < 0 else self.setPosY(self.getPosY() - 1)
                else:
                    self.setPosX(self.getPosX() + 1) if directionX < 0 else self.setPosX(self.getPosX() - 1)
        else:
            super().newCoordinates()

    def targetDetection(self):
        target = None
        myPosX = self.getPosX()
        myPosY = self.getPosY()
        minDistance = self._world.getSizeX() * self._world.getSizeY()
        for element in reversed(self._world.listOfOrganisms):
            if element.getInitiative() != 0:
                break;
            if element.whoIAm == 's':
                if element.isDead() == False:
                    distance = abs(myPosX - element.getPosX()) + abs(myPosY - element.getPosY())
                    if distance < minDistance:
                        minDistance = distance
                        target = element
        return target
