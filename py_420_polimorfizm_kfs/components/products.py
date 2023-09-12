class Food:
    def __init__(self, name, cost, about="") -> None:
        self.name = name
        self.about = about
        self.cost = cost

    def __str__(self) -> str:
        return f"""Name: {self.name}
About: {self.about}
Cost: {self.cost}
"""

    def get_food(self):
        return f"{self.name}|{self.about}|{self.cost}\n"


# class Burger(Food):
#     def __init__(self, name, about, cost) -> None:
#         super().__init__(name=name, about=about, cost=cost)


# class Basket(Food):
#     def __init__(self, name, about, cost) -> None:
#         super().__init__(name=name, about=about, cost=cost)


class Drink(Food):
    def __init__(self, name, cost) -> None:
        super().__init__(name=name, cost=cost)


# class Sweat(Food):
#     def __init__(self, name, about, cost) -> None:
#         super().__init__(name=name, about=about, cost=cost)


# class Ice_cream(Food):
#     def __init__(self, name, about, cost) -> None:
#         super().__init__(name=name, about=about, cost=cost)


# class Basket:
#     def __init__(self, name, about, cost) -> None:
# self.name = name
# self.about = about
# self.cost = cost
#
# def __str__(self) -> str:
# return f"""Name: {self.name}
# About: {self.about}
# Cost: {self.cost}
# """
#
# def get_basket(self):
# return f"{self.name}|{self.about}|{self.cost}\n"
#
#
# class Drink:
# def __init__(self, name, cost) -> None:
# self.name = name
# self.cost = cost
#
# def __str__(self) -> str:
# return f"""Name: {self.name}
# Cost: {self.cost}
# """
#
# def get_drink(self):
# return f"{self.name}|{self.cost}\n"
