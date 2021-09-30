from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
from menu_style import Ui_MainWindow


class TelaMenu(QMainWindow):
    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAzul.triggered.connect(self.azul)
        self.ui.actionVerde.triggered.connect(self.verde)
        self.ui.actionVermelho.triggered.connect(self.vermelho)

    def vermelho(self):
        label = self.ui.label_2.setText("Vermelho")
        label = self.ui.label_2.setStyleSheet("color: red;\n"
                                            "font-size: 30px;\n"
                                            "padding-left:20px")


    def azul(self):
        label = self.ui.label_2.setText("Azul")
        label = self.ui.label_2.setStyleSheet("color: blue;\n"
                                              "font-size: 30px;\n"
                                              "padding-left: 20px;")
    def verde(self):
        label = self.ui.label_2.setText("Verde")
        label = self.ui.label_2.setStyleSheet("color: green;\n"
                                              "font-size: 30px;\n"
                                              "padding-left: 20px;")
if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = TelaMenu()
    window.show()
    sys.exit(app.exec_())