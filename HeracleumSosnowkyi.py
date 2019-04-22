from Plant import Plant


class HeracleumSosnowkyi(Plant):
    def __init__(self, posX, posY, world):
        super().__init__()
        self.myColor = (255, 255, 255)
        self.myTextColor = (255, 0, 0)
        self.whoIAm = 's'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(10)

    def action(self):
        super().action()
        self.killNeighbours()

    def targetIsHere(self, x, y):
        boardSizeX = self._world.getSizeX() - 1
        boardSizeY = self._world.getSizeY() - 1
        if (x < 0 or x > boardSizeX or y < 0 or y > boardSizeY):
            return False
        if (self._world.getBoard()[y][x] == None):
            return False
        if (self._world.getBoard()[y][x].whoIAm == 'C' or self._world.getBoard()[y][x].whoIAm == 's' or self._world.getBoard()[y][x].whoIAm == 'g' or self._world.getBoard()[y][x].whoIAm == 'u' or self._world.getBoard()[y][x].whoIAm == 'o' or self._world.getBoard()[y][x].whoIAm == 'b'):
            return False
        return True

    def killNeighbours(self):
        posX = self.getPosX()
        posY = self.getPosY()
        for i in range(0, 4):
            if (self.targetIsHere(posX + 1, posY) == True):
                self._world.getBoard()[posY][posX + 1].setIsDead(True)
                tmp = self._world.getBoard()[posY][posX + 1].whoIAm + " killed by s"

                if (self._world.getBoard()[posY][posX + 1].whoIAm == 'H'):
                    self._world.setPlayerIsActive(False)
                self._world.commentList.append(tmp)
                self._world.getBoard()[posY][posX + 1] = None

            elif (self.targetIsHere(posX - 1, posY) == True):
                self._world.getBoard()[posY][posX - 1].setIsDead(True)
                tmp = self._world.getBoard()[posY][posX - 1].whoIAm + " killed by s"

                if (self._world.getBoard()[posY][posX - 1].whoIAm == 'H'):
                    self._world.setPlayerIsActive(False)

                self._world.commentList.append(tmp)
                self._world.getBoard()[posY][posX - 1] = None

            elif (self.targetIsHere(posX, posY + 1) == True):
                self._world.getBoard()[posY + 1][posX].setIsDead(True)
                tmp = self._world.getBoard()[posY + 1][posX].whoIAm + " killed by s"

                if (self._world.getBoard()[posY + 1][posX].whoIAm == 'H'):
                    self._world.setPlayerIsActive(False)

                self._world.commentList.append(tmp)
                self._world.getBoard()[posY + 1][posX] = None

            elif (self.targetIsHere(posX, posY - 1) == True):
                self._world.getBoard()[posY - 1][posX].setIsDead(True)
                tmp = self._world.getBoard()[posY - 1][posX].whoIAm + " killed by s"

                if (self._world.getBoard()[posY - 1][posX].whoIAm == 'H'):
                    self._world.setPlayerIsActive(False)

                self._world.commentList.append(tmp)
                self._world.getBoard()[posY - 1][posX] = None
