import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer, QTimerEvent

class ProgressBarDemo(QWidget):
	def __init__(self):
		super().__init__()
		self.progressBar = QProgressBar(self)
		self.progressBar.setGeometry(30, 40, 200, 25)

		self.btnStart = QPushButton("Start", self)
		self.btnStart.move(30, 80)
		self.btnStart.clicked.connect() # TODO

		self.btnRest = QPushButton("Reset", self)
		self.btnReset.move(120, 80)
		self.btnReset.clicked.connect() # TODO

		self.timer = QBasicTimer()
		self.step = 0

	def startProgress(self):
         if self.timer.isActive():
            self.timer.stop() 
            self.btnStart.set("start")
         else:
             self.timer.start(100, self)
             self.btnStart.setText("Stop")
             
     def timerEvent(self, event) -> None:
		 if self.step >= 100:
			self.timer.setText("start")

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = ProgressBarDemo()
	demo.show()

	sys.exit(app.exec_())

