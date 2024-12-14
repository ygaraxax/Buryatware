from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QColorDialog

# Import UI windows
import UI.VisualUI as VisualWindow
import UI.AimAsistUI as AiBotWindow
import UI.AntiAimAsistUI as AntiAimWindow
import UI.TriggerBotUI as TriggerBotWindow
import UI.AutoPistolUI as AutoPistolWindow

# Import cheat functions
import Function.Visual as Visual
import Function.AimBot as AimBot
import Function.AntiAim as AntiAim
import Function.TriggerBot as TriggerBot
import Function.AutoPistol as AutoPistol

class Ui_Window(object):
    def setupUi(self, Window):
        # Main window setup
        Window.setObjectName("Window")
        Window.setWindowModality(QtCore.Qt.NonModal)
        Window.resize(943, 368)
        
        # Background setup
        self.Background = QtWidgets.QLabel(Window)
        self.Background.setGeometry(QtCore.QRect(0, 0, 951, 402))
        self.Background.setAutoFillBackground(False)
        self.Background.setStyleSheet("background-color: rgb(30, 30, 35);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(30, 30, 35);")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        
        # Title panel setup
        self.titlePanel = QtWidgets.QLabel(Window)
        self.titlePanel.setGeometry(QtCore.QRect(0, 0, 851, 23))
        self.titlePanel.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(245, 36, 250);\n"
"padding-left: 1px;")
        self.titlePanel.setObjectName("titlePanel")
        
        # Close button setup
        self.closeButton = QtWidgets.QPushButton(Window)
        self.closeButton.setGeometry(QtCore.QRect(915, 0, 25, 23))
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.closeButton.setTabletTracking(False)
        self.closeButton.setStyleSheet("QPushButton{\n"
"  background-color: rgb(225, 0, 0);\n"
"  border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(55, 55, 60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(60, 60, 65);\n"
"}\n"
"")
        self.closeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(22, 22))
        self.closeButton.setObjectName("closeButton")
        
        # Minimize button setup
        self.minimazeButton = QtWidgets.QPushButton(Window)
        self.minimazeButton.setGeometry(QtCore.QRect(855, 0, 25, 23))
        self.minimazeButton.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.minimazeButton.setStyleSheet("QPushButton{\n"
"  background-color: rgb(50, 50, 255);\n"
"  border: none;\n"
"  padding-top: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(55, 55, 60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(60, 60, 65);\n"
"}\n"
"")
        self.minimazeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Image/Subtract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimazeButton.setIcon(icon1)
        self.minimazeButton.setIconSize(QtCore.QSize(16, 16))
        self.minimazeButton.setObjectName("minimazeButton")
        
        # Visual features section
        self.visualChild = QtWidgets.QWidget(Window)
        self.visualChild.setGeometry(QtCore.QRect(5, 55, 200, 311))
        self.visualChild.setStyleSheet("border: 1px solid rgb(80, 80, 85)")
        self.visualChild.setObjectName("visualChild")
        
        # Visual checkbox setup
        self.visualCheckBox = QtWidgets.QCheckBox(self.visualChild)
        self.visualCheckBox.setGeometry(QtCore.QRect(5, 5, 61, 20))
        self.visualCheckBox.setStyleSheet("QCheckBox {\n"
"color: rgb(241, 242, 246);\n"
"spacing: 5px;\n"
"border: none;\n"
"font: 10pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator  {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: rgb(232, 65, 24);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color:  rgb(232, 65, 24);\n"
"}")
        self.visualCheckBox.setObjectName("visualCheckBox")
        
        # Visual settings button
        self.visualSettingButton = QtWidgets.QPushButton(self.visualChild)
        self.visualSettingButton.setGeometry(QtCore.QRect(175, 5, 20, 20))
        self.visualSettingButton.setStyleSheet("QPushButton{\n"
"  background-color: rgb(30, 30, 35);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgb(255, 255, 255);\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(190, 190, 190);\n"
"}")
        self.visualSettingButton.setObjectName("visualSettingButton")
        
        # Aim assist section
        self.aimAsistChild = QtWidgets.QWidget(Window)
        self.aimAsistChild.setGeometry(QtCore.QRect(210, 55, 200, 311))
        self.aimAsistChild.setStyleSheet("border: 1px solid rgb(80, 80, 85)")
        self.aimAsistChild.setObjectName("aimAsistChild")
        
        # Aim assist checkbox
        self.aimAsistCheckBox = QtWidgets.QCheckBox(self.aimAsistChild)
        self.aimAsistCheckBox.setGeometry(QtCore.QRect(5, 5, 81, 20))
        self.aimAsistCheckBox.setStyleSheet("QCheckBox {\n"
"color: rgb(241, 242, 246);\n"
"spacing: 5px;\n"
"border: none;\n"
"font: 10pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator  {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: rgb(232, 65, 24);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color:  rgb(232, 65, 24);\n"
"}")
        self.aimAsistCheckBox.setObjectName("aimAsistCheckBox")
        
        # Aim assist settings button
        self.aimAsistSettingButton = QtWidgets.QPushButton(self.aimAsistChild)
        self.aimAsistSettingButton.setGeometry(QtCore.QRect(175, 5, 20, 20))
        self.aimAsistSettingButton.setStyleSheet("QPushButton{\n"
"  background-color: rgb(30, 30, 35);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgb(255, 255, 255);\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(190, 190, 190);\n"
"}")
        self.aimAsistSettingButton.setObjectName("aimAsistSettingButton")
        
        # Trigger bot checkbox
        self.triggerBotCheckBox = QtWidgets.QCheckBox(self.aimAsistChild)
        self.triggerBotCheckBox.setGeometry(QtCore.QRect(5, 30, 111, 20))
        self.triggerBotCheckBox.setStyleSheet("QCheckBox {\n"
"color: rgb(241, 242, 246);\n"
"spacing: 5px;\n"
"border: none;\n"
"font: 10pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator  {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: rgb(232, 65, 24);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color:  rgb(232, 65, 24);\n"
"}")
        self.triggerBotCheckBox.setObjectName("triggerBotCheckBox")
        
        # Trigger bot settings button
        self.triggerBotSettingButton = QtWidgets.QPushButton(self.aimAsistChild)
        self.triggerBotSettingButton.setGeometry(QtCore.QRect(175, 30, 20, 20))
        self.triggerBotSettingButton.setStyleSheet("QPushButton{\n"
"  background-color: rgb(30, 30, 35);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgb(255, 255, 255);\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(190, 190, 190);\n"
"}")
        self.triggerBotSettingButton.setObjectName("triggerBotSettingButton")
        
        # Misc features section
        self.miscChild = QtWidgets.QWidget(Window)
        self.miscChild.setGeometry(QtCore.QRect(415, 55, 200, 311))
        self.miscChild.setStyleSheet("border: 1px solid rgb(80, 80, 85)")
        self.miscChild.setObjectName("miscChild")
        
        # Auto pistol checkbox
        self.autoPistolCheckBox = QtWidgets.QCheckBox(self.miscChild)
        self.autoPistolCheckBox.setGeometry(QtCore.QRect(5, 5, 91, 20))
        self.autoPistolCheckBox.setStyleSheet("QCheckBox {\n"
"color: rgb(241, 242, 246);\n"
"spacing: 5px;\n"
"border: none;\n"
"font: 10pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator  {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: rgb(232, 65, 24);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color:  rgb(232, 65, 24);\n"
"}")
        self.autoPistolCheckBox.setObjectName("autoPistolCheckBox")
        
        # Auto pistol settings button
        self.autoPistolSettingButton = QtWidgets.QPushButton(self.miscChild)
        self.autoPistolSettingButton.setGeometry(QtCore.QRect(175, 5, 20, 20))
        self.autoPistolSettingButton.setStyleSheet("QPushButton{\n"
"  background-color: rgb(30, 30, 35);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgb(255, 255, 255);\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(190, 190, 190);\n"
"}")
        self.autoPistolSettingButton.setObjectName("autoPistolSettingButton")
        
        # Bunny hop checkbox
        self.bunnyHopCheckBox = QtWidgets.QCheckBox(self.miscChild)
        self.bunnyHopCheckBox.setGeometry(QtCore.QRect(5, 30, 91, 20))
        self.bunnyHopCheckBox.setStyleSheet("QCheckBox {\n"
"color: rgb(241, 242, 246);\n"
"spacing: 5px;\n"
"border: none;\n"
"font: 10pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator  {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: rgb(232, 65, 24);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color:  rgb(232, 65, 24);\n"
"}")
        self.bunnyHopCheckBox.setObjectName("bunnyHopCheckBox")
        
        # Question button setup
        self.questionButton = QtWidgets.QPushButton(Window)
        self.questionButton.setGeometry(QtCore.QRect(885, 0, 25, 23))
        self.questionButton.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.questionButton.setStyleSheet("QPushButton{\n"
"  background-color: rgb(150, 150, 155);\n"
"  border: none;\n"
"  padding-top: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(55, 55, 60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(60, 60, 65);\n"
"}\n"
"")
        self.questionButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Image/Question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.questionButton.setIcon(icon2)
        self.questionButton.setIconSize(QtCore.QSize(16, 16))
        self.questionButton.setObjectName("questionButton")
        
        # Section title panels
        self.titlePanel_2 = QtWidgets.QLabel(Window)
        self.titlePanel_2.setGeometry(QtCore.QRect(0, 30, 951, 23))
        self.titlePanel_2.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(45, 246, 250);\n"
"padding-left: 1px;")
        self.titlePanel_2.setObjectName("titlePanel_2")
        
        # Rage assist section
        self.rageAsistChild = QtWidgets.QWidget(Window)
        self.rageAsistChild.setGeometry(QtCore.QRect(620, 55, 200, 311))
        self.rageAsistChild.setStyleSheet("border: 1px solid rgb(80, 80, 85)")
        self.rageAsistChild.setObjectName("rageAsistChild")
        
        # Anti aim checkbox
        self.antiAimCheckBox = QtWidgets.QCheckBox(self.rageAsistChild)
        self.antiAimCheckBox.setGeometry(QtCore.QRect(5, 5, 81, 20))
        self.antiAimCheckBox.setStyleSheet("QCheckBox {\n"
"color: rgb(241, 242, 246);\n"
"spacing: 5px;\n"
"border: none;\n"
"font: 10pt \"Arial\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox::indicator  {\n"
"width: 13px;\n"
"height: 13px;\n"
"border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: rgb(40,40,45);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"background-color: rgb(45,45,50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: rgb(232, 65, 24);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"background-color:  rgb(232, 65, 24);\n"
"}")
        self.antiAimCheckBox.setObjectName("antiAimCheckBox")
        
        # Decorative title panels
        self.titlePanel_3 = QtWidgets.QLabel(Window)
        self.titlePanel_3.setGeometry(QtCore.QRect(820, 50, 121, 23))
        self.titlePanel_3.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(255, 0, 0);\n"
"padding-left: 1px;")
        self.titlePanel_3.setObjectName("titlePanel_3")
        
        self.titlePanel_4 = QtWidgets.QLabel(Window)
        self.titlePanel_4.setGeometry(QtCore.QRect(820, 70, 121, 23))
        self.titlePanel_4.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(255, 165, 0);\n"
"padding-left: 1px;")
        self.titlePanel_4.setObjectName("titlePanel_4")
        
        self.titlePanel_5 = QtWidgets.QLabel(Window)
        self.titlePanel_5.setGeometry(QtCore.QRect(820, 90, 121, 23))
        self.titlePanel_5.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 0);\n"
"padding-left: 1px;")
        self.titlePanel_5.setObjectName("titlePanel_5")
        
        self.titlePanel_6 = QtWidgets.QLabel(Window)
        self.titlePanel_6.setGeometry(QtCore.QRect(820, 110, 121, 23))
        self.titlePanel_6.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 255, 20);\n"
"padding-left: 1px;")
        self.titlePanel_6.setObjectName("titlePanel_6")
        
        self.titlePanel_7 = QtWidgets.QLabel(Window)
        self.titlePanel_7.setGeometry(QtCore.QRect(820, 130, 121, 23))
        self.titlePanel_7.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 255, 255);\n"
"padding-left: 1px;")
        self.titlePanel_7.setObjectName("titlePanel_7")
        
        self.titlePanel_8 = QtWidgets.QLabel(Window)
        self.titlePanel_8.setGeometry(QtCore.QRect(820, 150, 121, 23))
        self.titlePanel_8.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 100, 255);\n"
"padding-left: 1px;")
        self.titlePanel_8.setObjectName("titlePanel_8")
        
        self.titlePanel_9 = QtWidgets.QLabel(Window)
        self.titlePanel_9.setGeometry(QtCore.QRect(820, 170, 121, 23))
        self.titlePanel_9.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(139, 0, 255);\n"
"padding-left: 1px;")
        self.titlePanel_9.setObjectName("titlePanel_9")
        
        self.titlePanel_19 = QtWidgets.QLabel(Window)
        self.titlePanel_19.setGeometry(QtCore.QRect(820, 340, 121, 23))
        self.titlePanel_19.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(33, 1, 0);\n"
"padding-left: 1px;")
        self.titlePanel_19.setObjectName("titlePanel_19")
        
        self.titlePanel_10 = QtWidgets.QLabel(Window)
        self.titlePanel_10.setGeometry(QtCore.QRect(820, 190, 121, 23))
        self.titlePanel_10.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(139, 0, 255);\n"
"padding-left: 1px;")
        self.titlePanel_10.setObjectName("titlePanel_10")
        
        self.titlePanel_11 = QtWidgets.QLabel(Window)
        self.titlePanel_11.setGeometry(QtCore.QRect(820, 210, 121, 23))
        self.titlePanel_11.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 100, 255);\n"
"padding-left: 1px;")
        self.titlePanel_11.setObjectName("titlePanel_11")
        
        self.titlePanel_12 = QtWidgets.QLabel(Window)
        self.titlePanel_12.setGeometry(QtCore.QRect(820, 230, 121, 23))
        self.titlePanel_12.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 255, 255);\n"
"padding-left: 1px;")
        self.titlePanel_12.setObjectName("titlePanel_12")
        
        self.titlePanel_13 = QtWidgets.QLabel(Window)
        self.titlePanel_13.setGeometry(QtCore.QRect(820, 250, 121, 23))
        self.titlePanel_13.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 255, 20);\n"
"padding-left: 1px;")
        self.titlePanel_13.setObjectName("titlePanel_13")
        
        self.titlePanel_14 = QtWidgets.QLabel(Window)
        self.titlePanel_14.setGeometry(QtCore.QRect(820, 270, 121, 23))
        self.titlePanel_14.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 0);\n"
"padding-left: 1px;")
        self.titlePanel_14.setObjectName("titlePanel_14")
        
        self.titlePanel_15 = QtWidgets.QLabel(Window)
        self.titlePanel_15.setGeometry(QtCore.QRect(820, 290, 121, 23))
        self.titlePanel_15.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(255, 165, 0);\n"
"padding-left: 1px;")
        self.titlePanel_15.setObjectName("titlePanel_15")
        
        self.titlePanel_16 = QtWidgets.QLabel(Window)
        self.titlePanel_16.setGeometry(QtCore.QRect(820, 310, 121, 23))
        self.titlePanel_16.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 12pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(255, 0, 0);\n"
"padding-left: 1px;")
        self.titlePanel_16.setObjectName("titlePanel_16")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Buryatware v2"))
        self.titlePanel.setText(_translate("Window", "BURYATWARE.CC                                                                                                                                                    t.me/burware"))
        self.visualCheckBox.setText(_translate("Window", "Visual"))
        self.visualSettingButton.setText(_translate("Window", "+"))
        self.aimAsistCheckBox.setText(_translate("Window", "Aim asist"))
        self.aimAsistSettingButton.setText(_translate("Window", "+"))
        self.triggerBotCheckBox.setText(_translate("Window", "Trigger Bot"))
        self.triggerBotSettingButton.setText(_translate("Window", "+"))
        self.autoPistolCheckBox.setText(_translate("Window", "Auto pistol"))
        self.autoPistolSettingButton.setText(_translate("Window", "+"))
        self.bunnyHopCheckBox.setText(_translate("Window", "Bunny hop"))
        self.titlePanel_2.setText(_translate("Window", "ESP                                           LEGIT                                        MISC                                         RAGE"))
        self.antiAimCheckBox.setText(_translate("Window", "AntiAim"))
        self.titlePanel_3.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_4.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_5.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_6.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_7.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_8.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_9.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_19.setText(_translate("Window", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic; text-decoration: underline;\">Release 2</span></p></body></html>"))
        self.titlePanel_10.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_11.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_12.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_13.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_14.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_15.setText(_translate("Window", "BURYATWARE"))
        self.titlePanel_16.setText(_translate("Window", "BURYATWARE"))
    def chengeBoxStatus(self): Visual.BoxESPStatus = self.VisualWin.boxESPCheckBox.isChecked()
    def changeTeamStatus(self): Visual.TeamCheck = self.VisualWin.teamCheckCheckBox.isChecked()
    def changeHealthBarStatus(self): Visual.HealthStatus = self.VisualWin.healthBarCheckBox.isChecked()
    def changeWeaponStatus(self): Visual.WeaponStatus = self.VisualWin.weaponCheckBox.isChecked()
    def changeLineStatus(self): Visual.LineStatus = self.VisualWin.lineCheckBox.isChecked()

    def changeCrosshairStatus(self): Visual.CrosshairStatus = self.VisualWin.crosshairESPCheckBox_2.isChecked()
    def changeCrosshairSize(self):
        self.VisualWin.sniperCrosshairLable.setText(f"{self.VisualWin.sniperCrosshairSlider.value()}")
        Visual.CrosshairSize = self.VisualWin.sniperCrosshairSlider.value()

    def changeBombStatus(self): Visual.BombESPStatus = self.VisualWin.BombTimerCheckBox.isChecked()

    def changeBoxESPColor(self):
        Color = QColorDialog.getColor()
        Visual.BoxESPColor = Color.name()

        self.VisualWin.boxESPColorEdit.setStyleSheet(f"background-color: {Visual.BoxESPColor}; border: none;")


    def changeLineColor(self):
        Color = QColorDialog.getColor()
        Visual.LineColor = Color.name()
        
        self.VisualWin.lineColorEdit.setStyleSheet(f"background-color: {Visual.LineColor}; border: none;")


    def changeCrosshairColor(self):
        Color = QColorDialog.getColor()
        Visual.CrosshairColor = Color.name()
        
        self.VisualWin.sniperCorsshairColorEdit.setStyleSheet(f"background-color: {Visual.CrosshairColor}; border: none;")


    def ShowVisualWindow(self):
        self.VisualWin = VisualWindow.Widget()

        self.VisualWin.boxESPCheckBox.stateChanged.connect(self.chengeBoxStatus)
        self.VisualWin.teamCheckCheckBox.stateChanged.connect(self.changeTeamStatus)
        self.VisualWin.healthBarCheckBox.stateChanged.connect(self.changeHealthBarStatus)
        self.VisualWin.weaponCheckBox.stateChanged.connect(self.changeWeaponStatus)
        self.VisualWin.lineCheckBox.stateChanged.connect(self.changeLineStatus)

        self.VisualWin.crosshairESPCheckBox_2.stateChanged.connect(self.changeCrosshairStatus)
        self.VisualWin.sniperCrosshairSlider.valueChanged.connect(self.changeCrosshairSize)

        self.VisualWin.BombTimerCheckBox.stateChanged.connect(self.changeBombStatus)

        self.VisualWin.boxESPColorEdit.clicked.connect(self.changeBoxESPColor)
        self.VisualWin.lineColorEdit.clicked.connect(self.changeLineColor)
        self.VisualWin.sniperCorsshairColorEdit.clicked.connect(self.changeCrosshairColor)

        self.VisualWin.show()


    def changeAimBotFOV(self):
        self.AimBotWin.FOVLable.setText(f"{self.AimBotWin.FOVSlider.value()}")
        AimBot.Fov = self.AimBotWin.FOVSlider.value()


    def changeAimBotSmooth(self):
        self.AimBotWin.smoothLable.setText(f"{self.AimBotWin.smoothSlider.value()}")
        AimBot.Smooth = self.AimBotWin.smoothSlider.value()


    def changeAimBotMaxShot(self):
        self.AimBotWin.maxShotLable.setText(f"{self.AimBotWin.maxShotSlider.value()}")
        AimBot.MaxShot = self.AimBotWin.maxShotSlider.value()


    def changeAimBotMouse(self):
        Mouse = self.AimBotWin.mouseListComboBox.currentText()

        if (Mouse == "MOUSE1"): AimBot.VirtualKey = 1
        if (Mouse == "MOUSE2"): AimBot.VirtualKey = 2
        if (Mouse == "MOUSE4"): AimBot.VirtualKey = 4
        if (Mouse == "MOUSE5"): AimBot.VirtualKey = 5
        if (Mouse == "MOUSE6"): AimBot.VirtualKey = 6
        if (Mouse == "None"): AimBot.VirtualKey = 0


    def changeAimBotBone(self):
        Bone = self.AimBotWin.boneListComboBox.currentText()

        if (Bone == "Head"): AimBot.Bone = 6
        if (Bone == "Heck"): AimBot.Bone = 5
        if (Bone == "Chest"): AimBot.Bone = 4
        if (Bone == "Stomach"): AimBot.Bone = 0
        if (Bone == "Nearest"): AimBot.Bone = -1


    def changeFovColor(self):
        Color = QColorDialog.getColor()
        AimBot.AimFOVColor = Color.name()
        
        self.AimBotWin.FovColorEdit.setStyleSheet(f"background-color: {AimBot.AimFOVColor}; border: none;")


    def changeAimBotTeamStatus(self): AimBot.TeamCheck = self.AimBotWin.teamCheckCheckBox.isChecked()
    def changeAimBotShowFOVStatus(self): AimBot.AimBotFOVStatus = self.AimBotWin.showFOVCheckBox.isChecked()

    def ShowAimBotWindow(self):
        self.AimBotWin = AiBotWindow.Widget()

        self.AimBotWin.teamCheckCheckBox.stateChanged.connect(self.changeAimBotTeamStatus)
        self.AimBotWin.showFOVCheckBox.stateChanged.connect(self.changeAimBotShowFOVStatus)

        self.AimBotWin.FOVSlider.valueChanged.connect(self.changeAimBotFOV)
        self.AimBotWin.smoothSlider.valueChanged.connect(self.changeAimBotSmooth)
        self.AimBotWin.maxShotSlider.valueChanged.connect(self.changeAimBotMaxShot)
        self.AimBotWin.mouseListComboBox.currentTextChanged.connect(self.changeAimBotMouse)
        self.AimBotWin.boneListComboBox.currentTextChanged.connect(self.changeAimBotBone)

        self.AimBotWin.FovColorEdit.clicked.connect(self.changeFovColor)
        self.AimBotWin.show()


    def changeTriggerBotDelay(self):
        self.TriggerBotWin.FOVLable.setText(f"{self.TriggerBotWin.delaySlider.value()}")
        TriggerBot.Delay = self.TriggerBotWin.delaySlider.value()


    def changeTriggerBotMaxShot(self):
        self.TriggerBotWin.maxShotLable.setText(f"{self.TriggerBotWin.maxShotSlider.value()}")
        TriggerBot.MaxShot = self.TriggerBotWin.maxShotSlider.value()


    def changeTriggerBotMouse(self):
        Mouse = self.TriggerBotWin.mouseListComboBox.currentText()

        if (Mouse == "MOUSE1"): TriggerBot.VirtualKey = 1
        if (Mouse == "MOUSE2"): TriggerBot.VirtualKey = 2
        if (Mouse == "MOUSE4"): TriggerBot.VirtualKey = 4
        if (Mouse == "MOUSE5"): TriggerBot.VirtualKey = 5
        if (Mouse == "MOUSE6"): TriggerBot.VirtualKey = 6
        if (Mouse == "None"): TriggerBot.VirtualKey = 0


    def changeTriggerBotTeamStatus(self): TriggerBot.TeamCheck = self.TriggerBotWin.teamCheckCheckBox.isChecked()

    def ShowTriggerBotWindow(self):
        self.TriggerBotWin = TriggerBotWindow.Widget()

        self.TriggerBotWin.teamCheckCheckBox.stateChanged.connect(self.changeTriggerBotTeamStatus)
        self.TriggerBotWin.delaySlider.valueChanged.connect(self.changeTriggerBotDelay)
        self.TriggerBotWin.maxShotSlider.valueChanged.connect(self.changeTriggerBotMaxShot)
        self.TriggerBotWin.mouseListComboBox.currentTextChanged.connect(self.changeTriggerBotMouse)

        self.TriggerBotWin.show()


    def changeAutoPistolMouse(self):
        Mouse = self.AutoPistolWin.mouseListComboBox.currentText()

        if (Mouse == "MOUSE2"): AutoPistol.VirtualKey = 2
        if (Mouse == "MOUSE4"): AutoPistol.VirtualKey = 4
        if (Mouse == "MOUSE5"): AutoPistol.VirtualKey = 5
        if (Mouse == "MOUSE6"): AutoPistol.VirtualKey = 6


    def ShowAutoPistolWindow(self):
        self.AutoPistolWin = AutoPistolWindow.Widget()
        self.AutoPistolWin.mouseListComboBox.currentTextChanged.connect(self.changeAutoPistolMouse)
        self.AutoPistolWin.show()



class Widget(QtWidgets.QWidget, Ui_Window):
    def __init__(self, parent = None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x_main, y_main = self.geometry().x(), self.geometry().y()
            cursor_x, cursor_y = QtGui.QCursor.pos().x(), QtGui.QCursor.pos().y()

            if x_main <= cursor_x <= x_main + self.geometry().width():
                if y_main <= cursor_y <= y_main + self.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None

        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None


    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None


    def mouseMoveEvent(self, event):
        try:
            if not self.old_pos: return
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)

        except: pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QWidget()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
