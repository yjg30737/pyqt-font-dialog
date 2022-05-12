# pyqt-font-dialog
PyQt Font Dialog

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-font-dialog.git --upgrade```

## Usage
```python
dialog = FontDialog(textEdit.currentFont())
reply = dialog.exec()
if reply == QDialog.Accepted:
    textEdit.setCurrentFont(dialog.get_font())
```

## Preview
![image](https://user-images.githubusercontent.com/55078043/167970048-cd8e1d76-d2f2-4c63-964d-87158d8dc53c.png)
