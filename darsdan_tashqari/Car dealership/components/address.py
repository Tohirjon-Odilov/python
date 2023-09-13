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
