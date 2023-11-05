from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel

class intro(QWidget):
    def __init__(self) -> None:
        super().__init__()
    
    def __ui(self):
        user_name = QLineEdit()
        user_name.setPlaceholderText("Enter your name...")
        
        vertical = QVBoxLayout()
        vertical.addLayout(user_name)
        
    def __enable_main_ui(self):
        self.hide
        # show main ui
        

        
    