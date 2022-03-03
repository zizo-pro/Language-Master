# import mysql.connector
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
# db = mysql.connector.connect(
#   host = "localhost",
#   user = "ziad",
#   passwd = "@zizo2412@",
#   database = "german_database"
# )
FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"GUI/main-gui-file.ui"))

class mainapp(QMainWindow,FORM_CLASS):
    def __init__(self, parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
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
        self.comboBox.lineEdit().textEdited.connect(self.comboBox.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)
    def on_completer_activated(self, text):
        if text:
            index = self.comboBox.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))
            print(index)

    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)

    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column) 




if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    window = mainapp()
    string_list = ['hola muchachos',
                   'adios amigos', 'hello world', 'good bye',
                   'more data', 'just','maro','zizo','potato','das']
    apply_stylesheet(app, theme='dark_teal.xml')
    combo = window.comboBox
    combo.addItems(string_list)

    window.show()
    exit(app.exec_())
