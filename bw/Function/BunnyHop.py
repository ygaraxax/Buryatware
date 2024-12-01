import time

from Tool.Process import *
from Tool.Device.Keyboard import *

from Classes.Player import *
from SDK.GameVar import *


BunnyHopStatus = False

IN_AIR = 65664
IN_GROUND = 65665
IN_SITTING = 65667


def Function():
    while (BunnyHopStatus):
        if (Game.WindowIsOpen() and Game.KeyStatus(0x20)):
            if (GameVar.LocalPlayer.Alive):
                PlayerMoveFlag = GameVar.LocalPlayer.getMoveFlag()

                if (PlayerMoveFlag == IN_GROUND or PlayerMoveFlag == IN_SITTING):
                    ForceJump()

        time.sleep(0.03)

