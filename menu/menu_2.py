
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
from salvar import Ui_MainWindow

from menu2 import Ui_MainWindow

class TelaMenu(QMainWindow):
    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #File
        self.ui.actionSalvar.triggered.connect(self.salvar)

    def salvar(self):
        pass



if __name__ == "__main__":
    import os,sys
    app = QApplication(sys.argv)
    window = TelaMenu()
    window.show()
    sys.exit(app.exec_())