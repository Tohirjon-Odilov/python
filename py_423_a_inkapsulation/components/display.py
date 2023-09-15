def admin():
    # system("clear")
    print(f"Yana salom Tohirjon")


def auth():
    # system("clear")
    user_name = input("Enter your name: ")
    if user_name != "admin":
        return user_name
    else:
        admin()


def welcome_display(user_name):
    # system("clear")
    user_name = "Tohirjon" if user_name == "" else user_name
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
    # system("clear")
    print(
        f"1. Beeline\n" f"2. Mobiuz\n" f"3. Ucell\n" f"4. Uzmobile\n" f"5. All abonent"
    )
    welcome_chance = input(">>> ")
    return welcome_chance


def show_number(company):
    for idx, phone in enumerate(company.get_company_numbers(), 1):
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
    print(f"1. Id bo'yicha raqam tanlash\n2. Orqaga qaytish\n3. Exit")
    selected_number = input(">>> ")
    return int(selected_number) - 1


class Display:
    def __init__(self):
        pass
