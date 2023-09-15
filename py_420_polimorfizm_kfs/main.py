from components.core import Core
from components.menu import show, user_choice
from components.products import Drink, Food


class Display:
    def __init__(self) -> None:
        self.core = Core()

    def user_selection(self, select, new):
        if select == 1:
            self.core.insert_food(new.get_food(), "burgers")
        elif select == 2:
            self.core.remove_food(input("Name: "), "burgers")
        elif select == 3:
            self.core.update_food("burgers")
        elif select == 4:
            self.core.show_all_food("burgers")
        elif select == 5:
            self.core.search_food("burgers")
        elif select == 0:
            exit("\033[1;31mDastur to'xtadi\033[1;0m")
        else:
            print("Invalid input")
            self.choice()

    def choice(self):
        ch = int(input(">>> "))
        if ch == 1:
            select = user_choice("Burgers")
            new = Food(input("Name: "), input("About: "), input("Cost: "))
            self.user_select = self.user_selection(select, new)
            if select == 1:
                self.core.insert_food(new.get_food(), "burgers")
            elif select == 2:
                self.core.remove_food(input("Name: "), "burgers")
            elif select == 3:
                self.core.update_food("burgers")
            elif select == 4:
                self.core.show_all_food("burgers")
            elif select == 5:
                self.core.search_food("burgers")
            elif select == 0:
                exit("\033[1;31mDastur to'xtadi\033[1;0m")
            else:
                print("Invalid input")
            self.choice()

        elif ch == 2:
            select = user_choice("Baskets")
            if select == 1:
                new = Food(input("Name: "), input("About: "), input("Cost: "))
                self.core.insert_food(new.get_food(), "baskets")
            elif select == 2:
                self.core.remove_food(input("Name: "), "baskets")
            elif select == 3:
                self.core.update_food("baskets")
            elif select == 4:
                self.core.show_all_food("baskets")
            elif select == 5:
                self.core.search_food("baskets")
            elif select == 0:
                exit("\033[1;31mDastur to'xtadi\033[1;0m")
            else:
                print("Invalid input")
                self.choice()

        elif ch == 3:
            select = user_choice("Drinks")
            if select == 1:
                new = Drink(input("Name: "), input("Cost: "))
                self.core.insert_food(new.get_food(), "drinks")
            elif select == 2:
                self.core.remove_food(input("Name: "), "drinks")
            elif select == 3:
                self.core.update_food("drinks")
            elif select == 4:
                self.core.show_all_food("drinks")
            elif select == 5:
                self.core.search_food("drinks")
            elif select == 0:
                exit("\033[1;31mDastur to'xtadi\033[1;0m")
            else:
                print("Invalid input")
                self.choice()

        elif ch == 4:
            select = user_choice("Sweats")
            if select == 1:
                new = Food(input("Name: "), input("About: "), input("Cost: "))
                self.core.insert_food(new.get_food(), "sweats")
            elif select == 2:
                self.core.remove_food(input("Name: "), "sweats")
            elif select == 3:
                self.core.update_food("sweats")
            elif select == 4:
                self.core.show_all_food("sweats")
            elif select == 5:
                self.core.search_food("sweats")
            elif select == 0:
                exit("\033[1;31mDastur to'xtadi\033[1;0m")
            else:
                print("Invalid input")
                self.choice()

        elif ch == 5:
            select = user_choice("Ice-creams")
            if select == 1:
                new = Food(input("Name: "), input("About: "), input("Cost: "))
                self.core.insert_food(new.get_food(), "ice-creams")
            elif select == 2:
                self.core.remove_food(input("Name: "), "ice-creams")
            elif select == 3:
                self.core.update_food("ice-creams")
            elif select == 4:
                self.core.show_all_food("ice-creams")
            elif select == 5:
                self.core.search_food("ice-creams")
            elif select == 0:
                exit("\033[1;31mDastur to'xtadi\033[1;0m")
            else:
                print("Invalid input")
                self.choice()


menu = Display()
show()
menu.choice()
