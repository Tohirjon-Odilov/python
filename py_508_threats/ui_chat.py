from sys import argv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit


class main(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Chat")
        self.setGeometry(100, 100, 500, 500)
        self.ui()
        
    def ui(self):
        vertical = QVBoxLayout()
        horizontal = QHBoxLayout()

        edit_name = QLineEdit()
        edit_name.setPlaceholderText("Your name...")
        vertical.addWidget(edit_name)

        label = QLabel()
        vertical.addWidget(label)
        label.setStyleSheet("border: 1px solid #919;")
        
        edit_message = QLineEdit()
        edit_message.setPlaceholderText("Enter your message...")
        horizontal.addWidget(edit_message)

        btn_send = QPushButton("Send")
        horizontal.addWidget(btn_send)
        
        vertical.addLayout(horizontal)
        
        self.setLayout(vertical)
        

        
app = QApplication(argv)
win = main()
win.show()
app.exec_()