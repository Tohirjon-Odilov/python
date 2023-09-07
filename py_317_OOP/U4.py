class Account:
    def __init__(self, idx: int, name: str, balance: int = 0) -> None:
        self.idx = idx
        self.name = name
        self.balance = balance

    def get_idx(self):
        return self.idx

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> int:
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Amount exceeded balance")
        return self.balance

    def transfer_to(self, another, amount: int) -> int:
        if amount <= another.balance:
            another.balance -= amount
            self.balance += amount
        else:
            print("Amount exceeded balance")
        return self.balance

    def to_string(self):
        return f"Account[{self.idx}, {self.name}, {self.balance}]"


person1 = Account(1, "Ali")  # 500
person2 = Account(2, "Vali", 2000)  # 1500

person1.transfer_to(person2, 500)
person1.transfer_to(person2, 1000)
print(person1.to_string())
print(person2.to_string())
