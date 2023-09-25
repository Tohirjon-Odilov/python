class Mydate:
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        self.MONTHS = [
            "Yanvar",
            "Fevral",
            "Mart",
            "Aprel",
            "May",
            "Iyun",
            "Iyul",
            "Avgust",
            "Sentyabr",
            "Oktyabr",
        ]
        self.DAY_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def isLeapYear(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            return True
        else:
            return False

    def isValidateDate(self):
        if self.isLeapYear() and self.month == 2 and self.day == 29:
            return True
        elif self.day <= self.DAY_IN_MONTHS[self.month - 1]:
            return True
        else:
            return False

    def setDate(self, day, month, year):
        if self.isValidateDate():
            self.day = day
            self.month = month
            self.year = year
        else:
            return f"Yil, oy yoki kun noto'g'ri"

    def setYear(self, year):
        if 1 < int(year) < 9999:
            self.year = year
        else:
            return f"Yil noto'g'ri"

    def setMonth(self, month):
        if 1 < int(month) < 13:
            self.month = month
        else:
            return f"Oy noto'g'ri"

    def setDay(self, day):
        if (
            1 < int(day) < 32
            and self.year % 4 == 0
            and self.year % 100 != 0
            or self.year % 400 == 0
        ):
            self.day = day
        else:
            return f"Kun noto'g'ri"

    def getYear(self):
        if self.isValidateDate:
            return self.year
        else:
            return f"Yil noto'g'ri"

    def getMonth(self):
        if self.isValidateDate:
            return self.month
        else:
            return f"Oy noto'g'ri"

    def getMonthName(self):
        if self.isValidateDate():
            return self.MONTHS[self.month - 1]
        else:
            return f"\033[1;31m{self.MONTHS[self.month - 1]}\033[0m"

    def getDay(self):
        if self.isValidateDate():
            return self.day
        else:
            return f"Kun noto'g'ri"

    def __str__(self):
        if self.isLeapYear() and self.month == 2 and self.day <= 29:
            return f"{self.day} {self.getMonthName()} {self.year} yil"
        elif self.isValidateDate():
            return f"{self.day} {self.getMonthName()} {self.year} yil"
        else:
            return f"\033[1;31m{self.day} {self.getMonthName()} {self.year} yil\033[0m"

    def nextDay(self):
        txt = "Kun, oy yoki yil noto'g'ri"
        self.day += 1
        if self.isValidateDate() and self.day == self.DAY_IN_MONTHS[self.month - 1]:
            self.day = 1
            self.month += 1
            txt = f"{self.day} {self.getMonthName()} {self.year} yil"
            if self.month == 13:
                self.month = 1
                self.year += 1
                txt = f"{self.day} {self.getMonthName()} {self.year} yil"
                # if self.isLeapYear():
                    # self.DAY_IN_MONTHS[1] = 29
        return txt

    def nextMonth(self):
        pass

    def nextYear(self):
        pass

    def previousDay(self):
        pass

    def previousMonth(self):
        pass

    def previousYear(self):
        pass


d1 = Mydate(28, 2, 2012)
d2 = Mydate(32, 2, 2012)
d3 = Mydate(21, 4, 2013)
d4 = Mydate(31, 5, 2014)
d5 = Mydate(33, 6, 2015)
d6 = Mydate(30, 9, 2016)
print(d1.nextDay())
print(d1.nextDay())
print(d1.nextDay())
print(d1.nextDay())
print(d1.nextDay())
# print(d2)
# print(d3)
# print(d4)
# print(d5.getDay())
# print(d6)
