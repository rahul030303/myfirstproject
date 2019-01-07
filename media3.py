# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'media3.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Documents(object):
    def setupUi(self, Documents):
        Documents.setObjectName("Documents")
        Documents.resize(436, 370)
        self.centralwidget = QtWidgets.QWidget(Documents)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 411, 231))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 231, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 310, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 310, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 310, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 310, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        Documents.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Documents)
        self.statusbar.setObjectName("statusbar")
        Documents.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(Documents)
        self.actionNew.setObjectName("actionNew")
        self.actionEdit = QtWidgets.QAction(Documents)
        self.actionEdit.setObjectName("actionEdit")
        self.actionSave = QtWidgets.QAction(Documents)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(Documents)
        self.actionOpen.setObjectName("actionOpen")
        self.actionFonts = QtWidgets.QAction(Documents)
        self.actionFonts.setObjectName("actionFonts")

        self.retranslateUi(Documents)
        QtCore.QMetaObject.connectSlotsByName(Documents)

    def retranslateUi(self, Documents):
        _translate = QtCore.QCoreApplication.translate
        Documents.setWindowTitle(_translate("Documents", "MainWindow"))
        self.label.setText(_translate("Documents", "See Your Documents Here!"))
        self.pushButton.setText(_translate("Documents", "Open"))
        self.pushButton_2.setText(_translate("Documents", "Save"))
        self.pushButton_3.setText(_translate("Documents", "Delete"))
        self.pushButton_4.setText(_translate("Documents", "Cancel"))
        self.actionNew.setText(_translate("Documents", "New"))
        self.actionEdit.setText(_translate("Documents", "Edit"))
        self.actionSave.setText(_translate("Documents", "Save"))
        self.actionOpen.setText(_translate("Documents", "Open"))
        self.actionFonts.setText(_translate("Documents", "Fonts"))

