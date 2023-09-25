from os import system


def see_stats(name, username):
    system("clear")
    print(f"1. See yours stats" f"2. See leaderboard" f"3. Return game" f"4. Exit")

    user_choice = input(">>> ")
    if user_choice == "1":
        system("clear")
        print(f"Hello {name}")
        print(f"Your stats are: ")
        print(f"Wins: {username.wins}")
        print(f"Losses: {username.losses}")
        print(f"Draws: {username.draws}")
        input("Press enter to continue")
        return True
