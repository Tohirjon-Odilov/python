# import typing
# from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class main(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Currency")
        self.setFixedSize(500, 400)
        self.setStyleSheet()