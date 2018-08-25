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

DataF=pd.read_excel("/home/emir/Masaüstü/artikel.xlsx")

print("Column headings:")
print(DataF.columns)

for i in DataF.index:
    print(DataF['artikel'][i])

for i in DataF.index:
    print(DataF['Wort'][i])

for i in DataF.index:
    print(DataF['Plural'][i])


#if((DataF['artikel'][1])=='das'):
#    print("evet bildiniz")
#else:
#    print("bilemedin dogru cevap")


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Deutsch Lern'
        self.left = 10
        self.top = 100
        self.width = 320
        self.height = 200


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

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox



        self.label1 = QLabel(DataF['Wort'][1], self)
        self.label1.move(130,80)


        self.show()

    @pyqtSlot()
    def on_click(self):

     if(DataF['artikel'][1]=="der"):
        #print(DataF['Plural'][1])
        print('dogru')
     else:
         print("yanlış")

    def on_click2(self):

     if (DataF['artikel'][1] == "die"):

        print('dogru')
     else:
         print("yanlış")

    def on_click3(self):

     if (DataF['artikel'][1] == "das"):

        print('dogru')
     else:
         print("yanlış")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


