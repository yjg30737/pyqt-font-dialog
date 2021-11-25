from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QListWidget, QWidget, QVBoxLayout, QLabel, QLineEdit


class FontWidget(QWidget):
    fontItemChanged = pyqtSignal(str, QFontDatabase)

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__fontLineEdit = QLineEdit()
        self.__fontLineEdit.setReadOnly(True)

        self.__fontListWidget = QListWidget()
        self.__initFonts()
        self.__fontListWidget.itemSelectionChanged.connect(self.__fontItemChanged)

        lay = QVBoxLayout()
        lay.addWidget(self.__fontLineEdit)
        lay.addWidget(self.__fontListWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        fontBottomWidget = QWidget()
        fontBottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(QLabel('Font'))
        lay.addWidget(fontBottomWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(5)

        self.setLayout(lay)

    def __initFonts(self):
        fd = QFontDatabase()
        fm = fd.families(QFontDatabase.Any)
        self.__fontListWidget.addItems(fm)
        item = self.__fontListWidget.item(0)
        self.__fontListWidget.setCurrentItem(item)
        font_name = item.text()
        self.__fontLineEdit.setText(font_name)

    def __fontItemChanged(self):
        font_name = self.__fontListWidget.currentItem().text()
        self.__fontLineEdit.setText(font_name)
        fd = QFontDatabase()
        self.fontItemChanged.emit(font_name, fd)

    def getFontFamily(self):
        return self.__fontListWidget.currentItem().text()
        