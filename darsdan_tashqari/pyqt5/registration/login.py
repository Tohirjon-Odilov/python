from json import dumps, loads
from sys import argv
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)

# from registration import Window

class Login(QWidget):
    def __init__(self) -> None:
        super().__init__()
        print("salom")
        self.setFixedSize(450, 400)
        # label = QPushButton("Salom")
        # self.setLayout(label)
        self.show()



