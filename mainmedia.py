import PyQt5
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QListWidget,QListWidgetItem
from media import Ui_Home
from media2 import Ui_SignIn
from media3 import Ui_Documents
from browsermedia import Ui_ToBrowser
from mapbrowse import Ui_Map
from musicwindow import Ui_Music
from images import Ui_Images
from emailwindow import Ui_Email
import sys

class firstmedia(QMainWindow):
    def documents(self):
        self.tm = thirdmedia()
        self.tm.show()
        self.hide()
        
    def browse(self):
        self.b = browserclass()
        self.b.show()
        self.hide()

    def gotomap(self):
        self.mapobj = mapclass()
        self.mapobj.show()
        self.hide()
        
    def musicframe(self):
        self.cm = classmusic()
        self.cm.show()
        self.hide()

    def imagesframe(self):
        self.iff = imageclass()
        self.iff.show()
        self.hide()

    def email(self):
        self.ec = emailclass()
        self.ec.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.musicframe)
        self.ui.pushButton_3.clicked.connect(self.documents)
        self.ui.pushButton_6.clicked.connect(self.email)
        self.ui.pushButton_2.clicked.connect(self.imagesframe)
        self.ui.pushButton_4.clicked.connect(self.browse)
        self.ui.pushButton_7.clicked.connect(self.gotomap)



class thirdmedia(QMainWindow):
    def back1(self):
        self.fm3 = firstmedia()
        self.fm3.show()
        self.hide()

    def op(self):
        file = QFileDialog.getOpenFileName(self,"Open File", "","doc files(*.json *.odt *.txt)")
        if file[0]:
            f = open(file[0],'r')
            data = f.read()
            f.close()
            self.ui.textEdit.setText(data)

    def new(self):
        self.ui.textEdit.setText(" ")

    def save(self):
        x = self.ui.textEdit.toPlainText()
        #print(x)
        file = QFileDialog.getSaveFileName(self,"Save File")
        if file[0]:
            f = open(file[0],'w')
            f.write(x)
            f.close()
            self.ui.statusbar.showMessage("Saved!")

    def delete(self):
        self.ui.textEdit.setText("")
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_Documents()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.save)
        self.ui.pushButton_3.clicked.connect(self.delete)
        self.ui.pushButton_4.clicked.connect(self.back1)
        self.ui.pushButton.clicked.connect(self.op)
        #self.ui.actionNew.triggered.connect(self.new)

class browserclass(QMainWindow):
    def back(self):
        self.fm4 = firstmedia()
        self.fm4.show()
        self.hide()
        
    def goto(self):
        import webbrowser
        
        url = self.ui.lineEdit.text()
        webbrowser.open(url,new=2)
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_ToBrowser()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.goto)
        self.ui.pushButton_2.clicked.connect(self.back)

class mapclass(QMainWindow):
    def back(self):
        self.fm4 = firstmedia()
        self.fm4.show()
        self.hide()

    def see(self):
        import webbrowser

        loc = self.ui.lineEdit.text()
        webbrowser.open(f"https://www.google.com/maps/place/{loc}",new=2)
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Map()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.see)
        self.ui.pushButton_2.clicked.connect(self.back)

class classmusic(QMainWindow):
    def load(self):
        file = QFileDialog.getOpenFileName(self,"Select Audio:", "","music files(*.mp3)")
        self.ui.listWidget.addItem(file[0])

    def first(self):
        self.fm = firstmedia()
        self.fm.show()
        self.hide()

    def play(self, item):
        import os
        x = item.text()
        os.system(f"start {x}")

    def next(self):
        import os 
        y = self.ui.listWidget.currentItem().text()#selects current selected item's text
        itemlist = []
        x = self.ui.listWidget.count()#counts total no. of items in listwidget
        for i in range(x):
            itemlist.append(self.ui.listWidget.item(i).text())
        nowplaying = itemlist.index(y)
        #currentitem = nowplaying+1
        #print(QListWidgetItem(currentitem))
        #self.ui.listWidget.setCurrentItem(QListWidgetItem(nowplaying+1))
        os.system(f"start {itemlist[nowplaying+1]}")

    def previous(self):
        import os
        y = self.ui.listWidget.currentItem().text()
        itemlist = []
        x = self.ui.listWidget.count()
        for i in range(x):
            itemlist.append(self.ui.listWidget.item(i).text())
        nowplaying = itemlist.index(y)
        os.system(f"start {itemlist[nowplaying-1]}")
        
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_Music()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.load)
        self.ui.pushButton_5.clicked.connect(self.first)
        self.ui.listWidget.itemDoubleClicked.connect(self.play)
        self.ui.pushButton_2.clicked.connect(self.next)
        self.ui.pushButton_3.clicked.connect(self.previous)

class imageclass(QMainWindow):
    def goback(self):
        self.fm6 = firstmedia()
        self.fm6.show()
        self.hide()

    def loadimages(self):
        #pass #put code here
        file = QFileDialog.getOpenFileName(self,"Select and Load Image:", "", "pictures(*.jpg)")
        #print(file)
        self.ui.listWidget.addItem(file[0])

    def openit(self,item):
        import os
        x = item.text()
        print(x)
        os.system(f"start {x}")
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Images()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.loadimages)
        self.ui.pushButton_2.clicked.connect(self.goback)
        self.ui.listWidget.itemDoubleClicked.connect(self.openit)

class emailclass(QMainWindow):
    def cancel(self):
        self.fm7 = firstmedia()
        self.fm7.show()
        self.hide()

    def send(self):
        #pass #put code here
        import smtplib

        to = self.ui.lineEdit_2.text()
        content = self.ui.textEdit.toPlainText()
        mail = smtplib.SMTP('smtp.gmail.com',587) #465
        mail.ehlo()
        mail.starttls()
        mail.login('pyappmedia@gmail.com','pythonmultimediaapp2018')
        mail.sendmail('pyappmedia@gmail.com',to,content)
        mail.close()
        self.ui.statusbar.showMessage("E-Mail Sent Successfully!")
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Email()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.cancel)
        self.ui.pushButton.clicked.connect(self.send)
        
class mainclass:
    def __init__(self):
        pass

    def showfirstmedia(self):
        self.fm = firstmedia()
        self.fm.show()

def main():
    app = QApplication(sys.argv)
    mc = mainclass()
    mc.showfirstmedia()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
