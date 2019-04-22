import random
from Animal import Animal

class Human(Animal):

    def __init__(self, posX, posY, world):
        super().__init__()
        self.__specialAbilityMoves = 0
        self.myColor = (255, 0, 255)
        self.whoIAm = 'H'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(5)
        self.setInitiative(4)

    def action(self):
        prevPosX = self.getPosX()
        prevPosY = self.getPosY()

        self.newCoordinates()
        if(self.collision(prevPosX, prevPosY) == "DEAD"):
            self._world.setPlayerIsActive(False)

    def newCoordinates(self):		
        worldSizeX = self._world.getSizeX() - 1
        worldSizeY = self._world.getSizeY() - 1
        newPosX = self.getPosX()
        newPosY = self.getPosY()
        newSpareX = newPosX
        newSpareY = newPosY

        if (self.specialAbilityIsActive() == True):
            self.moveLength = 2
        else:
            self.moveLength = 1

        if self._world.direction == "UP":
            newPosY -= self.moveLength
            newSpareY -= 1
        elif self._world.direction == "DOWN":
            newPosY += self.moveLength
            newSpareY += 1
        elif self._world.direction == "LEFT":
            newPosX -= self.moveLength
            newSpareX -= 1
        elif self._world.direction == "RIGHT":
            newPosX += self.moveLength
            newSpareX += 1

        if (newPosX >= 0 and newPosX <= worldSizeX and newPosY >= 0 and newPosY <= worldSizeY):
            self.setPosX(newPosX)
            self.setPosY(newPosY)
        elif (newSpareX >= 0 and newSpareX <= worldSizeX and newSpareY >= 0 and newSpareY <= worldSizeY):
            self.setPosX(newSpareX)
            self.setPosY(newSpareY)
        self.decreaseSpecialAbilityMoves()

    def organismInfo(self):
        return self.whoIAm + " " + str(self.getPosX()) + " " + str(self.getPosY()) + " " + str(self.getPower()) + " " + str(self.getSpecialAbilityMoves()) + "\n"

    def specialAbilityIsActive(self):
        if (self.getSpecialAbilityMoves() >= 8):
            return True
        elif (self.getSpecialAbilityMoves() >= 6):
            val = random.randint(0, 100)
            if (val <= 50):
                return True
        return False

    def turnOnAbility(self):
        if (self.__specialAbilityMoves == 0):
            self.__specialAbilityMoves = 10
            return True
        return False

    def decreaseSpecialAbilityMoves(self):
        if (self.__specialAbilityMoves > 0):
            self.__specialAbilityMoves -= 1
	
    def getSpecialAbilityMoves(self):
        return self.__specialAbilityMoves

    def setSpecialAbilityMoves(self, val):
        self.__specialAbilityMoves = val