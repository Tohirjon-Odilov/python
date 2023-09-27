from sys import argv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,QPushButton

from cls_style import window

class mainWindow(window):
   pass      
      
app = QApplication(argv)
win = mainWindow()
win.show()
app.exec_()