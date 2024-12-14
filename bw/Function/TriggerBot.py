import time

from Tool.Process import *
from Tool.Device.Mouse import *

from Classes.Entity import *
from Classes.Player import *
from Classes.Weapon import *

from SDK.GameVar import *
from SDK.GameSDK import *


# TriggerBot Configuration
TRIGGER_BOT_ENABLED = False  # Main toggle for triggerbot
TEAM_CHECK = True  # Enable friendly fire check

MAX_SHOTS = 3  # Maximum shots before reset
TRIGGER_KEY = 6  # Virtual key code for activation  
DELAY_MS = 110  # Delay in milliseconds before shooting


def is_valid_target():
    """Check if there is a valid target in crosshair"""
    target = csEntity(SDK.getEntityInCross())

    if target.Valid():
        # Skip if target is teammate and team check is enabled
        if TEAM_CHECK and target.getTeam() == GameVar.LocalPlayer.Team:
            return False
        
        # Add artificial delay and verify target still valid
        time.sleep(DELAY_MS / 1000)
        return csEntity(SDK.getEntityInCross()).Valid()
        
    return False


def trigger_bot_loop():
    """Main triggerbot function that handles automatic firing"""
    while TRIGGER_BOT_ENABLED:
        if Game.KeyStatus(TRIGGER_KEY) and MAX_SHOTS > 0 and Game.WindowIsOpen():
            # Check if exceeded max shots
            if GameVar.LocalPlayer.getShotFired() >= MAX_SHOTS:
                continue
            
            # Verify scoped status for sniper weapons
            if GameVar.LocalPlayer.WeaponCattegory in [WEAPON_SNIPER, WEAPON_AUTOSNIPER]:
                if not GameVar.LocalPlayer.Scoped:
                    continue
            
            # Fire if valid target acquired
            if is_valid_target():
                ClickMouse()
        
        time.sleep(0.01)
