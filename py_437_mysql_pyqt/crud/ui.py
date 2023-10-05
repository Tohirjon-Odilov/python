import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from qtwidgets import PasswordEdit

from core import Core

class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        
        self.setFixedSize(500,120)
        self.setStyleSheet('''
            margin: 10px;
            padding: 10px;
            background: #4A55A2;
            border-radius: 15%;
            font-size: 30px;
            font-family: Bad Script;
        ''')


class Window(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("CRUD APP")
        self.setFixedSize(1500, 1000)

        self.__initUI()
        self.show()
    
    def __initUI(self):
        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignCenter)

        self.btnCreateUser = Button('Create New User')
        self.btnReadAllUsers = Button('Read All Users')
        self.btnReadById = Button('Read By Id Users')
        self.btnUpdateUser = Button('Update Users')
        self.btnDeleteUser = Button('Delete Users')

        self.vBox.addStretch()
        self.vBox.addWidget(self.btnCreateUser)
        self.vBox.addWidget(self.btnReadAllUsers)
        self.vBox.addWidget(self.btnReadById)
        self.vBox.addWidget(self.btnUpdateUser)
        self.vBox.addWidget(self.btnDeleteUser)
        self.vBox.addStretch()

        self.setLayout(self.vBox)


class CreateUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.core = Core()
        self.setWindowTitle("Create New User")
        self.setFixedSize(1500, 1000)

        self.__initUI()
        self.show()
    
    def __initUI(self):
        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignCenter)

        self.editFullName = QLineEdit()
        self.editFullName.setPlaceholderText("Full name")

        self.editUserName = QLineEdit()
        self.editUserName.setPlaceholderText("Username")

        self.editPassword = PasswordEdit()
        self.editPassword.setPlaceholderText("Password")

        self.editMobileNumber = QLineEdit()
        self.editMobileNumber.setPlaceholderText("Mobile Number")

        self.btnSave = QPushButton('Save')
        self.btnSave.clicked.connect(self.insertUser)

        self.btnMenu = QPushButton('Menu')

        self.vBox.addStretch()
        self.vBox.addWidget(self.editFullName)
        self.vBox.addWidget(self.editUserName)
        self.vBox.addWidget(self.editPassword)
        self.vBox.addWidget(self.editMobileNumber)
        self.vBox.addWidget(self.btnSave)
        self.vBox.addStretch()
        self.vBox.addWidget(self.btnMenu)
        self.vBox.addStretch()

        self.setLayout(self.vBox)

    def insertUser(self):
        fname = self.editFullName.text()
        uname = self.editUserName.text()
        pwd = self.editPassword.text()
        mobnum = self.editMobileNumber.text()

        if fname and uname and pwd and mobnum:
            user = {
                'full name':fname, 
                'username':uname, 
                'password':pwd, 
                'mobile number':mobnum
            }
            print(user)
            message = self.core.createUser(user)
            print(message)
        else:
            print('error')

class ShowUsersWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.core = Core()
        self.setWindowTitle("Read All Users")
        self.setFixedSize(1500, 1000)

        self.__initUI()
        self.show()
    
    def __initUI(self):
        users = self.__getData()
        print(users)
        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignCenter)

        self.labelTitle = QLabel('List of Users')

        self.btnMenu = QPushButton('Menu')
        
        self.table = QTableWidget()

        self.table.setColumnCount(5)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)

        self.table.setHorizontalHeaderLabels(users[0].keys())
        self.table.setRowCount(len(users))

        row = 0
        for user in users:
            self.table.setItem(row, 0, QTableWidgetItem(f"{user['id']}"))
            self.table.setItem(row, 1, QTableWidgetItem(user['full name']))
            self.table.setItem(row, 2, QTableWidgetItem(user['username']))
            self.table.setItem(row, 3, QTableWidgetItem(user['password']))
            self.table.setItem(row, 4, QTableWidgetItem(user['mobile number']))
            row += 1

        self.vBox.addWidget(self.labelTitle)
        self.vBox.addWidget(self.table)
        self.vBox.addWidget(self.btnMenu)

        self.setLayout(self.vBox)

    def __getData(self):
        data = self.core.getAllUsers()
        data = list(map(lambda user: {'id':user[0],'full name': user[1], 'username': user[2], 'password': user[3], 'mobile number': user[4]}, data))
        return data


class UpdateUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.core = Core()
        self.setWindowTitle("Update User")
        self.setFixedSize(1500, 1000)

        self.__initUI()
        self.show()
    
    def __initUI(self):
        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignCenter)

        self.editId = QLineEdit()
        self.editId.setPlaceholderText("ID")

        self.editFullName = QLineEdit()
        self.editFullName.setPlaceholderText("Full name")

        self.editUserName = QLineEdit()
        self.editUserName.setPlaceholderText("Username")

        self.editPassword = QLineEdit()
        self.editPassword.setPlaceholderText("Password")

        self.editMobileNumber = QLineEdit()
        self.editMobileNumber.setPlaceholderText("Mobile Number")

        self.btnUpdate = QPushButton('Update')
        self.btnUpdate.clicked.connect(self.updateUser)
        self.btnMenu = QPushButton('Menu')

        self.vBox.addStretch()
        self.vBox.addWidget(self.editId)
        self.vBox.addWidget(self.editFullName)
        self.vBox.addWidget(self.editUserName)
        self.vBox.addWidget(self.editPassword)
        self.vBox.addWidget(self.editMobileNumber)
        self.vBox.addWidget(self.btnUpdate)
        self.vBox.addStretch()
        self.vBox.addWidget(self.btnMenu)
        self.vBox.addStretch()

        self.setLayout(self.vBox)

    def updateUser(self):
        ID = self.editId.text()
        fname = self.editFullName.text()
        uname = self.editUserName.text()
        pwd = self.editPassword.text()
        mobnum = self.editMobileNumber.text()

        if ID and fname and uname and pwd and mobnum:
            user = {'id': int(ID), 'full name':fname, 'username':uname, 'password':pwd, 'mobile number':mobnum}
            print(user)
            message = self.core.setUser(user)
            print(message)
        else:
            print('error')



class DeleteUserWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Delete User")
        self.setFixedSize(1500, 1000)

        self.__initUI()
        self.show()
    
    def __initUI(self):
        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignCenter)

        self.editId = QLineEdit()
        self.editId.setPlaceholderText("ID")

        self.btnDelete = QPushButton('Delete')
        self.btnMenu = QPushButton('Menu')

        self.vBox.addStretch()
        self.vBox.addWidget(self.editId)
        self.vBox.addWidget(self.btnDelete)
        self.vBox.addStretch()
        self.vBox.addWidget(self.btnMenu)
        self.vBox.addStretch()

        self.setLayout(self.vBox)