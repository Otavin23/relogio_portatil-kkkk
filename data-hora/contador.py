# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relogio.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 134)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 311, 20))
        self.label_2.setStyleSheet("QLabel{\n"
"    color: rgb(33, 192, 91);\n"
"    font-size: 15px;\n"
"\n"
"    \n"
"    font: 8pt \"Meiryo\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 0, 341, 91))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    font-size: 45px;\n"
"    font-family:Arial,Helvetica,sans-serif;\n"
"    color: rgb(33, 192, 91);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "                        "))