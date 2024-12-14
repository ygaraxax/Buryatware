import time

from Tool.Process import *
from Tool.Device.Keyboard import *

from Classes.Player import *
from SDK.GameVar import *


# Configuration
BHOP_ENABLED = False  # Flag to enable/disable bunny hop
JUMP_KEY = 0x20  # Space bar virtual key code
SLEEP_TIME = 0.03  # Sleep duration between checks

# Player movement states
IN_AIR = 65664
IN_GROUND = 65665 
IN_SITTING = 65667


def bunny_hop():
    """Main bunny hop function that handles automatic jumping"""
    while (BHOP_ENABLED):
        # Check if game window is active and jump key is pressed
        if (Game.WindowIsOpen() and Game.KeyStatus(JUMP_KEY)):
            if (GameVar.LocalPlayer.Alive):
                move_state = GameVar.LocalPlayer.getMoveFlag()
                
                # Force jump if player is on ground or crouching
                if (move_state == IN_GROUND or move_state == IN_SITTING):
                    ForceJump()

        time.sleep(SLEEP_TIME)
