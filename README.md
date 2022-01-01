# pyqt-font-dialog
Font dialog made with PyQt

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-font-dialog.git --upgrade```

## Usage
```python
dialog = FontDialog()
reply = dialog.exec()
if reply == QDialog.Accepted:
    self.__mainTextEdit.setCurrentFont(dialog.get_font())
```

## Preview
![example](example/example.png)
