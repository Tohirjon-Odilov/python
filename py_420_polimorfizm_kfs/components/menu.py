from os import system


def show(self):
    system("clear")
    print(f"###### Menu ######\n")
    print(f"1. Burgers")
    print(f"2. Baskets")
    print(f"3. Drinks")
    print(f"4. Sweats")
    print(f"5. Ice-creams\n")

def user_choice(self, name):
    system("clear")
    print(f"###### {name} ######\n")
    print(f"1. Add new item")
    print(f"2. Remove item")
    print(f"3. Update item")
    print(f"4. Show all items")
    print(f"5. Search item")
    print(f"0. Exit\n")
    return int(input(">>> "))
