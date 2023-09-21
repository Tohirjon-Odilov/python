import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Kalkulyator")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.result_display = QLineEdit()
        self.result_display.setFixedHeight(40)
        # self.result_display.setAlignment(QtP.AlignRight)
        # self.layout.addWidget(self.result_display)

        button_grid = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        button_layout = QVBoxLayout()

        for row in button_grid:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                # button.clicked.connect(self.on_button_click)
                row_layout.addWidget(button)
            button_layout.addLayout(row_layout)

        self.layout.addLayout(button_layout)

    def on_button_click(self):
        clicked_button = self.sender()
        if clicked_button:
            button_text = clicked_button.text()
            if button_text == '=':
                try:
                    result = eval(self.result_display.text())
                    self.result_display.setText(str(result))
                except Exception as e:
                    self.result_display.setText("Error")
            else:
                current_text = self.result_display.text()
                self.result_display.setText(current_text + button_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
