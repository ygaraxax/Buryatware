import time

from Tool.Process import *
from Tool.Memory import *
from Tool.Offsets import *
from Tool.Vector import *

from SDK.GameSDK import *


class csBomb():
    BombPlantedTime = 0
    BombDefusedTime = 0

    
    def getC4BaseClass():
        PlantedC4Class = Memory.Read.longlong(Game.Client + dwPlantedC4)
        return Memory.Read.longlong(PlantedC4Class)
    

    def getPositionWTS():
        C34Position = Vector3()

        C4Node = Memory.Read.longlong(csBomb.getC4BaseClass() + m_pGameSceneNode)

        C34Position.x = Memory.Read.float(C4Node + m_vecAbsOrigin)
        C34Position.y = Memory.Read.float(C4Node + m_vecAbsOrigin + 0x4)
        C34Position.z = Memory.Read.float(C4Node + m_vecAbsOrigin + 0x8)

        Matrix = SDK.getViewMatrix()
        return SDK.WorldToScreen(C34Position, Matrix)
    

    def getSite():
        Site = Memory.Read.int(csBomb.getC4BaseClass() + m_nBombSite)
        return "А" if (Site != 1) else "B"
    

    def isPlanted():
        BombIsPlanted = Memory.Read.bool(Game.Client + dwPlantedC4 - 0x8)

        if (BombIsPlanted):
            if (csBomb.BombPlantedTime == 0):
                csBomb.BombPlantedTime = time.time() 

        else:
            csBomb.BombPlantedTime = 0

        return BombIsPlanted
    

    def isBeingDefused():
        BombIsDefused = Memory.Read.bool(csBomb.getC4BaseClass() + m_bBeingDefused)

        if (BombIsDefused):
            if (csBomb.BombDefusedTime == 0):
                csBomb.BombDefusedTime = time.time() 

        else:
            csBomb.BombDefusedTime = 0

        return BombIsDefused
    

    def getDefuseLength():
        return Memory.Read.float(csBomb.getC4BaseClass() + m_flDefuseLength)
    

    def getTimerLength():
        return Memory.Read.float(csBomb.getC4BaseClass() + m_flTimerLength)
    

    def getBombTime():
        BombTime = csBomb.getTimerLength() - (time.time() - csBomb.BombPlantedTime)
        return BombTime if (BombTime >= 0) else 0
    

    def getDefuseTime():
        DefuseTime = csBomb.getDefuseLength() - (time.time() - csBomb.BombDefusedTime)
        return DefuseTime if (csBomb.isBeingDefused() and DefuseTime >= 0) else 0

