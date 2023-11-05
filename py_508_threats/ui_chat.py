from sys import argv
from threading import Thread
from time import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QListWidget

from api import write_file 


class main1(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Chat")
        self.setGeometry(100, 100, 500, 500)
        self.message = write_file()
        self.ui()
        Thread(target=self.__update_ListWidget).start()
        
    def ui(self):
        self.vertical = QVBoxLayout()
        horizontal = QHBoxLayout()

        self.edit_name = QLineEdit()
        self.edit_name.setPlaceholderText("Your name...")
        self.vertical.addWidget(self.edit_name)

        self.list_message = QListWidget()
        self.vertical.addWidget(self.list_message)
        self.list_message.setStyleSheet("border: 1px solid #919;")
        
        self.edit_message = QLineEdit()
        self.edit_message.setPlaceholderText("Enter your message...")
        horizontal.addWidget(self.edit_message)

        self.btn_send = QPushButton("Send")
        # if self.edit_name.text() != "" and self.edit_message.text() != "":
        self.btn_send.clicked.connect(self.__update_message)
        horizontal.addWidget(self.btn_send)
        
        self.vertical.addLayout(horizontal)
        
        self.setLayout(self.vertical)
        # self.__update_ListWidget()

    def label(self):
        self.edit_name = QLineEdit()
        if self.edit_name.text():
            self.edit_name.hide()
            self.lable_name = QLabel(self.edit_name.text())
            self.vertical.addWidget(self.lable_name)
        else:
            self.edit_name.setPlaceholderText("Your name...")
            self.vertical.addWidget(self.edit_name)
        return self.vertical
        
    
    def __update_message(self):
        self.message.send(self.edit_name.text(), self.edit_message.text())
        self.__clear_input()
        
    def __clear_input(self):
        # self.edit_name.clear()
        self.edit_message.clear()
    
    def __update_ListWidget(self):
        while True:
            sleep(1)
            self.list_message.clear()
            self.data = self.message.get_all()
            for i in self.data:
                item = f"""{i['name']}
                {i['message']}
                {i['date']}"""
                self.list_message.addItem(item)
    
app = QApplication(argv)
win = main1()
win.show()
app.exec_()