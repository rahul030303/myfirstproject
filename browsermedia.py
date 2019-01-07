# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browsermedia.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ToBrowser(object):
    def setupUi(self, ToBrowser):
        ToBrowser.setObjectName("ToBrowser")
        ToBrowser.resize(240, 320)
        self.centralwidget = QtWidgets.QWidget(ToBrowser)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 151, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 120, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(76, 100, 71, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        ToBrowser.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ToBrowser)
        self.statusbar.setObjectName("statusbar")
        ToBrowser.setStatusBar(self.statusbar)

        self.retranslateUi(ToBrowser)
        QtCore.QMetaObject.connectSlotsByName(ToBrowser)

    def retranslateUi(self, ToBrowser):
        _translate = QtCore.QCoreApplication.translate
        ToBrowser.setWindowTitle(_translate("ToBrowser", "MainWindow"))
        self.pushButton.setText(_translate("ToBrowser", "Go"))
        self.label.setText(_translate("ToBrowser", "Access Internet Here..."))
        self.label_2.setText(_translate("ToBrowser", "Enter URL:"))
        self.pushButton_2.setText(_translate("ToBrowser", "Cancel"))

