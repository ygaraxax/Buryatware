# Import required modules
from os import system
system("pip install win32api")

import SDK.GameLoop as GameLoop
from Tool.Process import *
import UI.MainUI as GUI
import UI.AntiAimAsistUI as AntiAimWindow
import threading
import signal
import sys
import os
import webbrowser

# Import cheat functions
import Function.Visual as Visual
import Function.AimBot as AimBot 
import Function.TriggerBot as TriggerBot
import Function.AutoPistol as AutoPistol
import Function.BunnyHop as BunnyHop
import Function.AntiAim as AntiAim

# Initialize game connection
Game.Connect("cs2.exe", "Counter-Strike 2")
GameLoop.GameLoop.Start()

if __name__ == "__main__":
    # Initialize UI
    app = GUI.QtWidgets.QApplication(sys.argv)
    ui = GUI.Widget()
    ui.show()

    # Helper functions to start cheat features
    def start_feature(feature, checkbox):
        """Generic function to start a cheat feature in a new thread"""
        feature.Status = checkbox.checkState()
        if feature.Status:
            threading.Thread(target=feature.Function).start()

    def StartVisual():
        start_feature(Visual, ui.visualCheckBox)

    def StartAimBot():
        start_feature(AimBot, ui.aimAsistCheckBox)

    def StartTriggerBot():
        start_feature(TriggerBot, ui.triggerBotCheckBox)

    def StartAutoPistol():
        start_feature(AutoPistol, ui.autoPistolCheckBox)

    def StartBunnyHop():
        start_feature(BunnyHop, ui.bunnyHopCheckBox)

    def StartAntiAim():
        start_feature(AntiAim, ui.antiAimCheckBox)

    # Connect UI buttons to settings windows
    ui.visualSettingButton.clicked.connect(ui.ShowVisualWindow)
    ui.aimAsistSettingButton.clicked.connect(ui.ShowAimBotWindow)
    ui.triggerBotSettingButton.clicked.connect(ui.ShowTriggerBotWindow)
    ui.autoPistolSettingButton.clicked.connect(ui.ShowAutoPistolWindow)

    # Connect checkboxes to feature start functions
    ui.visualCheckBox.stateChanged.connect(StartVisual)
    ui.aimAsistCheckBox.stateChanged.connect(StartAimBot)
    ui.triggerBotCheckBox.stateChanged.connect(StartTriggerBot)
    ui.autoPistolCheckBox.stateChanged.connect(StartAutoPistol)
    ui.bunnyHopCheckBox.stateChanged.connect(StartBunnyHop)
    ui.antiAimCheckBox.stateChanged.connect(StartAntiAim)

    # Connect utility buttons
    ui.closeButton.clicked.connect(lambda: os.kill(os.getpid(), signal.SIGTERM))
    ui.questionButton.clicked.connect(lambda: webbrowser.open("https://t.me/burware/", new=2))

    sys.exit(app.exec_())
