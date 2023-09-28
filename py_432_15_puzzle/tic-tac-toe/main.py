from sys import argv
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout

class main_window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("TIC TAC TOE")
        self.setFixedSize(500, 500)
        self.matrix = [1,2,3,
                       4,5,6,
                       7,8,9]
        # self.matrix = list()
        self._ui()
        
    # create ui
    def _ui(self):
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()
        for i, el in enumerate(self.matrix,1):
            self.btn = QPushButton(" ")
            self.btn.setStyleSheet("""
                    font-size: 100px;
                    padding-bottom: 20px;
                    font-weight: 900;
                    background-color: royalblue;
                    border-radius: 10px;                   
                """)
            self.btn.clicked.connect(self._button)
            self.h_box.addWidget(self.btn)
            if i % 3 == 0: 
                self.v_box.addLayout(self.h_box)
                self.h_box = QHBoxLayout()
        self.setLayout(self.v_box)
            

    def _button(self):
        self.btn.sender().setText("x")

        
app = QApplication(argv)
win = main_window()
win.show()
app.exec_()