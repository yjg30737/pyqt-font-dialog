from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QTextEdit
from pyqt_font_dialog.fontWidget import FontWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__te = QTextEdit()
        fontWidget = FontWidget()
        fontWidget.fontChanged.connect(self.fontChanged)
        # fontWidget.setCurrentFont(QFont('Arial', 18))

        lay = QHBoxLayout()
        lay.addWidget(self.__te)
        lay.addWidget(fontWidget)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

    def fontChanged(self, font):
        self.__te.setFont(font)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())