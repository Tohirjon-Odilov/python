# admin_main
from components.admin.admin_add_number import add_number
from components.admin.admin_all_sold_number import get_all_sold_number
from components.admin.admin_change_number import change_number
from components.admin.admin_delete_number import delete_number
from components.comapany import Company


# try:
def admin_main(admin_panel):
    while True:
        # system("clear")
        admin_selected, select_company = admin_panel()
        if admin_selected == "1":
            is_continue = False
            while True:
                if add_number(Company, select_company) == "6":
                    break
                    is_continue = True
            if is_continue:
                input()
        elif admin_selected == "2":
            is_continue = False
            while True:
                if delete_number(Company, select_company) == "6":
                    break
                    is_continue = True
            if is_continue:
                input()
        elif admin_selected == "3":
            change_number()
            input()
        elif admin_selected == "4":
            get_all_sold_number(select_company)
            input()
        elif admin_selected == "0":
            exit(0)


# except Exception as e:
#     print(e)
# else:
#     print("\033[1;31mProgram stopped!\033[1;0m")
