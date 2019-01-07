# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'images.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Images(object):
    def setupUi(self, Images):
        Images.setObjectName("Images")
        Images.resize(462, 348)
        self.centralwidget = QtWidgets.QWidget(Images)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(110, 50, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 280, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 211, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(46, 50, 31, 20))
        self.label_2.setObjectName("label_2")
        Images.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Images)
        self.statusbar.setObjectName("statusbar")
        Images.setStatusBar(self.statusbar)

        self.retranslateUi(Images)
        QtCore.QMetaObject.connectSlotsByName(Images)

    def retranslateUi(self, Images):
        _translate = QtCore.QCoreApplication.translate
        Images.setWindowTitle(_translate("Images", "MainWindow"))
        self.pushButton.setText(_translate("Images", "Load Images"))
        self.pushButton_2.setText(_translate("Images", "Cancel"))
        self.label.setText(_translate("Images", "Images!!!"))
        self.label_2.setText(_translate("Images", "Files:"))

