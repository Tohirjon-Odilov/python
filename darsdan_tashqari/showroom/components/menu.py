from os import system

from components.address import Address
from components.car import Car
from components.showroom import CarShowroom


def second_apperance(showroom, cars):
    system("clear")
    print(f"1. Go back\n2. Exit")
    user_selection = input("")
    if user_selection == "1":
        car_tools(showroom, cars)
    elif user_selection == "2":
        exit("\033[1;31m Dasturdan chiqdingiz! \033[1;0m")


def car_tools(showroom: CarShowroom, cars: list) -> None:
    system("clear")
    print("1. Add car\n2. Remove car\n3. Get cars\n4. Rating\n0. Exit")
    user_selection = input(">>> ")
    if user_selection == "1":
        system("clear")
        print("Add car: ")
        car_name = input("Enter the car name: ")
        car_model = input("Enter the car model: ")
        car_price = float(input("Enter the car price: "))
        car_rate = int(input("Enter the car rate: "))
        car_color = input("Enter the car color: ")
        car = Car(car_name, car_model, car_price, car_rate, car_color)
        # car = Car("BMW", "gt 32", 35600, 4, "black")
        showroom.add_car(car)
        second_apperance(showroom, cars)
        # car_tools(user_selection, showroom, cars)
    elif user_selection == "2":
        system("clear")
        print("Choose one for remove: ")
        for idx, car in enumerate(cars, 1):
            print(idx, car.get_name())
        # user_selection = int(input(">>> "))
        # raise IndexError("\033[1;31mIltimos to'g'ri son kiriting!\033[1;0m")

    elif user_selection == "3":
        system("clear")
        print("Choose one for get info:")
        for idx, car in enumerate(showroom.get_cars_info(), 1):
            print(idx, car.get_name())
        selected = int(input(">>> "))
        # raise IndexError("\033[1;31mIltimos to'g'ri son kiriting!\033[1;0m")
        for car in cars:
            if car.get_name() == selected:
                print(car)

    elif user_selection == "4":
        system("clear")
        print(showroom.get_avarage_rate())
    elif user_selection == "0":
        exit("\033[1;31m Dasturdan chiqdingiz! \033[1;0m")


def first_apperance():
    system("clear")
    print("Welcome to the car showroom!")
    print("1. Create show room\n2. Exit")
    user_selection = input(">>> ")
    if user_selection == "1":
        system("clear")
        showroom_name = input("Enter your showroom name: ")
        print("Where the car showroom is located: ")
        showroom_country = input("Country: ")
        showroom_city = input("City: ")
        showroom_street = input("Street: ")
        showroom_add = Address(showroom_country, showroom_city, showroom_street)
        showroom = CarShowroom(showroom_name, showroom_add)
        cars = showroom.get_cars_info()
        while True:
            car_tools(showroom, cars)
    elif user_selection == "2":
        exit("\033[1;31m Dasturdan chiqdingiz! \033[1;0m")
    else:
        print("\033[1;31mIltimos to'g'ri tanlov kiriting!\033[1;0m")
