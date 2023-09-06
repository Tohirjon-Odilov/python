from os import system


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



def start_game():
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
                exit("\033[1;35mX Won!\033[1;0m")
            game_input[ai_choice(choosable_indexes)] = "\033[1;34mO\033[1;0m"
            is_over = check_game_status(game_input)
            if is_over:
                show_table(game_input)
                exit("\033[1;34mO Won!\033[1;0m")
        except ValueError:
            system("clear")
            print("\033[1;31mXato\033[1;0m")
        except KeyboardInterrupt:
            exit("\n\033[1;31mDasturni to'xtatdingiz!\033[0m")
    # print(f"\033[1;35mX Won!\033[1;0m")

def see_stats():
    print("Stats")
