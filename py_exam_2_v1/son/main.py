from sys import argv

from son import uzbek_convert, ingliz_convert

from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QLineEdit,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)

# self.btn_convert.setStyleSheet("background-color: purple")

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.translet()
        self.setWindowTitle('Numbers to Words')
        self.setFixedSize(400,200)
        
    def translet(self):
        
        self.box_v = QVBoxLayout()
        
        self.box_h = QHBoxLayout()
        
        self.oyna = QLineEdit(self)
        self.oyna.setStyleSheet('background-color: #97DEFF')
        self.uzb_out_put = QLabel(self)
        self.uzb_out_put.setStyleSheet('background-color: #40F8FF')
        self.ing_out_put = QLabel(self)
        self.ing_out_put.setStyleSheet('background-color: #40F8FF')
        self.convert = QPushButton(self)
        self.convert.setText('Convert')
        self.convert.setStyleSheet('background-color: rgb(0,255,0)')
        
        self.box_h.addWidget(self.oyna)
        self.box_h.addWidget(self.convert)
        
        self.box_v.addLayout(self.box_h)
        self.box_v.addWidget(self.uzb_out_put)
        self.box_v.addWidget(self.ing_out_put)
        
        self.setLayout(self.box_v)
        
        self.convert.clicked.connect(self.fun)
        
        
        
    def fun(self):
        num = self.oyna.text()
        try:
            int(num)
            tayyor_num = uzbek_convert(int(num))
            self.uzb_out_put.setText(f'   {tayyor_num}')
            num1 = self.oyna.text()
            tayyor_num1 = ingliz_convert(int(num1))
            self.ing_out_put.setText(f'   {tayyor_num1}')
        except:
            self.uzb_out_put.setText('FAQAT SON KIRITING !!!')
            self.ing_out_put.setText('JUST ENTER A NUMBER !!!')
        
        
        
        
        
app = QApplication(argv)
win = Window()
win.setStyleSheet('background-color: yellow')
win.show()
app.exec_()
