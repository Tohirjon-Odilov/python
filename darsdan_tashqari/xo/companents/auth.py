import os

from companents.home import menu


def is_user_exists(users, username):
    for i in users:
        if i == username + "\n":
            return True
    return False


def sign_up():
    name = ""
    username = ""
    while True:
        username = input("Enter your username-> ")
        users_list = open("users.txt", "r")
        all_users = users_list.readlines()
        if not is_user_exists(all_users, username):
            password = input("Create password for your account-> ")
            name = input("Enter your name-> ")
            with open("user_data/" + username + ".txt", "w") as file:
                file.write(username + "|" + password + "|" + name + "|0|0\n")
            with open("users.txt", "a") as users_list:
                users_list.write(username + "\n")
            os.system("clear")
            print("Your account created successfully!")
            break

        else:
            print("Account has been already created")
    menu(name, username)


def sign_in():
    username = input("Enter your username-> ")
    users_list = open("users.txt", "r")
    all_users = users_list.read()
    users_list.close()
    if username in all_users:
        with open("user_data/" + username + ".txt", "r") as current_user:
            correct_password = current_user.readline().split("|")[1]

            while True:
                password = input("Enter password-> ")
                if password == correct_password:
                    print("You have been successfully logged in")
                    current_user.seek(0)
                    break
                else:
                    print("Entered password is incorrect")
            menu(current_user.readline().split("|")[2], username)
    else:
        print(
            "\033[1;31mAccaunt has not been created!\033[1;0m\nPlease register first!"
        )
        first_register = input("1. Register now  2. Exit\n>>> ")
        if first_register == "1":
            sign_up()
        elif first_register == "2":
            exit("\033[1;31mGame has been stopped!\033[1;0m")
        else:
            exit("\033[1;31mEntered unknown number!\033[1;0m")
