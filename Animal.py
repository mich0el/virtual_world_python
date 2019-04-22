import random
from Organism import Organism


class Animal(Organism):
    def __init__(self):
        self._moveLength = 1
        self._justBorn = False
        self._dead = False
   
    def action(self):
        prevPosX = self.getPosX()
        prevPosY = self.getPosY()

        self.newCoordinates()
        self.collision(prevPosX, prevPosY)

    def collision(self, pX, pY):
        currentX = self.getPosX()
        currentY = self.getPosY()

        if (currentX == pX and currentY == pY):
            return "NO_CHANGES"
        elif (self._world.getBoard()[self.getPosY()][self.getPosX()] == None):
            self._world.getBoard()[pY][pX] = None
            self._world.getBoard()[self.getPosY()][self.getPosX()] = self
            return "MOVE_TO_NULL"
        
        if (self._world.getBoard()[self.getPosY()][self.getPosX()].whoIAm == self.whoIAm):
            self.setPosX(pX)
            self.setPosY(pY)
            if (self.makeNewChild() == True):
                tmp = self.whoIAm + " was born"
                self._world.commentList.append(tmp)
                return "NEW_CHILD"
            else:
                return "NO_NEW_CHILD"

        if (self._world.getBoard()[self.getPosY()][self.getPosX()].defenced(self) == True):
            if (self._world.getBoard()[self.getPosY()][self.getPosX()].whoIAm == 'T'):
                self.setPosX(pX)
                self.setPosY(pY)
                tmp = "T avaded from " + self.whoIAm
                self._world.commentList.append(tmp)
                return "DEFENCED"
            elif (self._world.getBoard()[self.getPosY()][self.getPosX()].whoIAm == 'A'):
                killer = self
                escaper = self._world.getBoard()[self.getPosY()][self.getPosX()]
                self._world.getBoard()[pY][pX] = escaper
                escaper.setPosX(pX)
                escaper.setPosY(pY)
                self._world.getBoard()[self.getPosY()][self.getPosX()] = killer

                tmp = "A avaded from " + self.whoIAm
                self._world.commentList.append(tmp)
                return "DEFENCED"
        else:
            if (self.getPower() >= self._world.getBoard()[self.getPosY()][self.getPosX()].getPower()):
                if (self._world.getBoard()[self.getPosY()][self.getPosX()].whoIAm == 'u'):
                    self.setPower(self.getPower() + 3)

                tmp = self.whoIAm + " ate " + self._world.getBoard()[self.getPosY()][self.getPosX()].whoIAm

                if (self._world.getBoard()[self.getPosY()][self.getPosX()].whoIAm == 'H'):
                    self._world.setPlayerIsActive(False)

                self._world.commentList.append(tmp)
                self._world.getBoard()[self.getPosY()][self.getPosX()].setIsDead(True)
                self._world.getBoard()[self.getPosY()][self.getPosX()] = self
                self._world.getBoard()[pY][pX] = None
                return "WIN"
            else:
                tmp = self.whoIAm + " killed by " + self._world.getBoard()[self.getPosY()][self.getPosX()].whoIAm
                self._world.commentList.append(tmp)
                tmpType = self._world.getBoard()[self.getPosY()][self.getPosX()].whoIAm

                if (tmpType == 'b' or tmpType == 's'):
                    self._world.getBoard()[self.getPosY()][self.getPosX()].setIsDead(True)

                self.setPosX(pX)
                self.setPosY(pY)
                self._world.getBoard()[pY][pX] = None
                self._dead = True
                return "DEAD"
        return "NO_CHANGES"

    def defenced(self, enemyObject):
        return False

    def newCoordinates(self):
        worldSizeX = self._world.getSizeX() - 1
        worldSizeY = self._world.getSizeY() - 1
        newPosX = self.getPosX()
        newPosY = self.getPosY()

        if (newPosX == 0 and newPosY == 0):
            moveTo = random.randint(0,1)
            if (moveTo == 0): #down
                newPosY = self._moveLength
            elif (moveTo == 1): #right
                newPosX = self._moveLength

        elif (newPosX == worldSizeX and newPosY == 0):
            moveTo = random.randint(0,1)
            if (moveTo == 0): #down
                newPosY = self._moveLength
            elif (moveTo == 1): #left
                newPosX -= self._moveLength

        elif (newPosX == 0 and newPosY == worldSizeY):
            moveTo = random.randint(0,1)
            if (moveTo == 0): #up
                newPosY -= self._moveLength
            elif (moveTo == 1): #right
                newPosX = self._moveLength

        elif (newPosX == worldSizeX and newPosY == worldSizeY):
            moveTo = random.randint(0,1)
            if (moveTo == 0): #up
                newPosY -= self._moveLength
            elif (moveTo == 1): #left
                newPosX -= self._moveLength

        elif (newPosX == 0):
            moveTo = random.randint(0,2)
            if (moveTo == 0): #up
                if (newPosY < self._moveLength):
                    newPosY -= 1
                else:
                    newPosY -= self._moveLength
            elif (moveTo == 1): #down
                if (newPosY > worldSizeY - self._moveLength):
                    newPosY += 1
                else:
                    newPosY += self._moveLength
            elif (moveTo == 2): #right
                newPosX = self._moveLength

        elif (newPosX == worldSizeX):
            moveTo = random.randint(0,2)
            if (moveTo == 0): #up
                if (newPosY < self._moveLength):
                    newPosY -= 1
                else:
                    newPosY -= self._moveLength
            elif (moveTo == 1): #down
                if (newPosY > worldSizeY - self._moveLength):
                    newPosY += 1
                else:
                    newPosY += self._moveLength
            elif (moveTo == 2): #left
                newPosX -= self._moveLength

        elif (newPosY == 0):
            moveTo = random.randint(0,2)
            if (moveTo == 0): #down
                newPosY = self._moveLength
            elif (moveTo == 1): #left
                if (newPosX < self._moveLength):
                    newPosX -= 1
                else:
                    newPosX -= self._moveLength
            elif (moveTo == 2): #right
                if (newPosX > worldSizeX - self._moveLength):
                    newPosX += 1
                else:
                    newPosX += self._moveLength

        elif (newPosY == worldSizeY):
            moveTo = random.randint(0,2)
            if (moveTo == 0): #up
                if (newPosY < self._moveLength):
                    newPosY -= 1
                else:
                    newPosY -= self._moveLength
            elif (moveTo == 1): #left
                if (newPosX < self._moveLength):
                    newPosX -= 1
                else:
                    newPosX -= self._moveLength
            elif (moveTo == 2): #right
                if (newPosX > worldSizeX - self._moveLength):
                    newPosX += 1
                else:
                    newPosX += self._moveLength
        else:
            moveTo = random.randint(0,3)
            if (moveTo == 0): #up
                if (newPosY < self._moveLength):
                    newPosY -= 1
                else:
                    newPosY -= self._moveLength
            elif (moveTo == 1): #down
                if (newPosY > worldSizeY - self._moveLength):
                    newPosY += 1
                else:
                    newPosY += self._moveLength
            elif (moveTo == 2): #left
                if (newPosX < self._moveLength):
                    newPosX -= 1
                else:
                    newPosX -= self._moveLength
            elif (moveTo == 3): #right
                if (newPosX > worldSizeX - self._moveLength):
                    newPosX += 1
                else:
                    newPosX += self._moveLength

        self.setPosX(newPosX)
        self.setPosY(newPosY)

    def makeNewChild(self):
        bornIn = random.randint(0,4)
        if (bornIn == 0): #up
            if (self.isItFreeSquare(self.getPosX(), self.getPosY() - 1) == True):
                self.addNewAnimal(self.whoIAm, self.getPosX(), self.getPosY() - 1)
                return True
            else:
                if (self.isItFreeSquare(self.getPosX(), self.getPosY() + 1) == True):
                    self.addNewAnimal(self.whoIAm, self.getPosX(), self.getPosY() + 1)
                    return True
                else:
                    if (self.isItFreeSquare(self.getPosX() - 1, self.getPosY()) == True):
                        self.addNewAnimal(self.whoIAm, self.getPosX() - 1, self.getPosY())
                        return True
                    else:
                        if (self.isItFreeSquare(self.getPosX() + 1, self.getPosY()) == True):
                            self.addNewAnimal(self.whoIAm, self.getPosX() + 1, self.getPosY())
                            return True
        elif (bornIn == 1): #down
            if (self.isItFreeSquare(self.getPosX(), self.getPosY() + 1) == True):
                self.addNewAnimal(self.whoIAm, self.getPosX(), self.getPosY() + 1)
                return True
            else:
                if (self.isItFreeSquare(self.getPosX(), self.getPosY() - 1) == True):
                    self.addNewAnimal(self.whoIAm, self.getPosX(), self.getPosY() - 1)
                    return True
                else:
                    if (self.isItFreeSquare(self.getPosX() - 1, self.getPosY()) == True):
                        self.addNewAnimal(self.whoIAm, self.getPosX() - 1, self.getPosY())
                        return True
                    else:
                        if (self.isItFreeSquare(self.getPosX() + 1, self.getPosY()) == True):
                            self.addNewAnimal(self.whoIAm, self.getPosX() + 1, self.getPosY())
                            return True
        elif (bornIn == 2): #left
            if (self.isItFreeSquare(self.getPosX() - 1, self.getPosY()) == True):
                self.addNewAnimal(self.whoIAm, self.getPosX() - 1, self.getPosY())
                return True
            else:
                if (self.isItFreeSquare(self.getPosX() + 1, self.getPosY()) == True):
                    self.addNewAnimal(self.whoIAm, self.getPosX() + 1, self.getPosY())
                    return True
                else:
                    if (self.isItFreeSquare(self.getPosX(), self.getPosY() - 1) == True):
                        self.addNewAnimal(self.whoIAm, self.getPosX(), self.getPosY() - 1)
                        return True
                    else:
                        if (self.isItFreeSquare(self.getPosX(), self.getPosY() + 1) == True):
                            self.addNewAnimal(self.whoIAm, self.getPosX(), self.getPosY() + 1)
                            return True
        elif (bornIn == 3): #right
            if (self.isItFreeSquare(self.getPosX() + 1, self.getPosY()) == True):
                self.addNewAnimal(self.whoIAm, self.getPosX() + 1, self.getPosY())
                return True
            else:
                if (self.isItFreeSquare(self.getPosX() - 1, self.getPosY()) == True):
                    self.addNewAnimal(self.whoIAm, self.getPosX() - 1, self.getPosY())
                    return True
                else:
                    if (self.isItFreeSquare(self.getPosX(), self.getPosY() + 1) == True):
                        self.addNewAnimal(self.whoIAm, self.getPosX(), self.getPosY() + 1)
                        return True
                    else:
                        if (self.isItFreeSquare(self.getPosX(), self.getPosY() - 1) == True):
                            self.addNewAnimal(self.whoIAm, self.getPosX(), self.getPosY() - 1)
                            return True
        return False

    def isItFreeSquare(self, x, y):
        boardSizeX = self._world.getSizeX() - 1
        boardSizeY = self._world.getSizeY() - 1
        if (x < 0 or x > boardSizeX or y < 0 or y > boardSizeY):
            return False
        if (self._world.getBoard()[y][x] == None):
            return True
        return False

    def addNewAnimal(self, type, x, y):
        newAnimal = self._world.returnMyBrother(type, x, y)
        newAnimal.setJustBorn(True)
        self._world.getBoard()[newAnimal.getPosY()][newAnimal.getPosX()] = newAnimal

        for i in range(0, len(self._world.listOfOrganisms)):
            if (self._world.listOfOrganisms[i].getInitiative() < newAnimal.getInitiative()):
                self._world.listOfOrganisms.insert(i, newAnimal)
                break
            elif (i == len(self._world.listOfOrganisms) - 1):
                self._world.listOfOrganisms.append(newAnimal)
                break
