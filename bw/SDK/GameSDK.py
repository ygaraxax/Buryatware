from math import *

from Tool.Memory import *
from Tool.Vector import *
from Tool.Process import *

from SDK.GameVar import *



class SDK():
    def getViewMatrix():
        ViewMatrix = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        for Index in range(len(ViewMatrix)):
            ViewMatrix[Index] = Memory.Read.float(Game.Client + dwViewMatrix + (Index * 4))

        return ViewMatrix


    def WorldToScreen(BonePosition: Vector3, ViewMatrix: list):
        Matrix = VecMatrix()
        NDC, BonePositionWTS = Vector3(), Vector3()
        
        Matrix.w = BonePosition.x * ViewMatrix[12] + BonePosition.y * ViewMatrix[13] + BonePosition.z * ViewMatrix[14] + ViewMatrix[15]

        if (Matrix.w > 0.001):
            Matrix.x = BonePosition.x * ViewMatrix[0] + BonePosition.y * ViewMatrix[1] + BonePosition.z * ViewMatrix[2] + ViewMatrix[3]
            Matrix.y = BonePosition.x * ViewMatrix[4] + BonePosition.y * ViewMatrix[5] + BonePosition.z * ViewMatrix[6] + ViewMatrix[7]

            NDC.x = Matrix.x / Matrix.w
            NDC.y = Matrix.y / Matrix.w
            
            BonePositionWTS.x = (GameVar.WindowScreen.x / 2 * NDC.x) + (NDC.x + GameVar.WindowScreen.x / 2)
            BonePositionWTS.y = -(GameVar.WindowScreen.y / 2 * NDC.y) + (NDC.y + GameVar.WindowScreen.y / 2)


        return BonePositionWTS
    

    def Distance(Player: Vector3, Entity: Vector3):
        return sqrt(pow(Player.x - Entity.x, 2) + pow(Player.y - Entity.y, 2) + pow(Player.z - Entity.z, 2))
    

    def getDistanceFromCenter(BonePosition: Vector3, FOV):
        Distance = Vector2()

        Distance.x = BonePosition.x - (GameVar.WindowScreen.x / 2)
        Distance.y = BonePosition.y - (GameVar.WindowScreen.y / 2)

        return FOV * FOV - (Distance.x * Distance.x + Distance.y * Distance.y)
    

    def getEntityInCross():
        CrossID = Memory.Read.int(GameVar.LocalPlayer.Player + m_iIDEntIndex)

        if (CrossID > 0):
            EntityEntry = Memory.Read.longlong(GameVar.dwEntityList + 0x8 * (CrossID >> 9) + 0x10)
            if (not EntityEntry): return 0

            Entity = Memory.Read.longlong(EntityEntry + 120 * (CrossID & 0x1FF))
            return Entity
        
        return 0

        
