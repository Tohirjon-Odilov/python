from os import system


def admin():
    system("clear")
    input("Hello again, dear Tohirjon")


def auth():
    system("clear")
    user_name = input("Enter your name: ")
    if user_name == "admin":
        admin()
    return user_name.capitalize()


def welcome_display(user_name):
    system("clear")
    user_name = user_name
    print(
        f"########## Hello {user_name} ############\n"
        f"1. Buy number\n"
        f"2. Show my number\n"
        f"3. Show tariffs\n"
        f"4. About company\n"
        f"0. Exit\n"
    )
    user_selection = input(">>> ")
    return user_selection


def select_company() -> object:
    system("clear")
    print(f"1. Beeline\n2. Mobiuz\n3. Ucell\n4. Uzmobile\n5. Mixed\n0. Exit")
    welcome_chance = input(">>> ")
    return welcome_chance


def show_number(company):
    for idx, phone in enumerate(company.get_phone_numbers(), 1):
        print(
            "%s%s%s%s%s%s%s%s%s"
            % ("+", "-" * 2, "+", "-" * 6, "+", "-" * 5, "+", "-" * 18, "+")
        )
        print("|ID|%5d |PHONE| %s|" % (idx, phone.get_number()[0:-1]))
    print(
        "%s%s%s%s%s%s%s%s%s"
        % ("+", "-" * 2, "+", "-" * 6, "+", "-" * 5, "+", "-" * 18, "+")
    )


def select_number():
    print(f"1. Id bo'yicha raqam tanlash\n2. Orqaga qaytish\n0. Exit")
    selected_number = input(">>> ")
    return selected_number


class Display:
    def __init__(self):
        pass
