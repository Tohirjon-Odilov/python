from math import sqrt
from sys import argv
from time import sleep

from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QMainWindow,
    QLabel,
)


class window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet(open("style.css").read())
        self.calc()
        self.text = str()
        self.isSqrt = False

    def calc(self):
        self.setWindowTitle("Calculator")
        self.setFixedSize(500, 290)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.label_input = QLabel(self)
        self.label_input.setText("0")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_input)
        self.central_widget.setLayout(self.layout)

        btn_grid = [
            ["Clear", "🔙", "%"],
            ["(", ")", "**"],
            ["1", "2", "3", "/"],
            ["4", "5", "6", "*"],
            ["7", "8", "9", "-"],
            ["0", ".", "+", "="],
        ]

        button_layout = QVBoxLayout(self)

        for row in btn_grid:
            row_layout = QHBoxLayout(self)
            for button_text in row:
                btn = QPushButton(self)
                btn.setText(button_text)
                btn.clicked.connect(self.btn_clicked)
                row_layout.addWidget(btn)
                if button_text == "Clear":
                    btn.setStyleSheet("background-color: crimson; color: white")
                elif button_text == "🔙":
                    btn.setStyleSheet("background-color: #999")
                elif button_text == "=":
                    btn.setStyleSheet("background-color: yellowgreen; color: white")
            button_layout.addLayout(row_layout)

        self.layout.addLayout(button_layout)

    def btn_clicked(self):
        try:
            self.clicked_button = self.sender().text()
            print(self.text, "||", self.clicked_button)
            if (
                not self.clicked_button.isalnum()
                and self.text.count(self.clicked_button) != 0
            ):
                self.label_input.setText("Two character")
            elif self.clicked_button == "=":
                self.text = str(eval(self.text.strip()))
                self.label_input.setText(self.text)
            elif self.clicked_button.find("Clear") != -1:
                self.label_input.setText("0")
                self.text = ""
            elif self.clicked_button == "🔙":
                Dell = self.text[:-1]
                self.label_input.setText(Dell)
                self.text = Dell
            else:
                self.text += self.clicked_button
                self.label_input.setText(self.text)

            if self.text == "":
                self.label_input.setText("0")

        except ZeroDivisionError:
            self.label_input.setText("Zero division error")
            self.text = ""
        except SyntaxError:
            self.label_input.setText("Syntax Error")
            self.text = ""
        except AttributeError:
            self.label_input.setText("Entered invalid value")
            self.text = ""
        except TypeError:
            self.label_input.setText("Don't press equal two")
            self.text = ""


app = QApplication(argv)
win = window()
win.show()
app.exec_()
