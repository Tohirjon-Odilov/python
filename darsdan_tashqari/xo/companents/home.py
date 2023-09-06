from os import system
from game import start_game, see_stats

# from companents.game import start_game, see_stats


# def menu(name):
name = "Tohirjon"
system("clear")
print(f"Hello {name}")
print("1. Start game 2. See stats 3.Exit")
choice = input("Enter your choice-> ")
if choice == "1":
    start_game()
elif choice == "2":
    see_stats()
elif choice == "3":
    print("Bye")
    exit(0)
