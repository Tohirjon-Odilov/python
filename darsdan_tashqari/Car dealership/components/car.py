class Car:
    def __init__(
        self, name: str, model: str, price: float, capactiy: int, color: str
    ) -> None:
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
        return (
            f"Name: {self.name}"
            f"Model: {self.model}"
            f"Color: {self.color}"
            f"Capacity: {self.capactiy}"
            f"Price: {self.price}"
        )
