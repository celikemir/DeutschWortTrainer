import pandas as pd
import xlrd as xl
from pandas import ExcelWriter
from pandas import ExcelFile
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import time

DataF=pd.read_excel("/home/emir/Masaüstü/artikel.xlsx")

print("Column headings:")
print(DataF.columns)

for q in DataF.index:
    print(DataF['artikel'][q])

for q in DataF.index:
    print(DataF['Wort'][q])

for q in DataF.index:
    print(DataF['Plural'][q])

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Deutsch Lern'
        self.left = 10
        self.top = 100
        self.width = 320
        self.height = 200
        self.i=0


        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        button = QPushButton('Der', self)
        button.setToolTip('Kontrol Et')
        button.move(20, 160)
        button.clicked.connect(self.on_click)

        button2 = QPushButton('Die', self)
        button2.setToolTip('Kontrol Et')
        button2.move(110, 160)
        button2.clicked.connect(self.on_click2)

        button3 = QPushButton('Das', self)
        button3.setToolTip('Kontrol Et')
        button3.move(200, 160)
        button3.clicked.connect(self.on_click3)

        button4 = QPushButton('Kein', self)
        button4.setToolTip('Kontrol Et')
        button4.move(110,135)
        button4.clicked.connect(self.on_click4)


        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox



        self.label1=QLabel(DataF['Wort'][self.i], self)

        newfont = QtGui.QFont("Times", 15, QtGui.QFont.Bold)
        self.label1.setFont(newfont)
        self.label1.setGeometry(QtCore.QRect(110, 30, 200, 100))  # (x, y, width, height)

        self.show()


    @pyqtSlot()
    def on_click(self):

     if(DataF['artikel'][self.i]=="der"):
        #print(DataF['Plural'][1])
        self.i+=1
        print('dogru {}' .format(self.i))
        return  self.label1.setText(DataF['Wort'][self.i])
     else:
         print("yanlış")

    def on_click2(self):

     if (DataF['artikel'][self.i] == "die"):
        self.i+=1
        print('dogru {}' .format(self.i))
        return self.label1.setText(DataF['Wort'][self.i])

     else:
         print("yanlýŷ")

    def on_click3(self):

     if (DataF['artikel'][self.i] == "das"):
        self.i+=1
        print('dogru {}' .format(self.i))

        return self.label1.setText(DataF['Wort'][self.i])


     else:
         print("yanlış")

    def on_click4(self):

     if (DataF['artikel'][self.i] == "-"):
        self.i+=1
        print('dogru {}' .format(self.i))

        return self.label1.setText(DataF['Wort'][self.i])


     else:
         print("yanlış")






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


