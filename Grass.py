from Plant import Plant

class Grass(Plant):

    def __init__(self, posX, posY, world):
        super().__init__()
        self.myColor = (91, 255, 91)
        self.whoIAm = 'g'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(0)