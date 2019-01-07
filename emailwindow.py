# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emailwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Email(object):
    def setupUi(self, Email):
        Email.setObjectName("Email")
        Email.resize(418, 376)
        self.centralwidget = QtWidgets.QWidget(Email)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 111, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 50, 231, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 80, 47, 13))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 80, 181, 171))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        Email.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Email)
        self.statusbar.setObjectName("statusbar")
        Email.setStatusBar(self.statusbar)

        self.retranslateUi(Email)
        QtCore.QMetaObject.connectSlotsByName(Email)

    def retranslateUi(self, Email):
        _translate = QtCore.QCoreApplication.translate
        Email.setWindowTitle(_translate("Email", "MainWindow"))
        self.label.setText(_translate("Email", "Send An Email Here..."))
        self.label_3.setText(_translate("Email", "To:"))
        self.label_4.setText(_translate("Email", "Message:"))
        self.pushButton.setText(_translate("Email", "Send"))
        self.pushButton_2.setText(_translate("Email", "Cancel"))

