from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QListWidget, QWidget, QVBoxLayout, QLabel, QLineEdit


class SizeWidget(QWidget):
    sizeItemChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__sizeLineEdit = QLineEdit()
        self.__sizeLineEdit.setReadOnly(True)

        self.__sizeListWidget = QListWidget()
        self.__initSizes()
        self.__sizeListWidget.itemSelectionChanged.connect(self.__sizeItemChanged)

        lay = QVBoxLayout()
        lay.addWidget(self.__sizeLineEdit)
        lay.addWidget(self.__sizeListWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        sizeBottomWidget = QWidget()
        sizeBottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(QLabel('Size'))
        lay.addWidget(sizeBottomWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(5)

        self.setLayout(lay)

    def __initSizes(self):
        fd = QFontDatabase()
        fm = fd.families(QFontDatabase.Any)
        font_name = fm[0]
        style_name = fd.styles(font_name)[0]
        sizes = fd.pointSizes(font_name, style_name)
        sizes = list(map(str, sizes))
        self.__sizeListWidget.addItems(sizes)
        self.__sizeListWidget.setCurrentRow(0)
        self.__sizeLineEdit.setText(sizes[0])

    def setSizes(self, sizes, prev_size=10):
        sizes = list(map(str, sizes))
        self.__sizeListWidget.clear()
        self.__sizeListWidget.addItems(sizes)
        item = self.__sizeListWidget.findItems(str(prev_size), Qt.MatchFixedString)[0]
        if item:
            pass
        else:
            item = self.__sizeListWidget.item(0)
        self.__sizeListWidget.setCurrentItem(item)
        self.__sizeLineEdit.setText(item.text())

    def __sizeItemChanged(self):
        self.sizeItemChanged.emit(int(self.__sizeListWidget.currentItem().text()))

