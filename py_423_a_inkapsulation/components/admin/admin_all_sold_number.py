# admin all sold number
from json import loads
from os import system
from time import sleep

from pyfiglet import Figlet


def get_sold_number(company_name):
    with open(f"datas/sold_numbers.json", "r") as read_sold_number_file:
        datas = loads(read_sold_number_file.read())
    name_data = list()
    # name
    for i in datas:
        name_data.append(datas.get(i))
        name_data.append(i)
    filtered_data = list()
    for i in name_data:
        if isinstance(i, list):
            for j in i:
                for keys, values in j.items():
                    price, company, date = values
                    if company != company_name:
                        continue
                    filtered_data.append([keys, price, date])
    for phone, price, date in filtered_data:
        print(f"Phone: {phone}\n" f"Price: {price}\n" f"Purchased date: {date}\n")


def get_all_sold_number(select_company):
    system("clear")
    f = Figlet(font="digital")
    print(f.renderText("Get all sold number"))
    selected_company = select_company()
    if selected_company == "1":
        system("clear")
        for i in range(3, 0, -1):
            print(f.renderText("Selected Beeline"))
            print(f"Time -> {i}")
            sleep(1)
            system("clear")
        get_sold_number("Beeline")
    elif selected_company == "2":
        system("clear")
        for i in range(3, 0, -1):
            print(f.renderText("Selected Mobiuz"))
            print(f"Time -> {i}")
            sleep(1)
            system("clear")
        get_sold_number("Mobiuz")
    elif selected_company == "3":
        system("clear")
        for i in range(3, 0, -1):
            print(f.renderText("Selected Ucell"))
            print(f"Time -> {i}")
            sleep(1)
            system("clear")
        get_sold_number("Ucell")
    elif selected_company == "4":
        system("clear")
        for i in range(3, 0, -1):
            print(f.renderText("Selected Uzmobile"))
            print(f"Time -> {i}")
            sleep(1)
            system("clear")
        get_sold_number("Uzmobile")
    elif selected_company == "5":
        input("Tex orada...")
