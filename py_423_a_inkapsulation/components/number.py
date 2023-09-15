from datetime import date


class Number:
    def __init__(self, company, number: str, price: int) -> None:
        self.created_at = date.today()
        self.__company = company
        self.__number = number
        self.__price = price

    def set_company_name(self, company):
        self.__company = company

    def get_company(self):
        return self.__company

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def __str__(self) -> str:
        return (
            f"Company: {self.__company}\n"
            f"Number: {self.__number}"
            f"Price: {self.__price}\n"
            f"Created at: {self.created_at}\n"
        )
