import time

from Tool.Process import *
from Tool.Device.Mouse import *

from Classes.Entity import *
from Classes.Player import *
from Classes.Weapon import *

from SDK.GameVar import *
from SDK.GameSDK import *


TriggerBotStatus = False
TeamCheck = True

MaxShot = 3
VirtualKey = 6
Delay = 110


def getTargetInCross():
    Entity = csEntity(SDK.getEntityInCross())

    if (Entity.Valid()):
        if (TeamCheck and Entity.getTeam() == GameVar.LocalPlayer.Team):
            return False
        
        time.sleep(Delay / 1000)
        return csEntity(SDK.getEntityInCross()).Valid()
        
    return False


def Function():
    while (TriggerBotStatus):
        if (Game.KeyStatus(VirtualKey) and MaxShot > 0 and Game.WindowIsOpen()):
            if (GameVar.LocalPlayer.getShotFired() >= MaxShot):
                    continue
            
            if (GameVar.LocalPlayer.WeaponCattegory == WEAPON_SNIPER or GameVar.LocalPlayer.WeaponCattegory == WEAPON_AUTOSNIPER):
                 if (not GameVar.LocalPlayer.Scoped):
                      continue
            
            if (getTargetInCross()):
                 ClickMouse()
        
        time.sleep(0.01)