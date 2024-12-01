import Function.AimBot as AimBot
import SDK.GameVar as GameVar

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aimAsistWindow(object):
    def setupUi(self, aimAsistWindow):
        aimAsistWindow.setObjectName("aimAsistWindow")
        aimAsistWindow.resize(300, 320)
        self.titlePanel = QtWidgets.QLabel(aimAsistWindow)
        self.titlePanel.setGeometry(QtCore.QRect(0, 0, 300, 20))
        self.titlePanel.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 10pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(245, 246, 250);\n"
"padding-left: 1px;")
        self.titlePanel.setObjectName("titlePanel")
        self.closeButton = QtWidgets.QPushButton(aimAsistWindow)
        self.closeButton.setGeometry(QtCore.QRect(280, 0, 20, 20))
        self.closeButton.setStyleSheet("QPushButton{\n"
"  background-color: rgb(50, 50, 55);\n"
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
        icon.addPixmap(QtGui.QPixmap("UI/Image/Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(20, 20))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(lambda: self.close())
        self.Background = QtWidgets.QLabel(aimAsistWindow)
        self.Background.setGeometry(QtCore.QRect(0, 0, 300, 370))
        self.Background.setStyleSheet("background-color: rgb(30, 30, 35)")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.teamCheckCheckBox = QtWidgets.QCheckBox(aimAsistWindow)
        self.teamCheckCheckBox.setGeometry(QtCore.QRect(5, 25, 96, 16))
        self.teamCheckCheckBox.setStyleSheet("QCheckBox {\n"
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
        self.teamCheckCheckBox.setObjectName("teamCheckCheckBox")
        self.teamCheckCheckBox.setChecked(AimBot.TeamCheck)
        self.showFOVCheckBox = QtWidgets.QCheckBox(aimAsistWindow)
        self.showFOVCheckBox.setGeometry(QtCore.QRect(5, 45, 87, 16))
        self.showFOVCheckBox.setStyleSheet("QCheckBox {\n"
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
        self.showFOVCheckBox.setObjectName("showFOVCheckBox")
        self.showFOVCheckBox.setChecked(AimBot.AimBotFOVStatus)
        self.FOVSlider = QtWidgets.QSlider(aimAsistWindow)
        self.FOVSlider.setGeometry(QtCore.QRect(5, 100, 130, 22))
        self.FOVSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.FOVSlider.setMinimum(1)
        self.FOVSlider.setMaximum(360)
        self.FOVSlider.setProperty("value", 360)
        self.FOVSlider.setSliderPosition(AimBot.Fov)
        self.FOVSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FOVSlider.setObjectName("FOVSlider")
        self.FOVLable = QtWidgets.QLabel(aimAsistWindow)
        self.FOVLable.setGeometry(QtCore.QRect(140, 102, 21, 16))
        self.FOVLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.FOVLable.setAlignment(QtCore.Qt.AlignCenter)
        self.FOVLable.setObjectName("FOVLable")
        self.FovColorEdit = QtWidgets.QPushButton(aimAsistWindow)
        self.FovColorEdit.setGeometry(QtCore.QRect(280, 40, 16, 16))
        self.FovColorEdit.setStyleSheet(f"background-color: {AimBot.AimFOVColor};\n"
"border: none;")
        self.FovColorEdit.setText("")
        self.FovColorEdit.setObjectName("FovColorEdit")
        self.FOVTitleLable = QtWidgets.QLabel(aimAsistWindow)
        self.FOVTitleLable.setGeometry(QtCore.QRect(5, 85, 27, 16))
        self.FOVTitleLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.FOVTitleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.FOVTitleLable.setObjectName("FOVTitleLable")
        self.smoothTitleLable = QtWidgets.QLabel(aimAsistWindow)
        self.smoothTitleLable.setGeometry(QtCore.QRect(5, 130, 49, 16))
        self.smoothTitleLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.smoothTitleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.smoothTitleLable.setObjectName("smoothTitleLable")
        self.smoothSlider = QtWidgets.QSlider(aimAsistWindow)
        self.smoothSlider.setGeometry(QtCore.QRect(6, 145, 130, 22))
        self.smoothSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.smoothSlider.setMinimum(1)
        self.smoothSlider.setMaximum(10)
        self.smoothSlider.setSingleStep(1)
        self.smoothSlider.setPageStep(10)
        self.smoothSlider.setProperty("value", 0)
        self.smoothSlider.setSliderPosition(AimBot.Smooth)
        self.smoothSlider.setOrientation(QtCore.Qt.Horizontal)
        self.smoothSlider.setObjectName("smoothSlider")
        self.smoothLable = QtWidgets.QLabel(aimAsistWindow)
        self.smoothLable.setGeometry(QtCore.QRect(140, 148, 21, 16))
        self.smoothLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.smoothLable.setAlignment(QtCore.Qt.AlignCenter)
        self.smoothLable.setObjectName("smoothLable")
        self.maxShotTitleLable = QtWidgets.QLabel(aimAsistWindow)
        self.maxShotTitleLable.setGeometry(QtCore.QRect(5, 175, 123, 16))
        self.maxShotTitleLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.maxShotTitleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.maxShotTitleLable.setObjectName("maxShotTitleLable")
        self.maxShotSlider = QtWidgets.QSlider(aimAsistWindow)
        self.maxShotSlider.setGeometry(QtCore.QRect(5, 190, 130, 22))
        self.maxShotSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.maxShotSlider.setMinimum(0)
        self.maxShotSlider.setMaximum(10)
        self.maxShotSlider.setSingleStep(1)
        self.maxShotSlider.setPageStep(10)
        self.maxShotSlider.setProperty("value", 5)
        self.maxShotSlider.setSliderPosition(AimBot.MaxShot)
        self.maxShotSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxShotSlider.setObjectName("maxShotSlider")
        self.maxShotLable = QtWidgets.QLabel(aimAsistWindow)
        self.maxShotLable.setGeometry(QtCore.QRect(140, 194, 21, 16))
        self.maxShotLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.maxShotLable.setAlignment(QtCore.Qt.AlignCenter)
        self.maxShotLable.setObjectName("maxShotLable")
        self.mouseListComboBox = QtWidgets.QComboBox(aimAsistWindow)
        self.mouseListComboBox.setGeometry(QtCore.QRect(5, 240, 130, 22))
        self.mouseListComboBox.setStyleSheet("QComboBox{\n"
"font: 8pt \"Arial\";\n"
"border: none;\n"
"background-color: rgb(30,30,30);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border: none;\n"
"    background-color: rgb(100,100,100);\n"
"    font-weight: bold;\n"
"}")
        self.mouseListComboBox.setObjectName("mouseListComboBox")
        self.mouseListComboBox.addItem("")
        self.mouseListComboBox.addItem("")
        self.mouseListComboBox.addItem("")
        self.mouseListComboBox.addItem("")
        self.mouseListComboBox.addItem("")
        self.mouseListComboBox.addItem("")
        self.mouseListLable = QtWidgets.QLabel(aimAsistWindow)
        self.mouseListLable.setGeometry(QtCore.QRect(5, 220, 63, 16))
        self.mouseListLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.mouseListLable.setAlignment(QtCore.Qt.AlignCenter)
        self.mouseListLable.setObjectName("mouseListLable")
        self.boneListTitlte = QtWidgets.QLabel(aimAsistWindow)
        self.boneListTitlte.setGeometry(QtCore.QRect(5, 270, 55, 16))
        self.boneListTitlte.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.boneListTitlte.setAlignment(QtCore.Qt.AlignCenter)
        self.boneListTitlte.setObjectName("boneListTitlte")
        self.boneListComboBox = QtWidgets.QComboBox(aimAsistWindow)
        self.boneListComboBox.setGeometry(QtCore.QRect(5, 290, 130, 22))
        self.boneListComboBox.setStyleSheet("QComboBox{\n"
"font: 8pt \"Arial\";\n"
"border: none;\n"
"background-color: rgb(30,30,30);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border: none;\n"
"    background-color: rgb(100,100,100);\n"
"    font-weight: bold;\n"
"}")
        self.boneListComboBox.setObjectName("boneListComboBox")
        self.boneListComboBox.addItem("")
        self.boneListComboBox.addItem("")
        self.boneListComboBox.addItem("")
        self.boneListComboBox.addItem("")
        self.boneListComboBox.addItem("")

        self.Background.raise_()
        self.titlePanel.raise_()
        self.closeButton.raise_()
        self.teamCheckCheckBox.raise_()
        self.showFOVCheckBox.raise_()
        self.FOVSlider.raise_()
        self.FOVLable.raise_()
        self.FovColorEdit.raise_()
        self.FOVTitleLable.raise_()
        self.smoothTitleLable.raise_()
        self.smoothSlider.raise_()
        self.smoothLable.raise_()
        self.maxShotTitleLable.raise_()
        self.maxShotSlider.raise_()
        self.maxShotLable.raise_()
        self.mouseListComboBox.raise_()
        self.mouseListLable.raise_()
        self.boneListTitlte.raise_()
        self.boneListComboBox.raise_()

        self.retranslateUi(aimAsistWindow)
        QtCore.QMetaObject.connectSlotsByName(aimAsistWindow)

    def retranslateUi(self, aimAsistWindow):
        _translate = QtCore.QCoreApplication.translate
        aimAsistWindow.setWindowTitle(_translate("aimAsistWindow", "Aim asist"))
        self.titlePanel.setText(_translate("aimAsistWindow", "Aim asist"))
        self.teamCheckCheckBox.setText(_translate("aimAsistWindow", "Team check"))
        self.showFOVCheckBox.setText(_translate("aimAsistWindow", "Show FOV"))
        self.FOVLable.setText(_translate("aimAsistWindow", str(AimBot.Fov)))
        self.FOVTitleLable.setText(_translate("aimAsistWindow", "FOV"))
        self.smoothTitleLable.setText(_translate("aimAsistWindow", "Smooth"))
        self.smoothLable.setText(_translate("aimAsistWindow", str(AimBot.Smooth)))
        self.maxShotTitleLable.setText(_translate("aimAsistWindow", "Max shot to disable"))
        self.maxShotLable.setText(_translate("aimAsistWindow", str(AimBot.MaxShot)))
        self.mouseListComboBox.setItemText(0, _translate("aimAsistWindow", "MOUSE1"))
        self.mouseListComboBox.setItemText(1, _translate("aimAsistWindow", "MOUSE2"))
        self.mouseListComboBox.setItemText(2, _translate("aimAsistWindow", "MOUSE4"))
        self.mouseListComboBox.setItemText(3, _translate("aimAsistWindow", "MOUSE5"))
        self.mouseListComboBox.setItemText(4, _translate("aimAsistWindow", "MOUSE6"))
        self.mouseListComboBox.setItemText(5, _translate("aimAsistWindow", "None"))
        self.mouseListComboBox.setCurrentText("None" if (AimBot.VirtualKey == 0) else f"MOUSE{AimBot.VirtualKey}")
        self.mouseListLable.setText(_translate("aimAsistWindow", "Mouse list"))
        self.boneListTitlte.setText(_translate("aimAsistWindow", "Bone list"))
        self.boneListComboBox.setItemText(0, _translate("aimAsistWindow", "Head"))
        self.boneListComboBox.setItemText(1, _translate("aimAsistWindow", "Heck"))
        self.boneListComboBox.setItemText(2, _translate("aimAsistWindow", "Chest"))
        self.boneListComboBox.setItemText(3, _translate("aimAsistWindow", "Stomach"))
        self.boneListComboBox.setItemText(4, _translate("aimAsistWindow", "Nearest"))
        self.boneListComboBox.setCurrentText(GameVar.GameVar.BoneListName[AimBot.Bone])


class Widget(QtWidgets.QWidget, Ui_aimAsistWindow):
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