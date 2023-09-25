from os import system

from companents.game import start_game
from companents.stats import see_stats


# from game import start_game
# from stats import see_stats


def menu(name, username):
    end = True
    while end:
        system("clear")
        print(f"Hello {name}")
        print("1. Start game 2. See stats 3.Exit")
        choice = input("Enter your choice-> ")
        if choice == "1":
            end = start_game(username)
        elif choice == "2":
            end = see_stats(name, username)
        elif choice == "3":
            print("Bye")
            exit(0)
