from Animal import Animal


class Sheep(Animal):
    def __init__(self, posX, posY, world):
        super().__init__()
        self.myColor = (204, 153, 255)
        self.whoIAm = 'S'
        self.setPosX(posX)
        self.setPosY(posY)
        self._world = world
        self.setPower(4)
        self.setInitiative(4)
