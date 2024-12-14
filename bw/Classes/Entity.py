from Tool.Offsets import *
from Tool.Process import *
from Tool.Vector import *
from Tool.Memory import *

from Classes.Weapon import Weapon
from SDK.GameVar import *


class csEntity():
    """Base class representing a CS:GO entity with core attributes and methods"""
    def __init__(self, address):
        # Base memory address of entity
        self.Player = address
        self.Name = None
        self.Controller = None

    def getTeam(self):
        """Get entity team number"""
        return Memory.Read.int(self.Player + m_iTeamNum)

    def getHealth(self):
        """Get entity health value"""
        return Memory.Read.int(self.Player + m_iHealth)
    
    def getArmor(self):
        """Get entity armor value"""
        return Memory.Read.int(self.Player + m_ArmorValue)

    def getScoped(self):
        """Check if entity is scoped"""
        return Memory.Read.int(self.Player + m_bIsScoped)

    def getSpotted(self, LocalPlayer):
        """Check if entity is spotted by local player"""
        return Memory.Read.bool(self.Player + m_entitySpottedState + m_bSpottedByMask) & (1 << LocalPlayer)

    def getAlive(self):
        """Check if entity is alive"""
        return Memory.Read.int(self.Player + m_lifeState) == 256

    def Valid(self):
        """Validate if entity is valid target"""
        return (self.Player != 0) and (self.getAlive()) and (self.getHealth() > 0)

    def getWeaponID(self):
        """Get entity's current weapon ID"""
        WeaponBase = Memory.Read.longlong(self.Player + m_pClippingWeapon)
        return Memory.Read.short(WeaponBase + m_iItemDefinitionIndex + m_Item + m_AttributeManager)

    def getWeaponCategory(self):
        """Get entity's current weapon category"""
        return Weapon.getWeaponCategory(self.getWeaponID())

    def getAmmo(self):
        """Get entity's current weapon ammo count"""
        ClippingWeapon = Memory.Read.longlong(self.Player + m_pClippingWeapon)
        Ammo = Memory.Read.int(ClippingWeapon + m_iClip1)
        return max(Ammo, 0)

    def getOriginPosition(self):
        """Get entity's origin position vector"""
        pos = Vector3()
        pos.x = Memory.Read.float(self.Player + m_vOldOrigin)
        pos.y = Memory.Read.float(self.Player + m_vOldOrigin + 0x4) 
        pos.z = Memory.Read.float(self.Player + m_vOldOrigin + 0x8)
        return pos

    def getEyePosition(self):
        """Get entity's eye position vector"""
        pos = Vector3()
        pos.x = Memory.Read.float(self.Player + m_vecViewOffset)
        pos.y = Memory.Read.float(self.Player + m_vecViewOffset + 0x4)
        pos.z = Memory.Read.float(self.Player + m_vecViewOffset + 0x8)
        return pos

    def getHeadPosition(self):
        """Get entity's head position by combining origin and view offset"""
        pos = Vector3()
        pos.x = Memory.Read.float(self.Player + m_vOldOrigin)
        pos.y = Memory.Read.float(self.Player + m_vOldOrigin + 0x4)
        view_z = Memory.Read.float(self.Player + m_vecViewOffset + 0x8)
        pos.z = Memory.Read.float(self.Player + m_vOldOrigin + 0x8) + view_z
        return pos

    def getBonePosition(self, Bone):
        """Get position of specific bone from entity's skeleton"""
        pos = Vector3()
        GameSceneNode = Memory.Read.longlong(self.Player + m_pGameSceneNode)
        BoneArray = Memory.Read.longlong(GameSceneNode + m_modelState + 0x80)
        
        pos.x = Memory.Read.float(BoneArray + Bone * 32)
        pos.y = Memory.Read.float(BoneArray + Bone * 32 + 0x4)
        pos.z = Memory.Read.float(BoneArray + Bone * 32 + 0x8)
        return pos

    def getController(self, Index):
        """Get entity controller from index"""
        ListEntity = Memory.Read.longlong(GameVar.dwEntityList + (8 * (Index & 0x7FFF) >> 9) + 16)
        if not ListEntity:
            return 0
            
        return Memory.Read.longlong(ListEntity + 120 * (Index & 0x1FF))

    def getPawn(self, EntityController):
        """Get entity pawn from controller"""
        EntityControllerPawn = Memory.Read.longlong(EntityController + m_hPawn)
        if not EntityControllerPawn:
            return 0

        NextListEntity = Memory.Read.longlong(GameVar.dwEntityList + 0x8 * ((EntityControllerPawn & 0x7FFF) >> 9) + 16)
        if not NextListEntity:
            return 0

        return Memory.Read.longlong(NextListEntity + 120 * (EntityControllerPawn & 0x1FF))
