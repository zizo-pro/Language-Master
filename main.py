import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QStringListModel
from os import path
from sys import argv,exit
from qt_material import apply_stylesheet
from speech import deutsch_lang
from add import myapp

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"GUI/main-gui-file.ui"))

class mainapp(QMainWindow,FORM_CLASS):
  def __init__(self, parent=None):
      super(mainapp,self).__init__(parent)
      QMainWindow.__init__(self)
      self.setupUi(self)
      self.initialize()
      self.Database()
      self.button_setup()
      self.combobox_init()

  def initialize(self):
    self.first_open()
    self.search_shortcut = QShortcut("return", self)

  def combobox_init(self):
      self.comboBox.setEditable(True)
      self.comboBox.setFocusPolicy(Qt.StrongFocus)
      self.comboBox.completer().setCompletionMode(QCompleter.PopupCompletion)
      self.comboBox.setInsertPolicy(QComboBox.NoInsert)
      self.comboBox.pFilterModel = QSortFilterProxyModel(self)
      self.comboBox.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
      self.comboBox.pFilterModel.setSourceModel(self.comboBox.model())
      self.completer = QCompleter(self.comboBox.pFilterModel, self)
      self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
      self.comboBox.setCompleter(self.completer)
      self.comboBox.setCurrentText("")
      self.comboBox.lineEdit().textEdited.connect(self.comboBox.pFilterModel.setFilterFixedString)
      self.completer.activated.connect(self.on_completer_activated)

  def on_completer_activated(self, text):
      if text:
          index = self.comboBox.findText(text)
          self.comboBox.setCurrentIndex(index)
          self.comboBox.activated[str].emit(self.comboBox.itemText(index))

  def setModel(self, model):
      super(ExtendedComboBox, self).setModel(model)
      self.pFilterModel.setSourceModel(model)
      self.completer.setModel(self.pFilterModel)

  def setModelColumn(self, column):
      self.completer.setCompletionColumn(column)
      self.pFilterModel.setFilterKeyColumn(column)
      super(ExtendedComboBox, self).setModelColumn(column) 

  def button_setup(self):
      self.search_BT.clicked.connect(self.check_word)
      self.speaker_BT.clicked.connect(self.speaker)
      self.search_shortcut.activated.connect(self.check_word)
      self.add_BT.clicked.connect(self.add_db)
      

  def check_word(self):
    self.comb = self.comboBox.currentText()
    if self.comb in self.all:
      self.search()

  def first_open(self):
      self.article_DB.hide()
      self.article_LB.hide()
      self.category_DB.hide()
      self.category_LB.hide()
      self.meaning_DB.hide()
      self.meaning_LB.hide()
      self.plural_DB.hide()
      self.plural_LB.hide()
      self.type_DB.hide()
      self.type_LB.hide()
      self.word_DB.hide()
      self.word_LB.hide()
      self.setGeometry(200,200,335,90)
      self.setFixedSize(335,90)
      self.comboBox.setGeometry(15,20,230,25)
      self.search_BT.setGeometry(255,20,30,25)
      self.speaker_BT.setGeometry(290,20,30,25)
      self.add_BT.setGeometry(115,55,75,25)

  def search(self):
    self.combotext = self.comboBox.currentText()
    self.article_DB.show()
    self.article_LB .show()
    self.category_DB.show()
    self.category_LB.show()
    self.meaning_DB.show()
    self.meaning_LB.show()
    self.plural_DB.show()
    self.plural_LB.show()
    self.type_DB.show()
    self.type_LB.show()
    self.word_DB.show()
    self.word_LB.show()
    self.resize(445,315)
    self.setFixedSize(445,315)
    self.comboBox.setGeometry(80,20,230,25)
    self.search_BT.setGeometry(315,20,30,25)
    self.speaker_BT.setGeometry(350,20,30,25)
    self.add_BT.setGeometry(350,270,75,25)

    if self.combotext in self.verbs:
      self.word_LB.setText("Verb :")
      self.article_LB.setText("Perfect :")
      self.plural_LB.setText("Status :")
      self.category_LB.setText("Hilfsverb :")

      self.cr.execute(f"SELECT * FROM verbs WHERE verb = '{self.combotext}'")
      self.data = self.cr.fetchone()

      self.word_DB.setText(self.data[0])
      self.article_DB.setText(self.data[1])
      self.meaning_DB.setText(self.data[2])
      self.type_DB.setText(self.data[3])
      self.plural_DB.setText(self.data[4])
      self.category_DB.setText(self.data[5])
      self.example_DB.setText(self.data[6])

    elif self.combotext in self.nouns:
      self.word_LB.setText("Word :")
      self.article_LB.setText("Article :")
      self.plural_LB.setText("Plural :")
      self.category_LB.setText("Category :")
      self.cr.execute(f"SELECT * FROM nouns WHERE noun = '{self.combotext}'")
      self.data = self.cr.fetchone()
      self.article_DB.setText(self.data[0])
      self.word_DB.setText(self.data[1])
      self.meaning_DB.setText(self.data[2])
      self.type_DB.setText(self.data[3])
      self.plural_DB.setText(self.data[4])
      self.category_DB.setText(self.data[5])
      self.example_DB.setText(self.data[6])

    elif self.combotext in self.adjectives:
      self.word_LB.setText("adjective :")
      self.article_LB.setText("Type :")
      self.plural_LB.setText("weiblich :")
      self.category_LB.setText("Neutral :")
      self.type_LB.setText("männlich :")
      self.cr.execute(f"SELECT * FROM adjectives WHERE adjective = '{self.combotext}'")
      self.data = self.cr.fetchone()
      self.word_DB.setText(self.data[0])
      self.meaning_DB.setText(self.data[1])
      self.type_DB.setText(self.data[2])
      self.plural_DB.setText(self.data[3])
      self.category_DB.setText(self.data[4])
      self.article_DB.setText(self.data[5])
      self.example_DB.setText(self.data[6])
  
  def speaker(self):
      deutsch_lang(self.comboBox.currentText())

  def add_db(self):
    self.add_db_win = myapp()
    self.add_db_win.show()
    self.add_db_win.add_BT.clicked.connect(self.add_DATA)

  def Database(self):
      self.verbs = []
      self.nouns = []
      self.adjectives = []
      self.all = [""]

      self.db = mysql.connector.connect(
        host = "localhost",
        user = "ziad",
        passwd = "@zizo2412@",
        database = "german_database"
      )
      self.cr = self.db.cursor()
      
      self.cr.execute("SELECT noun FROM nouns")
      self.combodata = self.cr.fetchall()
      for noun in self.combodata:
        self.nouns.append(noun[0])
        self.all.append(noun[0])

      self.cr.execute("SELECT verb FROM verbs")
      self.combodata2 = self.cr.fetchall()
      for verb in self.combodata2:
        self.verbs.append(verb[0])
        self.all.append(verb[0])

      
      self.cr.execute("SELECT adjective FROM adjectives")
      self.combodata3 = self.cr.fetchall()
      for adjective in self.combodata3:
        self.adjectives.append(adjective[0])
        self.all.append(adjective[0])

  def add_DATA(self):
    self.word_typ = self.add_db_win.word_type.currentText()
    
    word = self.add_db_win.word_input.text()
    meaning = self.add_db_win.meaning_input.text()
    plural = self.add_db_win.plural_input.text()
    article = self.add_db_win.article_input.text()
    category = self.add_db_win.category_input.text()
    example = self.add_db_win.example_input.text()
    if self.word_typ.upper() == "NOUN":
      cr.execute("INSERT INTO nouns (article,noun,meaning,type,plural,category,example) VALUES (%s,%s,%s,%s,%s,%s,%s)",(article,word,meaning,self.word_typ,plural,category,example))

    self.add_db_win.word_input.setText("")
    self.add_db_win.meaning_input.setText("")
    self.add_db_win.plural_input.setText("")
    self.add_db_win.article_input.setText("")
    self.add_db_win.category_input.setText("")
    self.add_db_win.example_input.setText("")
if __name__ == "__main__":
  app = QApplication(argv)
  MainWindow = QtWidgets.QMainWindow()
  window = mainapp()

  apply_stylesheet(app, theme='dark_teal.xml')

  combo = window.comboBox
  combo.addItems(sorted(window.all))

  window.show()
  exit(app.exec_())