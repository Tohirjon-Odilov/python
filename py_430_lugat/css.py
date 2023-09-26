from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QListWidget, QLabel
from PyQt5.QtGui import QIcon

class QLW(QListWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""background: #fff; 
                           color: black;
                           border: 1px solid; 
                           border-radius: 15px;
                           font-size: 20px;
                           padding: 5px 
                           """)
        
class Label(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("""color: black; 
                           font-size: 20px;
                           padding: 5px 
                           """)

class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(300,70)
        self.setStyleSheet("""background: #79AC78; 
                           border: 2px solid; 
                           border-radius: 25px;
                           font-size: 20px; 
                           margin: 5 0""")
        
class FooterButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(150,40)
        self.setStyleSheet("""background: #79AC78; 
                           border: 1px solid; 
                           border-radius: 15px;
                           font-size: 16px; 
                           """)
        
class Edit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""background: #B0D9B1; 
                           border: 1px solid; 
                           border-radius: 5px;
                           font-size: 25px;
                            padding-left: 5px
                           """)
        
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,600)
        self.setStyleSheet("background: #D0E7D2")
        self.setWindowIcon(QIcon('./assets/tr_logo.png'))