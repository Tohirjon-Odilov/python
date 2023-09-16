from components.about_company import about_company

# from components.comapany import Company
from components.display import welcome_display, auth

# from components.number import Number
from components.tools import all_numbers

try:

    class MainCompany:
        def __init__(self, company_name) -> None:
            self.company_name = company_name
            self.__company_numbers = None
            self.main_company = None

        # def company(self):
        #     with open(f"datas/{self.company_name}.txt", "r") as file:
        #         company_phone_numbers = file.readlines()
        #         self.main_company = Company(self.company_name)
        #         for i in company_phone_numbers:
        #             self.main_company.add_number(Number(self.company_name, i))
        #         self.__company_numbers = self.main_company.get_phone_numbers()
        #         # print(self.main_company.get_phone_numbers())

        def get_company_numbers(self):
            # self.company()

            return self.__company_numbers

    user_name = auth()
    company = None
    while True:
        user_selection = welcome_display(user_name)
        if user_selection == "1":
            select_number, company = all_numbers()
            selected_number = company.get_phone_numbers()[select_number]
            company.sell_number(selected_number)
        elif user_selection == "4":
            about_company()
            print(company)
        elif user_selection == "0":
            break
        else:
            print("Please other number!")


except Exception as e:
    print(e)
finally:
    print("\033[1;31mProgram stopped!\033[1;0m")
