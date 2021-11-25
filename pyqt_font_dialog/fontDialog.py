from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QLabel, QDialog, QSizePolicy, \
    QTextEdit, QApplication, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt

from pyqt_font_dialog.fontWidget import FontWidget
from pyqt_font_dialog.sizeWidget import SizeWidget
from pyqt_font_dialog.styleWidget import StyleWidget


class FontDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Font')
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setFixedSize(500, 400)

        self.__previewTextEdit = QTextEdit()
        self.__previewTextEdit.setText('Sample')

        self.__fontWidget = FontWidget()
        self.__fontWidget.fontItemChanged.connect(self.__fontItemChangedExec)

        self.__styleWidget = StyleWidget()
        self.__styleWidget.boldChecked.connect(self.__setBold)
        self.__styleWidget.italicChecked.connect(self.__setItalic)

        self.__sizeWidget = SizeWidget()
        self.__sizeWidget.sizeItemChanged.connect(self.__sizeItemChangedExec)

        lay = QHBoxLayout()
        lay.addWidget(self.__fontWidget)
        lay.addWidget(self.__styleWidget)
        lay.addWidget(self.__sizeWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        topWidget = QWidget()
        topWidget.setLayout(lay)

        okBtn = QPushButton('OK')
        cancelBtn = QPushButton('Cancel')

        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.close)

        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignRight)
        lay.addWidget(okBtn)
        lay.addWidget(cancelBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        okCancelWidget = QWidget()
        okCancelWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(QLabel('Preview'))
        lay.addWidget(self.__previewTextEdit)
        lay.addWidget(okCancelWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(5)

        bottomWidget = QWidget()
        bottomWidget.setLayout(lay)
        bottomWidget.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

        lay = QVBoxLayout()
        lay.addWidget(topWidget)
        lay.addWidget(bottomWidget)
        lay.setContentsMargins(5, 5, 5, 5)
        self.setLayout(lay)

    def __setBold(self, f: int):
        font = self.__previewTextEdit.currentFont()
        font.setBold(f)
        self.__previewTextEdit.setCurrentFont(font)

    def __setItalic(self, f: bool):
        font = self.__previewTextEdit.currentFont()
        font.setItalic(f)
        self.__previewTextEdit.setCurrentFont(font)

    def __sizeItemChangedExec(self, size):
        self.__previewTextEdit.selectAll()
        font = self.__previewTextEdit.currentFont()
        font.setPixelSize(size)
        self.__previewTextEdit.setCurrentFont(font)

    def __fontItemChangedExec(self, font_text, fd):
        styles = fd.styles(font_text)
        self.__styleWidget.setStyles(styles)

        sizes = fd.pointSizes(font_text, styles[0])
        self.__sizeWidget.setSizes(sizes)

        font = QFont()
        font.setFamily(font_text)
        font.setPixelSize(int(sizes[0]))
        font.setStyleName(styles[0])

        self.__previewTextEdit.setCurrentFont(font)

    def getFont(self):
        return self.__previewTextEdit.currentFont()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dialog = FontDialog()
    dialog.show()
    app.exec_()
