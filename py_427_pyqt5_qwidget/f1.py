from sys import argv
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QMainWindow
    )

class window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__Init()
    
    def __Init(self):
        self.setWindowTitle("My First Window")
        self.setFixedSize(400,300)

        self.user_name = QLabel(self)
        self.edit_name = QLineEdit(self)

        self.user_last_name = QLabel(self)
        self.edit_last_name = QLineEdit(self)
        
        self.user_phone = QLabel(self)
        self.edit_phone = QLineEdit(self)
        
        self.btn_add = QPushButton(self)

        self.user_name.setText('First name')
        self.user_last_name.setText('Last name')
        self.user_phone.setText('Phone number')
        self.btn_add.setText("Add new contact")

        self.user_name.move(50,50)
        self.edit_name.move(125,45)
        self.user_last_name.move(50,100)
        self.edit_last_name.move(125,95)
        self.user_phone.move(50,150)
        self.edit_phone.move(150, 145)

        # self.edit_last_name.clear()

        self.btn_add.move(50,200)
        self.btn_add.setMinimumWidth(240)



app = QApplication(argv)
print(app)
win = window()
win.show()
app.exec_()


