import pygame
from abc import ABC, abstractmethod


class Organism(ABC):
    myTextColor = (0, 0, 0)

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, pX, pY):
        pass

    @abstractmethod
    def defenced(self, enemyObject):
        pass

    def drawing(self):
        x0, y0 = self.getPosX() * self._world.SQUARE_SIZE, self.getPosY() * self._world.SQUARE_SIZE
        x1, y1 = x0 + self._world.SQUARE_SIZE, y0 + self._world.SQUARE_SIZE
        pygame.draw.rect(self._world.screen, self.myColor, [x0, y0, x1, y1], 0)


        text = self._world.font.render(self.whoIAm, True, self.myTextColor)
        self._world.screen.blit(text, [x0 + 5, y0 + 3])

    def organismInfo(self):
	    return self.whoIAm + " " + str(self.getPosX()) + " " + str(self.getPosY()) + " " + str(self.getPower()) + "\n"

    def getPower(self):
	    return self.__power

    def setPower(self, power):
        self.__power = power

    def getInitiative(self):
        return self.__initiative

    def setInitiative(self, initiative):
        self.__initiative = initiative

    def getPosX(self):
        return self.__posX

    def setPosX(self, posX):
        self.__posX = posX

    def getPosY(self):
        return self.__posY

    def setPosY(self, posY):
	    self.__posY = posY

    def getJustBorn(self):
	    return self._justBorn

    def setJustBorn(self, boolVal):
    	self._justBorn = boolVal

    def isDead(self):
        if (self._dead == True):
            return True
        return False

    def setIsDead(self, boolVal):
	    self._dead = boolVal
