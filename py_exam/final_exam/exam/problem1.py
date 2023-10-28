# Foydalanuvchi tomonidan sana (kun.oy.yil ko‘rinishida) kiritiladi. 
# Sizning vazifangiz ushbu sanadan boshlab eng yaqin oldindagi 13-Juma sanasini aniqlang.

import datetime


def time_13(date: str) -> str:
    day, month, year = list(map(int, date.split(".")))
    # time = None
    start_month = month if month > 1 else 1
    # start_day = day if day > 13 else 13


    for month in range(start_month,13):
        time = datetime.date(year, month, 13)
        # print(time)
        # for j in range(14):
            
        if time.weekday() == 4:
            return time
        year += 1
        
    # time = datetime.date(year, month, day)
    # print(time)

print(time_13("28.10.2023"))