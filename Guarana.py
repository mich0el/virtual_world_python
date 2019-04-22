from Plant import Plant


class Guarana(Plant):
    def __init__(self, posX, posY, world):
        super().__init__()
        self.myColor = (119, 255, 247)
        self.whoIAm = 'u'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(0)
