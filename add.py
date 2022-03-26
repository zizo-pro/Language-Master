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
        self.admin_password = "1"
        self.first_open()
        self.button_setup()

    def button_setup(self):
      self.proceed_BT.clicked.connect(self.proceed)
      self.word_type.currentIndexChanged.connect(self.change_labels)

    def first_open(self):
      self.article_LB.hide()
      self.word_LB.hide()
      self.password.setGeometry(15,20,230,20)
      self.word_type.setGeometry(209,20,90,20)
      self.proceed_BT.setGeometry(112,50,75,25)
      self.setGeometry(200,200,320,85)
      self.setFixedSize(320,85)

    def proceed(self):
      if self.password.text() == self.admin_password:
        self.setGeometry(200,200,445,300)
        self.setFixedSize(445,300)
        self.word_type.setGeometry(280,139,150,25)
        self.word_type.setStyleSheet("border:0;")
        self.password.hide()
        self.proceed_BT.hide()
        self.article_LB.show()
        self.word_LB.show()
        self.change_labels()
      else:
        print("error")

    def change_labels(self):
      self.wordtyp = self.word_type.currentText()
      if self.wordtyp == "Verb":
        self.word_LB.setText("Verb :")
        self.article_LB.setText("Perfect :")
        self.plural_LB.setText("Status :")
        self.category_LB.setText("Hilfsverb :")
        self.type_LB.setText("Type :")

      elif self.wordtyp == "Noun":
        self.word_LB.setText("Word :")
        self.article_LB.setText("Article :")
        self.plural_LB.setText("Plural :")
        self.category_LB.setText("Category :")
        self.type_LB.setText("Type :")

      elif self.wordtyp == "Adjective":
        self.word_LB.setText("Adjective :")
        self.article_LB.setText("männlich :")
        self.plural_LB.setText("Weiblich :")
        self.category_LB.setText("Neutral :")
        self.type_LB.setText("Type :")

      self.move_things()

    def move_things(self):
      self.word_LB.setGeometry(15,29,210,20)
      self.meaning_LB.setGeometry(15,79,210,20)
      self.plural_LB.setGeometry(15,129,210,20)

      self.word_input.setGeometry(15,49,210,25)
      self.meaning_input.setGeometry(15,99,210,25)
      self.plural_input.setGeometry(15,149,210,25)


      self.article_LB.setGeometry(280,29,140,20)
      self.type_LB.setGeometry(280,79,140,20)
      self.category_LB.setGeometry(280,129,140,20)
      self.example_LB.setGeometry(190,182,140,20)

      self.article_input.setGeometry(280,49,150,25)
      self.word_type.setGeometry(280,99,150,25)
      self.category_input.setGeometry(280,149,150,25)
      self.example_input.setGeometry(15,202,415,25)

      self.add_BT.setGeometry(180,235,75,25)

      self.resize(445, 280)
      self.setFixedSize(445,280)

if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    window = myapp()
    window.show()
    apply_stylesheet(app, theme='dark_teal.xml')
    app.exec()