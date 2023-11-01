from sys import argv
from PyQt5.QtWidgets import QApplication
# from login import Login
from registration import Window, Login


app = QApplication(argv)
win = Login("Tohirjon")
win = Window()

# win.show()
app.exec_()
