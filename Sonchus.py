from Plant import Plant


class Sonchus(Plant):
    def __init__(self, posX, posY, world):
        super().__init__()
        self.myColor = (255, 255, 51)
        self.whoIAm = 'o'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(0)

    def action(self):
        for i in range(0,3):
            super().action()
