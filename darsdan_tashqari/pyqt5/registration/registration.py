from json import dumps, loads
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)

# from login import Login

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__my_window()
        self.move(450, 100)
        self.setStyleSheet(open("style.css").read())
        self.data = dict()
        self.show()

    def __my_window(self):
        self.setWindowTitle("QDialog")
        self.setFixedSize(450, 400)
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
        self.label_name.setFixedWidth(87)
        h_line.addWidget(self.line_name)
        v_line.addLayout(h_line)
        # print(self.line_name.text())

        # age
        h_line = QHBoxLayout()
        self.label_age = QLabel(self)
        self.line_age = QLineEdit(self)
        self.label_age.setText("Age:")
        self.line_age.setPlaceholderText("Enter your age...")
        self.label_age.setFixedWidth(87)
        h_line.addWidget(self.label_age)
        h_line.addWidget(self.line_age)
        v_line.addLayout(h_line)

        # job
        h_line = QHBoxLayout()
        self.label_job = QLabel(self)
        self.line_job = QLineEdit(self)
        self.label_job.setText("Job:")
        self.line_job.setPlaceholderText("Enter your Job...")
        self.label_job.setFixedWidth(87)
        h_line.addWidget(self.label_job)
        h_line.addWidget(self.line_job)
        v_line.addLayout(h_line)

        # hobbie
        h_line = QHBoxLayout()
        self.label_hobbie = QLabel(self)
        self.line_hobbie = QLineEdit(self)
        self.label_hobbie.setText("Hobbies:")
        self.line_hobbie.setPlaceholderText("Enter your Hobbies...")
        self.line_hobbie.setFixedWidth(337)
        h_line.addWidget(self.label_hobbie)
        h_line.addWidget(self.line_hobbie)
        v_line.addLayout(h_line)

        # Show status
        h_line = QHBoxLayout()
        self.status = QLabel("Waiting...")
        self.status.setStyleSheet("font-size: 25px; margin: 10px 0;color: #999}")
        h_line.addWidget(self.status)
        # h_line.
        v_line.addLayout(h_line)

        # Button Cancel
        h_line = QHBoxLayout()
        self.btn_cancel = QPushButton(self)
        self.btn_cancel.setText("✖️ Cancel")
        self.btn_cancel.setCursor(Qt.PointingHandCursor)
        self.btn_cancel.setStyleSheet(
            """
            QPushButton{
                color: crimson;
                border: 1px solid crimson;
            }
            QPushButton:hover{
                color: white;
                background-color: crimson;
            }
            QPushButton:focus{
                color: white;
                background-color: crimson;
            }
        """
        )
        h_line.addWidget(self.btn_cancel)
        h_line.setContentsMargins(0, 0, 0, 0)
        v_line.addLayout(h_line)
        self.btn_cancel.clicked.connect(self.stop_program)

        # Button Confirm
        self.btn_ok = QPushButton(self)
        self.btn_ok.setText("✔️ OK")
        self.btn_ok.setCursor(Qt.PointingHandCursor)
        self.btn_ok.setStyleSheet(
            """
            QPushButton{
                color: lime;
                border: 1px solid lime;
            }
            QPushButton:hover{
                color: white;
                background-color: lime;
            }
            QPushButton:focus{
                color: white;
                background-color: lime;
            }
        """
        )

        h_line.addWidget(self.btn_ok)
        
        
        # h_line.setAlignment(Qt.AlignmentFlag.AlignBottom)
        # v_line.addLayout(h_line)

        # Set Display
        v_line.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # login button
        self.login = QLabel("<u>I have already account.</u>")
        self.login.setCursor(Qt.PointingHandCursor)
        self.login.setStyleSheet("color: lime")
        self.login.setAlignment(Qt.AlignCenter)
        self.underlined = False

        v_line.addWidget(self.login)

        self.setLayout(v_line)
        self.btn_ok.clicked.connect(self.clicked_ok)

        # set data
        # self.data.update("name", self.line_name.text())

        # write data to file
        # with open(f"datas/{self.line_name}.json", "w") as write_file:
        # write_file.write()
        
    # def toggle_underline(self):

    def mousePressEvent(self, event):
        if self.login.geometry().contains(event.pos()):
            if self.underlined:
                self.login.setText("<u>I have already account.</u>")
                self.underlined = False
            else:
                self.login.setText("I have already account.")
                self.underlined = True
            # print("Labelga bosildi!")
            login = Login(self.line_name.text())
            # print(login)
            # self.close()
            login.show()

    def clicked_ok(self):
        red = "border: 1px solid crimson; padding: 5px; border-radius: 5px"
        black = "border: 1px solid #999; padding: 5px; border-radius: 5px"
        if (
            self.line_name.text() != ""
            and self.line_age.text() != ""
            and self.line_job.text() != ""
            and self.line_hobbie.text() != ""
        ):
            name = self.line_name.text()
            self.data["name"] = name.capitalize()
            self.data["age"] = self.line_age.text()
            self.data["job"] = self.line_job.text()
            self.data["hobbies"] = self.line_hobbie.text()

            self.line_name.setText("")
            self.line_age.setText("")
            self.line_job.setText("")
            self.line_hobbie.setText("")

            with open("data/users.json", "r+") as write_json:
                old_data = write_json.read()
                self.isHas = True
                if old_data == "":
                    old_data = []
                else:
                    old_data = loads(old_data)
                for i in old_data:
                    for j in i.values():
                        print(f"j = {j} name = {name}")
                        if j == name:
                            self.isHas = False
                            break
                    if not self.isHas:
                        break

                if self.isHas:
                    old_data.append(self.data)
                    write_json.seek(0)
                    convert = dumps(old_data, indent=4)
                    write_json.write(convert)
                    self.status.setText("Added successfully.")
                    self.status.setStyleSheet(
                        "color: lime; margin: 10px 0; font-size: 25px;"
                    )
                else:
                    self.status.setText("Already available.")

                self.label_name.setStyleSheet("color: black")
                self.label_age.setStyleSheet("color: black")
                self.label_job.setStyleSheet("color: black")
                self.label_hobbie.setStyleSheet("color: black")
                self.line_name.setStyleSheet(black)
                self.line_age.setStyleSheet(black)
                self.line_job.setStyleSheet(black)
                self.line_hobbie.setStyleSheet(black)
        else:
            if self.line_name.text() == "":
                self.label_name.setStyleSheet("color: crimson")
                self.label_age.setStyleSheet("color: black")
                self.label_job.setStyleSheet("color: black")
                self.label_hobbie.setStyleSheet("color: black")
                self.line_name.setStyleSheet(red)
                self.line_age.setStyleSheet(black)
                self.line_job.setStyleSheet(black)
                self.line_hobbie.setStyleSheet(black)
            elif self.line_age.text() == "":
                self.label_name.setStyleSheet("color: black")
                self.label_age.setStyleSheet("color: crimson")
                self.label_job.setStyleSheet("color: black")
                self.label_hobbie.setStyleSheet("color: black")
                self.line_name.setStyleSheet(black)
                self.line_age.setStyleSheet(red)
                self.line_job.setStyleSheet(black)
                self.line_hobbie.setStyleSheet(black)
            elif self.line_job.text() == "":
                self.label_name.setStyleSheet("color: black")
                self.label_age.setStyleSheet("color: black")
                self.label_job.setStyleSheet("color: crimson")
                self.label_hobbie.setStyleSheet("color: black")
                self.line_name.setStyleSheet(black)
                self.line_age.setStyleSheet(black)
                self.line_job.setStyleSheet(red)
                self.line_hobbie.setStyleSheet(black)
            elif self.line_hobbie.text() == "":
                self.label_name.setStyleSheet("color: black")
                self.label_age.setStyleSheet("color: black")
                self.label_job.setStyleSheet("color: black")
                self.label_hobbie.setStyleSheet("color: crimson")
                self.line_name.setStyleSheet(black)
                self.line_age.setStyleSheet(black)
                self.line_job.setStyleSheet(black)
                self.line_hobbie.setStyleSheet(red)
 
            self.status.setText("Fill it up.")
            self.status.setStyleSheet("font-size: 25px; margin: 10px 0;color: crimson}")

    def stop_program(self):
        exit(0)
    
    
# ulayolmadim yangi oyna ochilmadi    
class Login(QWidget):
    def __init__(self, name):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 300)
        self.__ui(name)
        self.show()

    def __ui(self, name):
        print(name)
        self.setStyleSheet("background-color: royalblue")
        self.label = QLabel("Normal Text")
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.label)
        self.setLayout(self.v_line)