import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class sondantextga(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Problem 2")
        self.setGeometry(100, 100, 300, 150)
        self.setContentsMargins(10, 10, 10, 10)
        self.__init_ui()

    def __init_ui(self):
        layout = QVBoxLayout()
        self.input = QLineEdit()
        self.button = QPushButton("Parse", self)
        self.button.setStyleSheet("""
            border-radius: 10px; 
            font-size: 25px;
            background-color: #00bfff;
        """)
        self.label = QLabel()
        self.label.setStyleSheet("font-size: 25px")
        self.button.clicked.connect(self.__print_label)

        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def __print_label(self):
        sentense = self.__reverse_sentense_upper(self.input.text())
        self.label.setText(sentense)
        
    def __reverse_sentense_upper(self, sentense:str):
        return sentense.upper()[::-1]
        

def main():
    app = QApplication(sys.argv)
    window = sondantextga()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()