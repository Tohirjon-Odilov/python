from random import randint
from sys import argv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import QTimer

from cls_style import label

# from cls_style import window

class mainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lotoreya")
        self.setStyleSheet(open("style.css", "r").read())
        self.setFixedSize(1000, 600)

        self.isTrue = False
        self.lst = list()
        self.entered_number_count = 0
        self.selected_numbers = str()

        self.h_box_left = QHBoxLayout()
        self.h_box_right = QHBoxLayout()

        self.h_box_left.addLayout(self.user_panel())
        self.h_box_right.addLayout(self.admin_panel())

        self.h_box = QHBoxLayout()
        self.h_box.addLayout(self.h_box_left)
        self.h_box.addLayout(self.h_box_right)
        self.setLayout(self.h_box)

    def user_panel(self):
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()
        # create widgets
        self.label_entered_number = QLabel("Click on one of numbers below")
        self.btn_plus = QPushButton("+")
        self.btn_random = QPushButton("Random")
        self.btn_random.setStyleSheet("""
            margin: 20px 0 0 0;
            padding: 13px;
            border-radius: 10px;
            background-color: #79AC78;
      """)
        

        self.btn_plus.clicked.connect(self.write_label_box)
        self.btn_random.clicked.connect(self.random)
        # customize widegets
        # btn_plus
        self.btn_plus.setFixedWidth(50)
        self.btn_plus.setStyleSheet("""
            border-radius: 10px;
            background-color: #79AC78;
      """)

        # add widgets
        self.h_box.addWidget(self.label_entered_number)
        self.h_box.addWidget(self.btn_plus)
        self.v_box.addLayout(self.h_box)

        self.h_box = QHBoxLayout()
        self.v_num = QVBoxLayout()
        for i in range(1, 37):
            self.btn_num = QPushButton(str(i))
            self.btn_num.setStyleSheet("margin: 10px 10px 0 0;")
            self.btn_num.clicked.connect(self.write_text)
            self.h_box.addWidget(self.btn_num)
            if i % 6 == 0:
                self.v_box.addLayout(self.h_box)
                self.h_box = QHBoxLayout()
        self.v_box.addWidget(self.btn_random)
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box)
        return self.v_box


    def write_text(self):
        if self.entered_number_count == 0:
            self.label_entered_number.clear()
        if self.isTrue:
            self.isTrue = False            
            self.restart()
        lst = self.lst
        num = self.btn_num.sender().text()

        if num in self.lst:
            self.message("Kiritilgan raqamni kiritdingiz!")
        else:    
            if self.entered_number_count < 6:
                self.lst.append(num)
                num = " ".join(list(i for i in self.lst))
                self.label_entered_number.setText(num)
                self.entered_number_count += 1
            else:
                self.message("Faqat 6 dona raqam kiritish mumkin!")

    def message(self, text):
        mes = QMessageBox()
        mes.setIcon(QMessageBox.Warning)

        mes.setText(text)
        mes.setStandardButtons(QMessageBox.Ok)
        returnValue = mes.exec()
        if returnValue == QMessageBox.Ok:
            print('Ok clikced')
    
    def write_label_box(self):
        if self.entered_number_count == 6:
            self.lst.clear()
            self.entered_number_count = 0
            self.selected_numbers += self.label_entered_number.text()+"\n"
            self.label_window.setText(self.selected_numbers)
            self.label_entered_number.setText("Click on one of numbers below")
        else:
            self.message("Iltimos oldin 6 dona raqam kiriting!")
            

    def random(self):
        if self.isTrue:
            self.isTrue = False
            self.restart()
        i = 6-(len(self.lst)%6)
        # self.label_window.setText(str(i<6)+" "+str(6-(len(self.lst)%6)))
        ist = False
        while i != 0:
            rand_num = randint(1,36)
            ##! takrorlanmas raqam
            for j in self.lst:
                if j == rand_num:
                    ist = True
                    break
            if ist:
                ist = False
                # self.message(str(rand_num))
                continue
            if len(self.lst) < 6:
                self.lst.append(rand_num)
                num = " ".join(list(str(ele) for ele in self.lst))
                self.label_entered_number.setText(num)
                i -= 1
            else:
                self.message("Faqat 6 dona son kiritish mumkin!!!")
                break
        self.entered_number_count = 6
        
        

    def admin_panel(self):
        # create widgets
        # create box
        self.v_box_right = QVBoxLayout()
        # self.h_box = QHBoxLayout()
        self.h_nav_box = QHBoxLayout()
        h_circle_box = QHBoxLayout()

        # create elements
        self.btn_start = QPushButton("Start")
        self.btn_start.clicked.connect(self.check)
        self.btn_start.setStyleSheet("""
            padding: 10px;
            border-radius: 10px;
            background-color: #79AC78;
      """)

        self.label_circle_1 = label(" ")
        self.label_circle_2 = label(" ")
        self.label_circle_3 = label(" ")
        self.label_circle_4 = label(" ")
        self.label_circle_5 = label(" ")
        self.label_circle_6 = label(" ")

        h_circle_box.addWidget(self.label_circle_1)
        h_circle_box.addWidget(self.label_circle_2)
        h_circle_box.addWidget(self.label_circle_3)
        h_circle_box.addWidget(self.label_circle_4)
        h_circle_box.addWidget(self.label_circle_5)
        h_circle_box.addWidget(self.label_circle_6)

        self.label_window = QLabel("")
        self.return_btn = QPushButton("Restart")
        self.return_btn.clicked.connect(self.restart)
        self.return_btn.setStyleSheet("""
            padding: 10px;
            border-radius: 10px;
            background-color: #79AC78;
      """)

        # customize widgets
        # add box
        self.h_nav_box.addWidget(self.btn_start)
        self.h_nav_box.addLayout(h_circle_box)
        self.v_box_right.addLayout(self.h_nav_box)
        self.v_box_right.addWidget(self.label_window)
        self.v_box_right.addWidget(self.return_btn)

        return self.v_box_right

    def check(self):
        self.isTrue = True
        von = str()
        lst = list(range(1,37))
        # print(lst)
        if self.selected_numbers:
            time = QTimer(self)
            rem = lst.pop(randint(0,len(lst)))
            self.label_circle_1.setText(str(rem))
            rem = lst.pop(randint(0,len(lst)))
            self.label_circle_2.setText(str(rem))
            time.start(1000)
            rem = lst.pop(randint(0,len(lst)))
            self.label_circle_3.setText(str(rem))
            rem = lst.pop(randint(0,len(lst)))
            self.label_circle_4.setText(str(rem))
            rem = lst.pop(randint(0,len(lst)))
            self.label_circle_5.setText(str(rem))
            rem = lst.pop(randint(0,len(lst)))
            self.label_circle_6.setText(str(rem))
            von += self.label_circle_1.text() + " "
            von += self.label_circle_2.text() + " "
            von += self.label_circle_3.text() + " "
            von += self.label_circle_4.text() + " "
            von += self.label_circle_5.text() + " "
            von += self.label_circle_6.text()
            for i in self.selected_numbers.split("\n"):
                if i == von:
                    self.message("Won!!!")
                else:
                    self.message("Defeted!")
                    break
        else:
            self.message("Hali plus tugmasi bosilmadi!!!")
        
    def restart(self):
        self.lst.clear()
        self.selected_numbers = str()
        self.entered_number_count = 0
        self.label_entered_number.setText("Click on one of numbers below")
        self.label_window.clear()
        self.label_circle_1.setText(' ')
        self.label_circle_2.setText(' ')
        self.label_circle_3.setText(' ')
        self.label_circle_4.setText(' ')
        self.label_circle_5.setText(' ')
        self.label_circle_6.setText(' ')

app = QApplication(argv)
win = mainWindow()
win.show()
app.exec_()
