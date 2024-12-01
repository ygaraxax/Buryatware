from Tool.Offsets import *
from Tool.Process import *
from Tool.Vector import *
from Tool.Memory import *

from Classes.Weapon import Weapon
from SDK.GameVar import *


class csEntity():
    Player = None
    Name = None
    Controller = None

    def __init__(self, Addres):
        self.Player = Addres


    def getTeam(self):
        return Memory.Read.int(self.Player + m_iTeamNum)


    def getHealth(self):
        return Memory.Read.int(self.Player + m_iHealth)
    
    
    def getArmor(self):
        return Memory.Read.int(self.Player + m_ArmorValue)
    

    def getScoped(self):
        return Memory.Read.int(self.Player + m_bIsScoped)
    

    def getSpotted(self, LocalPlayer):
        return Memory.Read.bool(self.Player + m_entitySpottedState + m_bSpottedByMask) & (1 << LocalPlayer)
    

    def getAlive(self):
        return Memory.Read.int(self.Player + m_lifeState) == 256
    

    def Valid(self):
        return (self.Player != 0) and (self.getAlive()) and (self.getHealth() > 0)
    

    def getWeaponID(self):
        WeaponBase = Memory.Read.longlong(self.Player + m_pClippingWeapon)
        WeaponID = Memory.Read.short(WeaponBase + m_iItemDefinitionIndex + m_Item + m_AttributeManager)

        return WeaponID 
    

    def getWeaponCategory(self):
        return Weapon.getWeaponCategory(self.WeaponID)
    

    def getAmmo(self):
        ClippingWeapon = Memory.Read.longlong(self.Player + m_pClippingWeapon)
        Ammo = Memory.Read.int(ClippingWeapon + m_iClip1)

        return Ammo if (Ammo > 0) else 0
    
    
    def getOriginPosition(self):
        OriginPosition = Vector3()

        OriginPosition.x = Memory.Read.float(self.Player + m_vOldOrigin)
        OriginPosition.y = Memory.Read.float(self.Player + m_vOldOrigin + 0x4)
        OriginPosition.z = Memory.Read.float(self.Player + m_vOldOrigin + 0x8)

        return OriginPosition
    

    def getEyePosition(self):
        EyePosition = Vector3()

        EyePosition.x = Memory.Read.float(self.Player + m_vecViewOffset)
        EyePosition.y = Memory.Read.float(self.Player + m_vecViewOffset + 0x4)
        EyePosition.z = Memory.Read.float(self.Player + m_vecViewOffset + 0x8)

        return EyePosition
    

    def getHeadPosition(self):
        OriginPosition = Vector3()

        OriginPosition.x = Memory.Read.float(self.Player + m_vOldOrigin)
        OriginPosition.y = Memory.Read.float(self.Player + m_vOldOrigin + 0x4)
        VectorView_z     = Memory.Read.float(self.Player + m_vecViewOffset + 0x8)
        OriginPosition.z = Memory.Read.float(self.Player + m_vOldOrigin + 0x8) + VectorView_z

        return OriginPosition
    

    def getBonePosition(self, Bone):
        BonePosition = Vector3()

        GameSceneNode =  Memory.Read.longlong(self.Player + m_pGameSceneNode)
        BoneArray =  Memory.Read.longlong(GameSceneNode + m_modelState + 0x80)

        BonePosition.x = Memory.Read.float(BoneArray + Bone * 32)
        BonePosition.y = Memory.Read.float(BoneArray + Bone * 32 + 0x4)
        BonePosition.z = Memory.Read.float(BoneArray + Bone * 32 + 0x8)

        return BonePosition
    

    def getController(self, Index):
        ListEntity = Memory.Read.longlong(GameVar.dwEntityList + (8 * (Index & 0x7FFF) >> 9) + 16)
        if (not ListEntity): return 0

        EntityController = Memory.Read.longlong(ListEntity + 120 * (Index & 0x1FF))

        return EntityController
    

    def getPawn(self, EntityController):
        EntityControllerPawn = Memory.Read.longlong(EntityController + m_hPawn)
        if (not EntityControllerPawn): return 0

        NextListEntity = Memory.Read.longlong(GameVar.dwEntityList + 0x8 * ((EntityControllerPawn & 0x7FFF) >> 9) + 16)
        if (not NextListEntity): return 0

        EntityPawn = Memory.Read.longlong(NextListEntity + 120 * (EntityControllerPawn & 0x1FF))

        return EntityPawn