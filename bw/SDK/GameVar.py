from Classes.Player import *
from Tool.Vector import *

class GameVar():
    LocalPlayer = csPlayer(0)

    EntityList = []

    BoneList = [6, 5, 4, 0]
    BoneListName = {
        6 : "Head",
        5 : "Heck",
        4 : "Chest",
        0 : "Stomach",
        -1 : "Nearest",
    }

    dwEntityList = 0

    WindowScreen = Vector2()

