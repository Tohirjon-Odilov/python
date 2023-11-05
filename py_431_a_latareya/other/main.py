# from sys import argv
# from PyQt5.QtWidgets import QApplication

# from components.ui import mainWindow

# app = QApplication(argv)
# win = mainWindow()
# win.show()

# exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve

class AnimateWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton("Start Animation", self)
        self.button.setGeometry(10, 10, 150, 30)
        self.button.clicked.connect(self.start_animation)

        self.rect = QRect(10, 50, 50, 50)
        self.rect_animation = QPropertyAnimation(self, b'geometry')
        self.rect_animation.setDuration(2000)  # Animatsiya davomiyligi (millyonidavomiga millisaniya)
        self.rect_animation.setStartValue(self.rect)
        self.rect_animation.setEndValue(QRect(250, 50, 50, 50))
        self.rect_animation.setEasingCurve(QEasingCurve.OutBounce)  # Animatsiya usuli
        self.rect_animation.finished.connect(self.animation_finished)

    def start_animation(self):
        self.rect_animation.start()

    def animation_finished(self):
        print("Animatsiya tugadi!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimateWidget()
    window.show()
    sys.exit(app.exec_())
