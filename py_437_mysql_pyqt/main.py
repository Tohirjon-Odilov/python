from sys import argv
from PyQt5.QtWidgets import QApplication
from components.mainWindow import MainWindow

app = QApplication(argv)
win = MainWindow()
win.show()
app.exec_()
