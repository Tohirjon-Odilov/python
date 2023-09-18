from json import loads
from os import system


def show_my_number(user_name):
    with open("datas/sold_numbers.json", "r") as read_file:
        system("clear")
        user_datas = read_file.read()
        if not user_datas:
            print("Unavailable data!")
        user_datas = loads(user_datas)
        if user_name in user_datas:
            user = user_datas.get(user_name)
            for i in user:
                print("Phone: ", end="")
                print(*i)
                for price, company, purchased_time in i.values():
                    print(
                        f"Price: {format(price, ',')} sum\n"
                        f"Company: {company}\n"
                        f"Purchased time: {purchased_time}\n"
                    )
                    # for g in j:
        else:
            print("The number is not available")
    user_selection = input("Ortga qaytish uchun enterni bosing.")
    return user_selection
