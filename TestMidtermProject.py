from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowMidtermExt import MainWindowMidtermExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowMidtermExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()