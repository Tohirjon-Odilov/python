from datetime import datetime

from components.number import Number


class Company:
    def __init__(self, companyName) -> None:
        self.company_name = companyName
        self.__budget = 0
        self.__phone_numbers = list()
        self.established_at = datetime.now()

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
        self.set_budget(number.get_price())
        if number_list > len(self.__phone_numbers):
            print("\033[1;33mNumber removed successfully\033[1;0m")
        else:
            raise ValueError("\033[1;31mNumber not removed\033[1;0m")
        # return removed

    def __str__(self) -> str:
        return (
            f"Company name: {self.company_name}\n"
            f"Established at: {self.established_at}\n"
            f"Numbers: {len(self.__phone_numbers)}\n"
            f"Budget: {self.__budget}\n"
        )
