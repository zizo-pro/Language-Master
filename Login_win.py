from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from sys import argv
from qt_material import apply_stylesheet



FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),r"GUI/Login_win.ui"))

class lol(QMainWindow,FORM_CLASS):
    def __init__(self, parent=None):
        super(lol,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    apps = QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    window = lol()
    window.show()
    apply_stylesheet(apps, theme='dark_teal.xml')
    apps.exec()