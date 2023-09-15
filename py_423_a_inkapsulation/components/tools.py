from components.display import (
    show_number,
    select_number,
    select_company,
)

# from main import MainCompany


def all_numbers(MainCompany):
    selected_company = select_company()
    if selected_company == "1":
        company = MainCompany("Beeline")
        show_number(company)
        return select_number(), company
    elif selected_company == "2":
        company = MainCompany("MobiUz")
        show_number(company)
        return select_number(), company
    elif selected_company == "3":
        company = MainCompany("Ucell")
        show_number(company)
        return select_number(), company
    elif selected_company == "4":
        company = MainCompany("Uzmobile")
        show_number(company)
        return select_number(), company
    elif selected_company == "5":
        uzmobile = MainCompany("Uzmobile")
        print(uzmobile.company())
