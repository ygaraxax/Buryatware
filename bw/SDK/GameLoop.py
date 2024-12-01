import threading, win32api
from time import *

from Tool.Offsets import *
from Tool.Memory import *

from SDK.GameVar import *

from Classes.Player import *
from Classes.Entity import *



class GameLoop():
    SlowSleep = 0.5
    AverageSleep = 0.25
    FastSleep = 0.1

    Mutex = threading.Lock()


    def Disposable():
        GameVar.WindowScreen.x = win32api.GetSystemMetrics(0)
        GameVar.WindowScreen.y = win32api.GetSystemMetrics(1)


    def Slow():
        while (True):
            GameLoop.Mutex.acquire()

            GameVar.LocalPlayer = csPlayer(Memory.Read.longlong(Game.Client + dwLocalPlayerPawn))
            GameVar.dwEntityList = Memory.Read.longlong(Game.Client + dwEntityList)

            GameLoop.Mutex.release()
            sleep(GameLoop.SlowSleep)


    def Fast():
        while (True):
            GameVar.EntityList.clear()

            if (Game.WindowIsOpen()):
                GameLoop.Mutex.acquire()

                for Index in range(0, 64):
                    Entity = csEntity(0)

                    Entity.Controller = Entity.getController(Index)
                    Entity.Player = Entity.getPawn(Entity.Controller)

                    if (Entity.Valid() and (Entity.Player != GameVar.LocalPlayer.Player)):
                        GameVar.EntityList.append(Entity)

                GameLoop.Mutex.release()
            sleep(GameLoop.FastSleep)


    def Start():
        GameLoop.Disposable()
        threading.Thread(target = GameLoop.Slow).start()
        threading.Thread(target = GameLoop.Fast).start()