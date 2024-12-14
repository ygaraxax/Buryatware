import time

from Tool.Process import *
from Tool.Device.Mouse import *

from Classes.Weapon import *
from SDK.GameVar import *


# Configuration settings
AUTO_PISTOL_ENABLED = False  # Flag to enable/disable auto pistol
TRIGGER_KEY = 6  # Virtual key code for activation


def auto_pistol_loop():
    """Main auto pistol function that handles automatic firing of pistols"""
    while (AUTO_PISTOL_ENABLED):
        # Check if trigger key is pressed and game window is active
        if (Game.KeyStatus(TRIGGER_KEY) and Game.WindowIsOpen()):
            # Only auto-fire if player is holding a pistol
            if (GameVar.LocalPlayer.WeaponCattegory == WEAPON_PISTOL):
                ClickMouse()
        
        # Small delay to prevent excessive CPU usage
        time.sleep(0.01)
