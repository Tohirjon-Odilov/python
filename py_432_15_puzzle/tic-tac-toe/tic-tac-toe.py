import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QPushButton, 
    QHBoxLayout, 
    QVBoxLayout, 
    QMessageBox,
    QLabel
)

from login import Login

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("TIC TAC TOE")
        self.setFixedSize(500, 500)
        self.status = True
        self.matrix = [""] * 9  # 3x3 o'yin matritsasi
        self.current_player = "X"  # O'yinchi boshlanishi "X" bilan
        self.buttons = []  # Matritsani ko'rsatish uchun tugmalar
        self.init_ui()
        self.show()

    def init_ui(self):
        layout = QVBoxLayout()

        for i in range(3):
            row_layout = QHBoxLayout()
            for j in range(3):
                button = QPushButton("", self)
                button.setFixedSize(120, 120)
                button.setStyleSheet("""
                    font-size: 100px;
                    font-weight: 900;
                    background-color: royalblue;
                    border-radius: 10px; 
                    color: white;   
                """)
                button.clicked.connect(lambda _, row=i, col=j: self.on_button_click(row, col))
                row_layout.addWidget(button)
                self.buttons.append(button)
            layout.addLayout(row_layout)

        reset_button = QPushButton("Restart", self)
        reset_button.clicked.connect(self.reset_game)
        layout.addWidget(reset_button)
        # reset_button.setFixedWidth(400)
        reset_button.setStyleSheet("""
            margin: 0 20px;
            padding: 20px 0;
            background-color: crimson;
            color: white;
            font-size: 20px;                           
        """)

        self.setLayout(layout)

    def on_button_click(self, row, col):
        index = row * 3 + col
        if self.matrix[index] == "":
            # print(index, row, col)
            self.matrix[index] = self.current_player
            self.buttons[index].setText(self.current_player)
            self.buttons[index].setEnabled(False)
            self.check_winner()
            self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Qatorlar
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Ustunlar
            (0, 4, 8), (2, 4, 6)             # Diagonal
        ]
        print()
        for combo in winning_combinations:
            
            a, b, c = combo
            print(a,b,c)
            if self.matrix[a] == self.matrix[b] == self.matrix[c] != "":
                self.show_winner_message(self.current_player)
                return

        if "" not in self.matrix:
            self.show_winner_message("Durrang!")

    def show_winner_message(self, winner):
        message_box = QMessageBox(self)
        if winner.find("Durrang") != -1:
            message_box.setText(winner)
        else: 
            message_box.setText(f"{winner} yutdi!")
        message_box.setWindowTitle("Natija")
        message_box.exec_()
        self.reset_game()

    def reset_game(self):
        Login()
        self.close()
        
        self.matrix = [""] * 9
        for button in self.buttons:
            button.setText("")
            button.setEnabled(True)
        self.current_player = "X"
        
class Login(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 500)
        self.setStyleSheet("background-color: crimson")
        self.label = QLabel("salom")
        self.h = QHBoxLayout()
        self.h.addWidget(self.label)
        self.setLayout(self.h)
        self.show()

app = QApplication(sys.argv)
window = TicTacToe()
# window.show()
sys.exit(app.exec_())
