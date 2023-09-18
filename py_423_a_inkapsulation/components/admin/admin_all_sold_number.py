# admin change number
from json import loads

from pyfiglet import Figlet

from components.display import select_company


def get_sold_number(company_name):
    with open(f"datas/sold_numbers.json", "r") as read_sold_number_file:
        datas = loads(read_sold_number_file.read())
        datas = [filter(lambda phone: phone, [map(lambda item: item, datas.values())])]
        print(*datas)
        # print(f"{datas.get('Budget')}")
        # for company in datas:


# def get_all_sold_number(select_company):
def get_all_sold_number():
    # system('clear')
    f = Figlet(font="digital")
    print(f.renderText("Get all sold number"))
    selected_company = select_company()
    if selected_company == "1":
        print(f.renderText("Selected Beeline"))
        get_sold_number("Beeline")
    # get_sold_number()


print("salom")
get_all_sold_number()
