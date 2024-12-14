from ctypes import *
from ctypes.wintypes import *
from win32process import *
from win32event import *

from Tool.Process import *


class Memory:
    class Read:
        # Helper method to avoid code duplication in read operations
        @staticmethod
        def _read_memory(address, buffer_type):
            buffer = buffer_type()
            windll.kernel32.ReadProcessMemory(
                Game.Process,
                ctypes.c_void_p(address), 
                byref(buffer),
                sizeof(buffer),
                0
            )
            return buffer.value

        @staticmethod
        def longlong(address):
            return Memory.Read._read_memory(address, c_longlong)

        @staticmethod 
        def int(address):
            return Memory.Read._read_memory(address, c_int)

        @staticmethod
        def float(address):
            return Memory.Read._read_memory(address, c_float)

        @staticmethod
        def bool(address):
            return Memory.Read._read_memory(address, c_bool)

        @staticmethod
        def short(address):
            return Memory.Read._read_memory(address, c_short)
