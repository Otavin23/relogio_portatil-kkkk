from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from menu2 import Ui_MainWindow

class TelaSalvar(QMainWindow):

    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Salvar
        self.ui.actionSalvar.triggered.connect(self.salvar)

    def salvar(self):
        nome = self.ui.lineEdit_3.text()
        idade = self.ui.lineEdit.text()
        telefone = self.ui.lineEdit_2.text()
        dados = "Nome:" + nome + "\n"+"Idade:" + idade + "\n" +"Telefone:" + telefone + "\n"

        arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]
        with open(arquivo + ".txt", "w") as arquivos:
            arquivos.write(dados)
            print(arquivo)


if __name__ == "__main__":
    import os,sys
    app = QApplication(sys.argv)
    window = TelaSalvar()
    window.show()
    sys.exit(app.exec_())