import random
from Animal import Animal


class Fox(Animal):
    def __init__(self, posX, posY, world):
        super().__init__()
        self.myColor = (255, 128, 0)
        self.whoIAm = 'F'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(3)
        self.setInitiative(7)

    def newCoordinates(self):
        newPosX = self.getPosX()
        newPosY = self.getPosY()
        moveTo = random.randint(0,3)

        if (moveTo == 0): #up
            if (self.isItSafeForMe(newPosX, newPosY - 1) == True):
                newPosY -= 1
            elif (self.isItSafeForMe(newPosX, newPosY + 1) == True):
                newPosY += 1
            elif (self.isItSafeForMe(newPosX - 1, newPosY) == True):
                newPosX -= 1
            elif (self.isItSafeForMe(newPosX + 1, newPosY) == True):
                newPosX += 1
        elif (moveTo == 1): #down
            if (self.isItSafeForMe(newPosX, newPosY + 1) == True):
                newPosY += 1
            elif (self.isItSafeForMe(newPosX, newPosY - 1) == True):
                newPosY -= 1
            elif (self.isItSafeForMe(newPosX - 1, newPosY) == True):
                newPosX -= 1
            elif (self.isItSafeForMe(newPosX + 1, newPosY) == True):
                newPosX += 1
        elif (moveTo == 2): #left
            if (self.isItSafeForMe(newPosX - 1, newPosY) == True):
                newPosX -= 1
            elif (self.isItSafeForMe(newPosX + 1, newPosY) == True):
                newPosX += 1
            elif (self.isItSafeForMe(newPosX, newPosY - 1) == True):
                newPosY -= 1
            elif (self.isItSafeForMe(newPosX, newPosY + 1) == True):
                newPosY += 1
        elif (moveTo == 3): #right
            if (self.isItSafeForMe(newPosX + 1, newPosY) == True):
                newPosX += 1
            elif (self.isItSafeForMe(newPosX - 1, newPosY) == True):
                newPosX -= 1
            elif (self.isItSafeForMe(newPosX, newPosY - 1) == True):
                newPosY -= 1
            elif (self.isItSafeForMe(newPosX, newPosY + 1) == True):
                newPosY += 1

        self.setPosX(newPosX)
        self.setPosY(newPosY)

    def isItSafeForMe(self, possibleX, possibleY):
        if (possibleX < 0 or possibleY < 0 or possibleX >= self._world.getSizeX() or possibleY >= self._world.getSizeY()):
            return False
        elif (self._world.getBoard()[possibleY][possibleX] != None):
            if (self._world.getBoard()[possibleY][possibleX].getPower() > self.getPower()):
                return False
        return True
