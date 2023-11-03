# import typing
# from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit, 
    QLabel,
    QPushButton
)

class Login(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 500)
        self.setStyleSheet("background-color: crimson")
        self.label = QLabel("salom")
        self.h = QHBoxLayout()
        self.h.addWidget(self.label)
        self.setLayout(self.h)
        # input("salom")
        self.show()
        
        