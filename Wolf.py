from Animal import Animal


class Wolf(Animal):
    def __init__(self, posX, posY, world):
        super().__init__()
        self.myColor = (95, 95, 95)
        self.whoIAm = 'W'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(9)
        self.setInitiative(5)
