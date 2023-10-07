from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QListWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
)

from core import convert_number


class number_to_word(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Numbers to Words")
        # set style all
        self.setStyleSheet(
            """
            QWidget{
                width: 250px;
                height: 170px;
                background-color: #713ABE;
            }
            QLineEdit{
                height: 40px;
                background-color: white;
                padding: 0 8px;
                color: black;
                font-size: 25px;
                border: 2px solid;
                border-radius: 10px
            }
            textChanged{
                color: red;
            }
            QPushButton{
                height: 40px;
                background-color: #5B0888;
                padding: 0 8px;
                font-size: 25px;
                border: 2px solid;
                border-radius: 10px;
            }
            QListWidget{
                border: 2px solid;
                border-radius: 10px;
                background-color: white;
                padding: 10px 15px;
                font-size: 30px;
                color: black;
            }
        """
        )
        self.main_window()

    def main_window(self):
        # create input
        self.input = QLineEdit()
        self.input.setText("134")
        self.input.setPlaceholderText("Enter number...")

        # create button and connect function
        self.btn = QPushButton("Convert")
        self.btn.clicked.connect(self.convert_num)

        # create horizontal and add widget for horizontal
        self.h_line = QHBoxLayout()
        self.h_line.addWidget(self.input)
        self.h_line.addWidget(self.btn)

        # create vertical and add horizontal to vertical
        self.v_line = QVBoxLayout()
        self.v_line.addLayout(self.h_line)

        # create big box
        self.box = QListWidget()
        self.box.addItem("One hundred thirty four")

        # add box to vertical
        self.v_line.addWidget(self.box)

        self.setLayout(self.v_line)

    def convert_num(self):
        self.box.addItem(str(convert_number(self.input.text())).capitalize())


app = QApplication([])
win = number_to_word()
win.show()
app.exec_()
