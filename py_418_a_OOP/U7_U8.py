"""
U7:

User nomli class ochilsin, unda name, age, balance, nomli atributlar, getBalance, addMoney,
getMoney metodlari bo'lsin.

User dasturni run qilsa, undan ism,balance, yoshni so'rasin va obyekt atributlariga o'zlashtirilsin.

Keyin esa menyu chiqsin, 1.Add Money 2. GetMoney, 3. Get Balance 4.Exit nomli menyu chiqsin.

1.ni tanlasa balancega kiritilgan pulni qo'shsin.
2.ni tanlasa balancedan kiritilgan pulni agar balanceda pul yetarli bo'lsa yechsin.
3.ni tanlasa balance haqida ma'lumot bersin.
4.ni tanlasa dasturdan chiqsin

Obyekt print qilinsa ichidagi bor ma'lumotlardan foydalanib, "Salom mening ismim {name},
yoshim {age}da lekin, shu yoshimda {balance} UZS pulim bor" degan ma'lumot chiqsin.
"""

if 0:
    from os import system

    class User:
        def __init__(self, name, age, balance):
            self.name = name
            self.age = age
            self.balance = balance

        def get_balance(self):
            print("Your balance ->", self.balance)

        def add_money(self, money):
            self.balance += money

        def get_money(self, money):
            if self.balance >= money:
                self.balance -= money
            else:
                print("Not enough money?")

        def __str__(self):
            return (
                f"Salom mening ismim {self.name},\n"
                f"yoshim {self.age}da lekin, shu yoshimda {self.balance}UZS pulim bor"
            )

    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    user_balance = int(input("Enter your balance: "))
    person1 = User(user_name, user_age, user_balance)
    system("clear")
    while True:
        print("1. Add Money  2. Get Money  3. Get Balance  4. Get full info  5. Exit")
        menu = input("Choose your selection: ")
        if menu == "1":
            system("clear")
            person1.add_money(int(input("Add balance: ")))
        if menu == "2":
            system("clear")
            person1.get_money(int(input("Debit balance: ")))
        if menu == "3":
            system("clear")
            person1.get_balance()
        if menu == "4":
            system("clear")
            print(person1)
        if menu == "5":
            break

"""
U8:

Market nomli class oching. Undagi atributlar:
Dictionary products
float balance
String name
String adress
bo'lsin.

Metodlar:
getProductsInfo() -> ekranga qaysi productlar borligini chiqarsin.
addPoduct -> product qo'shish
removeProduct -> Productni o'chirish

addMoney()-> Balancega pul qo'shadi

sell() ->  kiritilgan tovar bo'lsa, sonini so'raydi va narxini hisoblab, 
addMoney orqali balancega o'sha pulni qo'shib qo'yadi.
"""
if 0:
    from os import system

    class Market:
        def __init__(self, balance: float, name: str, address: str):
            self.products = {
                "Bread": 2800,
                "Apple": 4500,
                "Banana": 20000,
                "Butter": 45000,
                "Potato": 3000,
                "Tomato": 4500,
                "Water": 11000,
                "CocaCola": 16000,
                "Kaktus": 5000,
            }
            self.balance = balance
            self.name = name
            self.address = address

        def get_products_info(self):
            print([i for i in self.products.keys()])

        def add_product(self, product_name, product_price):
            self.products[product_name] = product_price

        def add_balance(self, balance):
            self.balance += balance

        def remove_product(self, removed_product):
            self.products.pop(removed_product)

        def add_money(self, balance):
            self.balance += float(balance)

        def sell_product(self, sold_product, number_of_product):
            self.add_money(self.products.get(sold_product) * number_of_product)


def color(text):
    return f"\033[1;35{text}\033[1;0m"


market_1 = Market(0, "Magnum", "Qatortol ko'chasi 19-uy")
system("clear")
while True:
    print(
        "1. Get products info\n"
        "2. Add product\n"
        "3. Remove product\n"
        "4. Add money\n"
        "5. Sell product\n"
        "6. Show balance\n"
        "7. Exit\n"
    )
    user_selection = input("Enter your selection: ")
    if user_selection == "1":
        system("clear")
        print("Your product:")
        market_1.get_products_info()
        print()
    if user_selection == "2":
        system("clear")
        print("Enter your>>> ")
        market_1.add_product(input("product: "), int(input("price: ")))
        print()
    if user_selection == "3":
        system("clear")
        market_1.remove_product(input("Enter your product: "))
        print()
    if user_selection == "4":
        system("clear")
        market_1.add_money(int(input("Add money: ")))
        print()
    if user_selection == "5":
        system("clear")
        product = input("Enter product: ")
        if product in market_1.products:
            market_1.sell_product(product, int(input("Enter number of product: ")))
        else:
            print("Bunday mahsulot mavjud emas!")
        print()
    if user_selection == "6":
        system("clear")
        print(market_1.balance)
        print()
    if user_selection == "7":
        system("clear")
        break
