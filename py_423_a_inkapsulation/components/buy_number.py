from components.comapany import Company
from components.display import (
    show_number,
    select_number,
    select_company,
)


# from main import MainCompany


def choice_number(company):
    show_number(company)
    selected_number = select_number()
    if selected_number == "1":
        return int(input("Enter id: ")) - 1
    elif selected_number == "2":
        return ""
    elif selected_number == "0":
        exit("Program stopped!")
    else:
        input("Unexpected number!\nPlease choice only show numbers!")
        return "2"


def all_numbers():
    # system("clear")
    while True:
        selected_company = select_company()
        if selected_company == "1":
            while True:
                company = Company("Beeline")
                is_comeback = choice_number(company)
                if is_comeback == "":
                    break
                    continue
                elif is_comeback == "2":
                    continue
                else:
                    return is_comeback, company
        elif selected_company == "2":
            while True:
                company = Company("MobiUz")
                is_comeback = choice_number(company)
                if is_comeback == "2" or is_comeback == "":
                    continue
                else:
                    return is_comeback

        elif selected_company == "3":
            while True:
                company = Company("Ucell")
                is_comeback = choice_number(company)
                if is_comeback == "2" or is_comeback == "":
                    continue
                else:
                    return is_comeback

        elif selected_company == "4":
            while True:
                company = Company("Uzmobile")
                is_comeback = choice_number(company)
                if is_comeback == "2" or is_comeback == "":
                    continue
                else:
                    return is_comeback

        elif selected_company == "5":
            while True:
                company = Company("numbers")
                is_comeback = choice_number(company)
                if is_comeback == "2" or is_comeback == "":
                    continue
                else:
                    return is_comeback

        elif selected_company == "0":
            exit("Program stopped!")
