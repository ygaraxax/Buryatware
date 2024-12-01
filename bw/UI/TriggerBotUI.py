import Function.TriggerBot as TriggerBot
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_triggerBotWindow(object):
    def setupUi(self, triggerBotWindow):
        triggerBotWindow.setObjectName("triggerBotWindow")
        triggerBotWindow.resize(300, 300)
        self.titlePanel = QtWidgets.QLabel(triggerBotWindow)
        self.titlePanel.setGeometry(QtCore.QRect(0, 0, 300, 20))
        self.titlePanel.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 10pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(245, 246, 250);\n"
"padding-left: 1px;")
        self.titlePanel.setObjectName("titlePanel")
        self.closeButton = QtWidgets.QPushButton(triggerBotWindow)
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
        self.Background = QtWidgets.QLabel(triggerBotWindow)
        self.Background.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.Background.setStyleSheet("background-color: rgb(30, 30, 35)")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.teamCheckCheckBox = QtWidgets.QCheckBox(triggerBotWindow)
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
        self.teamCheckCheckBox.setChecked(TriggerBot.TeamCheck)
        self.delaySlider = QtWidgets.QSlider(triggerBotWindow)
        self.delaySlider.setGeometry(QtCore.QRect(5, 65, 130, 22))
        self.delaySlider.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")
        self.delaySlider.setMinimum(10)
        self.delaySlider.setMaximum(1000)
        self.delaySlider.setProperty("value", 50)
        self.delaySlider.setSliderPosition(TriggerBot.Delay)
        self.delaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.delaySlider.setObjectName("delaySlider")
        self.FOVLable = QtWidgets.QLabel(triggerBotWindow)
        self.FOVLable.setGeometry(QtCore.QRect(145, 68, 25, 16))
        self.FOVLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.FOVLable.setAlignment(QtCore.Qt.AlignCenter)
        self.FOVLable.setObjectName("FOVLable")
        self.delayTitleLable = QtWidgets.QLabel(triggerBotWindow)
        self.delayTitleLable.setGeometry(QtCore.QRect(5, 50, 36, 16))
        self.delayTitleLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.delayTitleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.delayTitleLable.setObjectName("delayTitleLable")
        self.maxShotTitleLable = QtWidgets.QLabel(triggerBotWindow)
        self.maxShotTitleLable.setGeometry(QtCore.QRect(5, 90, 123, 16))
        self.maxShotTitleLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.maxShotTitleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.maxShotTitleLable.setObjectName("maxShotTitleLable")
        self.maxShotSlider = QtWidgets.QSlider(triggerBotWindow)
        self.maxShotSlider.setGeometry(QtCore.QRect(5, 105, 130, 22))
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
        self.maxShotSlider.setSliderPosition(TriggerBot.MaxShot)
        self.maxShotSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxShotSlider.setObjectName("maxShotSlider")
        self.maxShotLable = QtWidgets.QLabel(triggerBotWindow)
        self.maxShotLable.setGeometry(QtCore.QRect(145, 108, 21, 16))
        self.maxShotLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.maxShotLable.setAlignment(QtCore.Qt.AlignCenter)
        self.maxShotLable.setObjectName("maxShotLable")
        self.mouseListComboBox = QtWidgets.QComboBox(triggerBotWindow)
        self.mouseListComboBox.setGeometry(QtCore.QRect(5, 150, 130, 22))
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
        self.mouseListLable = QtWidgets.QLabel(triggerBotWindow)
        self.mouseListLable.setGeometry(QtCore.QRect(5, 130, 63, 16))
        self.mouseListLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.mouseListLable.setAlignment(QtCore.Qt.AlignCenter)
        self.mouseListLable.setObjectName("mouseListLable")
      
        self.Background.raise_()
        self.titlePanel.raise_()
        self.closeButton.raise_()
        self.teamCheckCheckBox.raise_()
        self.delaySlider.raise_()
        self.FOVLable.raise_()
        self.delayTitleLable.raise_()
        self.maxShotTitleLable.raise_()
        self.maxShotSlider.raise_()
        self.maxShotLable.raise_()
        self.mouseListComboBox.raise_()
        self.mouseListLable.raise_()

        self.retranslateUi(triggerBotWindow)
        QtCore.QMetaObject.connectSlotsByName(triggerBotWindow)

    def retranslateUi(self, triggerBotWindow):
        _translate = QtCore.QCoreApplication.translate
        triggerBotWindow.setWindowTitle(_translate("triggerBotWindow", "Trigger Bot"))
        self.titlePanel.setText(_translate("triggerBotWindow", "Trigger Bot"))
        self.teamCheckCheckBox.setText(_translate("triggerBotWindow", "Team check"))
        self.FOVLable.setText(_translate("triggerBotWindow", str(TriggerBot.Delay)))
        self.delayTitleLable.setText(_translate("triggerBotWindow", "Delay"))
        self.maxShotTitleLable.setText(_translate("triggerBotWindow", "Max shot to disable"))
        self.maxShotLable.setText(_translate("triggerBotWindow", str(TriggerBot.MaxShot)))
        self.mouseListComboBox.setItemText(0, _translate("triggerBotWindow", "MOUSE1"))
        self.mouseListComboBox.setItemText(1, _translate("triggerBotWindow", "MOUSE2"))
        self.mouseListComboBox.setItemText(2, _translate("triggerBotWindow", "MOUSE4"))
        self.mouseListComboBox.setItemText(3, _translate("triggerBotWindow", "MOUSE5"))
        self.mouseListComboBox.setItemText(4, _translate("triggerBotWindow", "MOUSE6"))
        self.mouseListComboBox.setItemText(5, _translate("triggerBotWindow", "None"))
        self.mouseListComboBox.setCurrentText("None" if (TriggerBot.VirtualKey == 0) else f"MOUSE{TriggerBot.VirtualKey}")
        self.mouseListLable.setText(_translate("triggerBotWindow", "Mouse list"))


class Widget(QtWidgets.QWidget, Ui_triggerBotWindow):
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