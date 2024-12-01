from Tool.Offsets import *
from Tool.Process import *
from Tool.Vector import *
from Tool.Memory import *

from Classes.Weapon import Weapon


class csPlayer():
    Player = None
    Team = None
    WeaponID = None
    WeaponCattegory = None
    Scoped = None
    Alive = None


    def __init__(self, Addres):
        self.Player = Addres

        self.Team = self.getTeam()
        self.Scoped = self.getScoped()
        self.Alive = self.getAlive()

        self.WeaponID = self.getWeaponID()
        self.WeaponCattegory = self.getWeaponCategory()


    def getTeam(self):
        return Memory.Read.int(self.Player + m_iTeamNum)


    def getHealth(self):
        return Memory.Read.int(self.Player + m_iHealth)
    

    def getMoveFlag(self):
        return Memory.Read.int(self.Player + m_fFlags)
    

    def getShotFired(self):
        return Memory.Read.int(self.Player + m_iShotsFired)
    

    def getFlashAlpha(self):
        return Memory.Read.float(self.Player + m_flFlashOverlayAlpha)
    

    def getScoped(self):
        return Memory.Read.bool(self.Player + m_bIsScoped)
    

    def getAlive(self):
        return Memory.Read.int(self.Player + m_lifeState) == 256
    

    def getWeaponID(self):
        WeaponBase = Memory.Read.longlong(self.Player + m_pClippingWeapon)
        WeaponID = Memory.Read.short(WeaponBase + m_iItemDefinitionIndex + m_Item + m_AttributeManager)

        return WeaponID 
    

    def getWeaponCategory(self):
        return Weapon.getWeaponCategory(self.WeaponID)

    
    def getOriginPosition(self):
        OriginPosition = Vector3()

        OriginPosition.x = Memory.Read.float(self.Player + m_vOldOrigin)
        OriginPosition.y = Memory.Read.float(self.Player + m_vOldOrigin + 0x4)
        OriginPosition.z = Memory.Read.float(self.Player + m_vOldOrigin + 0x8)

        return OriginPosition
    

    def getHeadPosition(self):
        OriginPosition = Vector3()

        OriginPosition.x = Memory.Read.float(self.Player + m_vOldOrigin)
        OriginPosition.y = Memory.Read.float(self.Player + m_vOldOrigin + 0x4)
        VectorView_z     = Memory.Read.float(self.Player + m_vecViewOffset + 0x8)
        OriginPosition.z = Memory.Read.float(self.Player + m_vOldOrigin + 0x8) + VectorView_z

        return OriginPosition
    