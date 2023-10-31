from sys import argv
from PyQt5.QtWidgets import QApplication
# from login import Login
from registration import Window


app = QApplication(argv)
win = Window()

win.show()
app.exec_()
