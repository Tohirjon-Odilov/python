from os import system

# from companents.home import menu


def show_table(game_input):
    print(
        f"""
     {game_input[1]} | {game_input[2]} | {game_input[3]}
    ---|---|---
     {game_input[4]} | {game_input[5]} | {game_input[6]}
    ---|---|---
     {game_input[7]} | {game_input[8]} | {game_input[9]}
    """
    )


def check_game_status(data):
    if (
        data[1] == data[2] == data[3] != " "
        or data[4] == data[5] == data[6] != " "
        or data[7] == data[8] == data[9] != " "
        or data[1] == data[4] == data[7] != " "
        or data[2] == data[5] == data[8] != " "
        or data[3] == data[6] == data[9] != " "
        or data[1] == data[5] == data[9] != " "
        or data[3] == data[5] == data[7] != " "
    ):
        return True
    return False


def ai_choice(choosable_indexes):
    import random

    if len(choosable_indexes) == 0:
        exit("\033[1;31mGame is over!\033[0m")
    else:
        choosen_index = random.choice(choosable_indexes)
        choosable_indexes.remove(choosen_index)
        return choosen_index


def is_game():
    while True:
        user_game = input(
            "1. \033[1;35mContinue GAME\033[1;0m 2. \033[1;31mExit\033[1;0m\n>>> "
        )
        if user_game == "1":
            return True
        elif user_game == "2":
            return False
        else:
            print("Siz noma'lum son kiritdingiz!!!")


def start_game(username):
    game_input = {
        1: " ",
        2: " ",
        3: " ",
        4: " ",
        5: " ",
        6: " ",
        7: " ",
        8: " ",
        9: " ",
    }
    choosable_indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    system("clear")
    print("GAME HAS BEEN STARTED")
    is_over = False
    while not is_over:
        show_table(game_input)
        try:
            decision = int(input("X -> "))
            choosable_indexes.remove(decision)
            game_input[decision] = "\033[1;31mX\033[1;0m"
            if len(choosable_indexes) == 0:
                is_over = check_game_status(game_input)
                system("clear")
                show_table(game_input)
                exit("\033[1;31mTie!\033[0m")
            system("clear")
            is_over = check_game_status(game_input)
            if is_over:
                show_table(game_input)
                with open("user_data/" + username + ".txt", "r") as file_read:
                    user_data = file_read.readline().split("|")
                    user_won_count = int(user_data[3]) + 1

                    with open("user_data/" + username + ".txt", "w") as file_write:
                        file_write.write(
                            f"{user_data[0]}|{user_data[1]}|{user_data[2]}|{user_won_count}|{user_data[4]}"
                        )
                print("\033[1;35mX Won!\033[1;0m")
                return is_game()

            game_input[ai_choice(choosable_indexes)] = "\033[1;34mO\033[1;0m"
            is_over = check_game_status(game_input)
            if is_over:
                show_table(game_input)
                with open("user_data/" + username + ".txt", "r") as file_read:
                    user_data = file_read.readline().split("|")
                    user_won_count = int(user_data[4]) + 1

                    with open("user_data/" + username + ".txt", "w") as file_write:
                        file_write.write(
                            f"{user_data[0]}|{user_data[1]}|{user_data[2]}|{user_data[3]}|{user_won_count}"
                        )
                print("\033[1;34mO Won!\033[1;0m")
                return is_game()

        except ValueError:
            system("clear")
            print("\033[1;31mXato\033[1;0m")
        except KeyboardInterrupt:
            exit("\n\033[1;31mGame has been stopped!\033[0m")
