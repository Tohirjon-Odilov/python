# admin add number
from pyfiglet import Figlet

from components.number import Number


def input_phone(Company, company_name, phone):
    company = Company(company_name)
    if len(phone) == 12:
        company.add_number(
            Number(
                company_name,
                "+998 " + phone + "\n",
            )
        )
    else:
        input("Error, Please enter for continue.")


def add_number(Company, admin_select_company):
    # system('clear')
    f = Figlet(font="digital")
    print(f.renderText("Add number"))
    selected_company = admin_select_company()
    if selected_company == "1":
        phone = input("Create number:\nExample -> 90 203 08 19\n>>> ")
        input_phone(Company, "Beeline", phone)
        # return
    elif selected_company == "2":
        phone = input("Create number:\nExample -> 88 203 08 19\n>>> ")
        input_phone(Company, "MobiUz", phone)
    #         return
    elif selected_company == "3":
        phone = input("Create number:\nExample -> 93 333 33 33\n>>> ")
        input_phone(Company, "Ucell", phone)
    #         return
    elif selected_company == "4":
        phone = input("Create number:\nExample -> 99 999 99 99\n>>> ")
        input_phone(Company, "Uzmobile", phone)
    #         return
    elif selected_company == "5":
        phone = input("Create number:\nExample -> 9X XXX XX XX\n>>> ")
        input_phone(Company, "numbers", phone)
    #         return
    elif selected_company == "6":
        return "6"
    elif selected_company == "0":
        exit(0)
    else:
        print("Please, enter show numbers!")
