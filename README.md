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
