import win32api, win32con


def MoveMouseSmooth(x, y, Smooth):
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x / Smooth), int(y / Smooth), 0, 0)


def MoveMouse(x, y):
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x), int(y), 0, 0)


def ClickMouse():
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
