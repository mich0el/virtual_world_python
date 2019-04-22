import random
from Organism import Organism


class Plant(Organism):
    def __init__(self):
        self.setInitiative(0)
        self._justBorn = False
        self._dead = False

    def action(self):
        CHANCE_OF_SPREAD = 5
        chance = random.randint(0,100)
        if (chance <= CHANCE_OF_SPREAD):
            spreadTo = random.randint(0,3)
            if (spreadTo == 0): #up
                if (self.isItFreeSquare(self.getPosX(), self.getPosY() - 1) == True):
                    self.addNewPlant(self.whoIAm, self.getPosX(), self.getPosY() - 1)
                else:
                    if (self.isItFreeSquare(self.getPosX(), self.getPosY() + 1) == True):
                        self.addNewPlant(self.whoIAm, self.getPosX(), self.getPosY() + 1)
                    else:
                        if (self.isItFreeSquare(self.getPosX() - 1, self.getPosY()) == True):
                            self.addNewPlant(self.whoIAm, self.getPosX() - 1, self.getPosY())
                        else:
                            if (self.isItFreeSquare(self.getPosX() + 1, self.getPosY()) == True):
                                self.addNewPlant(self.whoIAm, self.getPosX() + 1, self.getPosY())
            elif (spreadTo == 1): #down
                if (self.isItFreeSquare(self.getPosX(), self.getPosY() + 1) == True):
                    self.addNewPlant(self.whoIAm, self.getPosX(), self.getPosY() + 1)
                else:
                    if (self.isItFreeSquare(self.getPosX(), self.getPosY() - 1) == True):
                        self.addNewPlant(self.whoIAm, self.getPosX(), self.getPosY() - 1)
                    else:
                        if (self.isItFreeSquare(self.getPosX() - 1, self.getPosY()) == True):
                            self.addNewPlant(self.whoIAm, self.getPosX() - 1, self.getPosY())
                        else:
                            if (self.isItFreeSquare(self.getPosX() + 1, self.getPosY()) == True):
                                self.addNewPlant(self.whoIAm, self.getPosX() + 1, self.getPosY())
            elif (spreadTo == 2): #left
                if (self.isItFreeSquare(self.getPosX() - 1, self.getPosY()) == True):
                    self.addNewPlant(self.whoIAm, self.getPosX() - 1, self.getPosY())
                else:
                    if (self.isItFreeSquare(self.getPosX() + 1, self.getPosY()) == True):
                        self.addNewPlant(self.whoIAm, self.getPosX() + 1, self.getPosY())
                    else:
                        if (self.isItFreeSquare(self.getPosX(), self.getPosY() - 1) == True):
                            self.addNewPlant(self.whoIAm, self.getPosX(), self.getPosY() - 1)
                        else:
                            if (self.isItFreeSquare(self.getPosX(), self.getPosY() + 1) == True):
                                self.addNewPlant(self.whoIAm, self.getPosX(), self.getPosY() + 1)
            elif (spreadTo == 3): #right
                if (self.isItFreeSquare(self.getPosX() + 1, self.getPosY()) == True):
                    self.addNewPlant(self.whoIAm, self.getPosX() + 1, self.getPosY())
                else:
                    if (self.isItFreeSquare(self.getPosX() - 1, self.getPosY()) == True):
                        self.addNewPlant(self.whoIAm, self.getPosX() - 1, self.getPosY())
                    else:
                        if (self.isItFreeSquare(self.getPosX(), self.getPosY() + 1) == True):
                            self.addNewPlant(self.whoIAm, self.getPosX(), self.getPosY() + 1)
                        else:
                            if (self.isItFreeSquare(self.getPosX(), self.getPosY() - 1) == True):
                                self.addNewPlant(self.whoIAm, self.getPosX(), self.getPosY() - 1)

    def collision(self, pX, pY):
        return None

    def defenced(self, enemyObject):
        return False

    def isItFreeSquare(self, x, y):
        boardSizeX = self._world.getSizeX() - 1
        boardSizeY = self._world.getSizeY() - 1
        if (x < 0 or x > boardSizeX or y < 0 or y > boardSizeY):
            return False
        if (self._world.getBoard()[y][x] != None):
            return False
        return True

    def addNewPlant(self, type, x, y):
        newPlant = self._world.returnMyBrother(type, x, y)
        newPlant.setJustBorn(True)
        self._world.getBoard()[newPlant.getPosY()][newPlant.getPosX()] = newPlant
        self._world.listOfOrganisms.append(newPlant)
