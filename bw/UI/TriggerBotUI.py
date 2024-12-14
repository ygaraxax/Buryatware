import Function.TriggerBot as TriggerBot
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_triggerBotWindow(object):
    def setupUi(self, triggerBotWindow):
        # Main window setup
        triggerBotWindow.setObjectName("triggerBotWindow")
        triggerBotWindow.resize(300, 300)
        
        # Title panel setup
        self.titlePanel = QtWidgets.QLabel(triggerBotWindow)
        self.titlePanel.setGeometry(QtCore.QRect(0, 0, 300, 20))
        self.titlePanel.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 10pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(245, 246, 250);\n"
"padding-left: 1px;")
        self.titlePanel.setObjectName("titlePanel")

        # Close button setup
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

        # Background setup
        self.Background = QtWidgets.QLabel(triggerBotWindow)
        self.Background.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.Background.setStyleSheet("background-color: rgb(30, 30, 35)")
        self.Background.setText("")
        self.Background.setObjectName("Background")

        # Team check checkbox setup
        self.teamCheckCheckBox = QtWidgets.QCheckBox(triggerBotWindow)
        self.teamCheckCheckBox.setGeometry(QtCore.QRect(5, 25, 96, 16))
        self._setupCheckboxStyle(self.teamCheckCheckBox)
        self.teamCheckCheckBox.setObjectName("teamCheckCheckBox")
        self.teamCheckCheckBox.setChecked(TriggerBot.TeamCheck)

        # Delay slider setup
        self.delaySlider = QtWidgets.QSlider(triggerBotWindow)
        self.delaySlider.setGeometry(QtCore.QRect(5, 65, 130, 22))
        self._setupSliderStyle(self.delaySlider)
        self.delaySlider.setMinimum(10)
        self.delaySlider.setMaximum(1000)
        self.delaySlider.setProperty("value", 50)
        self.delaySlider.setSliderPosition(TriggerBot.Delay)
        self.delaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.delaySlider.setObjectName("delaySlider")

        # Labels setup
        self._setupLabels(triggerBotWindow)

        # Max shot slider setup  
        self.maxShotSlider = QtWidgets.QSlider(triggerBotWindow)
        self.maxShotSlider.setGeometry(QtCore.QRect(5, 105, 130, 22))
        self._setupSliderStyle(self.maxShotSlider)
        self.maxShotSlider.setMinimum(0)
        self.maxShotSlider.setMaximum(10)
        self.maxShotSlider.setSingleStep(1)
        self.maxShotSlider.setPageStep(10)
        self.maxShotSlider.setProperty("value", 5)
        self.maxShotSlider.setSliderPosition(TriggerBot.MaxShot)
        self.maxShotSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxShotSlider.setObjectName("maxShotSlider")

        # Mouse list combo box setup
        self.mouseListComboBox = QtWidgets.QComboBox(triggerBotWindow)
        self.mouseListComboBox.setGeometry(QtCore.QRect(5, 150, 130, 22))
        self._setupComboBoxStyle(self.mouseListComboBox)
        self._populateMouseList()

        # Raise order of widgets
        self._setWidgetOrder()

        self.retranslateUi(triggerBotWindow)
        QtCore.QMetaObject.connectSlotsByName(triggerBotWindow)

    # Helper method to setup checkbox style
    def _setupCheckboxStyle(self, checkbox):
        checkbox.setStyleSheet("QCheckBox {\n"
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

    # Helper method to setup slider style
    def _setupSliderStyle(self, slider):
        slider.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")

    # Helper method to setup labels
    def _setupLabels(self, window):
        # FOV label
        self.FOVLable = QtWidgets.QLabel(window)
        self.FOVLable.setGeometry(QtCore.QRect(145, 68, 25, 16))
        self._setupLabelStyle(self.FOVLable)
        self.FOVLable.setAlignment(QtCore.Qt.AlignCenter)
        self.FOVLable.setObjectName("FOVLable")

        # Delay title label
        self.delayTitleLable = QtWidgets.QLabel(window)
        self.delayTitleLable.setGeometry(QtCore.QRect(5, 50, 36, 16))
        self._setupLabelStyle(self.delayTitleLable)
        self.delayTitleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.delayTitleLable.setObjectName("delayTitleLable")

        # Max shot title label
        self.maxShotTitleLable = QtWidgets.QLabel(window)
        self.maxShotTitleLable.setGeometry(QtCore.QRect(5, 90, 123, 16))
        self._setupLabelStyle(self.maxShotTitleLable)
        self.maxShotTitleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.maxShotTitleLable.setObjectName("maxShotTitleLable")

        # Max shot label
        self.maxShotLable = QtWidgets.QLabel(window)
        self.maxShotLable.setGeometry(QtCore.QRect(145, 108, 21, 16))
        self._setupLabelStyle(self.maxShotLable)
        self.maxShotLable.setAlignment(QtCore.Qt.AlignCenter)
        self.maxShotLable.setObjectName("maxShotLable")

        # Mouse list label
        self.mouseListLable = QtWidgets.QLabel(window)
        self.mouseListLable.setGeometry(QtCore.QRect(5, 130, 63, 16))
        self._setupLabelStyle(self.mouseListLable)
        self.mouseListLable.setAlignment(QtCore.Qt.AlignCenter)
        self.mouseListLable.setObjectName("mouseListLable")

    # Helper method to setup label style
    def _setupLabelStyle(self, label):
        label.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")

    # Helper method to setup combo box style
    def _setupComboBoxStyle(self, combobox):
        combobox.setStyleSheet("QComboBox{\n"
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

    # Helper method to populate mouse list
    def _populateMouseList(self):
        mouse_options = ["MOUSE1", "MOUSE2", "MOUSE4", "MOUSE5", "MOUSE6", "None"]
        for option in mouse_options:
            self.mouseListComboBox.addItem(option)
        current_value = "None" if (TriggerBot.VirtualKey == 0) else f"MOUSE{TriggerBot.VirtualKey}"
        self.mouseListComboBox.setCurrentText(current_value)

    # Helper method to set widget order
    def _setWidgetOrder(self):
        widgets = [self.Background, self.titlePanel, self.closeButton, 
                  self.teamCheckCheckBox, self.delaySlider, self.FOVLable,
                  self.delayTitleLable, self.maxShotTitleLable, 
                  self.maxShotSlider, self.maxShotLable,
                  self.mouseListComboBox, self.mouseListLable]
        for widget in widgets:
            widget.raise_()

    def retranslateUi(self, triggerBotWindow):
        _translate = QtCore.QCoreApplication.translate
        triggerBotWindow.setWindowTitle(_translate("triggerBotWindow", "Trigger Bot"))
        self.titlePanel.setText(_translate("triggerBotWindow", "Trigger Bot"))
        self.teamCheckCheckBox.setText(_translate("triggerBotWindow", "Team check"))
        self.FOVLable.setText(_translate("triggerBotWindow", str(TriggerBot.Delay)))
        self.delayTitleLable.setText(_translate("triggerBotWindow", "Delay"))
        self.maxShotTitleLable.setText(_translate("triggerBotWindow", "Max shot to disable"))
        self.maxShotLable.setText(_translate("triggerBotWindow", str(TriggerBot.MaxShot)))
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
