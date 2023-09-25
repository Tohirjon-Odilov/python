from components.address import Address
from components.car import Car


class CarShowroom:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address
        self.cars = list()
        self.rates = list()

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def remove_car(self, car: Car) -> None:
        self.cars.remove(car)

    def get_cars_info(self) -> list[Car]:
        return self.cars

    def get_address(self) -> Address:
        return self.address

    def change_name(self, name: str) -> None:
        self.name = name

    def change_address(self, country: str, city: str, street: str) -> None:
        self.address.set_country(country)
        self.address.set_city(city)
        self.address.set_street(street)

    def get_name(self) -> str:
        return self.name

    def set_rate(self, rate: int) -> None:
        if 0 < rate <= 5:
            self.rates.append(rate)
        else:
            raise ValueError("Rate must be between 1 and 5")

    def get_avarage_rate(self) -> float:
        return sum(self.rates) / len(self.rates)

    def __repr__(self) -> str:
        return f"name={self.name}, address={self.address}"
