import Function.Visual as Visual
from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_visualWindow(object):
    # Common checkbox style - extracted to reduce duplication
    CHECKBOX_STYLE = """
        QCheckBox {
            color: rgb(241, 242, 246);
            spacing: 5px;
            border: none;
            font: 10pt "Arial";
            font-weight: bold;
        }

        QCheckBox::indicator  {
            width: 13px;
            height: 13px;
            border: 1px solid rgb(255,255,255);
        }

        QCheckBox::indicator:unchecked {
            background-color: rgb(40,40,45);
        }

        QCheckBox::indicator:unchecked:hover {
            background-color: rgb(45,45,50);
        }

        QCheckBox::indicator:checked {
            background-color: rgb(232, 65, 24);
        }

        QCheckBox::indicator:checked:hover {
            background-color: rgb(232, 65, 24);
        }
    """

    # Common button style
    BUTTON_STYLE = """
        QPushButton {
            background-color: rgb(50, 50, 55);
            border: none;
        }

        QPushButton:hover {
            background-color: rgb(55, 55, 60);
        }

        QPushButton:pressed {
            background-color: rgb(60, 60, 65);
        }
    """

    def setupUi(self, visualWindow):
        visualWindow.setObjectName("visualWindow")
        visualWindow.resize(300, 300)

        # Setup background first so it's at the bottom layer
        self._setupBackground(visualWindow)
        
        # Setup title panel and close button
        self._setupTitleBar(visualWindow)

        # Setup all checkboxes
        self._setupCheckboxes(visualWindow)

        # Setup sliders and labels
        self._setupSliders(visualWindow)

        # Setup color edit buttons  
        self._setupColorButtons(visualWindow)

        # Raise elements in correct order
        self._setupZOrder()

        self.retranslateUi(visualWindow)
        QtCore.QMetaObject.connectSlotsByName(visualWindow)

    def _setupBackground(self, parent):
        self.Background = QtWidgets.QLabel(parent)
        self.Background.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.Background.setStyleSheet("background-color: rgb(30, 30, 35)")
        self.Background.setText("")
        self.Background.setObjectName("Background")

    def _setupTitleBar(self, parent):
        # Title panel
        self.titlePanel = QtWidgets.QLabel(parent)
        self.titlePanel.setGeometry(QtCore.QRect(0, 0, 300, 20))
        self.titlePanel.setStyleSheet("background-color: rgb(50, 50, 55);\n"
            "font: 75 10pt \"Arial\";\n"
            "font-weight: bold;\n"
            "color: rgb(245, 246, 250);\n"
            "padding-left: 1px;")
        self.titlePanel.setObjectName("titlePanel")

        # Close button
        self.closeButton = QtWidgets.QPushButton(parent)
        self.closeButton.setGeometry(QtCore.QRect(280, 0, 20, 20))
        self.closeButton.setStyleSheet(self.BUTTON_STYLE)
        self.closeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/Image/Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(20, 20))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(lambda: self.close())

    def _setupCheckboxes(self, parent):
        # Box ESP checkbox
        self.boxESPCheckBox = QtWidgets.QCheckBox(parent)
        self.boxESPCheckBox.setGeometry(QtCore.QRect(5, 25, 78, 16))
        self.boxESPCheckBox.setStyleSheet(self.CHECKBOX_STYLE)
        self.boxESPCheckBox.setObjectName("boxESPCheckBox")
        self.boxESPCheckBox.setChecked(Visual.BoxESPStatus)

        # Team check checkbox
        self.teamCheckCheckBox = QtWidgets.QCheckBox(parent)
        self.teamCheckCheckBox.setGeometry(QtCore.QRect(5, 45, 96, 16))
        self.teamCheckCheckBox.setStyleSheet(self.CHECKBOX_STYLE)
        self.teamCheckCheckBox.setObjectName("teamCheckCheckBox")
        self.teamCheckCheckBox.setChecked(Visual.TeamCheck)

        # Health bar checkbox
        self.healthBarCheckBox = QtWidgets.QCheckBox(parent)
        self.healthBarCheckBox.setGeometry(QtCore.QRect(5, 65, 86, 16))
        self.healthBarCheckBox.setStyleSheet(self.CHECKBOX_STYLE)
        self.healthBarCheckBox.setObjectName("healthBarCheckBox")
        self.healthBarCheckBox.setChecked(Visual.HealthStatus)

        # Weapon checkbox
        self.weaponCheckBox = QtWidgets.QCheckBox(parent)
        self.weaponCheckBox.setGeometry(QtCore.QRect(5, 85, 73, 16))
        self.weaponCheckBox.setStyleSheet(self.CHECKBOX_STYLE)
        self.weaponCheckBox.setObjectName("weaponCheckBox")
        self.weaponCheckBox.setChecked(Visual.WeaponStatus)

        # Line checkbox
        self.lineCheckBox = QtWidgets.QCheckBox(parent)
        self.lineCheckBox.setGeometry(QtCore.QRect(5, 105, 48, 16))
        self.lineCheckBox.setStyleSheet(self.CHECKBOX_STYLE)
        self.lineCheckBox.setObjectName("lineCheckBox")
        self.lineCheckBox.setChecked(Visual.LineStatus)

        # Crosshair ESP checkbox
        self.crosshairESPCheckBox_2 = QtWidgets.QCheckBox(parent)
        self.crosshairESPCheckBox_2.setGeometry(QtCore.QRect(5, 140, 130, 16))
        self.crosshairESPCheckBox_2.setStyleSheet(self.CHECKBOX_STYLE)
        self.crosshairESPCheckBox_2.setObjectName("crosshairESPCheckBox_2")
        self.crosshairESPCheckBox_2.setChecked(Visual.CrosshairStatus)

        # Bomb timer checkbox
        self.BombTimerCheckBox = QtWidgets.QCheckBox(parent)
        self.BombTimerCheckBox.setGeometry(QtCore.QRect(5, 195, 94, 16))
        self.BombTimerCheckBox.setStyleSheet(self.CHECKBOX_STYLE)
        self.BombTimerCheckBox.setObjectName("BombTimerCheckBox")
        self.BombTimerCheckBox.setChecked(Visual.BombESPStatus)

    def _setupSliders(self, parent):
        # Sniper crosshair slider
        self.sniperCrosshairSlider = QtWidgets.QSlider(parent)
        self.sniperCrosshairSlider.setGeometry(QtCore.QRect(5, 160, 130, 22))
        self.sniperCrosshairSlider.setStyleSheet("""
            QSlider::groove:horizontal {
                height: 8px;
                background: #0097e6;
            }

            QSlider::handle:horizontal {
                background: #1e3799;
                width: 15px;
            }
        """)
        self.sniperCrosshairSlider.setMinimum(2)
        self.sniperCrosshairSlider.setMaximum(20)
        self.sniperCrosshairSlider.setProperty("value", Visual.CrosshairSize)
        self.sniperCrosshairSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sniperCrosshairSlider.setObjectName("sniperCrosshairSlider")

        # Sniper crosshair label
        self.sniperCrosshairLable = QtWidgets.QLabel(parent)
        self.sniperCrosshairLable.setGeometry(QtCore.QRect(140, 163, 21, 16))
        self.sniperCrosshairLable.setStyleSheet("font: 10pt \"Arial\";\n"
            "color: rgb(220, 221, 225);\n"
            "font-weight: bold;")
        self.sniperCrosshairLable.setAlignment(QtCore.Qt.AlignCenter)
        self.sniperCrosshairLable.setObjectName("sniperCrosshairLable")

    def _setupColorButtons(self, parent):
        # Box ESP color button
        self.boxESPColorEdit = QtWidgets.QPushButton(parent)
        self.boxESPColorEdit.setGeometry(QtCore.QRect(280, 25, 16, 16))
        self.boxESPColorEdit.setStyleSheet(f"background-color: {Visual.BoxESPColor};\n"
            "border: none;")
        self.boxESPColorEdit.setText("")
        self.boxESPColorEdit.setObjectName("boxESPColorEdit")

        # Line color button
        self.lineColorEdit = QtWidgets.QPushButton(parent)
        self.lineColorEdit.setGeometry(QtCore.QRect(280, 105, 16, 16))
        self.lineColorEdit.setStyleSheet(f"background-color: {Visual.LineColor};\n"
            "border: none;")
        self.lineColorEdit.setText("")
        self.lineColorEdit.setObjectName("lineColorEdit")

        # Sniper crosshair color button
        self.sniperCorsshairColorEdit = QtWidgets.QPushButton(parent)
        self.sniperCorsshairColorEdit.setGeometry(QtCore.QRect(280, 135, 16, 16))
        self.sniperCorsshairColorEdit.setStyleSheet(f"background-color: {Visual.CrosshairColor};\n"
            "border: none;")
        self.sniperCorsshairColorEdit.setText("")
        self.sniperCorsshairColorEdit.setObjectName("sniperCorsshairColorEdit")

    def _setupZOrder(self):
        # Raise elements in correct order
        self.Background.raise_()
        self.titlePanel.raise_()
        self.closeButton.raise_()
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
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x_main, y_main = self.geometry().x(), self.geometry().y()
            cursor_x, cursor_y = QtGui.QCursor.pos().x(), QtGui.QCursor.pos().y()

            # Check if cursor is within window bounds
            if (x_main <= cursor_x <= x_main + self.geometry().width() and
                y_main <= cursor_y <= y_main + self.geometry().height()):
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
            if not self.old_pos:
                return
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)
        except:
            pass
