from result import Ui_MainWindow as ResWindow
from game import Ui_MainWindow as MainWindow
from PyQt5.QtWidgets import *
from sys import argv
from random import *


class ResultWindow(QMainWindow, ResWindow):
    def __init__(self, gameRes='testing'):
        super().__init__()
        super().setupUi(self)
        self.label.setText(gameRes)
        self.pushButton.clicked.connect(lambda: self.close())
        self.pushButton_2.clicked.connect(self.changeWindow)

    def changeWindow(self):
        nextWindow = Window()
        nextWindow.show()
        self.close()


class Window(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.cells = list(range(1, 10))
        self.setButtons()
        self.Buttons = [
            self.pushButton,
            self.pushButton_2,
            self.pushButton_3,
            self.pushButton_4,
            self.pushButton_5,
            self.pushButton_6,
            self.pushButton_7,
            self.pushButton_8,
            self.pushButton_9
        ]
        self.clicks = 0
        self.nextWindow = ResultWindow()

    def setButtons(self):
        self.pushButton.clicked.connect(lambda: self.write(1))
        self.pushButton_2.clicked.connect(lambda: self.write(2))
        self.pushButton_3.clicked.connect(lambda: self.write(3))
        self.pushButton_4.clicked.connect(lambda: self.write(4))
        self.pushButton_5.clicked.connect(lambda: self.write(5))
        self.pushButton_6.clicked.connect(lambda: self.write(6))
        self.pushButton_7.clicked.connect(lambda: self.write(7))
        self.pushButton_8.clicked.connect(lambda: self.write(8))
        self.pushButton_9.clicked.connect(lambda: self.write(9))

    def write(self, i=0):
        print(self.comboBox.currentText())
        self.clicks += 1
        val = 'X'
        if self.cells:
            if self.clicks % 2 == 0:
                val = 'O'
                i = choice(self.cells)
            if self.Buttons[i-1].text() == '':
                self.Buttons[i-1].setText(val)
                self.cells.remove(i)
                res = self.isFinished()
                if res[0]:
                    for j in range(9):
                        if j in res[1]:
                            self.Buttons[j].setStyleSheet('background-color: rgb(255,0,0);')
                        else:
                            self.Buttons[j].setEnabled(False)
                    text = 'Yutdiz 👏' if res[2] == 'X' else 'Yutqazdiz 😒'
                    self.nextWindow.label.setText(text)
                    self.nextWindow.label.adjustSize()
                    self.nextWindow.show()
                    self.close()
                if val == 'X' and res[0] == False:
                    self.write()
            else:
                self.clicks -= 1

    def isFinished(self):
        for i in range(0,9, 3):
            a, b, c = self.Buttons[i].text(), self.Buttons[i+1].text(), self.Buttons[i+2].text()
            if len(a+b+c) == 3 and a == b and b == c:
                return [True, [i, i+1, i+2], a]
        for i in range(3):
            a, b, c = self.Buttons[i].text(), self.Buttons[i+3].text(), self.Buttons[i+6].text()
            if len(a+b+c) == 3 and a == b and b == c:
                return [True, [i, i+3, i+6], a]
        a, b, c = self.Buttons[0].text(), self.Buttons[4].text(), self.Buttons[8].text()
        if len(a + b + c) == 3 and a == b and b == c:
            return [True, [0, 4, 8], a]
        a, b, c = self.Buttons[2].text(), self.Buttons[4].text(), self.Buttons[6].text()
        if len(a + b + c) == 3 and a == b and b == c:
            return [True, [2, 4, 6], a]
        return [False, '']


if __name__ == "__main__":
    app = QApplication(argv)
    window = Window()
    window.show()
    app.exec()
