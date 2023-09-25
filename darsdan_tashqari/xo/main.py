from os import system

from companents.auth import sign_up, sign_in

system("clear")
print("Welcome!")
print("1. Sign Up  2.Sign IN  3. Exit")
try:
    auth_decision = int(input("Enter your decision-> "))
    system("clear")
    if auth_decision == 1:
        sign_up()
    elif auth_decision == 2:
        sign_in()
    else:
        exit("Bye")
except Exception as e:
    print(e)
    exit("\033[1;31mMain has been stopped!\033[0m")
except KeyboardInterrupt:
    exit("\033[1;31m\nYou have stopped the program!\033[0m")
