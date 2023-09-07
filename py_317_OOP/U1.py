class Employee:
    def __init__(self, idx, firstname, lastname, salary) -> None:
        self.id = idx
        self.lname = lastname
        self.fname = firstname
        self.salary = salary

    def get_id(self) -> int:
        return self.id

    def get_first_name(self) -> str:
        return self.fname

    def get_last_name(self) -> str:
        return f"{self.get_first_name()} {self.lname}"

    def get_name(self) -> str:
        return f"{self.get_first_name()} {self.get_last_name()}"

    def get_salary(self) -> int:
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_annual_salary(self) -> int:
        return self.salary * 12

    def raise_salary(self, percent) -> None:
        self.salary += self.salary * (percent / 100)

    def to_string(self):
        return f"ID: {self.id}\nNAME: {self.fname}\n{self.get_last_name()}\nSALARY: {self.salary}"

    def __str__(self):
        return f"{self.id} {self.fname} {self.lname} {self.salary}"


e1 = Employee(1, "Hamid", "Olimjonov", 150)
# print(e1.to_string())
# print(e1)
print(e1.get_annual_salary())
