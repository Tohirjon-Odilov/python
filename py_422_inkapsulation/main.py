from datetime import datetime
from os import system

from component.card import Card
from component.user import User


class ATM:
    """
    This class is ATM.
    """

    def __init__(self, name, cash, balans) -> None:
        self.name = name
        self.cash = cash
        self.balans = balans
        self.user = None

    def __show_menu(self):
        system("clear")
        print("1. Info")
        print("2. Get cash")
        print("3. Get balans")
        print("4. Change password")
        print("5. Exit")

    def __choice(self):
        ch = int(input(">>> "))
        if ch == 1:
            print(self.user.card)
            time, date = self.get_now_time()
            print(f"Time: {time}\nDate: {date}")
        elif ch == 2:
            self.get_cash()
        elif ch == 3:
            self.get_balans()
        elif ch == 4:
            psw = input("Password: ")
            new_psw = input("New password: ")
            print(self.user.card.set_password(new_psw, psw))

    def get_now_time(self):
        date = datetime.now()
        return datetime.strftime(date, f"%H:%M:%S"), datetime.strftime(
            date, f"%d-%m-%y"
        )

    def enter_card(self, user: User):
        self.user = user
        n = 3
        while n:
            pwd = input("Enter password: ")
            if user.card.get_password() == pwd:
                n = 3
                self.__show_menu()
                self.__choice()
                break
            else:
                print("Password incorrect. Please try again")
                n -= 1

    def get_cash(self):
        system("clear")
        summa = int(input("Enter summa: "))
        pnt = summa * 1.01
        if self.user.card.get_balans() >= pnt:
            self.balans += pnt
            self.cash -= summa
            self.user.card.minus_balans(pnt)
            self.user.add_cash(summa)

    def get_balans(self):
        system("clear")
        summa = int(input("Enter summa: "))
        if atm.cash >= summa:
            self.balans -= summa
            self.cash += summa
            self.user.card.add_balans(summa)
            self.user.minus_cash(summa)


card1 = Card("Asaka", "8600111122227777", "09/29", 1000000)
user1 = User("John", "Doe", card1)
atm = ATM("SQB", 10000000, 600000)

atm.enter_card(user1)

# print(atm.balans)
# print(atm.cash)
# print(user1.card.get_balans())
# print(user1.cash)
