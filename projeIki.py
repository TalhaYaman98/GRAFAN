import matplotlib.pyplot as plt
import numpy as np
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon
from pencere import Ui_MainWindow


class analiz(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("re1.jpg"))
        self.setToolTip("Devam Et")

        self.ui.pushButton.clicked.connect(self.std)
        self.ui.pushButton_2.clicked.connect(self.ygn)
        self.ui.pushButton_3.clicked.connect(self.piey)
        self.ui.pushButton_4.clicked.connect(self.bar)
        self.ui.pushButton_5.clicked.connect(self.hist)


    
    def std(self):
        x = self.ui.lineEdit.text()
        y = self.ui.lineEdit_2.text()
        xli = x.split(",")
        yli = y.split(",")
        listx = list(map(float, xli))
        listy = list(map(float, yli))
        plt.plot(listx,listy,"o--b")
        plt.title("Standart Grafik")
        plt.xlabel("X Ekseni")
        plt.ylabel("Y Ekseni")
        plt.legend()
        plt.show()
    
    def ygn(self):
        d1 = self.ui.lineEdit_3.text()
        d2 = self.ui.lineEdit_4.text()
        s = self.ui.lineEdit_5.text()
        d1li = d1.split(",")
        d2li = d2.split(",")
        sli = s.split(",")
        listd1 = list(map(float,d1li))
        listd2 = list(map(float,d2li))
        lists = list(map(float,sli))
        plt.stackplot(lists,listd2,listd1,colors=["grey","black"])
        plt.legend()
        plt.title("Yığın Grafik")
        plt.xlabel("Sabitler")
        plt.ylabel("Değişkenler")
        plt.show()


    def piey(self):
        p1 = self.ui.lineEdit_6.text()
        p2 = self.ui.lineEdit_7.text()
        p1x = p1.split(",")
        p2x = p2.split(",")
        listp1 = list(p1x)
        listp2 = list(map(float,p2x))
        plt.pie(listp2,labels=listp1,shadow=True,autopct="%1.1f%%")
        plt.title("Pasta Grafik")
        plt.show()

   
    def bar(self):
        barx1 = self.ui.lineEdit_8.text()
        barx2 = self.ui.lineEdit_10.text()
        bary1 = self.ui.lineEdit_9.text()
        bary2 = self.ui.lineEdit_11.text()
        barxisim = self.ui.lineEdit_12.text()
        baryisim = self.ui.lineEdit_13.text()
        bx1 = barx1.split(",")
        bx2 = barx2.split(",")
        by1 = bary1.split(",")
        by2 = bary2.split(",")
        lbx1 = list(map(float,bx1))
        lbx2 = list(map(float,bx2))
        lby1 = list(map(float,by1))
        lby2 = list(map(float,by2))
        plt.bar(lbx1,lbx2,label=barxisim,width=.2)
        plt.bar(lby1,lby2,label=baryisim,width=.2)
        plt.xlabel("X Ekseni")
        plt.ylabel("Y Ekseni")
        plt.title("Bar Grafik")
        plt.legend()
        plt.show()


    def hist(self):
        hx = self.ui.lineEdit_14.text()
        hy = self.ui.lineEdit_15.text()

        hxs = hx.split(",")
        hys = hy.split(",")

        hxl = list(map(float,hxs))
        hyl = list(map(float,hys))

        plt.hist(hxl,hyl,histtype="bar",rwidth=0.8)
        plt.xlabel("X Ekseni")
        plt.ylabel("Y Ekseni")
        plt.title("Histogtam Grafik")
        plt.show()

    



uyg=QApplication(sys.argv)
pen=analiz()
pen.show()
uyg.exec_()