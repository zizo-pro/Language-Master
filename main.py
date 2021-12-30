from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from sys import argv
from time import sleep

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"first_window.ui"))

class mainapp(QMainWindow,FORM_CLASS):
    def __init__(self, parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.welcome_label.hide()
        self.button_setup()


    def button_setup(self):
        self.proceed_button.clicked.connect(self.login)

    def login(self):
        self.welcome_label.show()
        sleep(1)
        QTimer.singleShot(750,self.hide)


if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QMainWindow()
    window = mainapp()
    window.show()
    app.exec()