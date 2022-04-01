from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from sys import argv
from qt_material import apply_stylesheet
import urllib.request

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"GUI/Flash_cards.ui"))

class Flash_cards(QMainWindow,FORM_CLASS):
	def __init__(self, parent=None):
			super(Flash_cards,self).__init__(parent)
			QMainWindow.__init__(self)
			self.setupUi(self)
			# self.set_img("https://i.ibb.co/DQt6SzK/Android-gallery-icon-png-Transparent-Images.png")
			self.das.setCheckable(True)
			self.der.setCheckable(True)
			self.die.setCheckable(True)
			self.checked = ""
			self.button_setup()
	
	def button_setup(self):
			self.das.clicked.connect(self.das_button)
			self.der.clicked.connect(self.der_button)
			self.die.clicked.connect(self.die_button)

	def das_button(self):
		self.checked = "das"
		self.der.setChecked(False)
		self.die.setChecked(False)
	def der_button(self):
		self.checked = "der"
		self.das.setChecked(False)
		self.die.setChecked(False)
	def die_button(self):
		self.checked = "die" 
		self.der.setChecked(False)
		self.das.setChecked(False)


	def set_img(self,url):
			data = urllib.request.urlopen(url).read()
			pixmap = QPixmap()
			pixmap.loadFromData(data)
			icon = QIcon(pixmap)
			self.label.setPixmap(pixmap)


if __name__ == "__main__":
		app = QApplication(argv)
		MainWindow = QtWidgets.QMainWindow()
		window = Flash_cards()
		window.show()
		apply_stylesheet(app, theme='dark_teal.xml')
		app.exec()