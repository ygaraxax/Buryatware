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


VisualStatus = False
BoxESPStatus = True
HealthStatus = True
WeaponStatus = True
LineStatus = False
TeamCheck = True

CrosshairStatus = False
CrosshairSize = 6

BombESPStatus = True

BoxESPColor = "#00aaff"
LineColor = "#ff0000"
CrosshairColor = "#ffffff"


def Function():
    GameOverlay = Overlay("Box ESP")

    while (VisualStatus):
        GameOverlay.BeginRender()

        if (Game.WindowIsOpen()):

            for Entity in GameVar.EntityList:
                if (TeamCheck and Entity.getTeam() == GameVar.LocalPlayer.Team):
                    continue
                
                FeetPosition = Entity.getOriginPosition()
                HeadPosition = Entity.getHeadPosition()

                Matrix = SDK.getViewMatrix()

                Feet = SDK.WorldToScreen(FeetPosition, Matrix)
                Head = SDK.WorldToScreen(HeadPosition, Matrix)

                if ((Head.x > 0 and Head.y > 0) and (Feet.x > 0 and Feet.y > 0)):
                    Height = Feet.y - Head.y
                    Width = Height / 2


                    if (BoxESPStatus):
                        GameOverlay.DrawRect(Head.x - Width / 2, Head.y, Head.x + Width / 2, Head.y + Height, BoxESPColor)
                        #GameOverlay.DrawRectangle(Head.x - Width / 2, Head.y, Width, Height, GameOverlay.RGBtoHEX(255, 255, 0))


                    if (HealthStatus):
                        Health = Entity.getHealth()
                        Armor = Entity.getArmor()

                        GameOverlay.DrawFilledRectangle(Head.x - Width / 2 - (Height / 9), Head.y, Width / 10, Height,abs(Health * Height / 100), GameOverlay.RGBtoHEX(255, 0, 0))

                        if (Armor > 0):
                            GameOverlay.DrawFilledRectangle(Head.x + Width / 2 + (Height / 11), Head.y, Width / 10, Height,abs(Armor * Height / 100), GameOverlay.RGBtoHEX(0, 168, 255))


                    if (WeaponStatus):
                        WeaponID = Entity.getWeaponID()
                        WeaponCategory = Weapon.getWeaponCategory(WeaponID)

                        if ((WeaponCategory != WEAPON_KNIFE) and (WeaponCategory != WEAPON_GRENADE) and (WeaponCategory != WEAPON_BOMB) and (WeaponCategory != WEAPON_TASER)):
                            Ammo = Entity.getAmmo()
                            Scopted = Entity.getScoped()

                            if (Scopted):
                                GameOverlay.DrawText(Feet.x, Feet.y + (Height / 10), f"{Weapon.getWeaponName(WeaponID)} ({Ammo}) (SCOPED)", GameOverlay.RGBtoHEX(255, 255, 255))
                            
                            else:
                                GameOverlay.DrawText(Feet.x, Feet.y + (Height / 10), f"{Weapon.getWeaponName(WeaponID)} ({Ammo})", GameOverlay.RGBtoHEX(255, 255, 255))
                        
                        else:
                            GameOverlay.DrawText(Feet.x, Feet.y + (Height / 10), f"{Weapon.getWeaponName(WeaponID)}", GameOverlay.RGBtoHEX(255, 255, 255))


                    if (LineStatus):
                        GameOverlay.DrawLine(GameVar.WindowScreen.x / 2, 0 , Head.x, Head.y - (Height / 11), LineColor)


            if (BombESPStatus):        
                if (csBomb.isPlanted()):
                    BombPosition = csBomb.getPositionWTS()
                    BombTime = csBomb.getBombTime()
                    DefuseTime = csBomb.getDefuseTime()

                    if (BombPosition.x > 0 and BombPosition.y > 0):

                        if (DefuseTime > 0):
                            GameOverlay.DrawText(BombPosition.x, BombPosition.y, f"BOMB ({round(BombTime, 2)} | {round(DefuseTime, 2)})", GameOverlay.RGBtoHEX(255, 255, 254))

                        else:
                            GameOverlay.DrawText(BombPosition.x, BombPosition.y, f"BOMB ({round(BombTime, 2)})", GameOverlay.RGBtoHEX(255, 255, 254))


            if (AimBot.AimBotFOVStatus):
                if (GameVar.LocalPlayer.Alive):
                    GameOverlay.DrawCircle(GameVar.WindowScreen.x / 2, GameVar.WindowScreen.y / 2, AimBot.Fov, AimBot.AimFOVColor)


            if (CrosshairStatus):
                if ((GameVar.LocalPlayer.WeaponCattegory == WEAPON_SNIPER or GameVar.LocalPlayer.WeaponCattegory == WEAPON_AUTOSNIPER)):
                    GameOverlay.DrawLine(GameVar.WindowScreen.x / 2, GameVar.WindowScreen.y / 2 - CrosshairSize, GameVar.WindowScreen.x / 2, GameVar.WindowScreen.y / 2 + CrosshairSize + 1, CrosshairColor)
                    GameOverlay.DrawLine(GameVar.WindowScreen.x / 2 - CrosshairSize, GameVar.WindowScreen.y / 2, GameVar.WindowScreen.x / 2 + CrosshairSize + 1, GameVar.WindowScreen.y / 2, CrosshairColor)


        GameOverlay.EndRender()
        time.sleep(0.01)

    GameOverlay.Destory()
