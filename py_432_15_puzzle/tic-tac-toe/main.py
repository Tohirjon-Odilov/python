from random import choice
from sys import argv
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout

class main_window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("TIC TAC TOE")
        self.setFixedSize(500, 500)
        self.matrix_id = [1,2,3,
                          4,5,6,
                          7,8,9]
        self.matrix_el = list()
        self._ui()
        self.is_true = False
        
        
    # create ui
    def _ui(self):
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()
        for i in range(1,10):
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
            self.matrix_el.append(self.btn)
            if i % 3 == 0: 
                self.v_box.addLayout(self.h_box)
                self.h_box = QHBoxLayout()
        self.setLayout(self.v_box)
            

    def _button(self):
        btn = self.btn.sender()
        if btn in self.matrix_el:
            if self.is_true:
                btn.setText("o")
                self.is_true = False
            else:
                btn.setText("x")
                self.is_true = True
            # btn.setEnabled(False)
            # print(self.matrix_el.index(btn))
            self.matrix_id.remove(self.matrix_el.index(btn)+1)
            # print(self.matrix_id, self.matrix_el.index(btn)+1)
        else:
            print("o'chirib tashlandi")
        
        # if is_true:
            # ai = choice(self.matrix_id)
            # print(ai, self.matrix_id)
            # print(self.matrix_id, self.matrix_el.index(btn)+1, ai)
            # self.matrix_el[ai].setText("o")
            # self.matrix_el[ai].setEnabled(False)
            # self.matrix_id.remove(ai)
            
        # print(self.matrix_id)
        # print(self.matrix)
        # for i, el in enumerate(self.matrix):
            # pass
            

        
app = QApplication(argv)
win = main_window()
win.show()
app.exec_()