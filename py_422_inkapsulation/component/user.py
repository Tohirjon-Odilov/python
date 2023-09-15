class User:
    """
    This class is for creating a user.
    """
    def __init__(self, fname, lname, card=None, cash=20000) -> None:
        self.fname = fname
        self.lname = lname
        self.card = card
        self.cash = cash

    def add_card(self, new_card):
        self.card = new_card

    def get_card(self):
        return self.card

    def add_cash(self, amount):
        self.cash += amount

    def minus_cash(self, amount):
        self.cash -= amount

