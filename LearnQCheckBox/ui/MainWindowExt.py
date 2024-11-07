import os
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from LearnQCheckBox.ui.tt import Ui_MainWindow
class MainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSingalAndSlot()
    def showWindow(self):
        self.show()
    def xuly_doihinh(self,value):
        state=Qt.CheckState(value)
        current_dir = os.getcwd()
        if state==Qt.CheckState.Checked:
            hinh=f"{current_dir}/Users/nguyenngocaithien/NguyenNgocAiThien_K234111417_K234111E/LearnQCheckBox/images/185028_iphone_phone_icon.png"
        elif state==Qt.CheckState.Unchecked:
            hinh=f"{current_dir}/Users/nguyenngocaithien/NguyenNgocAiThien_K234111417_K234111E/LearnQCheckBox/images/185028_iphone_phone_icon.png"
        pixmap=QPixmap(hinh)
        self.labelHinh.setPixmap(pixmap)
    def setupSingalAndSlot(self):
        self.checkBoxHinh.stateChanged.connect(self.xuly_doihinh)
