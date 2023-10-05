from sys import argv
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton, QLabel, QHBoxLayout, 
    QVBoxLayout, QLineEdit)
from qtwidgets import PasswordEdit
from PyQt5.QtCore import Qt

class CreateUser(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("CRUD APP")
        self.setFixedSize(800,500)
        self.setStyleSheet("""
            background-color: #FFF;
            color: #000;
        """)
        self.__createUi()

    def __createUi(self):
        v_box = QVBoxLayout()
        
        fname = QLineEdit()
        fname.setPlaceholderText("Full Name")
        v_box.addWidget(fname)
        
        username = QLineEdit()
        username.setPlaceholderText("Username")
        v_box.addWidget(username)
        
        password = PasswordEdit()
        password.setPlaceholderText("Password")
        v_box.addWidget(password)
        
        mobileNumber = QLineEdit()
        mobileNumber.setPlaceholderText("Mobile Number")
        v_box.addWidget(mobileNumber)
        
    