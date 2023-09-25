from os import system


class MyPrint:
    def show(self):
        system("clear")
        print(
            f"###### Menu ######\n"
            f"1. Burgers"
            f"2. Baskets"
            f"3. Drinks"
            f"4. Sweats"
            f"5. Ice-creams\n"
        )

    def user_choice(self, name):
        system("clear")
        print(
            f"###### {name} ######\n"
            f"1. Add new item"
            f"2. Remove item"
            f"3. Update item"
            f"4. Show all items"
            f"5. Search item"
            f"0. Exit\n"
        )
        return int(input(">>> "))

    def invalid_input(self):
        system("clear")
        print("Invalid input, try again!")
        input("Press enter to continue...")
        self.show()
