import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QShortcut, QListWidget
from PyQt5.QtGui import QKeySequence


from core import Core


class Label(QLabel):
    def __init__(self, text) -> None:
        super().__init__(text)
        self.setStyleSheet("padding-left: 20px")


class TestWindow(QWidget):
    def __init__(self, ques) -> None:
        super().__init__()
        self.ques = ques
        self.id = 0
        self.user_answers = list()

        self.setWindowTitle("Test")
        self.setFixedSize(1000, 400)
        self.setStyleSheet("font-size : 30px;")
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.label_que = QLabel(f"""{self.id+1}. {self.ques[self.id]["question"]}""")

        self.rbtn_a = QRadioButton(f'{self.ques[self.id]["variants"][0]}')
        self.rbtn_b = QRadioButton(f'{self.ques[self.id]["variants"][1]}')
        self.rbtn_c = QRadioButton(f'{self.ques[self.id]["variants"][2]}')
        self.rbtn_d = QRadioButton(f'{self.ques[self.id]["variants"][3]}')

        self.btn_next = QPushButton("Next")
        self.btn_next.setStyleSheet(
            "background-color: rgb(0, 255, 0); border-radius: 15%; padding: 5px 15px; border: 2px solid"
        )

        self.h_box.addStretch()
        self.h_box.addWidget(self.btn_next)
        self.h_box.addStretch()

        self.v_box.addWidget(self.label_que)
        self.v_box.addWidget(self.rbtn_a)
        self.v_box.addWidget(self.rbtn_b)
        self.v_box.addWidget(self.rbtn_c)
        self.v_box.addWidget(self.rbtn_d)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.shortcut = QShortcut(QKeySequence("Ctrl+1"), self)
        self.shortcut.activated.connect(self.get_next_question)

        self.btn_next.clicked.connect(self.get_next_question)

        self.show()

    def get_next_question(self):
        if self.rbtn_a.isChecked():
            self.user_answers.append(self.rbtn_a.text())
        elif self.rbtn_b.isChecked():
            self.user_answers.append(self.rbtn_b.text())
        elif self.rbtn_c.isChecked():
            self.user_answers.append(self.rbtn_c.text())
        elif self.rbtn_d.isChecked():
            self.user_answers.append(self.rbtn_d.text())
        else:
            self.user_answers.append("")

        self.id += 1

        if self.id == len(self.ques):
            self.close()
            self.res = ResultWin(self.ques, self.user_answers)
        else:
            self.next_question()

    def next_question(self):
        self.rbtn_a.setCheckable(False)
        self.rbtn_b.setCheckable(False)
        self.rbtn_c.setCheckable(False)
        self.rbtn_d.setCheckable(False)

        self.rbtn_a.setCheckable(True)
        self.rbtn_b.setCheckable(True)
        self.rbtn_c.setCheckable(True)
        self.rbtn_d.setCheckable(True)

        self.label_que.setText(f"""{self.id+1}. {self.ques[self.id]["question"]}""")

        self.rbtn_a.setText(f'{self.ques[self.id]["variants"][0]}')
        self.rbtn_b.setText(f'{self.ques[self.id]["variants"][1]}')
        self.rbtn_c.setText(f'{self.ques[self.id]["variants"][2]}')
        self.rbtn_d.setText(f'{self.ques[self.id]["variants"][3]}')

        if self.id == len(self.ques) - 1:
            self.btn_next.setText("Result")


class ResultWin(QWidget):
    def __init__(self, ques, user_ans) -> None:
        super().__init__()
        self.setWindowTitle("Javoblar")
        self.setFixedSize(1000, 400)
        self.setStyleSheet("font-size : 30px;")

        self.h_box = QHBoxLayout()

        self.v_box_id = QVBoxLayout()
        self.v_box_cor_ans = QVBoxLayout()
        self.v_box_user_ans = QVBoxLayout()
        self.v_box_res = QVBoxLayout()

        for i in range(len(user_ans)):
            res = "To'g'ri" if ques[i]["correct_answer"] == user_ans[i] else "Noto'g'ri"

            self.label_id = Label(str(i + 1))
            self.label_cor_ans = Label(ques[i]["correct_answer"])
            self.label_user_ans = Label(user_ans[i])
            self.label_res = Label(res)

            self.v_box_id.addWidget(self.label_id)
            self.v_box_cor_ans.addWidget(self.label_cor_ans)
            self.v_box_user_ans.addWidget(self.label_user_ans)
            self.v_box_res.addWidget(self.label_res)

        self.h_box.addLayout(self.v_box_id)
        self.h_box.addLayout(self.v_box_cor_ans)
        self.h_box.addLayout(self.v_box_user_ans)
        self.h_box.addLayout(self.v_box_res)

        self.setLayout(self.h_box)

        self.show()


app = QApplication(sys.argv)

db = Core()
ques = db.readFile()
win = TestWindow(ques)

sys.exit(app.exec_())
