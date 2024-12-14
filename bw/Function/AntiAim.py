import time
from Tool.Process import *
from Tool.Device.Mouse import *

from Classes.Entity import *
from Classes.Player import *
from Classes.Weapon import *

from SDK.GameVar import *
from SDK.GameSDK import *

from SDK.Render import *

# Anti-Aim Configuration
ROTATE_LEFT = True  # Enable left rotation
ROTATE_SPEED = 500000  # Rotation speed in pixels
SLEEP_TIME = 0.01  # Sleep duration between rotations

# Aim Configuration  
AIM_STATUS = False
AIM_FOV_STATUS = False
TEAM_CHECK = True

# Aim Parameters
BONE_TARGET = 6
FOV = 90 
SMOOTH = 1
VIRTUAL_KEY = 6
MAX_SHOTS = 5

AIM_FOV_COLOR = "#ffffff"


def rotate_continuously():
    """
    Main anti-aim function that continuously rotates the view angle
    while game window is open and local player is alive
    """
    while ROTATE_LEFT:
        if Game.WindowIsOpen() and GameVar.LocalPlayer.Alive:
            # Smooth mouse movement to the left on X axis
            MoveMouseSmooth(-ROTATE_SPEED, 0, 1)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    rotate_continuously()
