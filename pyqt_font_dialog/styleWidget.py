from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QListWidget, QWidget, QLineEdit, QVBoxLayout, QLabel, QGroupBox, QCheckBox, QGridLayout


class StyleWidget(QWidget):
    boldChecked = pyqtSignal(int)
    italicChecked = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        groupBox = QGroupBox()
        groupBox.setTitle('Style')

        self.__boldChkBox = QCheckBox('Bold')
        self.__italicChkBox = QCheckBox('Italic')

        self.__boldChkBox.stateChanged.connect(self.boldChecked)
        self.__italicChkBox.stateChanged.connect(self.italicChecked)

        lay = QVBoxLayout()
        lay.setAlignment(Qt.AlignTop)
        lay.addWidget(self.__boldChkBox)
        lay.addWidget(self.__italicChkBox)
        lay.setContentsMargins(0, 0, 0, 0)

        groupBox.setLayout(lay)

        lay = QGridLayout()
        lay.addWidget(groupBox)
        lay.setContentsMargins(0, 0, 0, 0)

        self.setLayout(lay)

    def isBold(self):
        return self.__boldChkBox.isChecked()

    def isItalic(self):
        return self.__italicChkBox.isChecked()
