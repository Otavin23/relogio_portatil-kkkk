import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from contador import Ui_Dialog

class TelaPrincipal(QDialog):

    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #Label
        self.ui.pushButton.clicked.connect(self.hora)


       # MOSTRA A HORA ,MINUTO,SEGUNDO

    def hora(self):
        import datetime
        tudo = time.localtime()
        hora = tudo[3]
        minuto = tudo[4]
        segundo = tudo[5]
        texto = self.ui.pushButton.text()
        texto = self.ui.pushButton.setText("{}:{}:{}".format(hora,minuto,segundo))
        return self.atualizar_label()


   # ATUALIZA A LABEL DA DATA OU SEJA MOSTRAR_DIA_MES_ANO

    def atualizar_label(self):
        import datetime
        tudo = time.localtime()
        dia = tudo[2]
        mes = tudo[1]
        ano = tudo[0]
        label = self.ui.label_2.text()
        label = self.ui.label_2.setStyleSheet("font-size: 17px;\n"
                                              "margin-bottom: 1px;\n"
                                              "color: rgb(33, 192, 91)\n")
        label = self.ui.label_2.setText("                      {}:{}:{}".format( dia, mes, ano))



if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = TelaPrincipal()
    window.show()
    sys.exit(app.exec_())