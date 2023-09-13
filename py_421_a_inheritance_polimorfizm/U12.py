class Car:
    def __init__(self, name: str, model: str, price: float, capactiy: int, color: str) -> None:
        self.name = name
        self.model = model
        self.price = price
        self.capactiy = capactiy
        self.color = color

    def set_price(self, price: float) -> None:
        self.price = price

    def get_price(self) -> float:
        return self.price    

    def set_name(self, name: str) -> None:
        self.name = name
    
    def get_name(self) -> str:
        return self.name
    
    def set_capacity(self, capactiy: int) -> None:
        self.capactiy = capactiy

    def get_capacity(self) -> int:
        return self.capactiy
    
    def set_color(self, color: str) -> None:
        self.color = color
    
    def get_color(self) -> str:
        return self.color
    
    def set_model(self, model: str) -> None:
        self.model = model

    def get_model(self) -> str:
        return self.model

    def __repr__(self) -> str:
        return f"{self.name}"

class Address:
    def __init__(self, country: str, city: str, street: str) -> None:
        self.country = country
        self.city = city
        self.street = street

    def set_country(self, country: str) -> None:
        self.country = country
    
    def get_country(self) -> str:
        return self.country
    
    def set_city(self, city: str) -> None:
        self.city = city
    
    def get_city(self) -> str:
        return self.city
    
    def set_street(self, street: str) -> None:
        self.street = street

    def get_street(self) -> str:
        return self.street
    
    def __repr__(self) -> str:
        return f"country={self.country}, city={self.city}, street={self.street}"
    
class CarShowRoom:
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
        for id, car in enumerate(self.cars, 1):
            print(id, car)
        # return self.cars
    
    def get_address(self) -> Address:
        return self.address

    def change_name(self, name: str) -> None:
        self.name = name

    def change_address(self, country: str, city: str, street: str) -> None:
        Address.set_country = country
        Address.set_city = city
        Address.set_street = street
    
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
        return f"name={self.name}, address={self.address}, "
            
car1 = Car("BMW", "X5", 20000, 5, "red")
car2 = Car("Mercedes", "S500", 25000, 5, "black")
add1 = Address("Poland", "Warsaw", "Krakowska")
add2 = Address('Uzb', "Tashkent", 'Qatortol st')
car_show_room1 = CarShowRoom("ShowRoom1", add1)
car_show_room2 = CarShowRoom("ShowRoom2", add2)
car_show_room1.add_car(car1)
car_show_room1.add_car(car2)
car_show_room1.get_cars_info()
car_show_room1.set_rate(3)
car_show_room1.set_rate(4)
car_show_room1.set_rate(5)
car_show_room1.set_rate(5)
print(car_show_room1.get_avarage_rate())

