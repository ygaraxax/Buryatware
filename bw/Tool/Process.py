import ctypes, psutil, win32api
from win32gui import GetForegroundWindow, GetWindowText, SetForegroundWindow, FindWindow


class Module:
    # Helper method to get last Windows error message
    @staticmethod
    def GetLastError():
        buffer = ctypes.create_unicode_buffer(0x100)
        ctypes.windll.kernel32.FormatMessageW(0x12FF, None, 
            ctypes.windll.kernel32.GetLastError, 1024, buffer, len(buffer), None)
        return buffer.value

    # Context manager for module snapshots
    class ModuleSnap:
        def __init__(self, process_id):
            self.snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot(8 | 16, process_id)
            if self.snapshot == -1:
                raise OSError(Module.GetLastError())

        def __del__(self):
            if not ctypes.windll.kernel32.CloseHandle(self.snapshot):
                Module.GetLastError()

        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.__del__()

    # Structure for module information
    class tagMODULEENTRY32(ctypes.Structure):
        _fields_ = [
            ("dwSize", ctypes.c_ulong),
            ("th32ModuleID", ctypes.c_ulong), 
            ("th32ProcessID", ctypes.c_ulong),
            ("GlblcntUsage", ctypes.c_ulong),
            ("ProccntUsage", ctypes.c_ulong),
            ("modBaseAddr", ctypes.POINTER(ctypes.c_byte)),
            ("modBaseSize", ctypes.c_ulong),
            ("hModule", ctypes.c_void_p),
            ("szModule", ctypes.c_char * 256),
            ("_szExePath", ctypes.c_char * 260),
        ]

        def __init__(self):
            self.dwSize = ctypes.sizeof(self)

        @property
        def szExePath(self):
            return str(self._szExePath, "ascii", "replace")

    # Get base address of a module in a process
    @staticmethod
    def GetModuleAddress(process_id, module_name):
        with Module.ModuleSnap(process_id) as handle:
            module_entry = Module.tagMODULEENTRY32()
            has_next = ctypes.windll.kernel32.Module32First(handle.snapshot, ctypes.byref(module_entry))
            
            while has_next:
                if module_entry.szModule.decode() == module_name:
                    return module_entry.hModule
                has_next = ctypes.windll.kernel32.Module32Next(handle.snapshot, ctypes.byref(module_entry))
            
            return 0


class Game:
    # Game process information
    Process = 0
    Client = 0  
    Server = 0
    WindowName = ""
    HWND = 0

    @staticmethod
    def GetProcessID(process_name):
        for process in psutil.process_iter():
            if process.name() == process_name:
                return process.pid
        return None

    @staticmethod
    def Connect(process_name, window_name):
        Game.ProcessID = Game.GetProcessID(process_name)

        if Game.ProcessID:
            Game.HWND = FindWindow("SDL_app", window_name)
            Game.WindowName = window_name

            Game.Client = Module.GetModuleAddress(Game.ProcessID, "client.dll")
            Game.Server = Module.GetModuleAddress(Game.ProcessID, "server.dll")

            Game.Process = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, Game.ProcessID)

        return Game.ProcessID

    @staticmethod
    def WindowIsOpen():
        return GetWindowText(GetForegroundWindow()) == Game.WindowName

    @staticmethod 
    def KeyStatus(virtual_key):
        return (win32api.GetAsyncKeyState(virtual_key) or virtual_key == 0) and Game.WindowIsOpen()
