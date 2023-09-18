from os import system

from components.comapany import Company
from components.display import select_company


def about_company():
    system("clear")
    selected_company = select_company()
    if selected_company == "1":
        system("clear")
        print(Company("Beeline"))
        input("Exit for enter.")
    elif selected_company == "2":
        system("clear")
        print(Company("MobiUz"))
        input("Exit for enter.")
    elif selected_company == "3":
        system("clear")
        print(Company("Ucell"))
        input("Exit for enter.")
    elif selected_company == "4":
        system("clear")
        print(Company("Uzmobile"))
        input("Exit for enter.")
