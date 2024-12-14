import time

from Tool.Process import *
from Tool.Device.Mouse import *

from Classes.Entity import *
from Classes.Player import *
from Classes.Weapon import *

from SDK.GameVar import *
from SDK.GameSDK import *

from SDK.Render import *


# Aimbot configuration
AimBotStatus = False
AimBotFOVStatus = False
TeamCheck = True

# Targeting settings
Bone = 6  # Default bone target (head)
Fov = 90  # Field of view for target acquisition
Smooth = 1  # Mouse movement smoothing
VirtualKey = 6  # Activation key
MaxShot = 5  # Maximum shots before reset

AimFOVColor = "#ffffff"


def getBestTarget():
    """Find the best target within FOV"""
    best_entity = csEntity(0)
    best_distance = float('-inf')
    view_matrix = SDK.getViewMatrix()

    for entity in GameVar.EntityList:
        if not entity.Valid() or (TeamCheck and entity.getTeam() == GameVar.LocalPlayer.Team):
            continue
            
        bone_screen_pos = SDK.WorldToScreen(entity.getBonePosition(6), view_matrix)
        
        if bone_screen_pos.x > 0 and bone_screen_pos.y > 0:
            distance = SDK.getDistanceFromCenter(bone_screen_pos, Fov)
            if distance > best_distance and distance > 0:
                best_entity = entity
                best_distance = distance

    return best_entity


def getBestBone(entity: csEntity):
    """Find the most optimal bone to target"""
    best_distance = float('-inf')
    best_bone = 6
    view_matrix = SDK.getViewMatrix()

    for bone in GameVar.BoneList:
        bone_screen_pos = SDK.WorldToScreen(entity.getBonePosition(bone), view_matrix)

        if bone_screen_pos.x > 0 and bone_screen_pos.y > 0:
            distance = SDK.getDistanceFromCenter(bone_screen_pos, 360)
            if distance > best_distance and distance > 0:
                best_bone = bone
                best_distance = distance

    return best_bone


def Function():
    """Main aimbot function"""
    target_entity = csEntity(0)

    while AimBotStatus:
        if not Game.WindowIsOpen():
            time.sleep(0.01)
            continue

        # Check shot limit
        if MaxShot > 0 and GameVar.LocalPlayer.getShotFired() >= MaxShot:
            continue
        
        # Check if aimbot should be active
        if (Game.KeyStatus(VirtualKey) and 
            GameVar.LocalPlayer.Alive and 
            GameVar.LocalPlayer.WeaponCattegory not in [WEAPON_KNIFE, WEAPON_BOMB]):

            # Get new target if needed
            if target_entity.Player == 0 or target_entity.getHealth() <= 0:
                target_entity = getBestTarget()

            if target_entity.Valid():
                # Get target bone position
                target_bone = getBestBone(target_entity) if Bone == -1 else Bone
                bone_position = target_entity.getBonePosition(target_bone)

                # Convert to screen coordinates
                view_matrix = SDK.getViewMatrix()
                screen_pos = SDK.WorldToScreen(bone_position, view_matrix)

                if screen_pos.x > 0 and screen_pos.y > 0:
                    # Calculate mouse movement
                    mouse_delta = Vector2()
                    mouse_delta.x = screen_pos.x - (GameVar.WindowScreen.x / 2)
                    mouse_delta.y = screen_pos.y - (GameVar.WindowScreen.y / 2)

                    MoveMouseSmooth(mouse_delta.x, mouse_delta.y, Smooth)

        else:
            target_entity.Player = 0

        time.sleep(0.01)
