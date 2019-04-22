from Antelope import Antelope
from Belladonna import Belladonna
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from HeracleumSosnowkyi import HeracleumSosnowkyi
from Human import Human
from Sheep import Sheep
from Sonchus import Sonchus
from Turtle import Turtle
from Wolf import Wolf
from CyberSheep import CyberSheep

class OrganismFactory:
    
    def createNewOrganism(self, code, posX, posY, world):
        if (code == 0 or code == 'F'):
            return Fox(posX, posY, world)
        elif (code == 1 or code == 'W'):
            return Wolf(posX, posY, world)
        elif (code == 2 or code == 'H'):
            return Human(posX, posY, world)
        elif (code == 3 or code == 'A'):
            return Antelope(posX, posY, world)
        elif (code == 4 or code == 'C'):
            return CyberSheep(posX, posY, world)
        elif (code == 5 or code == 'S'):
            return Sheep(posX, posY, world)
        elif (code == 6 or code == 'T'):
            return Turtle(posX, posY, world)
        elif (code == 7 or code == 'b'):
            return Belladonna(posX, posY, world)
        elif (code == 8 or code == 's'):
            return HeracleumSosnowkyi(posX, posY, world)
        elif (code == 9 or code == 'o'):
            return Sonchus(posX, posY, world)
        elif (code == 10 or code == 'u'):
            return Guarana(posX, posY, world)
        elif (code == 11 or code == 'g'):
            return Grass(posX, posY, world)
        else:
            return None