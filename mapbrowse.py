# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapbrowse.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Map(object):
    def setupUi(self, Map):
        Map.setObjectName("Map")
        Map.resize(240, 320)
        self.centralwidget = QtWidgets.QWidget(Map)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 171, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(36, 110, 151, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 130, 161, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        Map.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Map)
        self.statusbar.setObjectName("statusbar")
        Map.setStatusBar(self.statusbar)

        self.retranslateUi(Map)
        QtCore.QMetaObject.connectSlotsByName(Map)

    def retranslateUi(self, Map):
        _translate = QtCore.QCoreApplication.translate
        Map.setWindowTitle(_translate("Map", "MainWindow"))
        self.label.setText(_translate("Map", "Search Places or Addresses Here.."))
        self.label_2.setText(_translate("Map", "Enter Place or Address Below:"))
        self.pushButton.setText(_translate("Map", "Search"))
        self.pushButton_2.setText(_translate("Map", "Cancel"))

