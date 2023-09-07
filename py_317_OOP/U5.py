class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def get_day(self) -> int:
        return self.day

    def get_month(self) -> int:
        return self.month

    def get_year(self) -> int:
        return self.year

    def set_day(self, day: int) -> None:
        self.day = day

    def set_month(self, month: int) -> None:
        self.month = month

    def set_year(self, year: int) -> None:
        self.year = year

    def set_date(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def to_string(self) -> str:
        return "%02d/%02d/%d" % (self.day, self.month, self.year)


date1 = Date(7, 9, 2023)
date1.day()
print(date1.to_string())
