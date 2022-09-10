# pyqt-font-dialog
PyQt "select the font" dialog and widget

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-font-dialog`

## Class/Method Overview
* `FontDialog(font: QFont = QFont('Arial', 10), title='Font')` - font is font, title is title of the dialog.
* `FontWidget(font: QFont = QFont('Arial', 10))`
    * `fontChanged` - When current font item is changed, this will be emitted.

## Usage
### 1. As a dialog
```python
dialog = FontDialog(textEdit.currentFont())
reply = dialog.exec()
if reply == QDialog.Accepted:
    textEdit.setCurrentFont(dialog.get_font())
```

### Preview
![image](https://user-images.githubusercontent.com/55078043/167970048-cd8e1d76-d2f2-4c63-964d-87158d8dc53c.png)

### 2. As a part of window
```python
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
        lay = QHBoxLayout()
        lay.addWidget(self.__te)
        lay.addWidget(fontWidget)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

    def fontChanged(self, font):
        self.__te.selectAll()
        self.__te.setCurrentFont(font)
        cur = self.__te.textCursor()
        cur.clearSelection()
        self.__te.setTextCursor(cur)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
```

### Preview

https://user-images.githubusercontent.com/55078043/189460933-387d3570-e153-4df9-8a21-d02a46fbfe64.mp4


