from os import system

from components.comapany import Company
from components.display import select_company


def about_company():
    system("clear")
    selected_company = select_company()
    if selected_company == "1":
        user_company = Company("Beeline")
        # from pprint import pprint

        # pprint(user_company)
        print(user_company)
    elif selected_company == "2":
        user_company = Company("MobiUz")
        print(user_company)
    elif selected_company == "3":
        user_company = Company("Ucell")
        print(user_company)
    elif selected_company == "4":
        user_company = Company("Uzmobile")
        print(user_company)
