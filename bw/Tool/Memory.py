from ctypes import *
from ctypes.wintypes import *
from win32process import *
from win32event import *

from Tool.Process import *


class Memory():
    class Read():
        def longlong(Address):
            Buffer = c_longlong()
            windll.kernel32.ReadProcessMemory(Game.Process, ctypes.c_void_p(Address), byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value
        

        def int(Address):
            Buffer = c_int()
            windll.kernel32.ReadProcessMemory(Game.Process, ctypes.c_void_p(Address), byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value


        def float(Address):
            Buffer = c_float()
            windll.kernel32.ReadProcessMemory(Game.Process, ctypes.c_void_p(Address), byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value


        def bool(Address):
            Buffer = c_bool()
            windll.kernel32.ReadProcessMemory(Game.Process, ctypes.c_void_p(Address), byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value


        def short(Address):
            Buffer = c_short()
            windll.kernel32.ReadProcessMemory(Game.Process, ctypes.c_void_p(Address), byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value