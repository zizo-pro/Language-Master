from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from sys import argv
from qt_material import apply_stylesheet


FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),r"GUI/add_to_db.ui"))

class myapp(QMainWindow,FORM_CLASS):
    def __init__(self, parent=None):
        super(myapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    window = myapp()
    window.show()
    apply_stylesheet(app, theme='dark_teal.xml')
    app.exec()