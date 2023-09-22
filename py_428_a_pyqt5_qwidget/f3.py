from sys import argv
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__my_window()
        self.move(450, 100)
        self.setStyleSheet(open("style.css").read())

    def __my_window(self):
        self.setWindowTitle("QDialog")
        self.setFixedSize(450, 300)

        v_line = QVBoxLayout()
        h_line = QHBoxLayout()

        # Registration
        auth = QLabel(self)
        auth.setText("Registration")
        auth.setStyleSheet("font-size: 32px;")
        auth.setFixedHeight(60)
        auth.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        v_line.addWidget(auth)

        # name
        self.label_name = QLabel(self)
        self.line_name = QLineEdit(self)
        h_line.addWidget(self.label_name)
        self.label_name.setText("Name:")
        self.line_name.setPlaceholderText("Enter your name...")
        self.label_name.setFixedWidth(90)
        h_line.addWidget(self.line_name)
        v_line.addLayout(h_line)

        # age
        h_line = QHBoxLayout()
        self.label_age = QLabel(self)
        self.line_age = QLineEdit(self)
        self.label_age.setText("Age:")
        self.line_age.setPlaceholderText("Enter your age...")
        self.label_age.setFixedWidth(90)
        h_line.addWidget(self.label_age)
        h_line.addWidget(self.line_age)
        v_line.addLayout(h_line)

        # job
        h_line = QHBoxLayout()
        self.label_job = QLabel(self)
        self.line_job = QLineEdit(self)
        self.label_job.setText("Job:")
        self.line_job.setPlaceholderText("Enter your Job...")
        self.label_job.setFixedWidth(90)
        h_line.addWidget(self.label_job)
        h_line.addWidget(self.line_job)
        v_line.addLayout(h_line)

        # hobbie
        h_line = QHBoxLayout()
        self.label_hobbie = QLabel(self)
        self.line_hobbie = QLineEdit(self)
        self.label_hobbie.setText("Hobbies:")
        self.line_hobbie.setPlaceholderText("Enter your Hobbies...")
        h_line.addWidget(self.label_hobbie)
        h_line.addWidget(self.line_hobbie)
        v_line.addLayout(h_line)

        # Button Cancel
        h_line = QHBoxLayout()
        self.btn_cancel = QPushButton(self)
        self.btn_cancel.setText("✖️ Cancel")
        self.btn_cancel.setStyleSheet(
            """
        QPushButton{
                                      background-color: crimson;
        }
        QPushButton:hover{
        color:crimson;
                                    background-color: transparent;
                                    border: 1px solid crimson;
                                    border-radius: 2px;

        }

"""
        )
        h_line.addWidget(self.btn_cancel)
        v_line.addLayout(h_line)

        # Button Confirm
        self.btn_ok = QPushButton(self)
        self.btn_ok.setText("✔️ OK")
        h_line.addWidget(self.btn_ok)
        # v_line.addLayout(h_line)

        # Set Display
        v_line.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(v_line)


app = QApplication(argv)
win = Window()
win.show()
app.exec_()
