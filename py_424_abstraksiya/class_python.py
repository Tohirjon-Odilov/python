from json import dumps, loads


def getUsers():
    with open("users.json", "r") as userFile:
        userData = userFile.read()
        if userData:
            userData = loads(userData)
        else:
            userData = []

    return userData


def createUser(userData: dict):
    allUsers = getUsers()
    with open("users.json", "w") as userFile:
        allUsers.append(userData)
        convertedUserData = dumps(allUsers, indent=4)
        userFile.write(convertedUserData)


# createUser({"name": "Asad", "age": 13})
# print(getUsers())
# user_data = {
#     "name": "Aziz",
#     "age": "45",
#     "username": "aziz1256"
# }

# # convertedUserData = json.dumps(user_data)


# # with open("users.json", "w") as userFile:
# #     userFile.write(convertedUserData)


# with open
