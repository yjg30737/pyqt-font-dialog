from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QListWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QListWidgetItem


class SizeWidget(QWidget):
    sizeItemChanged = pyqtSignal(int)

    def __init__(self, font: QFont = QFont('Arial', 10)):
        super().__init__()
        self.__initUi(font=font)

    def __initUi(self, font: QFont):
        self.__sizeLineEdit = QLineEdit()
        self.__sizeLineEdit.setReadOnly(True)

        self.__sizeListWidget = QListWidget()
        self.__initSizes(font=font)
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

    def __initSizes(self, font: QFont):
        self.__initSizesList(font=font)
        self.__initCurrentSize(font=font)

    def __initSizesList(self, font: QFont):
        fd = QFontDatabase()
        font_name = font.family()
        style_name = fd.styles(font_name)
        # In case of font is not in the font list
        if style_name:
            style_name = style_name[0]
        else:
            font_name = 'Arial'
            style_name = fd.styles(font_name)
        sizes = fd.pointSizes(font_name, style_name)
        sizes = list(map(str, sizes))
        self.__sizeListWidget.addItems(sizes)

    def __initCurrentSize(self, font: QFont):
        # find the pixel size instead of point size because point size is always -1 at this point for some reasons
        items = self.__sizeListWidget.findItems(str(font.pixelSize()), Qt.MatchFixedString)
        item = QListWidgetItem()
        if items:
            item = items[0]
        else:
            item = self.__sizeListWidget.item(0)
        self.__sizeListWidget.setCurrentItem(item)
        size_text = item.text()
        self.__sizeLineEdit.setText(size_text)

    def setSizes(self, sizes, prev_size=10):
        sizes = list(map(str, sizes))
        self.__sizeListWidget.clear()
        self.__sizeListWidget.addItems(sizes)
        items = self.__sizeListWidget.findItems(str(prev_size), Qt.MatchFixedString)
        item = ''
        if items:
            item = items[0]
        else:
            item = self.__sizeListWidget.item(0)
        self.__sizeListWidget.setCurrentItem(item)
        self.__sizeLineEdit.setText(item.text())

    def __sizeItemChanged(self):
        self.sizeItemChanged.emit(int(self.__sizeListWidget.currentItem().text()))

    def getSize(self):
        return self.__sizeListWidget.currentItem().text()