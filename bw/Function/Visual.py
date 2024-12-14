import time

from Tool.Process import *

from Classes.Entity import *
from Classes.Player import *
from Classes.Weapon import *
from Classes.Bomb import *

from SDK.GameVar import *
from SDK.GameSDK import *
from SDK.Render import *

import Function.AimBot as AimBot


# Visual settings
VisualStatus = False
BoxESPStatus = True
HealthStatus = True
WeaponStatus = True
LineStatus = False
TeamCheck = True

# Crosshair settings
CrosshairStatus = False
CrosshairSize = 6

# Bomb ESP settings
BombESPStatus = True

# ESP colors
BoxESPColor = "#00aaff"
LineColor = "#ff0000" 
CrosshairColor = "#ffffff"


def draw_player_esp(overlay, entity, matrix):
    """Draw ESP elements for a player entity"""
    feet_pos = entity.getOriginPosition()
    head_pos = entity.getHeadPosition()

    feet = SDK.WorldToScreen(feet_pos, matrix)
    head = SDK.WorldToScreen(head_pos, matrix)

    if not ((head.x > 0 and head.y > 0) and (feet.x > 0 and feet.y > 0)):
        return

    height = feet.y - head.y
    width = height / 2

    # Draw bounding box
    if BoxESPStatus:
        overlay.DrawRect(head.x - width/2, head.y, head.x + width/2, head.y + height, BoxESPColor)

    # Draw health and armor bars
    if HealthStatus:
        health = entity.getHealth()
        armor = entity.getArmor()
        
        overlay.DrawFilledRectangle(
            head.x - width/2 - (height/9), head.y,
            width/10, height, abs(health * height/100),
            overlay.RGBtoHEX(255, 0, 0)
        )

        if armor > 0:
            overlay.DrawFilledRectangle(
                head.x + width/2 + (height/11), head.y,
                width/10, height, abs(armor * height/100),
                overlay.RGBtoHEX(0, 168, 255)
            )

    # Draw weapon info
    if WeaponStatus:
        draw_weapon_info(overlay, entity, feet, height)

    # Draw line to player
    if LineStatus:
        overlay.DrawLine(GameVar.WindowScreen.x/2, 0, head.x, head.y - (height/11), LineColor)


def draw_weapon_info(overlay, entity, feet_pos, height):
    """Draw weapon name and ammo info"""
    weapon_id = entity.getWeaponID()
    weapon_category = Weapon.getWeaponCategory(weapon_id)
    
    if weapon_category not in [WEAPON_KNIFE, WEAPON_GRENADE, WEAPON_BOMB, WEAPON_TASER]:
        ammo = entity.getAmmo()
        scoped = entity.getScoped()
        
        weapon_text = f"{Weapon.getWeaponName(weapon_id)} ({ammo})"
        if scoped:
            weapon_text += " (SCOPED)"
    else:
        weapon_text = Weapon.getWeaponName(weapon_id)
        
    overlay.DrawText(feet_pos.x, feet_pos.y + (height/10), weapon_text, overlay.RGBtoHEX(255, 255, 255))


def draw_bomb_esp(overlay):
    """Draw bomb timer and defuse info"""
    if not (BombESPStatus and csBomb.isPlanted()):
        return
        
    bomb_pos = csBomb.getPositionWTS()
    if not (bomb_pos.x > 0 and bomb_pos.y > 0):
        return
        
    bomb_time = csBomb.getBombTime()
    defuse_time = csBomb.getDefuseTime()

    if defuse_time > 0:
        text = f"BOMB ({round(bomb_time, 2)} | {round(defuse_time, 2)})"
    else:
        text = f"BOMB ({round(bomb_time, 2)})"
        
    overlay.DrawText(bomb_pos.x, bomb_pos.y, text, overlay.RGBtoHEX(255, 255, 254))


def draw_crosshair(overlay):
    """Draw custom crosshair for sniper weapons"""
    if not (CrosshairStatus and GameVar.LocalPlayer.Alive):
        return
        
    if GameVar.LocalPlayer.WeaponCattegory in [WEAPON_SNIPER, WEAPON_AUTOSNIPER]:
        center_x = GameVar.WindowScreen.x/2
        center_y = GameVar.WindowScreen.y/2
        
        overlay.DrawLine(center_x, center_y - CrosshairSize,
                        center_x, center_y + CrosshairSize + 1, CrosshairColor)
        overlay.DrawLine(center_x - CrosshairSize, center_y,
                        center_x + CrosshairSize + 1, center_y, CrosshairColor)


def Function():
    """Main ESP rendering loop"""
    game_overlay = Overlay("Box ESP")

    while VisualStatus:
        game_overlay.BeginRender()

        if Game.WindowIsOpen():
            matrix = SDK.getViewMatrix()

            # Draw player ESP
            for entity in GameVar.EntityList:
                if TeamCheck and entity.getTeam() == GameVar.LocalPlayer.Team:
                    continue
                draw_player_esp(game_overlay, entity, matrix)

            # Draw bomb ESP
            draw_bomb_esp(game_overlay)

            # Draw aim FOV
            if AimBot.AimBotFOVStatus and GameVar.LocalPlayer.Alive:
                game_overlay.DrawCircle(GameVar.WindowScreen.x/2,
                                      GameVar.WindowScreen.y/2,
                                      AimBot.Fov, AimBot.AimFOVColor)

            # Draw custom crosshair
            draw_crosshair(game_overlay)

        game_overlay.EndRender()
        time.sleep(0.01)

    game_overlay.Destory()
