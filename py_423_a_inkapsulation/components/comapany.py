from json import dumps, loads
from os import system
from time import strftime

from components.number import Number


class Company:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        with open("datas/admin_panel.json", "r") as read_admin:
            datas = read_admin.read()
            datas = loads(datas)
            if datas.get(company_name):
                data = datas.get(company_name)
                self.__budget = data.get("Budget")
                self.last_purchased = data.get("LastPurchased")
            else:
                self.last_purchased = None
                self.__budget = 0
        self.__phone_numbers = list()
        with open(f"datas/{company_name}.txt", "r") as read_company_file:
            company_phone_numbers = read_company_file.readlines()
            for phone in company_phone_numbers:
                self.__phone_numbers.append(Number(self.company_name, phone))

    def get_budget(self):
        return self.__budget

    def set_budget(self, money):
        self.__budget += money

    def set_phoneNumber(self, numbers):
        self.__phone_numbers = numbers

    def get_phone_numbers(self):
        return self.__phone_numbers

    def add_number(self, number: Number):
        number_list = len(self.__phone_numbers)
        isHas = True
        for phone in self.__phone_numbers:
            if phone.get_number() != number.get_number():
                isHas = False
        if isHas:
            self.__phone_numbers.append(number)
            with open(f"datas/{self.company_name}.txt", "w") as write_file:
                for phone in self.__phone_numbers:
                    write_file.write(phone.get_number())
            if number_list < len(self.__phone_numbers):
                print("\033[1;33mNumber added successfully\033[1;0m")
            else:
                raise ValueError("\033[1;31mNumber not added\033[1;0m")
        else:
            print("Already added!")

    def sell_number(self, number: Number, user_name):
        number_list = len(self.__phone_numbers)

        # sotib olingan raqamni json formatdan faylaga yozadi
        with open("datas/sold_numbers.json", "r+") as file:
            old_data = file.read()
            old_data = loads(old_data) if old_data else {}
            file.seek(0)
            user_numbers = list()
            for data in old_data:
                if user_name == data:
                    user_numbers = old_data.get(data)
            user_numbers.append(
                {
                    number.get_number()[:-1]: [
                        number.get_price(),
                        number.get_company(),
                        strftime("%d/%m/%Y, %H:%M"),
                    ]
                },
            )
            old_data[f"{user_name}"] = [phone for phone in user_numbers]

            sold_numbers = dumps(old_data, indent=4)
            file.write(sold_numbers)
        self.__phone_numbers.remove(number)

        # sotib olinga raqamdan tashqari raqamlarni faylga yozadi
        with open(f"datas/{self.company_name}.txt", "w") as write_file:
            for i in self.__phone_numbers:
                write_file.write(i.get_number())

        # admin panel'ga yozish
        with open("datas/admin_panel.json", "r+") as read_write_file:
            company_datas = read_write_file.read()
            company_datas = loads(company_datas) if company_datas else {}
            read_write_file.seek(0)
            if company_datas and number.get_company() in company_datas:
                company_all_budget = company_datas.get(number.get_company()).get(
                    "Budget"
                )
            else:
                company_all_budget = 0
            company_all_budget += number.get_price()
            company_datas[number.get_company()] = {
                "Budget": company_all_budget,
                "Numbers": len(self.__phone_numbers),
                "LastPurchased": strftime("%d/%m/%Y, %H:%M"),
            }
            read_write_file.write(
                dumps(company_datas, indent=4),
            )
        self.set_budget(company_all_budget)
        if number_list > len(self.__phone_numbers):
            system("clear")
            print(
                f"\033[1;33mDear {user_name}, you are purchased:\n"
                f"number: {number.get_number()[:-1]}\n"
                f"price: {format(number.get_price(), ',')} sum\033[1;0m\n"
                f"Thank you for you purachase!"
            )
        #     i = 10
        #     while 0 < i:
        #         print(
        #             f"\033[1;33mDear {user_name}, you are purchased:\n"
        #             f"number: {number.get_number()[:-1]}\n"
        #             f"price: {format(number.get_price(), ',')} sum\033[1;0m\n"
        #             f"Thank you for you purachase!"
        #         )
        #         print(f"Oyna tozalanishiga {i} sekund qoldi.")
        #         i -= 1
        #         sleep(1)
        #         system("clear")
        else:
            raise ValueError("\033[1;31mNumber not found\033[1;0m")
        input("Retur back menu for enter.")

    def __str__(self) -> str:
        return (
            f"Company name: {self.company_name}\n"
            f"The last time the number was purchased: {self.last_purchased}\n"
            f"Numbers: {len(self.__phone_numbers)}\n"
            f"Budget: {format(self.__budget, ',')} sum\n"
        )
