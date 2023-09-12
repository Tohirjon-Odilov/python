from os import system
from components.core import Core
from components.products import Drink, Food


class Display:
    def __init__(self) -> None:
        self.core = Core()

    def show(self):
        system("clear")
        print(f"###### Menu ######\n")
        print(f"1. Burgers")
        print(f"2. Baskets")
        print(f"3. Drinks")
        print(f"4. Sweats")
        print(f"5. Ice-creams\n")

    def user_choice(self):
        print(f"1. Add new item")
        print(f"2. Remove item")
        print(f"3. Update item")
        print(f"4. Show all items")
        print(f"5. Search item")
        print(f"6. Exit\n")
        return int(input(">>> "))

    def choice(self):
        ch = int(input(">>> "))
        if ch == 1:
            select = self.user_choice()
            if select == 1:
                new = Food(input("Name: "), input("About: "), input("Cost: "))
                self.core.insert_food(new.get_food(), "burgers")
            elif select == 2:
                self.core.remove_food("BIG SANDERS BURGER ORIGINAL", "burgers")
            elif select == 3:
                self.core.update_food("burgers")
            elif select == 4:
                self.core.show_all_food("burgers")
            elif select == 5:
                self.core.search_food("burgers")
            elif select == 6:
                pass
            else:
                print("Invalid input")
                self.choice()

        elif ch == 2:
            select = self.user_choice()
            if select == 1:
                new = Food(input("Name: "), input("About: "), input("Cost: "))
                self.core.insert_food(new.get_food(), "baskets")
            elif select == 2:
                self.core.remove_food("baskets")
            elif select == 3:
                self.core.update_food("baskets")
            elif select == 4:
                self.core.show_all_food("baskets")
            elif select == 5:
                self.core.search_food("baskets")
            elif select == 6:
                pass
            else:
                print("Invalid input")
                self.choice()

        elif ch == 3:
            select = self.user_choice()
            if select == 1:
                new = Drink(input("Name: "), input("Cost: "))
                self.core.insert_food(new.get_food(), "drinks")
            elif select == 2:
                self.core.remove_food("drinks")
            elif select == 3:
                self.core.update_food("drinks")
            elif select == 4:
                self.core.show_all_food("drinks")
            elif select == 5:
                self.core.search_food("drinks")
            elif select == 6:
                pass
            else:
                print("Invalid input")
                self.choice()

        elif ch == 4:
            select = self.user_choice()
            if select == 1:
                new = Food(input("Name: "), input("About: "), input("Cost: "))
                self.core.insert_food(new.get_food(), "sweats")
            elif select == 2:
                self.core.remove_food("Maffin shokoladli", "sweats")
            elif select == 3:
                self.core.update_food("sweats")
            elif select == 4:
                self.core.show_all_food("sweats")
            elif select == 5:
                self.core.search_food("sweats")
            elif select == 6:
                pass
            else:
                print("Invalid input")
                self.choice()

        elif ch == 5:
            select = self.user_choice()
            if select == 1:
                new = Food(input("Name: "), input("About: "), input("Cost: "))
                self.core.insert_food(new.get_food(), "ice-creams")
            elif select == 2:
                self.core.remove_food("ice-creams")
            elif select == 3:
                self.core.update_food("ice-creams")
            elif select == 4:
                self.core.show_all_food("ice-creams")
            elif select == 5:
                self.core.search_food("ice-creams")
            elif select == 6:
                pass
            else:
                print("Invalid input")
                self.choice()


menu = Display()
menu.show()
menu.choice()
