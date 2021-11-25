from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QListWidget, QWidget, QLineEdit, QVBoxLayout, QLabel


class StyleWidget(QWidget):
    styleItemChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__styleLineEdit = QLineEdit()
        self.__styleLineEdit.setReadOnly(True)

        self.__styleListWidget = QListWidget()
        self.__initStyles()
        self.__styleListWidget.itemSelectionChanged.connect(self.__styleItemChanged)

        lay = QVBoxLayout()
        lay.addWidget(self.__styleLineEdit)
        lay.addWidget(self.__styleListWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        styleBottomWidget = QWidget()
        styleBottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(QLabel('Style'))
        lay.addWidget(styleBottomWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(5)

        self.setLayout(lay)

    def __initStyles(self):
        fd = QFontDatabase()
        fm = fd.families(QFontDatabase.Any)
        style_name = fm[0]
        styles = fd.styles(style_name)
        self.__styleListWidget.addItems(styles)
        self.__styleListWidget.setCurrentRow(0)
        self.__styleLineEdit.setText(style_name)

    def setStyles(self, styles):
        self.__styleListWidget.clear()
        self.__styleListWidget.addItems(styles)
        item = self.__styleListWidget.item(0)
        if item:
            self.__styleListWidget.setCurrentItem(item)
            self.__styleLineEdit.setText(item.text())

    def __styleItemChanged(self):
        style = self.__styleListWidget.currentItem().text()
        self.styleItemChanged.emit(style)