from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QListWidget, QWidget, QLineEdit, QVBoxLayout, QLabel, QGroupBox, QCheckBox, QGridLayout


class StyleWidget(QWidget):
    boldChecked = pyqtSignal(bool)
    italicChecked = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        groupBox = QGroupBox()
        groupBox.setTitle('Style')

        boldChkBox = QCheckBox('Bold')
        italicChkBox = QCheckBox('Italic')

        boldChkBox.stateChanged.connect(self.boldChecked)
        italicChkBox.stateChanged.connect(self.italicChecked)

        lay = QVBoxLayout()
        lay.addWidget(boldChkBox)
        lay.addWidget(italicChkBox)

        groupBox.setLayout(lay)

        lay = QGridLayout()
        lay.addWidget(groupBox)

        self.setLayout(lay)

