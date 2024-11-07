from PyQt6.QtWidgets import QMainWindow, QApplication
from LearnQCheckBox.ui.MainWindowExt import MainWindowExt
app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()