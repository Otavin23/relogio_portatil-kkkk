# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 548)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 160, 511, 121))
        self.label.setStyleSheet("QLabel{\n"
"    font-size: 40px;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 290, 511, 121))
        self.label_2.setStyleSheet("QLabel{\n"
"    font-size: 30px;\n"
"}")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 18))
        self.menubar.setObjectName("menubar")
        self.menuMenu_2 = QtWidgets.QMenu(self.menubar)
        self.menuMenu_2.setObjectName("menuMenu_2")
        MainWindow.setMenuBar(self.menubar)
        self.actionVerde = QtWidgets.QAction(MainWindow)
        self.actionVerde.setObjectName("actionVerde")
        self.actionVermelho = QtWidgets.QAction(MainWindow)
        self.actionVermelho.setObjectName("actionVermelho")
        self.actionAzul = QtWidgets.QAction(MainWindow)
        self.actionAzul.setObjectName("actionAzul")
        self.menuMenu_2.addAction(self.actionVerde)
        self.menuMenu_2.addAction(self.actionVermelho)
        self.menuMenu_2.addAction(self.actionAzul)
        self.menubar.addAction(self.menuMenu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Op????o Selecionada no menu:"))
        self.label_2.setText(_translate("MainWindow", "                                     "))
        self.menuMenu_2.setTitle(_translate("MainWindow", "Cores"))
        self.actionVerde.setText(_translate("MainWindow", "Verde"))
        self.actionVermelho.setText(_translate("MainWindow", "Vermelho"))
        self.actionAzul.setText(_translate("MainWindow", "Azul"))
