class Card:
    """
    This class is for creating a card.
    """
    def __init__(self, name, number, exp, balans=0, password="1111") -> None:
        self.name = name
        self._number = number
        self.exp = exp
        self.__password = password
        self.__balans = balans

    def get_password(self):
        return self.__password

    def set_password(self, new_password, password):
        if password == self.get_password():
            self.__password = new_password
            return "Changing password"
        return "Invalide password"

    def get_balans(self):
        return self.__balans

    def add_balans(self, amount):
        self.__balans += amount

    def minus_balans(self, amount):
        self.__balans -= amount

    def __str__(self) -> str:
        return f"{self.name} {self._number} {self.exp} {self.__balans}"
