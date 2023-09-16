from time import strftime

from components.number import Number


class Company:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.__budget = 0
        self.__phone_numbers = list()
        self.established_at = strftime("%d/%m/%Y %H:%M:%S")
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
        # number_list = len(self.__phone_numbers)
        self.__phone_numbers.append(number)
        # if number_list < len(self.__phone_numbers):
        #     print("\033[1;33mNumber added successfully\033[1;0m")
        # else:
        #     raise ValueError("\033[1;31mNumber not added\033[1;0m")

    def sell_number(self, number: Number):
        number_list = len(self.__phone_numbers)
        self.__phone_numbers.remove(number)
        with open(f"datas/{self.company_name}.txt", "w") as write_file:
            for i in self.__phone_numbers:
                write_file.write(i.get_number())
        self.set_budget(number.get_price())
        if number_list > len(self.__phone_numbers):
            print(
                f"\033[1;33mThis number purchased: {number.get_number()[:-1]}\n"
                f"This number price is {number.get_price()}\033[1;0m"
            )
        else:
            raise ValueError("\033[1;31mNumber not found\033[1;0m")
        # return removed

    def __str__(self) -> str:
        return (
            f"Company name: {self.company_name}\n"
            f"Established at: {self.established_at}\n"
            f"Numbers: {len(self.__phone_numbers)}\n"
            f"Budget: {self.__budget}\n"
        )
