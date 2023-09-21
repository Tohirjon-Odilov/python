from sys import argv

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

    def calc(self):
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 290)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.label_input = QLabel(self)
        self.label_input.setText("0")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_input)
        self.central_widget.setLayout(self.layout)

        btn_grid = [
            ["Clear","%"],
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
            button_layout.addLayout(row_layout)

        self.layout.addLayout(button_layout)

    def btn_clicked(self):
        clicked_button = self.sender()
        self.text += clicked_button.text()
        self.label_input.setText(self.text)


app = QApplication(argv)
# print(app)
win = window()
win.show()
app.exec_()



