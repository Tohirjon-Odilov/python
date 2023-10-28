# Fraction nomli class yarating va uning property elementlari quyidagilardan iborat:
# -        Numerator (Kasr sonning surati);

# -        Denominator (Kasr sonning maxraji).

# Fraction nomli classining 2ta obyektini yarating. Sizning vazifangiz ushbu ikkita kasr sonlarni qo‘shadigan, ayiradigan, ko‘paytiradigan va bo‘ladigan methodlarni yaratish kerak bo‘ladi.


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
            self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num == second_num

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den
    
    
    

# Foydalanuvchi tomonidan sana (kun.oy.yil ko‘rinishida) kiritiladi. 
# Sizning vazifangiz ushbu sanadan boshlab eng yaqin oldindagi 13-Juma sanasini aniqlang.

# def friday_13(date: str) -> str:
#     day, month, year = list(map(int, date.split(".")))
#     time = datetime.date(year, month, day)
#     # print(time)
#     for i in range(14):
#         time += datetime.timedelta(days=1)
#         print(time)
#         # print(time)
#         if time.weekday() == 4:
#             return time
#         year += 1
        
    # time = datetime.date(year, month, day)
    # print(time)
    
    # return "13-Juma sanasi yoq"

# def time_13(date: str) -> str:
#     day, month, year = list(map(int, date.split(".")))
#     # time = None
#     start_month = month if month > 1 else 1
#     # start_day = day if day > 13 else 13


#     for month in range(start_month,13):
#         time = datetime.date(year, month, 13)
#         # print(time)
#         # for j in range(14):
            
#         if time.weekday() == 4:
#             return time
#         year += 1
        
#     # time = datetime.date(year, month, day)
# #     # print(time)