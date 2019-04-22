from Plant import Plant


class Belladonna(Plant):
    def __init__(self, posX, posY, world):
        super().__init__()
        self.myColor = (0, 0, 0)
        self.myTextColor = (255, 0, 0)
        self.whoIAm = 'b'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(99)
