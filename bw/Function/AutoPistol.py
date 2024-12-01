import time

from Tool.Process import *
from Tool.Device.Mouse import *

from Classes.Weapon import *
from SDK.GameVar import *


AutoPistolStatus = False
VirtualKey = 6


def Function():
    while (AutoPistolStatus):
        if (Game.KeyStatus(VirtualKey) and Game.WindowIsOpen()):
            if (GameVar.LocalPlayer.WeaponCattegory == WEAPON_PISTOL):
                ClickMouse()

        time.sleep(0.01)
