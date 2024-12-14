# Import required modules
import Function.AimBot as AimBot
import SDK.GameVar as GameVar
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_antiAimAsistWindow(object):
    def setupUi(self, aimAsistWindow):
        # Main window setup
        aimAsistWindow.setObjectName("antiAimAsistWindow")
        aimAsistWindow.resize(300, 320)
        
        # Title panel setup
        self.titlePanel = QtWidgets.QLabel(aimAsistWindow)
        self.titlePanel.setGeometry(QtCore.QRect(0, 0, 300, 20))
        self.titlePanel.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 10pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(245, 246, 250);\n"
"padding-left: 1px;")
        self.titlePanel.setObjectName("titlePanel")

        # Close button setup
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

        # Background setup
        self.Background = QtWidgets.QLabel(aimAsistWindow)
        self.Background.setGeometry(QtCore.QRect(0, 0, 300, 370))
        self.Background.setStyleSheet("background-color: rgb(30, 30, 35)")
        self.Background.setText("")
        self.Background.setObjectName("Background")

        # Team check checkbox setup
        self.teamCheckCheckBox = QtWidgets.QCheckBox(aimAsistWindow)
        self.teamCheckCheckBox.setGeometry(QtCore.QRect(5, 25, 96, 16))
        self._setupCheckboxStyle(self.teamCheckCheckBox)
        self.teamCheckCheckBox.setObjectName("teamCheckCheckBox")
        self.teamCheckCheckBox.setChecked(AimBot.TeamCheck)

        # Show FOV checkbox setup  
        self.showFOVCheckBox = QtWidgets.QCheckBox(aimAsistWindow)
        self.showFOVCheckBox.setGeometry(QtCore.QRect(5, 45, 87, 16))
        self._setupCheckboxStyle(self.showFOVCheckBox)
        self.showFOVCheckBox.setObjectName("showFOVCheckBox")
        self.showFOVCheckBox.setChecked(AimBot.AimBotFOVStatus)

        # FOV slider setup
        self.FOVSlider = QtWidgets.QSlider(aimAsistWindow)
        self.FOVSlider.setGeometry(QtCore.QRect(5, 100, 130, 22))
        self._setupSliderStyle(self.FOVSlider)
        self.FOVSlider.setMinimum(1)
        self.FOVSlider.setMaximum(360)
        self.FOVSlider.setProperty("value", 360)
        self.FOVSlider.setSliderPosition(AimBot.Fov)
        self.FOVSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FOVSlider.setObjectName("FOVSlider")

        # FOV label setup
        self.FOVLable = QtWidgets.QLabel(aimAsistWindow)
        self.FOVLable.setGeometry(QtCore.QRect(140, 102, 21, 16))
        self._setupLabelStyle(self.FOVLable)
        self.FOVLable.setAlignment(QtCore.Qt.AlignCenter)
        self.FOVLable.setObjectName("FOVLable")

        # FOV color edit button setup
        self.FovColorEdit = QtWidgets.QPushButton(aimAsistWindow)
        self.FovColorEdit.setGeometry(QtCore.QRect(280, 40, 16, 16))
        self.FovColorEdit.setStyleSheet(f"background-color: {AimBot.AimFOVColor};\n"
"border: none;")
        self.FovColorEdit.setText("")
        self.FovColorEdit.setObjectName("FovColorEdit")

        # FOV title label setup
        self.FOVTitleLable = QtWidgets.QLabel(aimAsistWindow)
        self.FOVTitleLable.setGeometry(QtCore.QRect(5, 85, 27, 16))
        self._setupLabelStyle(self.FOVTitleLable)
        self.FOVTitleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.FOVTitleLable.setObjectName("FOVTitleLable")

        # Smooth title label setup
        self.smoothTitleLable = QtWidgets.QLabel(aimAsistWindow)
        self.smoothTitleLable.setGeometry(QtCore.QRect(5, 130, 49, 16))
        self._setupLabelStyle(self.smoothTitleLable)
        self.smoothTitleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.smoothTitleLable.setObjectName("smoothTitleLable")

        # Smooth slider setup
        self.smoothSlider = QtWidgets.QSlider(aimAsistWindow)
        self.smoothSlider.setGeometry(QtCore.QRect(6, 145, 130, 22))
        self._setupSliderStyle(self.smoothSlider)
        self.smoothSlider.setMinimum(1)
        self.smoothSlider.setMaximum(10)
        self.smoothSlider.setSingleStep(1)
        self.smoothSlider.setPageStep(10)
        self.smoothSlider.setProperty("value", 0)
        self.smoothSlider.setSliderPosition(AimBot.Smooth)
        self.smoothSlider.setOrientation(QtCore.Qt.Horizontal)
        self.smoothSlider.setObjectName("smoothSlider")

        # Smooth label setup
        self.smoothLable = QtWidgets.QLabel(aimAsistWindow)
        self.smoothLable.setGeometry(QtCore.QRect(140, 148, 21, 16))
        self._setupLabelStyle(self.smoothLable)
        self.smoothLable.setAlignment(QtCore.Qt.AlignCenter)
        self.smoothLable.setObjectName("smoothLable")

        # Max shot title label setup
        self.maxShotTitleLable = QtWidgets.QLabel(aimAsistWindow)
        self.maxShotTitleLable.setGeometry(QtCore.QRect(5, 175, 123, 16))
        self._setupLabelStyle(self.maxShotTitleLable)
        self.maxShotTitleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.maxShotTitleLable.setObjectName("maxShotTitleLable")

        # Max shot slider setup
        self.maxShotSlider = QtWidgets.QSlider(aimAsistWindow)
        self.maxShotSlider.setGeometry(QtCore.QRect(5, 190, 130, 22))
        self._setupSliderStyle(self.maxShotSlider)
        self.maxShotSlider.setMinimum(0)
        self.maxShotSlider.setMaximum(10)
        self.maxShotSlider.setSingleStep(1)
        self.maxShotSlider.setPageStep(10)
        self.maxShotSlider.setProperty("value", 5)
        self.maxShotSlider.setSliderPosition(AimBot.MaxShot)
        self.maxShotSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxShotSlider.setObjectName("maxShotSlider")

        # Max shot label setup
        self.maxShotLable = QtWidgets.QLabel(aimAsistWindow)
        self.maxShotLable.setGeometry(QtCore.QRect(140, 194, 21, 16))
        self._setupLabelStyle(self.maxShotLable)
        self.maxShotLable.setAlignment(QtCore.Qt.AlignCenter)
        self.maxShotLable.setObjectName("maxShotLable")

        # Mouse list combo box setup
        self.mouseListComboBox = QtWidgets.QComboBox(aimAsistWindow)
        self.mouseListComboBox.setGeometry(QtCore.QRect(5, 240, 130, 22))
        self._setupComboBoxStyle(self.mouseListComboBox)
        self.mouseListComboBox.setObjectName("mouseListComboBox")
        self._populateMouseList()

        # Mouse list label setup
        self.mouseListLable = QtWidgets.QLabel(aimAsistWindow)
        self.mouseListLable.setGeometry(QtCore.QRect(5, 220, 63, 16))
        self._setupLabelStyle(self.mouseListLable)
        self.mouseListLable.setAlignment(QtCore.Qt.AlignCenter)
        self.mouseListLable.setObjectName("mouseListLable")

        # Bone list title setup
        self.boneListTitlte = QtWidgets.QLabel(aimAsistWindow)
        self.boneListTitlte.setGeometry(QtCore.QRect(5, 270, 55, 16))
        self._setupLabelStyle(self.boneListTitlte)
        self.boneListTitlte.setAlignment(QtCore.Qt.AlignCenter)
        self.boneListTitlte.setObjectName("boneListTitlte")

        # Bone list combo box setup
        self.boneListComboBox = QtWidgets.QComboBox(aimAsistWindow)
        self.boneListComboBox.setGeometry(QtCore.QRect(5, 290, 130, 22))
        self._setupComboBoxStyle(self.boneListComboBox)
        self.boneListComboBox.setObjectName("boneListComboBox")
        self._populateBoneList()

        # Raise all widgets in correct order
        self._raiseWidgets()

        self.retranslateUi(aimAsistWindow)
        QtCore.QMetaObject.connectSlotsByName(aimAsistWindow)

    def _setupCheckboxStyle(self, checkbox):
        """Helper method to setup consistent checkbox styling"""
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

    def _setupSliderStyle(self, slider):
        """Helper method to setup consistent slider styling"""
        slider.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 8px;\n"
"background: #0097e6;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1e3799;\n"
"    width: 15px;\n"
"}")

    def _setupLabelStyle(self, label):
        """Helper method to setup consistent label styling"""
        label.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")

    def _setupComboBoxStyle(self, combobox):
        """Helper method to setup consistent combobox styling"""
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

    def _populateMouseList(self):
        """Helper method to populate mouse list combo box"""
        mouse_options = ["MOUSE1", "MOUSE2", "MOUSE4", "MOUSE5", "MOUSE6", "None"]
        for option in mouse_options:
            self.mouseListComboBox.addItem(option)
        current = "None" if (AimBot.VirtualKey == 0) else f"MOUSE{AimBot.VirtualKey}"
        self.mouseListComboBox.setCurrentText(current)

    def _populateBoneList(self):
        """Helper method to populate bone list combo box"""
        bone_options = ["Head", "Heck", "Chest", "Stomach", "Nearest"]
        for option in bone_options:
            self.boneListComboBox.addItem(option)
        self.boneListComboBox.setCurrentText(GameVar.GameVar.BoneListName[AimBot.Bone])

    def _raiseWidgets(self):
        """Helper method to raise widgets in correct order"""
        widgets = [self.Background, self.titlePanel, self.closeButton,
                  self.teamCheckCheckBox, self.showFOVCheckBox, self.FOVSlider,
                  self.FOVLable, self.FovColorEdit, self.FOVTitleLable,
                  self.smoothTitleLable, self.smoothSlider, self.smoothLable,
                  self.maxShotTitleLable, self.maxShotSlider, self.maxShotLable,
                  self.mouseListComboBox, self.mouseListLable, self.boneListTitlte,
                  self.boneListComboBox]
        for widget in widgets:
            widget.raise_()

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
        self.mouseListLable.setText(_translate("aimAsistWindow", "Mouse list"))
        self.boneListTitlte.setText(_translate("aimAsistWindow", "Bone list"))


class Widget(QtWidgets.QWidget, Ui_antiAimAsistWindow):
    def __init__(self, parent = None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.old_pos = None

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
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)
