from Tool.Offsets import *
from Tool.Process import *
from Tool.Vector import *
from Tool.Memory import *

from Classes.Weapon import Weapon


class csPlayer():
    """Class representing a CS:GO player entity with core attributes and methods"""
    def __init__(self, address):
        # Base memory address
        self.Player = address

        # Core player attributes 
        self.Team = self.getTeam()
        self.Scoped = self.getScoped()
        self.Alive = self.getAlive()

        # Weapon info
        self.WeaponID = self.getWeaponID()
        self.WeaponCattegory = self.getWeaponCategory()

    def getTeam(self):
        """Get player team number"""
        return Memory.Read.int(self.Player + m_iTeamNum)

    def getHealth(self):
        """Get player health value"""
        return Memory.Read.int(self.Player + m_iHealth)
    
    def getMoveFlag(self):
        """Get player movement flags"""
        return Memory.Read.int(self.Player + m_fFlags)
    
    def getShotFired(self):
        """Get number of shots fired"""
        return Memory.Read.int(self.Player + m_iShotsFired)
    
    def getFlashAlpha(self):
        """Get flash grenade effect intensity"""
        return Memory.Read.float(self.Player + m_flFlashOverlayAlpha)
    
    def getScoped(self):
        """Check if player is scoped"""
        return Memory.Read.bool(self.Player + m_bIsScoped)
    
    def getAlive(self):
        """Check if player is alive"""
        return Memory.Read.int(self.Player + m_lifeState) == 256
    
    def getWeaponID(self):
        """Get current weapon ID"""
        weapon_base = Memory.Read.longlong(self.Player + m_pClippingWeapon)
        weapon_id = Memory.Read.short(weapon_base + m_iItemDefinitionIndex + m_Item + m_AttributeManager)
        return weapon_id
    
    def getWeaponCategory(self):
        """Get weapon category based on weapon ID"""
        return Weapon.getWeaponCategory(self.WeaponID)
    
    def getOriginPosition(self):
        """Get player's feet position vector"""
        origin = Vector3()
        origin.x = Memory.Read.float(self.Player + m_vOldOrigin)
        origin.y = Memory.Read.float(self.Player + m_vOldOrigin + 0x4) 
        origin.z = Memory.Read.float(self.Player + m_vOldOrigin + 0x8)
        return origin
    
    def getHeadPosition(self):
        """Get player's head position vector"""
        head_pos = Vector3()
        head_pos.x = Memory.Read.float(self.Player + m_vOldOrigin)
        head_pos.y = Memory.Read.float(self.Player + m_vOldOrigin + 0x4)
        view_offset_z = Memory.Read.float(self.Player + m_vecViewOffset + 0x8)
        head_pos.z = Memory.Read.float(self.Player + m_vOldOrigin + 0x8) + view_offset_z
        return head_pos
