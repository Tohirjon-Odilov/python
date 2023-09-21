import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.result_label = QLabel("0")
        layout.addWidget(self.result_label)

        # Amallarni bajarish uchun tugmalar
        buttons = {
            '0': '0', '1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6', '7': '7',
            '8': '8', '9': '9', '+': '+', '-': '-',
            '*': '*', '/': '/', '=': '=', 'C': 'clear'
        }

        for btn_text, operation in buttons.items():
            button = QPushButton(btn_text)
            button.clicked.connect(lambda _, operation=operation: self.perform_operation(operation))
            layout.addWidget(button)

        central_widget.setLayout(layout)

        self.current_value = ""
        self.pending_operation = None

    def perform_operation(self, operation):
        if operation == '=':
            try:
                result = str(eval(self.current_value))
                self.result_label.setText(result)
                self.current_value = result
                self.pending_operation = None
            except Exception as e:
                self.result_label.setText("Error")
        elif operation == 'clear':
            self.result_label.setText("0")
            self.current_value = ""
            self.pending_operation = None
        else:
            if self.pending_operation:
                self.perform_operation('=')
                self.pending_operation = None
            self.current_value += operation
            self.result_label.setText(self.current_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())
