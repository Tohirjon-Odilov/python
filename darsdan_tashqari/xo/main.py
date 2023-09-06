from os import system
from companents.auth import sign_up, sign_in

system("clear")
print("Welcome!")
print("1. Sign Up  2.Sign IN  3. Exit")
authDecision = int(input("Enter your decision-> "))
system("clear")
try:    
    if authDecision == 1:
        sign_up()
    elif authDecision == 2:
        sign_in()
    else:
        print("Bye")
        exit(0)
except Exception as e:
    print(e)
    exit("\033[1;31mMain has been stopped\033[0m")
