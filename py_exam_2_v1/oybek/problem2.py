import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class sondantextga(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Problem 2")
        self.setGeometry(100, 100, 300, 150)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.field = QLineEdit()
        self.qbutton = QPushButton("Parse", self)
        self.result_label = QLabel()
        self.qbutton.clicked.connect(self.print_label)

        layout.addWidget(self.field)
        layout.addWidget(self.qbutton)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def print_label(self):
        son = self.field.text()

        try:
            number = int(son)
            if 1 <= number <= 99:
                number_text = self.number_to_text(number)
                self.result_label.setText(f"{number_text}")
            else:
                self.result_label.setText("Son 1 dan 99 gacha bo'lishi kerak")
        except ValueError:
            self.result_label.setText("Son kiriting")

    def number_to_text(self, number):
        ones = ["nol", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
        tens = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]

        if number == 0:
            return "nol"
        else:
            tens_digit = number // 10
            ones_digit = number % 10
            return tens[tens_digit] + " " + ones[ones_digit]

def main():
    app = QApplication(sys.argv)
    window = sondantextga()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()