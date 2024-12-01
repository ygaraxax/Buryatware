import time

from Tool.Process import *
from Tool.Device.Mouse import *

from Classes.Entity import *
from Classes.Player import *
from Classes.Weapon import *

from SDK.GameVar import *
from SDK.GameSDK import *

from SDK.Render import *


AimBotStatus = False
AimBotFOVStatus = False
TeamCheck = True

Bone = 6
Fov = 90
Smooth = 1
VirtualKey = 6
MaxShot = 5

AimFOVColor = "#ffffff"


def getBestTarget():
    BestEntity = csEntity(0)
    OldDistance = -9999

    Matrix = SDK.getViewMatrix()

    for Entity in GameVar.EntityList:
        if (Entity.Valid()):
            if ((TeamCheck and Entity.getTeam() == GameVar.LocalPlayer.Team) ):
                continue
            
            BoneWorldToScreen = SDK.WorldToScreen(Entity.getBonePosition(6), Matrix)
            
            if (BoneWorldToScreen.x > 0 and BoneWorldToScreen.y > 0):
                Distance = SDK.getDistanceFromCenter(BoneWorldToScreen, Fov)

                if (OldDistance < Distance and Distance > 0):
                    BestEntity = Entity
                    OldDistance = Distance

    return BestEntity


def getBestBone(Entity: csEntity):
    OldDistance = -9999
    BestBone = 6

    Matrix = SDK.getViewMatrix()

    for Bone in GameVar.BoneList:
        BoneWorldToScreen = SDK.WorldToScreen(Entity.getBonePosition(Bone), Matrix)

        if (BoneWorldToScreen.x > 0 and BoneWorldToScreen.y > 0):
            Distance = SDK.getDistanceFromCenter(BoneWorldToScreen, 360)

            if (OldDistance < Distance and Distance > 0):
                BestBone = Bone
                OldDistance = Distance

    return BestBone


def Function():
    Entity = csEntity(0)

    while (AimBotStatus):
        if (Game.WindowIsOpen()):
            if (MaxShot > 0):
                if (GameVar.LocalPlayer.getShotFired() >= MaxShot):
                    continue
            
            if (Game.KeyStatus(VirtualKey) and GameVar.LocalPlayer.Alive and (GameVar.LocalPlayer.WeaponCattegory != WEAPON_KNIFE and GameVar.LocalPlayer.WeaponCattegory != WEAPON_BOMB)):
                if (Entity.Player == 0 or Entity.getHealth() <= 0):
                    Entity = getBestTarget()

                if (Entity.Valid()):
                    EntityBonePosition = Entity.getBonePosition(getBestBone(Entity) if (Bone == -1) else Bone)

                    Matrix = SDK.getViewMatrix()
                    BonePositionWTS = SDK.WorldToScreen(EntityBonePosition, Matrix)

                    if (BonePositionWTS.x > 0 and BonePositionWTS.y > 0):
                        MousePosition = Vector2()

                        MousePosition.x = BonePositionWTS.x - (GameVar.WindowScreen.x / 2)
                        MousePosition.y = BonePositionWTS.y - (GameVar.WindowScreen.y / 2)

                        MoveMouseSmooth(MousePosition.x, MousePosition.y, Smooth)


            else:
                Entity.Player = 0

        time.sleep(0.01)