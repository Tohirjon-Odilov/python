from components.core import Core
from components.products import Drink, Food


class Display:
    def __init__(self) -> None:
        self.core = Core()

    def show(self):
        print(f"\n###### Menu ######\n")
        print(f"1. Burgers")
        print(f"2. Baskets")
        print(f"3. Drinks")
        print(f"4. Sweats")
        print(f"5. Ice-creams\n")

    def choice(self):
        ch = int(input(">>> "))
        if ch == 1:
            new = Food(input("Name: "), input("About: "), input("Cost: "))
            self.core.insert_food(new.get_food(), 'burgers')

        elif ch == 2:
            new = Food(input("Name: "), input("About: "), input("Cost: "))
            self.core.insert_food(new.get_food(), "baskets")

        elif ch == 3:
            new = Drink(input("Name: "), input("Cost: "))
            self.core.insert_food(new.get_food(), "drinks")


menu = Display()
menu.show()
menu.choice()
