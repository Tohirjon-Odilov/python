from sys import argv
from PyQt5.QtWidgets import  QLabel, QLineEdit,QPushButton

class label(QLabel):
   def __init__(self, text) -> None:
      super().__init__(text)
      
      self.setFixedSize(70,55)
      self.setStyleSheet("""
            border-radius: 25px; 
            background-color: #E5D283; 
            border: 1px solid crimson; 
            color: crimson;
            font-size: 30px; 
            padding-left: 10px; 
            font-weight: 900;
      """)