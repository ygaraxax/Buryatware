import Function.Visual as Visual
from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_visualWindow(object):
    def setupUi(self, visualWindow):
        visualWindow.setObjectName("visualWindow")
        visualWindow.resize(300, 300)
        self.titlePanel = QtWidgets.QLabel(visualWindow)
        self.titlePanel.setGeometry(QtCore.QRect(0, 0, 300, 20))
        self.titlePanel.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 10pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(245, 246, 250);\n"
"padding-left: 1px;")
        self.titlePanel.setObjectName("titlePanel")
        self.closeButton = QtWidgets.QPushButton(visualWindow)
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
        self.Background = QtWidgets.QLabel(visualWindow)
        self.Background.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.Background.setStyleSheet("background-color: rgb(30, 30, 35)")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.boxESPCheckBox = QtWidgets.QCheckBox(visualWindow)
        self.boxESPCheckBox.setGeometry(QtCore.QRect(5, 25, 78, 16))
        self.boxESPCheckBox.setStyleSheet("QCheckBox {\n"
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
        self.boxESPCheckBox.setObjectName("boxESPCheckBox")
        self.boxESPCheckBox.setChecked(Visual.BoxESPStatus)
        self.teamCheckCheckBox = QtWidgets.QCheckBox(visualWindow)
        self.teamCheckCheckBox.setGeometry(QtCore.QRect(5, 45, 96, 16))
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
        self.teamCheckCheckBox.setChecked(Visual.TeamCheck)
        self.healthBarCheckBox = QtWidgets.QCheckBox(visualWindow)
        self.healthBarCheckBox.setGeometry(QtCore.QRect(5, 65, 86, 16))
        self.healthBarCheckBox.setStyleSheet("QCheckBox {\n"
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
        self.healthBarCheckBox.setObjectName("healthBarCheckBox")
        self.healthBarCheckBox.setChecked(Visual.HealthStatus)
        self.weaponCheckBox = QtWidgets.QCheckBox(visualWindow)
        self.weaponCheckBox.setGeometry(QtCore.QRect(5, 85, 73, 16))
        self.weaponCheckBox.setStyleSheet("QCheckBox {\n"
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
        self.weaponCheckBox.setObjectName("weaponCheckBox")
        self.weaponCheckBox.setChecked(Visual.WeaponStatus)
        self.lineCheckBox = QtWidgets.QCheckBox(visualWindow)
        self.lineCheckBox.setGeometry(QtCore.QRect(5, 105, 48, 16))
        self.lineCheckBox.setStyleSheet("QCheckBox {\n"
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
        self.lineCheckBox.setObjectName("lineCheckBox")
        self.lineCheckBox.setChecked(Visual.LineStatus)
        self.crosshairESPCheckBox_2 = QtWidgets.QCheckBox(visualWindow)
        self.crosshairESPCheckBox_2.setGeometry(QtCore.QRect(5, 140, 130, 16))
        self.crosshairESPCheckBox_2.setStyleSheet("QCheckBox {\n"
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
        self.crosshairESPCheckBox_2.setObjectName("crosshairESPCheckBox_2")
        self.crosshairESPCheckBox_2.setChecked(Visual.CrosshairStatus)
        self.sniperCrosshairSlider = QtWidgets.QSlider(visualWindow)
        self.sniperCrosshairSlider.setGeometry(QtCore.QRect(5, 160, 130, 22))
        self.sniperCrosshairSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.sniperCrosshairSlider.setMinimum(2)
        self.sniperCrosshairSlider.setMaximum(20)
        self.sniperCrosshairSlider.setProperty("value", Visual.CrosshairSize)
        self.sniperCrosshairSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sniperCrosshairSlider.setObjectName("sniperCrosshairSlider")
        self.sniperCrosshairLable = QtWidgets.QLabel(visualWindow)
        self.sniperCrosshairLable.setGeometry(QtCore.QRect(140, 163, 21, 16))
        self.sniperCrosshairLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.sniperCrosshairLable.setAlignment(QtCore.Qt.AlignCenter)
        self.sniperCrosshairLable.setObjectName("sniperCrosshairLable")
        self.BombTimerCheckBox = QtWidgets.QCheckBox(visualWindow)
        self.BombTimerCheckBox.setGeometry(QtCore.QRect(5, 195, 94, 16))
        self.BombTimerCheckBox.setStyleSheet("QCheckBox {\n"
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
        self.BombTimerCheckBox.setObjectName("BombTimerCheckBox")
        self.BombTimerCheckBox.setChecked(Visual.BombESPStatus)
        self.boxESPColorEdit = QtWidgets.QPushButton(visualWindow)
        self.boxESPColorEdit.setGeometry(QtCore.QRect(280, 25, 16, 16))
        self.boxESPColorEdit.setStyleSheet(f"background-color: {Visual.BoxESPColor};\n"
"border: none;")
        self.boxESPColorEdit.setText("")
        self.boxESPColorEdit.setObjectName("boxESPColorEdit")
        self.lineColorEdit = QtWidgets.QPushButton(visualWindow)
        self.lineColorEdit.setGeometry(QtCore.QRect(280, 105, 16, 16))
        self.lineColorEdit.setStyleSheet(f"background-color: {Visual.LineColor};\n"
"border: none;")
        self.lineColorEdit.setText("")
        self.lineColorEdit.setObjectName("lineColorEdit")
        self.sniperCorsshairColorEdit = QtWidgets.QPushButton(visualWindow)
        self.sniperCorsshairColorEdit.setGeometry(QtCore.QRect(280, 135, 16, 16))
        self.sniperCorsshairColorEdit.setStyleSheet(f"background-color: {Visual.CrosshairColor};\n"
"border: none;")
        self.sniperCorsshairColorEdit.setText("")
        self.sniperCorsshairColorEdit.setObjectName("sniperCorsshairColorEdit")
        self.Background.raise_()
        self.titlePanel.raise_()
        self.closeButton.raise_()
        self.closeButton.clicked.connect(lambda: self.close())
        self.boxESPCheckBox.raise_()
        self.teamCheckCheckBox.raise_()
        self.healthBarCheckBox.raise_()
        self.weaponCheckBox.raise_()
        self.lineCheckBox.raise_()
        self.crosshairESPCheckBox_2.raise_()
        self.sniperCrosshairSlider.raise_()
        self.sniperCrosshairLable.raise_()
        self.BombTimerCheckBox.raise_()
        self.boxESPColorEdit.raise_()
        self.lineColorEdit.raise_()
        self.sniperCorsshairColorEdit.raise_()

        self.retranslateUi(visualWindow)
        QtCore.QMetaObject.connectSlotsByName(visualWindow)

    def retranslateUi(self, visualWindow):
        _translate = QtCore.QCoreApplication.translate
        visualWindow.setWindowTitle(_translate("visualWindow", "Visual"))
        self.titlePanel.setText(_translate("visualWindow", "Visual"))
        self.boxESPCheckBox.setText(_translate("visualWindow", "BOX ESP"))
        self.teamCheckCheckBox.setText(_translate("visualWindow", "Team check"))
        self.healthBarCheckBox.setText(_translate("visualWindow", "Health bar"))
        self.weaponCheckBox.setText(_translate("visualWindow", "Weapon"))
        self.lineCheckBox.setText(_translate("visualWindow", "Line"))
        self.crosshairESPCheckBox_2.setText(_translate("visualWindow", "Snipers crosshair"))
        self.sniperCrosshairLable.setText(_translate("visualWindow", str(Visual.CrosshairSize)))
        self.BombTimerCheckBox.setText(_translate("visualWindow", "Bomb timer"))


class Widget(QtWidgets.QWidget, Ui_visualWindow):
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