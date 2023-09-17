from os import system

from components.comapany import Company
from components.display import (
    show_number,
    select_number,
    select_company,
)


# from main import MainCompany


def all_numbers():
    system("clear")
    selected_company = select_company()
    if selected_company == "1":
        company = Company("Beeline")
        show_number(company)
        return select_number(), company
    elif selected_company == "2":
        company = Company("MobiUz")
        show_number(company)
        return select_number(), company
    elif selected_company == "3":
        company = Company("Ucell")
        show_number(company)
        return select_number(), company
    elif selected_company == "4":
        company = Company("Uzmobile")
        show_number(company)
        return select_number(), company
    elif selected_company == "5":
        print("Tez orada...")
        # uzmobile = Company("Uzmobile")
        # print(uzmobile.company())
