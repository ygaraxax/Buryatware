import ctypes, psutil, win32api
from win32gui import GetForegroundWindow, GetWindowText, SetForegroundWindow, FindWindow


class Module():
   def GetLastError():
      Buffer = ctypes.create_unicode_buffer(0x100)
      ctypes.windll.kernel32.FormatMessageW(0x12FF, None, ctypes.windll.kernel32.GetLastError, 1024, Buffer, len(Buffer), None)


   class ModuleSnap():
      def __init__(self, ProcessID):
         self.SnapShot = ctypes.windll.kernel32.CreateToolhelp32Snapshot(8 | 16, ProcessID)
         
         if -1 == self.SnapShot:
            raise OSError(Module.GetLastError())


      def __del__(self):
         if not ctypes.windll.kernel32.CloseHandle(self.SnapShot):
            Module.GetLastError()

      def __enter__(self): return self
      
      def __exit__(self):  del self


   class tagMODULEENTRY32(ctypes.Structure):
      _fields_ = [
         ("dwSize",        ctypes.c_ulong),
         ("th32ModuleID",  ctypes.c_ulong),
         ("th32ProcessID", ctypes.c_ulong),
         ("GlblcntUsage",  ctypes.c_ulong),
         ("ProccntUsage",  ctypes.c_ulong),
         ("modBaseAddr",   ctypes.POINTER(ctypes.c_byte)),
         ("modBaseSize",   ctypes.c_ulong),
         ("hModule",       ctypes.c_void_p),
         ("szModule",      ctypes.c_char * 256),
         ("_szExePath",    ctypes.c_char * 260),
      ]


      def __init__(self):
         self.dwSize = ctypes.sizeof(self)


      @property
      def szExePath(self):
         return str(self._szExePath, "ascii", "replace")
      

   def GetModuleAddress(ProcessID, Name):
      HNDL = Module.ModuleSnap(ProcessID)
      Dll  = Module.tagMODULEENTRY32()

      Lib  = ctypes.windll.kernel32.Module32First(HNDL.SnapShot, ctypes.byref(Dll))

      while (Lib):
        if (Dll.szModule.decode() == Name):
            return Dll.hModule

        Lib = ctypes.windll.kernel32.Module32Next(HNDL.SnapShot, ctypes.byref(Dll))

      return 0


class Game():
    Process = 0
    Client, Server = 0, 0
    WindowName = ""
    HWND = 0


    def GetProcessID(Name):
        for Process in psutil.process_iter():
            if Process.name() == Name:
                return Process.pid


    def Connect(Name, WindowName):
        Game.ProcessID = Game.GetProcessID(Name)

        if (Game.ProcessID):
            Game.HWND = FindWindow("SDL_app", WindowName)
            Game.WindowName = WindowName

            Game.Client = Module.GetModuleAddress(Game.ProcessID, "client.dll")
            Game.Server = Module.GetModuleAddress(Game.ProcessID, "server.dll")

            Game.Process = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, Game.ProcessID)

        return Game.ProcessID


    def WindowIsOpen():
      return GetWindowText(GetForegroundWindow()) == Game.WindowName
    

    def KeyStatus(VirtualKeyboard):
       return (win32api.GetAsyncKeyState(VirtualKeyboard) or VirtualKeyboard == 0) and Game.WindowIsOpen()
   