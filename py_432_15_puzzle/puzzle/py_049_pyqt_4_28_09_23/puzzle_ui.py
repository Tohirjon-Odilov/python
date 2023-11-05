import sys

from random import shuffle
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtCore import QTimer



class Game(QWidget):
    def __init__(self, size):
        super().__init__()

        self.size = size

        self.setWindowTitle("Game Puzzle")
        self.setStyleSheet('font-size: 30px')
        self.__initUI()
        self.show()
        # self.showMaximized()


    def __initUI(self):
        self.v_box = QVBoxLayout()
        self.h_box_top = QHBoxLayout()
        self.h_box_bottom = QHBoxLayout()
        self.grid = QGridLayout() 

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

        self.label_time = QLabel('Time: 0 s')
        self.label_moves = QLabel('Moves: 0')

        self.btn_restart = QPushButton('Restart')
        self.btn_toggle = QPushButton('Pause')
        
        self.btn_toggle.clicked.connect(self.start_action)
        self.btn_restart.clicked.connect(self.show_restart)

        self.h_box_top.addWidget(self.label_time)
        self.h_box_top.addStretch()
        self.h_box_top.addWidget(self.label_moves)

        self.h_box_bottom.addWidget(self.btn_restart)
        self.h_box_bottom.addStretch()
        self.h_box_bottom.addWidget(self.btn_toggle)

        self.v_box.addLayout(self.h_box_top)
        self.v_box.addLayout(self.grid)
        self.v_box.addLayout(self.h_box_bottom)

        self.setLayout(self.v_box)

        self.restart()
        if self.check_winner():
            print("Winner")
            self.start_action()
        

    def restart(self):
        self.count_move = 0
        self.start = True
        self.count = 0
        nums = self.__get_numbers(0)
        print(nums)
        self.label_moves.setText(f"Moves: {self.count_move}")

        self.matrix = list() 
        i = 0
        for x in range(self.size):
            row = list()
            for y in range(self.size):
                row.append(QPushButton(f"{nums[i]}"))
                i+=1
            self.matrix.append(row)

        for x in range(self.size):
            for y in range(self.size):
                self.grid.addWidget(self.matrix[x][y], x,y)
                self.matrix[x][y].clicked.connect(self.change_position)
                if not self.matrix[x][y].text():
                    self.matrix[x][y].hide()


    def __get_numbers(self, n):
        nums = list(range(1, self.size*self.size))
        nums = list(map(str, nums)) + ['']
        if n:
            return nums
        shuffle(nums)
        return nums
    
    def change_position(self):
        btn = self.sender()
        for i in range(self.size):
            for j in range(self.size):
                if btn == self.matrix[i][j]:
                    if i-1 >= 0 and self.matrix[i-1][j].text() == '':
                        self.matrix[i-1][j].setText(btn.text())
                        self.matrix[i-1][j].show()
                        btn.setText('')
                        btn.hide()
                        self.count_move +=1
                    elif i+1 < self.size and self.matrix[i+1][j].text() == '':                        
                        self.matrix[i+1][j].setText(btn.text())
                        self.matrix[i+1][j].show()
                        btn.setText('')
                        btn.hide()
                        self.count_move +=1

                    elif j-1 >= 0 and self.matrix[i][j-1].text() == '':
                        self.matrix[i][j-1].setText(btn.text())
                        self.matrix[i][j-1].show()
                        btn.setText('')
                        btn.hide()
                        self.count_move +=1
                    
                    elif j+1 < self.size and self.matrix[i][j+1].text() == '':                        
                        self.matrix[i][j+1].setText(btn.text())
                        self.matrix[i][j+1].show()
                        btn.setText('')
                        btn.hide()
                        self.count_move +=1
                    self.label_moves.setText(f"Moves: {self.count_move}")
                    if self.check_winner():
                        print("Winner")
                        self.start_action()


    def showTime(self):
        if self.start:
            self.count += 1
            text = f"Time: {self.count/10} s"
            self.label_time.setText(text)

    def start_action(self):
        if self.start:
            self.btn_toggle.setText('Start')
            self.disable_buttons()
        else:
            self.btn_toggle.setText('Pause')
            self.activate_buttons()

        self.start = False if self.start else True

    def disable_buttons(self):
        for x in range(self.size):
            for y in range(self.size):
                self.matrix[x][y].setEnabled(False)

    def activate_buttons(self):
        for x in range(self.size):
            for y in range(self.size):
                self.matrix[x][y].setEnabled(True)
            
    def show_restart(self):
        self.close()
        self.game = Game(self.size)

    def check_winner(self):
        nums = self.__get_numbers(1)
        matrix = list() 
        i = 0
        for _ in range(self.size):
            row = list()
            for _ in range(self.size):
                row.append(nums[i])
                i+=1
            matrix.append(row)
        
        for i in range(self.size):
            for j in range(self.size):
                if matrix[i][j] != self.matrix[i][j].text():
                    return False
        return True

app = QApplication(sys.argv)

game = Game(4)

sys.exit(app.exec_())
        