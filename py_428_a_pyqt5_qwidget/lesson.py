from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.__init()

    def changeText(self):
        self.text.setText(self.textField.text())
        self.textField.clear()

    def __init(self):
        self.setWindowTitle("Authorization")
        self.setFixedSize(400, 230)

        # name
        self.name = QLabel("Name:")
        self.name.setFixedSize(100, 30)
        self.name_edit = QLineEdit()
        self.name_lyt = QHBoxLayout()
        self.name_lyt.addWidget(self.name)
        self.name_lyt.addWidget(self.name_edit)

        # age
        self.age = QLabel("Age:")
        self.age.setFixedSize(100, 30)
        self.age_edit = QLineEdit()
        self.age_lyt = QHBoxLayout()
        self.age_lyt.addWidget(self.age)
        self.age_lyt.addWidget(self.age_edit)

        # job
        self.job = QLabel("Job:")
        self.job.setFixedSize(100, 30)
        self.job_edit = QLineEdit()
        self.job_lyt = QHBoxLayout()
        self.job_lyt.addWidget(self.job)
        self.job_lyt.addWidget(self.job_edit)

        # hobbies
        self.hobbies = QLabel("Hobbies:")
        self.hobbies.setFixedSize(100, 30)
        self.hobbies_edit = QLineEdit()
        self.hobbies_lyt = QHBoxLayout()
        self.hobbies_lyt.addWidget(self.hobbies)
        self.hobbies_lyt.addWidget(self.hobbies_edit)

        # buttons
        self.cancel_btn = QPushButton()
        self.cancel_btn.setText("Cancel")

        self.ok_btn = QPushButton()
        self.ok_btn.setText("Ok")
        self.buttons_lyt = QHBoxLayout()
        self.buttons_lyt.addWidget(self.cancel_btn)
        self.buttons_lyt.addWidget(self.ok_btn)

        self.main_lyt = QVBoxLayout()
        self.main_lyt.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_lyt.addLayout(self.name_lyt)
        self.main_lyt.addLayout(self.age_lyt)
        self.main_lyt.addLayout(self.job_lyt)
        self.main_lyt.addLayout(self.hobbies_lyt)
        self.main_lyt.addLayout(self.buttons_lyt)

        self.setLayout(self.main_lyt)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
