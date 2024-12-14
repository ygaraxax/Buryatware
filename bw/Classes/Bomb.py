import time

from Tool.Process import *
from Tool.Memory import *
from Tool.Offsets import *
from Tool.Vector import *

from SDK.GameSDK import *


class csBomb():
    # Track bomb plant and defuse timestamps
    BombPlantedTime = 0  
    BombDefusedTime = 0

    @staticmethod
    def getC4BaseClass():
        """Get base pointer to planted C4 entity"""
        PlantedC4Class = Memory.Read.longlong(Game.Client + dwPlantedC4)
        return Memory.Read.longlong(PlantedC4Class)

    @staticmethod 
    def getPositionWTS():
        """Get bomb position in world-to-screen coordinates"""
        C4Position = Vector3()
        C4Node = Memory.Read.longlong(csBomb.getC4BaseClass() + m_pGameSceneNode)

        # Read XYZ coordinates
        C4Position.x = Memory.Read.float(C4Node + m_vecAbsOrigin)
        C4Position.y = Memory.Read.float(C4Node + m_vecAbsOrigin + 0x4)
        C4Position.z = Memory.Read.float(C4Node + m_vecAbsOrigin + 0x8)

        Matrix = SDK.getViewMatrix()
        return SDK.WorldToScreen(C4Position, Matrix)

    @staticmethod
    def getSite():
        """Get bomb site identifier (A or B)"""
        Site = Memory.Read.int(csBomb.getC4BaseClass() + m_nBombSite)
        return "А" if Site != 1 else "B"

    @staticmethod
    def isPlanted():
        """Check if bomb is planted and track plant time"""
        BombIsPlanted = Memory.Read.bool(Game.Client + dwPlantedC4 - 0x8)

        if BombIsPlanted and csBomb.BombPlantedTime == 0:
            csBomb.BombPlantedTime = time.time()
        elif not BombIsPlanted:
            csBomb.BombPlantedTime = 0

        return BombIsPlanted

    @staticmethod
    def isBeingDefused():
        """Check if bomb is being defused and track defuse time"""
        BombIsDefused = Memory.Read.bool(csBomb.getC4BaseClass() + m_bBeingDefused)

        if BombIsDefused and csBomb.BombDefusedTime == 0:
            csBomb.BombDefusedTime = time.time()
        elif not BombIsDefused:
            csBomb.BombDefusedTime = 0

        return BombIsDefused

    @staticmethod
    def getDefuseLength():
        """Get total defuse time required"""
        return Memory.Read.float(csBomb.getC4BaseClass() + m_flDefuseLength)

    @staticmethod
    def getTimerLength():
        """Get total explosion timer length"""
        return Memory.Read.float(csBomb.getC4BaseClass() + m_flTimerLength)

    @staticmethod
    def getBombTime():
        """Get remaining time until explosion"""
        BombTime = csBomb.getTimerLength() - (time.time() - csBomb.BombPlantedTime)
        return max(BombTime, 0)

    @staticmethod
    def getDefuseTime():
        """Get remaining defuse time if being defused"""
        DefuseTime = csBomb.getDefuseLength() - (time.time() - csBomb.BombDefusedTime)
        return DefuseTime if (csBomb.isBeingDefused() and DefuseTime >= 0) else 0
