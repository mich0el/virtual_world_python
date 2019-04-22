import sys
import random
import pygame
from tkinter import *
from OrganismFactory import OrganismFactory
pygame.init()

class World:
    SQUARE_SIZE = 20
    COMMENTS_FIELD = 250
    BUTTONS_FIELD = 100
    BORDER_WIDTH = 1
    NULL_FIELD_COLOR = (224, 224, 224)
    screen = None
    font = pygame.font.SysFont("TNR", 19)

    def __init__(self, sizeX, sizeY, readFromFile):
        if (readFromFile == False):
            self.playerIsActive = False
            self.__sizeX = sizeX
            self.__sizeY = sizeY
            self.board = [[None for x in range(0, sizeX)] for y in range(0, sizeY)]
            self.listOfOrganisms = []
            self.commentList = []

            HUMAN_CODE = 2
            factory = OrganismFactory()
            uniqOrganismCount = ((sizeX * sizeY) // 20) // 10
            if ((sizeX * sizeY) < 200 and (sizeX * sizeY) >= 12):
                uniqOrganismCount = 1

            tmpY = random.randint(0, sizeY - 1)
            tmpX = random.randint(0, sizeX - 1)

            for i in range(0, uniqOrganismCount * 12):
                if (i // uniqOrganismCount != HUMAN_CODE):
                    while (self.board[tmpY][tmpX] != None):
                        tmpY = random.randint(0, sizeY - 1)
                        tmpX = random.randint(0, sizeX - 1)
                    self.board[tmpY][tmpX] = factory.createNewOrganism(i // uniqOrganismCount, tmpX, tmpY, self)
                    self.listOfOrganisms.append(self.board[tmpY][tmpX])
                elif (i % uniqOrganismCount == 0):
                    while (self.board[tmpY][tmpX] != None):
                        tmpY = random.randint(0, sizeY - 1)
                        tmpX = random.randint(0, sizeX - 1)
                    self.board[tmpY][tmpX] = factory.createNewOrganism('H', tmpX, tmpY, self)
                    self.listOfOrganisms.append(self.board[tmpY][tmpX])
                    self.playerIsActive = True
            
        else:
            self.playerIsActive = False
            saveFile = open("1.txt")
            line = saveFile.readline()
            sizeBoardX, sizeBoardY = (int(s) for s in line.split())
            
            self.__sizeX = sizeBoardX
            self.__sizeY = sizeBoardY
            self.listOfOrganisms = []
            self.commentList = []
            self.board = [[None for x in range(0, sizeBoardX)] for y in range(0, sizeBoardY)]

            line = saveFile.readline()
            organismCount = int(line)

            for i in range(0, organismCount):
                factory = OrganismFactory()
                line = saveFile.readline()
                variables = line.split()
                tmpType = variables[0]
                tmpX = int(variables[1])
                tmpY = int(variables[2])
                powerTmp = int(variables[3])

                if (tmpType == 'A' or tmpType == 'C' or tmpType == 'F' or tmpType == 'S' or tmpType == 'T' or tmpType == 'W'):
                    tmpOrg = factory.createNewOrganism(tmpType, tmpX, tmpY, self)
                    tmpOrg.setPower(powerTmp)
                    self.listOfOrganisms.append(tmpOrg)
                elif (tmpType == 'H'):
                    abilityMovesTmp = int(variables[4])
                    tmpH = factory.createNewOrganism(tmpType, tmpX, tmpY, self)
                    tmpH.setPower(powerTmp)
                    tmpH.setSpecialAbilityMoves(abilityMovesTmp)
                    self.listOfOrganisms.append(tmpH)
                    self.playerIsActive = True
                else:
                    tmpOrg = factory.createNewOrganism(tmpType, tmpX, tmpY, self)
                    self.listOfOrganisms.append(tmpOrg)

            for element in self.listOfOrganisms:
                self.board[element.getPosY()][element.getPosX()] = element

        self.gameStarter()


    def drawTheWorld(self):
        for y in range(0, self.__sizeY):
            for x in range(0, self.__sizeX):
                if (self.board[y][x] == None):
                    x0, y0 = x * self.SQUARE_SIZE, y * self.SQUARE_SIZE
                    x1, y1 = x0 + self.SQUARE_SIZE, y0 + self.SQUARE_SIZE
                    pygame.draw.rect(self.screen, self.NULL_FIELD_COLOR, [x0, y0, x1, y1], 0)
                    pygame.draw.rect(self.screen, (255, 255, 255), [x0, y0, x1, y1], self.BORDER_WIDTH)
                else:
                    x0, y0 = x * self.SQUARE_SIZE, y * self.SQUARE_SIZE
                    x1, y1 = x0 + self.SQUARE_SIZE, y0 + self.SQUARE_SIZE
                    self.board[y][x].drawing()
                    pygame.draw.rect(self.screen, (255, 255, 255), [x0, y0, x1, y1], self.BORDER_WIDTH)

        pygame.draw.rect(self.screen, self.NULL_FIELD_COLOR, [self.__sizeX * self.SQUARE_SIZE, 0, self.__sizeX * self.SQUARE_SIZE + self.COMMENTS_FIELD, self.__sizeY * self.SQUARE_SIZE], 0)
        pygame.draw.rect(self.screen, (255, 255, 255), [self.__sizeX * self.SQUARE_SIZE, 0, self.__sizeX * self.SQUARE_SIZE + self.COMMENTS_FIELD, self.__sizeY * self.SQUARE_SIZE], 1)

        text = self.font.render("=== Last world events ===", True, (0, 0, 0))
        self.screen.blit(text, [self.__sizeX * self.SQUARE_SIZE + 40, 0])

        if self.playerIsActive == True:
            for element in self.listOfOrganisms:
                if element.whoIAm == 'H':
                    txt = "Human power: " + str(element.getPower()) + ", ability is "
                    if element.specialAbilityIsActive():
                        txt += "ON"
                    else:
                        txt += "OFF"
        else:
            txt = "Human is dead"
        text = self.font.render(txt, True, (0, 0, 0))
        self.screen.blit(text, [self.__sizeX * self.SQUARE_SIZE + 10, 15])

        commentHeight = 15
        commentYPos = commentHeight * 2
        for i in range(len(self.commentList)):
            if i >= len(self.commentList):
                break
            text = self.font.render(self.commentList[i], True, (0, 0, 0))
            self.screen.blit(text, [self.__sizeX * self.SQUARE_SIZE + 10, commentYPos])
            commentYPos += commentHeight
            self.commentList.pop(i)
        pygame.display.flip()

    def nextRound(self):
        for i in range(0, len(self.listOfOrganisms)):
            if (i < len(self.listOfOrganisms)):
                if (self.listOfOrganisms[i].getJustBorn() == True):
                    self.listOfOrganisms[i].setJustBorn(False)
                else:
                    if (self.listOfOrganisms[i].isDead() == False):
                        self.listOfOrganisms[i].action()
                    else:
                        if (self.board[self.listOfOrganisms[i].getPosY()][self.listOfOrganisms[i].getPosX()] == self.listOfOrganisms[i]):
                            self.board[self.listOfOrganisms[i].getPosY()][self.listOfOrganisms[i].getPosX()] = None
                        self.listOfOrganisms.pop(i)
        self.drawTheWorld()


    def gameStarter(self):
        self.screen = pygame.display.set_mode((self.SQUARE_SIZE * self.__sizeX + self.COMMENTS_FIELD, self.SQUARE_SIZE * self.__sizeY))
        pygame.display.set_caption('Mikhail Lanchytski 172142')
        self.screen.fill((192, 192, 192))
        running = True
        self.drawTheWorld()
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.direction = "UP"
                        self.nextRound()
                    elif event.key == pygame.K_DOWN:
                        self.direction = "DOWN"
                        self.nextRound()
                    elif event.key == pygame.K_LEFT:
                        self.direction = "LEFT"
                        self.nextRound()
                    elif event.key == pygame.K_RIGHT:
                        self.direction = "RIGHT"
                        self.nextRound()
                    elif event.key == pygame.K_a:
                        if self.playerIsActive == True:
                            for element in self.listOfOrganisms:
                                if element.whoIAm == 'H':
                                    if element.turnOnAbility():
                                        self.drawTheWorld()
                    elif event.key == pygame.K_s:
                        self.saveGame()
                    elif event.key == pygame.K_ESCAPE:
                        running = False


    def saveGame(self):
        saveFile = open("1.txt", "w")

        saveFile.write(str(self.getSizeX()) + " " + str(self.getSizeY()) + "\n")
        saveFile.write(str(len(self.listOfOrganisms)) + "\n")

        for element in self.listOfOrganisms:
            saveFile.write(element.organismInfo())

        saveFile.close()

        self.drawTheWorld()
        pygame.draw.rect(self.screen, self.NULL_FIELD_COLOR, [self.__sizeX * self.SQUARE_SIZE, 0, self.__sizeX * self.SQUARE_SIZE + self.COMMENTS_FIELD, self.__sizeY * self.SQUARE_SIZE], 0)
        text = self.font.render("SAVED!", True, (0, 0, 0))
        self.screen.blit(text, [self.__sizeX * self.SQUARE_SIZE + 95, 15])
        pygame.display.flip()


    def getBoard(self):
        return self.board

    def getSizeX(self):
        return self.__sizeX

    def getSizeY(self):
        return self.__sizeY

    def returnMyBrother(self, type, x, y):
        factory = OrganismFactory()
        newOrganism = factory.createNewOrganism(type, x, y, self)
        return newOrganism

    def setPlayerIsActive(self, val):
        self.playerIsActive = val

    def getPlayerIsActive(self):
        return self.playerIsActive