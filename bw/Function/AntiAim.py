import time
from Tool.Process import *
from Tool.Device.Mouse import *

from Classes.Entity import *
from Classes.Player import *
from Classes.Weapon import *

from SDK.GameVar import *
from SDK.GameSDK import *

from SDK.Render import *

# Настройки
RotateLeft = True  # Включить вращение влево
RotateSpeed = 500000   # Скорость вращения (пиксели)
AntiAimStatus = False
AntiAimFOVStatus = False
TeamCheck = True

Bone = 6
Fov = 90
Smooth = 1
VirtualKey = 6
MaxShot = 5

AimFOVColor = "#ffffff"


def Function():
    while RotateLeft:
        if Game.WindowIsOpen() and GameVar.LocalPlayer.Alive:
            # Перемещение мыши влево
            MoveMouseSmooth(-RotateSpeed, 0, 1)  # Вращение влево по оси X
        time.sleep(0.01)  # Задержка для уменьшения нагрузки на процессор

if __name__ == "__main__":
    Function()