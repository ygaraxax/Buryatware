import Function.AutoPistol as AutoPistol
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_autoPistolWindow(object):
    def setupUi(self, autoPistolWindow):
        # Main window setup
        autoPistolWindow.setObjectName("autoPistolWindow")
        autoPistolWindow.resize(300, 320)
        
        # Title panel setup
        self.titlePanel = QtWidgets.QLabel(autoPistolWindow)
        self.titlePanel.setGeometry(QtCore.QRect(0, 0, 300, 20))
        self.titlePanel.setStyleSheet("background-color: rgb(50, 50, 55);\n"
"font: 75 10pt \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(245, 246, 250);\n"
"padding-left: 1px;")
        self.titlePanel.setObjectName("titlePanel")

        # Close button setup
        self.closeButton = QtWidgets.QPushButton(autoPistolWindow)
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
        self.closeButton.clicked.connect(lambda: self.close())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/Image/Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(20, 20))
        self.closeButton.setObjectName("closeButton")

        # Background setup
        self.Background = QtWidgets.QLabel(autoPistolWindow)
        self.Background.setGeometry(QtCore.QRect(0, 0, 300, 320))
        self.Background.setStyleSheet("background-color: rgb(30, 30, 35)")
        self.Background.setText("")
        self.Background.setObjectName("Background")

        # Mouse list combo box setup
        self.mouseListComboBox = QtWidgets.QComboBox(autoPistolWindow)
        self.mouseListComboBox.setGeometry(QtCore.QRect(5, 45, 130, 22))
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
        
        # Add mouse options
        mouse_options = ["MOUSE2", "MOUSE4", "MOUSE5", "MOUSE6"]
        for option in mouse_options:
            self.mouseListComboBox.addItem(option)

        # Mouse list label setup
        self.mouseListLable = QtWidgets.QLabel(autoPistolWindow)
        self.mouseListLable.setGeometry(QtCore.QRect(5, 25, 63, 16))
        self.mouseListLable.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(220, 221, 225);\n"
"font-weight: bold;")
        self.mouseListLable.setAlignment(QtCore.Qt.AlignCenter)
        self.mouseListLable.setObjectName("mouseListLable")

        # Set z-order of widgets
        self.Background.raise_()
        self.titlePanel.raise_()
        self.closeButton.raise_()
        self.mouseListComboBox.raise_()
        self.mouseListLable.raise_()

        self.retranslateUi(autoPistolWindow)
        QtCore.QMetaObject.connectSlotsByName(autoPistolWindow)

    def retranslateUi(self, autoPistolWindow):
        _translate = QtCore.QCoreApplication.translate
        autoPistolWindow.setWindowTitle(_translate("autoPistolWindow", "Auto Pistol"))
        self.titlePanel.setText(_translate("autoPistolWindow", "Auto Pistol"))
        
        # Set mouse list items
        for i, text in enumerate(["MOUSE2", "MOUSE4", "MOUSE5", "MOUSE6"]):
            self.mouseListComboBox.setItemText(i, _translate("autoPistolWindow", text))
            
        # Set current selection based on AutoPistol virtual key
        self.mouseListComboBox.setCurrentText("None" if (AutoPistol.VirtualKey == 0) else f"MOUSE{AutoPistol.VirtualKey}")
        self.mouseListLable.setText(_translate("autoPistolWindow", "Mouse list"))


class Widget(QtWidgets.QWidget, Ui_autoPistolWindow):
    def __init__(self, parent = None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.old_pos = None  # Initialize old_pos

    def mousePressEvent(self, event):
        # Handle window dragging
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
        # Move window with mouse drag
        try:
            if not self.old_pos:
                return
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)
        except:
            pass
