from sys import argv

from PyQt5.QtWidgets import(
    QWidget,
    QApplication,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QMainWindow,
    QLabel
) 

class window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # self.setStyleSheet("background-color: white")
        self.calc()

    def calc(self):
        self.setWindowTitle("Calculator")
        self.setFixedSize(410,250)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        btn_grid = [
            ['1','2','3','/'],
            ['4','5','6','*'],
            ['7','8','9','-'],
            ['0','=','+'],
        ]

        button_layout = QVBoxLayout(self)
        
        for row in btn_grid:
            row_layout = QHBoxLayout(self)
            for button_text in row:
                print(button_text)
                btn = QPushButton(self)
                btn.setText(button_text)
                row_layout.addWidget(btn)
            button_layout.addLayout(row_layout)        

        self.layout.addLayout(button_layout)
        # self.num1.setStyleSheet("color: black")
        # self.my_name = 
        # self.num.setText('salom')



app = QApplication(argv)
print(app)
win = window()
win.show()
app.exec_()
