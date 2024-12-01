import win32api, win32con, time
import Tool.Process as Process


def ForceJump():
    win32api.SendMessage(Process.Game.HWND, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
    time.sleep(0.05)
    win32api.SendMessage(Process.Game.HWND, win32con.WM_KEYUP, win32con.VK_SPACE, 0)