from json import dumps, loads

from tabulate import tabulate


class UserRepository:
    _userConnection = ""

    def __init__(self, fileName):
        self.fileName = fileName

    def getUsers(self):
        self.__openFileForRead()
        userData = self._userConnection.read()
        if userData:
            userData = loads(userData)
        else:
            userData = []

        return userData

    def createUser(self, userData):
        self.__openFileForRead()
        allUsers = self.getUsers()

        allUsers.append(userData)
        convertedUserData = dumps(allUsers, indent=4)
        self.__openFileForWrite()
        self._userConnection.write(convertedUserData)

    def deleteById(self, idx):
        pass

    def getById(self, idx):
        print(self.__openFileForRead())

    def __openFileForWrite(self):
        if self._userConnection:
            self._userConnection.close()
        self._userConnection = open(self.fileName, "w")

    def __openFileForRead(self):
        if self._userConnection:
            self._userConnection.close()
        self._userConnection = open(self.fileName, "r")


obj = UserRepository("users.json")
# from time import time

# start_time = time()
print(tabulate(obj.getUsers()))
# end_time = time()

# print(end_time - start_time)

# obj.createUser(
#     {
#         "name": "Abdulaziz",
#         "age" : 19
#     }
# )
