from sys import argv
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton, QLabel, QHBoxLayout, 
    QVBoxLayout)
from PyQt5.QtCore import Qt


from style import MainButton

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("CRUD APP")
        self.setFixedSize(800,500)
        self.setStyleSheet("""
            background-color: #FFF;
            color: #000;
        """)
        self.__allButton()
    
    def __allButton(self):
        v_box = QVBoxLayout()
        
        btn_create = MainButton("Create New User")
        btn_create.clicked.connect(self.create_user)        
        v_box.addWidget(btn_create)
        
        btn_read = MainButton("Read All Users")
        # btn_read.clicked.connect(read_all_users)        
        v_box.addWidget(btn_read)
        
        btn_read_by_id = MainButton("Read by ID User")
        # btn_read_by_id.clicked.connect(read_by_id)        
        v_box.addWidget(btn_read_by_id)
        
        btn_update = MainButton("Update User")
        # btn_update.clicked.connect(update_user)
        v_box.addWidget(btn_update)
        
        btn_delete = MainButton("Delete User")
        # btn_delete.clicked.connect(delete_user)
        v_box.addWidget(btn_delete)
        
        v_box.setAlignment(Qt.AlignCenter)
        self.setLayout(v_box)
        
    def create_user(self):
        self.hide()
        from create import CreateUser
        create_app = CreateUser()
        create_app.show()
        
        
app = QApplication(argv)
win = MainWindow()
win.show()
app.exec_()  
