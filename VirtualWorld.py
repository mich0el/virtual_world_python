from Animal import Animal
from Antelope import Antelope
from Belladonna import Belladonna
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from HeracleumSosnowkyi import HeracleumSosnowkyi
from Human import Human
from Organism import Organism
from Plant import Plant
from Sheep import Sheep
from Sonchus import Sonchus
from Turtle import Turtle
from Wolf import Wolf
from World import World

from OrganismFactory import OrganismFactory
from tkinter import *


class GUI(Frame):
    xSize = None
    ySize = None

    def __init__(self, master=Tk()):
        Frame.__init__(self, master, width=270)
        self.grid()

        master.title("Mikhail Lanchytski 172142")

        self.errorLabel = Label(master, text="VIRTUAL WORLD\nNEW GAME")
        self.errorLabel.grid()

        self.XLabel = Label(master, text="Board width")
        self.XLabel.grid()
        self.XEntry = StringVar()
        self.XEntry = Entry(textvariable=self.XEntry)
        self.XEntry.grid()

        self.YLabel = Label(master, text="Board height")
        self.YLabel.grid()
        self.YEntry = StringVar()
        self.YEntry = Entry(textvariable=self.YEntry)
        self.YEntry.grid()

        def newBoardAct():
            try:
                if (int(self.XEntry.get()) < 4 or int(self.YEntry.get()) < 4):
                    self.errorLabel['text'] = "WRON SIZE!\nTRY AGAIN"
                else:
                    self.xSize, self.ySize = int(self.XEntry.get()), int(self.YEntry.get())
                    master.destroy()
                    World(self.xSize, self.ySize, False)
            except:
                self.errorLabel['text'] = "WRON SIZE!\nTRY AGAIN"

        def savedBoardAct():
            try:
                master.destroy()
                World(0, 0, True)
            except:
                self.errorLabel['text'] = "ERROR!\nFile \"1.txt\" is empty"

        self.newBoardBtn = Button(master, text="Create new board", command=newBoardAct)
        self.newBoardBtn.grid()
        self.savedBoardBtn = Button(master, text="Load game from file", command=savedBoardAct)
        self.savedBoardBtn.grid()


guiFrame = GUI()
guiFrame.mainloop()