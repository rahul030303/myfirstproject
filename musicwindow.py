# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Music(object):
    def setupUi(self, Music):
        Music.setObjectName("Music")
        Music.resize(437, 415)
        self.centralwidget = QtWidgets.QWidget(Music)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(90, 100, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 181, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(46, 100, 31, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 330, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 330, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 330, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 330, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        Music.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Music)
        self.statusbar.setObjectName("statusbar")
        Music.setStatusBar(self.statusbar)

        self.retranslateUi(Music)
        QtCore.QMetaObject.connectSlotsByName(Music)

    def retranslateUi(self, Music):
        _translate = QtCore.QCoreApplication.translate
        Music.setWindowTitle(_translate("Music", "MainWindow"))
        self.label.setText(_translate("Music", "Play Some Music Here!!!"))
        self.label_2.setText(_translate("Music", "Files:"))
        self.pushButton.setText(_translate("Music", "Load Files"))
        self.pushButton_2.setText(_translate("Music", "Play Next"))
        self.pushButton_3.setText(_translate("Music", "Play Previous"))
        self.pushButton_5.setText(_translate("Music", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Music = QtWidgets.QMainWindow()
    ui = Ui_Music()
    ui.setupUi(Music)
    Music.show()
    sys.exit(app.exec_())

