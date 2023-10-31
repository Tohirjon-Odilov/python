
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Normal Text", self)
        self.label.setGeometry(100, 50, 200, 50)
        self.label.setAlignment(Qt.AlignCenter)

        self.label.mousePressEvent = self.toggle_underline
        self.underlined = False

    def toggle_underline(self, event):
        if self.underlined:
            # print()
            self.label.setText("<u>Normal Text</u>")
            self.underlined = False
        else:
            # print(self.sender())
            self.label.setText("Normal Text")
            self.underlined = True

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()

