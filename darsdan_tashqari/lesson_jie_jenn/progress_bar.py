import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer

class ProgressBarDemo(QWidget):
	def __init__(self):
		super().__init__()
		self.progressBar = QProgressBar(self)
		self.progressBar.setGeometry(30, 40, 200, 25)

		self.btnStart = QPushButton("Start", self)
		self.btnStart.move(30, 80)
		# self.btnStart.clicked.connect() # TODO

		# self.btnReset


if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = ProgressBarDemo()
	demo.show()

	sys.exit(app.exec_())

